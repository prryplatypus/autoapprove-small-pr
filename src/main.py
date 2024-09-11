from github import approve_pr, get_input, get_config, event_data


def main() -> None:
    event_name = get_config("EVENT_NAME")
    if event_name != "pull_request":
        print("This action only supports pull_request events.")
        exit(1)

    changed = event_data["pull_request"]["additions"]
    changed += event_data["pull_request"]["deletions"]
    max_diff_size = int(get_input("MAX-DIFF-SIZE"))

    if changed > max_diff_size:
        print(f"PR is too large ({changed} > {max_diff_size}) - not approving")
        exit(0)

    print(f"Approving PR with {changed} changes")
    approve_pr(event_data["pull_request"]["_links"]["self"]["href"])


if __name__ == "__main__":
    main()
