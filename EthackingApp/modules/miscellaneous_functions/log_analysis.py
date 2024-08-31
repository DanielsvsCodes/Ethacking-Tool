import os
import re
from datetime import datetime
from colorama import Fore, Style

class LogAnalyzer:
    def __init__(self, log_file_path):
        """
        Initialize the LogAnalyzer class with necessary parameters.
        :param log_file_path: Path to the log file to analyze.
        """
        self.log_file_path = log_file_path

        if not os.path.isfile(self.log_file_path):
            raise FileNotFoundError(f"{Fore.RED}Log file not found: {self.log_file_path}")

    def parse_logs(self):
        """
        Parse the log file and extract useful information.
        :return: List of log entries (dictionaries) containing extracted data.
        """
        log_entries = []
        ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
        date_pattern = re.compile(r'\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2})')
        status_pattern = re.compile(r'"\s(\d{3})\s')

        with open(self.log_file_path, 'r') as file:
            for line in file:
                ip_match = ip_pattern.search(line)
                date_match = date_pattern.search(line)
                status_match = status_pattern.search(line)

                if ip_match and date_match and status_match:
                    log_entry = {
                        'ip': ip_match.group(),
                        'date': datetime.strptime(date_match.group(1), '%d/%b/%Y:%H:%M:%S'),
                        'status': status_match.group(1)
                    }
                    log_entries.append(log_entry)

        return log_entries

    def analyze_logs(self):
        """
        Analyze the parsed log entries for patterns and anomalies.
        :return: A summary dictionary with analysis results.
        """
        log_entries = self.parse_logs()

        ip_counter = {}
        status_counter = {}

        for entry in log_entries:
            ip = entry['ip']
            status = entry['status']

            ip_counter[ip] = ip_counter.get(ip, 0) + 1
            status_counter[status] = status_counter.get(status, 0) + 1

        most_frequent_ip = max(ip_counter, key=ip_counter.get)
        most_common_status = max(status_counter, key=status_counter.get)

        return {
            'total_requests': len(log_entries),
            'unique_ips': len(ip_counter),
            'most_frequent_ip': most_frequent_ip,
            'most_common_status': most_common_status,
            'status_distribution': status_counter
        }

    def display_results(self):
        """
        Display the results of the log analysis.
        """
        results = self.analyze_logs()
        print(f"{Fore.GREEN}Total Requests: {results['total_requests']}")
        print(f"Unique IPs: {results['unique_ips']}")
        print(f"Most Frequent IP: {results['most_frequent_ip']}")
        print(f"Most Common Status Code: {results['most_common_status']}")
        print(f"Status Code Distribution:")
        for status, count in results['status_distribution'].items():
            print(f"  {status}: {count}")

def run_log_analysis():
    """
    Run the log analysis tool.
    """

    default_log_file_path = os.path.join('resources', 'log_events.txt')

    log_file_path = input(f"{Fore.GREEN}Enter the path to the log file: ").strip()

    if not log_file_path:
        log_file_path = default_log_file_path

    try:
        analyzer = LogAnalyzer(log_file_path)
        analyzer.display_results()
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"{Fore.RED}An error occurred while analyzing the log file: {e}")

if __name__ == "__main__":
    run_log_analysis()
