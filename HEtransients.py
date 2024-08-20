
import numpy as np
import matplotlib.pyplot as plt


# Define the log scale ranges for time (X-axis) and energy (Y-axis)
x_min, x_max = 1e-3, 10*365*24*3600  # seconds (milliseconds to 10 years)
y_min, y_max = 1e-2, 1e16            # keV (0.01 keV to 100 TeV)


energy_bands = [
    (0.1, 10, 'lightblue', 'Soft X: 0.1-10 keV'),
    (10, 100, 'blue', 'Hard X: 10-100 keV'),
    (100, 1e3, 'purple', 'Soft γ: 100 keV - 1 MeV'),
    (1e3, 4e4, 'violet', 'Medium E γ: 1 MeV - 40 MeV'),
    (5e4, 8e8, 'red', 'HE γ: 50 MeV - 800 GeV'),
    (1e9, 1e16, 'darkred', 'VHE γ: >1 TeV')
]

# Define rectangles for various cosmic events with their color and labels
events = [
    (0.1, 7, 1000, 94e6, '0.3', 'GRB Prompt', 2, '-'),
    (100, y_min, 365*24*3600, 1e14, '0.3', 'GRB Afterglow', 4, '-'),
    (1e-3, 0.1, 0.01, 1e5, 'yellow', 'Magnetar Bursts', 3, '-'),
    (7*24*3600, 0.3, 90*24*3600, 1e3, 'goldenrod', 'Magnetar Outbursts', 4, '-'),
    (1e-3, 1e2, 15e-3, 40e3, 'tab:orange', 'MGFs Spike', 4, '-'),
    (1e-3, 40e3, 15e-3, 1.7e6, 'tab:orange', 'MGFs (bow shock)', 4, '--'),
    (60, 1, 500, 1e3, 'orange', 'MGFs Tail', 2, '-'),
    (3600, 100e3, 90*24*3600, 13e14, 'green', 'Blazars Jets', 4, '-'),
    (3600, 12, 90*24*3600, 100e3, 'green', ' ', 4, '--'),
    (3600, 1e-3, 90*24*3600, 12, 'green', 'AGN Jets / Disk', 4, '-'),
    (24*3600, 1e-3, 14*24*3600, 1e4, 'cyan', 'SN', 5, '-'),
    (24*3600, 1e4, 14*24*3600, 1e6, 'cyan', 'SN (?)', 5, '--'),
    (12*3600, 1e-3, 21*24*3600, 50e6, 'blue', 'Novae', 3, '-'),
    (24*3600, 1e4, 14*24*3600, 1e6, 'cyan', 'SN (SBO)', 5, '--'),
    (3600, 0.1, 14*24*3600, 1e2, 'limegreen', 'X-ray Binary', 2, '-'),
    (24*3600, 0.1, 20*24*3600, 12, 'darkblue', 'TDEs', 2, '-'),
    # (24*3600, , 15*24*3600, ..., 'darkred', 'Kilonovae', 2),
    # (24*3600, ..., 15*24*3600, ..., 'darkblue', 'FBOT', 2)
]


