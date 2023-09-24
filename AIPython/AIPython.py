import psutil
import time

def get_most_cpu_intensive_process():
    # Get a list of all running processes and their CPU percentages
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent'])
        except psutil.NoSuchProcess:
            continue
        processes.append(process_info)

    # Sort the processes by CPU percentage in descending order
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)

    # Return the most CPU-intensive process
    return processes[0]

def main():
    try:
        while True:
            # Get the most CPU-intensive process
            most_cpu_intensive = get_most_cpu_intensive_process()

            # Display the process information
            print(f"Most CPU-Intensive Process: PID {most_cpu_intensive['pid']} - {most_cpu_intensive['name']} ({most_cpu_intensive['cpu_percent']}% CPU)")

            # Sleep for a few seconds before checking again
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()


