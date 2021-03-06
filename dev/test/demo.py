import pytest
from .cfg.test_configuration import TestConfiguration
from datetime import datetime

# Initialize a list of vaccine data counters - each index (0, 1, .. 9) represents percentile group,
# Inner lists represent counters of performed(left) and non-performed(right) vaccines for each percentile group
# All counters are being initialized with '0' value
group_to_vaccine_rates = [[0, 0], [0, 0], [0, 0], [0, 0],
                       [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
config = TestConfiguration()


def test_analyze_data():
    print('Analyze Data Test..')
    analyze_data_file(config.get_data_path())
    print_vaccine_rates()


def analyze_data_file(data_file):
    with open(data_file) as data:
        for row in data:

            # Analyze each row of the data
            data = row.split()
            if len(data) > 1:
                analyze_result(data[config.DOB_INDEX],
                               data[config.HAD_VACCINE_INDEX])


def analyze_result(date_of_birth, had_vaccine):
    age = calculate_age(get_percentile(date_of_birth))

    # Check corner case of younger than 10
    if age < 10:
        percentile_group = 0

    # Check corner case of older than 90
    elif age >= 90:
        percentile_group = 9
    else:
        percentile_group = age/10

    # Check whether given subject had vaccine
    if "Yes" in had_vaccine:
        group_to_vaccine_rates[percentile_group][0] += 1
    elif "No" in had_vaccine:
        group_to_vaccine_rates[percentile_group][1] += 1


def get_percentile(date_of_birth):
    datetime_object = datetime.strptime(date_of_birth, '%d/%m/%Y').date()
    return datetime_object


def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_percentage(part, whole):
    return 100 * float(part)/float(whole)


def print_vaccine_rates():
    # Initialize index at zero
    index = 0
    for percentile_group in group_to_vaccine_rates:
        total_subjects_in_group = percentile_group[config.PERFORMED_VACCINE_COUNTER_INDEX] + \
            percentile_group[config.NON_PERFORMED_VACCINE_COUNTER_INDEX]
        if total_subjects_in_group > 0:
            vaccine_rates = get_percentage(
                percentile_group[config.PERFORMED_VACCINE_COUNTER_INDEX], total_subjects_in_group)
            print(config.groups.get(index) + ': %' + str(vaccine_rates))
        else:
            print(config.groups.get(index) + ' has zero subjects')

        # Increment counter
        index += 1
