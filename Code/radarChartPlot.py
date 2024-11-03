import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Hàm vẽ biểu đồ radar
def radar_chart(player1_data, player2_data, attributes, player1_name, player2_name):
    num_vars = len(attributes)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Đóng vòng tròn

    player1_values = player1_data[attributes].values.flatten().tolist()
    player1_values += player1_values[:1]

    player2_values = player2_data[attributes].values.flatten().tolist()
    player2_values += player2_values[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    ax.plot(angles, player1_values, linewidth=2, linestyle='solid', label=player1_name)
    ax.fill(angles, player1_values, alpha=0.25)

    ax.plot(angles, player2_values, linewidth=2, linestyle='solid', label=player2_name)
    ax.fill(angles, player2_values, alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, fontsize=12)

    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.title(f'Comparison of {player1_name} vs {player2_name}', size=15, color='darkblue', weight='bold')
    plt.show()

# Xử lý tham số dòng lệnh
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare two players using a radar chart.')
    parser.add_argument('--p1', type=str, required=True, help='Name of the first player')
    parser.add_argument('--p2', type=str, required=True, help='Name of the second player')
    parser.add_argument('--Attribute', type=str, required=True, help='Comma-separated list of attributes to compare')

    args = parser.parse_args()
    player1_name = args.p1
    player2_name = args.p2
    attributes = args.Attribute.split(',')

    df = pd.read_csv("cau_1.csv")  

    if player1_name not in df['Player'].values or player2_name not in df['Player'].values:
        print("One or both players not found in the dataset.")
    else:
        player1_data = df[df['Player'] == player1_name].iloc[0]
        player2_data = df[df['Player'] == player2_name].iloc[0]
        radar_chart(player1_data, player2_data, attributes, player1_name, player2_name)


# python radarChartPlot.py --p1 "Phil Foden" --p2 "Erling Haaland" --Attribute "Standard_Gls,Standard_Sh,Standard_SoT,Standard_SoT%,Standard_Sh/90"
