from python.utils import Utils


class FCFS:
    def __init__(self):
        pass

    def sort_processes(self, n, processes, bt, at):
        for i in range(n - 1):
            for j in range(n - i - 1):
                if at[j] > at[j + 1]:
                    # Swap elements in all arrays
                    at[j], at[j + 1] = at[j + 1], at[j]
                    bt[j], bt[j + 1] = bt[j + 1], bt[j]
                    processes[j], processes[j + 1] = processes[j + 1], processes[j]

    def find_waiting_time(self, n, bt, wt, at):
        service_time = [at[0]]
        wt[0] = 0
        for i in range(1, n):
            service_time.append(service_time[i - 1] + bt[i - 1])
            wt[i] = service_time[i] - at[i]
            wt[i] = max(wt[i], 0)  # Ensure non-negative waiting time

    def find_turnaround_time(self, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]

    def find_average_time(self, processes, n, bt, at):
        wt = [0] * n
        tat = [0] * n
        total_wt = 0
        total_tat = 0

        self.sort_processes(n, processes, bt, at)
        self.find_waiting_time(n, bt, wt, at)
        self.find_turnaround_time(n, bt, wt, tat)

        result = "Process\tArrival_Time\tBurst_Time\tWaiting_Time\tTurnaround_Time\n"
        for i in range(n):
            total_wt += wt[i]
            total_tat += tat[i]
            result += f"{processes[i] + 1}\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}\n"

        avg_wt = total_wt / n
        avg_tat = total_tat / n

        result += f"\nAverage Waiting Time: {avg_wt:.2f}\n"
        result += f"Average Turnaround Time: {avg_tat:.2f}\n"

        result += "\n" + Utils().draw_gantt_chart(processes)

        return result