# Define atomic and nuclear lines
atomic_nuclear_lines = [
    {"element": "Hydrogen", "line": "Lyman-alpha", "energy_keV": 0.0136, "color":'orange'},
    {"element": "Carbon", "line": "K-alpha", "energy_keV": 0.277, "color":'blue'},
    {"element": "Nitrogen", "line": "K-alpha", "energy_keV": 0.392, "color":'blue'},
    {"element": "Oxygen", "line": "K-alpha", "energy_keV": 0.525, "color":'blue'},
    {"element": "Iron", "line": "K-alpha", "energy_keV": 6.4, "color":'blue'},
    {"element": "Copper", "line": "K-alpha", "energy_keV": 8.048, "color":'blue'},
    {"element": "Copper", "line": "K-beta", "energy_keV": 8.905, "color":'blue'},
    {"element": "Uranium", "line": "L-alpha", "energy_keV": 13.614, "color":'blue'},
    {"element": "Manganese", "line": "K-alpha", "energy_keV": 5.899, "color":'blue'},
    {"element": "Nickel", "line": "K-alpha", "energy_keV": 7.478, "color":'blue'},
    {"element": "Cobalt-60", "line": "Nuclear", "energy_keV": 1173.2, "color":'magenta'},
    {"element": "Cobalt-60", "line": "Nuclear", "energy_keV": 1332.5, "color":'magenta'},
    {"element": "Cesium-137", "line": "Nuclear", "energy_keV": 661.657, "color":'magenta'},
    {"element": "Americium-241", "line": "Nuclear", "energy_keV": 59.5409, "color":'magenta'},
    # Adding typical lines detected by NuSTAR
    {"element": "Iron", "line": "K-beta", "energy_keV": 7.058, "color":'blue'},
    {"element": "Titanium-44", "line": "Nuclear", "energy_keV": 68.0, "color":'magenta'},
    {"element": "Titanium-44", "line": "Nuclear", "energy_keV": 78.4, "color":'magenta'},
    # Common lines observed by COSI
    {"element": "Aluminum-26", "line": "Nuclear", "energy_keV": 1808.65, "color":'magenta'},
    # {"element": "Iron-60", "line": "Gamma", "energy_keV": 1173.23},
    # {"element": "Iron-60", "line": "Gamma", "energy_keV": 1332.492}
    {"element": "Positron Annihilation", "line": " ", "energy_keV": 511, "color":'green'}
]

if __name__ == '__main__':


    # Initialize the figure
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Add energy bands as colored regions
    for lower, upper, color, label in energy_bands:
        ax.fill_betweenx([lower, upper], x_min, x_max, color=color, alpha=0.2, zorder=0)
        # Add labels far to the right of the plot area
        ax.text(x_max * 1.2, np.sqrt(lower * upper), label, color=color, ha='left', va='center', fontsize=8)

    for line in atomic_nuclear_lines:
        if line["element"] == 'Positron Annihilation' or line["element"] == 'Hydrogen':
            ax.plot([1e8, 3e8], [line["energy_keV"],line["energy_keV"]], color=line["color"], linestyle='-', 
                linewidth=0.5, alpha=1, zorder=1, label='%s'%(line["element"]))
        elif line["energy_keV"] == 1173.2:
            ax.plot([1e8, 3e8], [line["energy_keV"],line["energy_keV"]], color=line["color"], linestyle='-', 
                linewidth=0.5, alpha=1, zorder=1, label='Nuclear lines')
        elif line["energy_keV"] == 0.277:
            ax.plot([1e8, 3e8], [line["energy_keV"],line["energy_keV"]], color=line["color"], linestyle='-', 
                linewidth=0.5, alpha=1, zorder=1, label='Atomic Lines')
        else:
            ax.plot([1e8, 3e8], [line["energy_keV"],line["energy_keV"]], color=line["color"], linestyle='-', 
                linewidth=0.5, alpha=1, zorder=1)
            

    # Add rectangles for events
    for start_time, start_energy, end_time, end_energy, color, label, lw, ls in events:
        ax.add_patch(plt.Rectangle((start_time, start_energy), end_time - start_time, end_energy - start_energy,
                                edgecolor=color, fill=None, linestyle=ls, linewidth=lw))
        ax.text(start_time, end_energy, label, color=color, ha='left', va='bottom')

    # Adjust grid visibility and add labels
    ax.grid(False)  # Disable the grid
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Energy (keV)', fontsize=12)

    ax.legend(fontsize=12)

    # Display the plot
    plt.title('Energy vs Time with Different Cosmic Phenomena and Events')
    plt.tight_layout()
    plt.savefig('HEtransients.png', dpi=200)

    plt.show()