from step import Step


def get_test_steps(step_data):
    step_list = []
    for step in step_data:
        new_step = Step(**step)
        step_list.append(new_step)
    return step_list


if __name__ == '__main__':
    parsed_steps = get_test_steps()
    print(parsed_steps, len(parsed_steps))



