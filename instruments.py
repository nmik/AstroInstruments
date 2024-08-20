
import csv
import numpy as np

def save_instruments_to_csv(instruments, filename='instruments.csv'):
    # Check if the input is a list of dictionaries
    # if not isinstance(instruments, list) or not all(isinstance(i, dict) for i in instruments):
    #     raise ValueError("Input must be a list of dictionaries.")
    
    # Define the header based on the dictionary keys
    header = ['name', 'type'] + [key for key in instruments[0].keys() if key not in ['name', 'type']]
    
    # Open the file in write mode
    with open(filename, 'w', newline='') as csvfile:
        # Initialize the writer object
        writer = csv.DictWriter(csvfile, fieldnames=header)
        
        # Write the header
        writer.writeheader()
        
        # Write the data rows
        for instrument in instruments:
            writer.writerow(instrument)
    print('Wrote %s'%filename)
    
	
sky = 4*np.pi

instruments_ = [
    {
        "min_energy_kev": 7,
        "max_energy_kev": 40000,
        "Energy_res_%":   10, 
        "time_res_s":     2.6e-6,
        "FoV_skyfrac":    0.7,
        "color":          "green",
        "name":           "Fermi-GBM",
        "type":           "Scintillating monitor",
        "min_repoint_t":      None,
        "notes": '',
        "contributors": 'M. Negro',
    
    },
    {
        "min_energy_kev": 100000,
        "max_energy_kev": 800000000,
        "Energy_res_%": 5,
        "time_res_s": 10e-3,
        "FoV_skyfrac": 0.25,
        "color": "green",
        "name": "Fermi-LAT",
        "type": "Pair production Imaging monitor",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
        {
        "min_energy_kev": 80,
        "max_energy_kev": 8000,
        "Energy_res_%": None,
        "time_res_s": 50e-3,
        "FoV_skyfrac": 1,
        "color": "green",
        "name": "INTEGRAL (SPI-ACS)",
        "type": "Scintillating monitor",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
   {
        "min_energy_kev": 20,
        "max_energy_kev": 8000,
        "Energy_res_%": 0.2,
        "time_res_s": 50e-3,
        "FoV_skyfrac": np.radians(30)*np.radians(30)/sky,
        "color": "green",
        "name": "INTEGRAL (SPI)",
        "type": "Compton Imaging Spectrometry",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 15,
        "max_energy_kev": 10000,
        "Energy_res_%": 0.2,
        "time_res_s": 50e-3,
        "FoV_skyfrac": np.radians(30)*np.radians(30)/sky,
        "color": "green",
        "name": "INTEGRAL (IBIS)",
        "type": "Scintillating Imaging monitor",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 200,
        "max_energy_kev": 5000,
        "Energy_res_%": 0.5,
        "time_res_s": 2e-3,
        "FoV_skyfrac": 0.33,
        "color": "green",
        "name": "COSI",
        "type": "Compton Imaging Spectrometry Polarimetry Monitor",
        "min_repoint_t": None,
        "notes": 'Energy resolution requirements: 0.2%-1% (0.2-5 MeV)',
        "contributors": 'M. Negro',
        
    },
    {
        "min_energy_kev": 15,
        "max_energy_kev": 150,
        "Energy_res_%": 5,
        "time_res_s": 100e-6,
        "FoV_skyfrac": 1.4/sky,
        "color": "green",
        "name": "Swift-BAT",
        "type": "Scintillating monitor",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 100e6,
        "max_energy_kev": 100e9,
        "Energy_res_%": None,
        "time_res_s": None,
        "FoV_skyfrac": np.radians(5)*np.radians(5)/sky,
        "color": "blue",
        "name": "HESS",
        "type": "IACT",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },

    {
        "min_energy_kev": 20e6,
        "max_energy_kev": 300e9,
        "Energy_res_%": 15,
        "time_res_s": 1,
        "FoV_skyfrac": 0.1,
        "color": "blue",
        "name": "CTAO",
        "type": "IACT",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 10*1e9,
        "max_energy_kev": 500*1e9,
        "Energy_res_%": 20, #??? not sure
        "time_res_s": 120, #2min ?
        "FoV_skyfrac": 1.8/sky,
        "color": "blue",
        "name": "HAWC",
        "type": "IACT",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 1e9,
        "max_energy_kev": 1e12,
        "Energy_res_%": 20,
        "time_res_s": 2e-9,
        "FoV_skyfrac": np.radians(5)*np.radians(5)/sky,
        "color": "blue",
        "name": "LHAASO",
        "type": "IACT",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 0.2,
        "max_energy_kev": 12,
        "Energy_res_%": 10,
        "time_res_s": 1e-7,
        "FoV_skyfrac": np.radians(5/60)*np.radians(5/60)/sky,
        "color": "red",
        "name": "NICER",
        "type": "Timing Pointed",
        "min_repoint_t": 4*3600,
        "notes": 'Non-imaging, great for timing',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 3,
        "max_energy_kev": 79,
        "Energy_res_%": 2,
        "time_res_s": 2e-6,
        "FoV_skyfrac": np.radians(10/60)*np.radians(10/60)/sky,
        "color": "red",
        "name": "NuSTAR",
        "type": "Imaging Spectrometry Pointed",
        "min_repoint_t": 24*3600,
        "notes": '',
        "contributors": 'M. Negro',
    },
        {
        "min_energy_kev": 2,
        "max_energy_kev": 8,
        "Energy_res_%": 30,
        "time_res_s": 2e-6,
        "FoV_skyfrac": np.radians(10/60)*np.radians(10/60)/sky,
        "color": "red",
        "name": "IXPE",
        "type": "Imaging Polarimetry Pointed",
        "min_repoint_t": 72*3600,
        "notes": '',
        "contributors": 'M. Negro',
    },
        {
        "min_energy_kev": 0.3,
        "max_energy_kev": 12,
        "Energy_res_%": 0.06,
        "time_res_s": 2e-6,
        "FoV_skyfrac": np.radians(10/60)*np.radians(10/60)/sky,
        "color": "red",
        "name": "XRISM",
        "type": "Imaging Spectrometry Pointed",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 0.1,
        "max_energy_kev": 10,
        "Energy_res_%": 20, # 10% -- 66% (0.4--10 keV)
        "time_res_s": 16e-6,
        "FoV_skyfrac": np.radians(30/60)*np.radians(30/60)/sky,
        "color": "red",
        "name": "Chandra",
        "type": "Imaging ",
        "min_repoint_t": 5*24*3600,
        "notes": 'Energy Res varies with energy 10%-66% (0.4--10 keV)',
        "contributors": 'M. Negro',
    },
        {
        "min_energy_kev": 0.5,
        "max_energy_kev": 4.0,
        "Energy_res_%": 10,
        "time_res_s": 16e-6,
        "FoV_skyfrac": 11,
        "color": "blue",
        "name": "Einstein Probe (WXT)",
        "type": "Lobster-eye wide-field telescope",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    },
     {
        "min_energy_kev": 0.2,
        "max_energy_kev": 8,
        "Energy_res_%": 10,
        "time_res_s": 50e-3,
        "FoV_skyfrac": np.radians(1)*np.radians(1)/sky,
        "color": "red",
        "name": "eROSITA",
        "type": "Imaging Wide-field Monitor",
        "min_repoint_t": None,
        "notes": 'Energy resolution varies: 2%-20% (10 - 0.2 keV)',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 2,
        "max_energy_kev": 20,
        "Energy_res_%": 18,
        "time_res_s": 50e-3,
        "FoV_skyfrac": 0.02,
        "color": "red",
        "name": "MAXI (GSC)",
        "type": "Wide Field Monitor",
        "min_repoint_t": None,
        "notes": 'Scans 90 to 98% of all-sky every 96 min (Non Imaging)',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 0.2,
        "max_energy_kev": 10,
        "Energy_res_%": 10, #2% @ 1 keV, 50% % 0.1 keV
        "time_res_s": 1.7e-3,
        "FoV_skyfrac": np.radians(23.6/60)*np.radians(23.6/60)/sky,
        "color": "red",
        "name": "Swift-XRT",
        "type": "Fast Pointed",
        "min_repoint_t": 150,
        "notes": '',
        "contributors": 'M. Negro',
    },
    {
        "min_energy_kev": 86400,
        "max_energy_kev": 0.2,
        "Energy_res_%": 2,
        "time_res_s":  30e-6,
        "FoV_skyfrac": np.radians(27.5/60)*np.radians(27.5/60)/sky,
        "color": "red",
        "name": "XMM-Newton",
        "type": "pointed",
        "min_repoint_t": None,
        "notes": '',
        "contributors": 'M. Negro',
    }
]



if __name__ == '__main__':
    
	save_instruments_to_csv(instruments_)