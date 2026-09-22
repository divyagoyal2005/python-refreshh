import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Automated Directory File Organizer"
    )

    parser.add_argument(
        "directory",
        help="Directory to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show changes without moving files"
    )

    args = parser.parse_args()

    print(f"Directory: {args.directory}")
    print(f"Dry run: {args.dry_run}")


if __name__ == "__main__":
    main()