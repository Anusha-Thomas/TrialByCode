import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path, parse_dates=["Date"])
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None

def plot_temperature(data, save_file=None):
    # rolliing average
    data["7-Day Average"] = data["Temperature"].rolling(window=7).mean()
    
    # Identify Anomalies
    mean_temp = data["Temperature"].mean()
    std_temp = data["Temperature"].std()
    data["Anomaly"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)
    
    # Plot
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Temperature"], label="Daily Temperature", color="green")
    plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--", color="orange")
    plt.scatter(data[data["Anomaly"]]["Date"], data[data["Anomaly"]]["Temperature"], color="red", label="Anomalies")
    plt.title("Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid(True)

    #save file
    if save_file:
        plt.savefig(save_file)
        print(f"Plot saved as {save_file}")
    else:
        plt.show()

def main():
    print("welcome to temperature plotter")

    file_path = input("enter the path to your temperature csv file: ")
    data = load_data(file_path)
    if data is None:
        return

    save_choice = input("Do you want to save the plot? (yes/no): ").lower()
    if save_choice == "yes":
        file_name = input("Enter the file name (e.g., temperature_plot.png): ")
        plot_temperature(data, save_file=file_name)
    else:
        plot_temperature(data)


if __name__ == "__main__":
    main()