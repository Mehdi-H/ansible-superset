import subprocess

from ansible.module_utils.basic import AnsibleModule


def dict_to_command_parameters(dic):
    command_mapping = map(
        lambda key: "--" + key + " " + dic[key],
        dic.keys()
    )
    return " ".join(command_mapping)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            app=dict(required=True, type="str"),
            username=dict(required=True, type="str"),
            firstname=dict(required=True, type="str"),
            lastname=dict(required=True, type="str"),
            email=dict(required=True, type="str"),
            password=dict(required=True, type="str", no_log=True),
            superset_env=dict(required=True, type="str")
        ),
        supports_check_mode=False
    )

    # get module params
    superset_env = module.params.pop("superset_env", None)

    command_parameters = dict_to_command_parameters(module.params)

    cmd = ". {superset_env}/bin/activate && fabmanager create-admin {command_params}"\
        .format(
            superset_env=superset_env,
            command_params=command_parameters
        )

    output, err = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    if not err:
            module.exit_json(changed=True, cmd=cmd, output=output, error=err)
    else:
        if "Error adding new user to database" in err and "UNIQUE constraint failed" in err:
            module.exit_json(
                msg="Failed when running fabmanager command, the user you want to create may already exist.",
                warning=err,
                output=output,
                changed=False
            )
        else:
            module.exit_json(changed=True, cmd=cmd, output=output,
                             msg="Failed when running fabmanager command --> " + err)


if __name__ == "__main__":
    main()
