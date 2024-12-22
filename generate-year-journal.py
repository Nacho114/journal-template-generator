import os
from datetime import datetime, timedelta

def get_first_monday(year, start_month=1):
    """Return the first Monday of the given month and year."""
    first_day_of_month = datetime(year, start_month, 1)
    first_monday = first_day_of_month + timedelta(days=(7 - first_day_of_month.weekday()) % 7)
    return first_monday

def create_week_file(month_folder, week_number, current_monday, end_sunday, year):
    """Create a weekly markdown file with formatted daily headers and year in filename."""
    week_file_name = f"week{week_number}-{current_monday.strftime('%b%d').lower()}-{end_sunday.strftime('%b%d').lower()}-{year}.md"
    file_path = os.path.join(month_folder, week_file_name)
    with open(file_path, 'w') as file:
        file.write(f"# Week {week_number}: {current_monday.strftime('%b %d')} - {end_sunday.strftime('%b %d')}\n\n")
        file.write("## Objectives for week {}\n\n".format(week_number))
        file.write("## Things I'm thankful for\n\n")
        for day in range(7):
            date = current_monday + timedelta(days=day)
            file.write(f"## {date.strftime('%A')} {date.strftime('%d %b')}\n\n")

def create_monthly_structure(root_folder, year, start_month, end_month):
    """Create folders and files for each month from start_month to end_month."""
    for month in range(start_month, end_month + 1):
        month_folder = os.path.join(root_folder, datetime(year, month, 1).strftime('%B').lower())
        os.makedirs(month_folder, exist_ok=True)
        create_month_objectives_file(month_folder, year, month)  # Create the monthly objectives file
        current_monday = get_first_monday(year, month)
        while current_monday.month == month or (current_monday.month == month - 1 and current_monday.day > 7):
            end_sunday = current_monday + timedelta(days=6)
            week_number = current_monday.isocalendar()[1]
            create_week_file(month_folder, week_number, current_monday, end_sunday, year)
            current_monday += timedelta(days=7)

def create_month_objectives_file(month_folder, year, month):
    """Create a monthly objectives markdown file in the specified month folder."""
    month_name = datetime(year, month, 1).strftime('%B').lower()
    objectives_file_name = f"{month_name}-{year}-objectives.md"
    objectives_file_path = os.path.join(month_folder, objectives_file_name)
    with open(objectives_file_path, 'w') as file:
        file.write(f"# Objectives for {month_name.capitalize()} {year}\n\n")

def create_year_objectives_file(year_folder, year):
    """Create a yearly objectives markdown file at the root of the year folder."""
    objectives_file_path = os.path.join(year_folder, f"{year}-objectives.md")
    with open(objectives_file_path, 'w') as file:
        file.write(f"# {year}\n\n")
        file.write(f"## Objectives\n\n")
        file.write(f"## Reflections at the end of the year\n\n")
        file.write(f"### Highlights\n\n")

def main():
    root_path = input("Enter the path where to create the year folder structure: ")
    year = int(input("Enter the year for the folder structure: "))
    year_folder = os.path.join(root_path, str(year))

    # Check if the main year folder already exists
    if os.path.exists(year_folder):
        print("Folder already exists. Exiting without creating any files.")
        return

    os.makedirs(year_folder, exist_ok=True)
    create_monthly_structure(year_folder, year, 1, 12)
    create_year_objectives_file(year_folder, year)

if __name__ == "__main__":
    main()

