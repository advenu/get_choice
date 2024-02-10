def _get_input(max: int, msg: str) -> int:
    try:
        i = int(input(f"\n{msg}: "))
        if not 1 <= i <= max:
            raise Exception(f"Input out of range. Enter a value between 1-{max}")
        return i
    except ValueError:
        raise Exception("Only numeric values are allowed.")


def _get_input_with_retries(max: int, msg: str, tries) -> int:
    while tries:
        try:
            return _get_input(max, msg)
        except Exception as e:
            print(f"Error: {e}", end="\n\n" if tries == 1 else "\n")
            tries -= 1
    raise Exception("Maximum retry limit reached. Please seek assistance if needed.")


def _print_choices(choices: list, fmt: str, repls: list[str]) -> None:
    assert (fmt and repls) or (
        not fmt and not repls
    ), "'fmt' and 'repls' both should be provided"
    for i, choice in enumerate(choices, 1):
        if isinstance(choice, dict) and repls:
            print(f"{i}. {fmt.format(*[choice[repl] for repl in repls])}")
        else:
            print(f"{i}. {choice}")


def get_choice(
    choices: list,
    title: str = "",
    msg: str = "Choose an option",
    tries: int = 3,
    fmt: str | None = None,
    repls: list[str] | None = None,
):
    """Prints all the `choices` with serial no. and asks user to choose one.

    Args:
        choices (list): List of choices. A choice can be any python object,
        but only `dict` parsing is supported.
            (required)
        title (str): A title for options.
            (optional, default is empty string)
        msg (str): A msg shown while taking input.
            (optional, default is 'Choose an option')
        tries (int): Maximum no. of retries on invalid input.
            (optional, default is `3`)
        fmt (str): String with replacement slots `{}` for dict parsing.
        No. of replacement slots should be equal to length of repls.
            (optional, default is `None`)
        repls (list): List of `str` used as dict keys of the choices 
        to populate `fmt`.
            (optional, default is `None`)

    Returns:
        any: Type of `choice`.
    """
    print(f"\n{title}", end="\n\n" if title else "")
    _print_choices(choices, fmt, repls)
    try:
        i = _get_input_with_retries(len(choices), msg, tries)
        return choices[i - 1]
    except Exception as e:
        print(e)


if __name__ == "__main__":

    # string choices

    choices = [f"Option {i + 1}" for i in range(5)]
    choice = get_choice(choices, "Options")

    if choice:
        print(f"\nYou have choosen: {choice}")

    # dict choices

    choices = [{"id": i + 11, "title": f"Option {i + 1}"} for i in range(5)]
    choice = get_choice(
        choices, "Options", fmt="Id: {}, Title: {}", repls=("id", "title")
    )

    if choice:
        print(f"\nYou have choosen: {choice}")
