class TestConfiguration:

    DATA_FILE_PATH = 'dev/reference_files/vaccine-report.csv'
    DOB_INDEX = 1
    HAD_VACCINE_INDEX = 2
    PERFORMED_VACCINE_COUNTER_INDEX = 0
    NON_PERFORMED_VACCINE_COUNTER_INDEX = 1

    groups = {0 : 'Ages 0-9 Percentile Group',
               1 : 'Ages 10-19 Percentile Group',
               2 : 'Ages 20-29 Percentile Group',
               3 : 'Ages 30-39 Percentile Group',
               4 : 'Ages 40-49 Percentile Group',
               5 : 'Ages 50-59 Percentile Group',
               6 : 'Ages 60-69 Percentile Group',
               7 : 'Ages 70-79 Percentile Group',
               8 : 'Ages 80-89 Percentile Group',
               9 : 'Ages 90 and Older Percentile Group',
    }

    # Getters for results paths.
    def get_data_path(self):
        return self.DATA_FILE_PATH
