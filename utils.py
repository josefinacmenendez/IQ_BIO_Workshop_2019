from scipy.io import loadmat
from matplotlib import pyplot as plt

def plot_ISIs(ISIs, n_bins, plot_title):
    plt.hist(ISIs,n_bins, density=True)
    plt.ylabel('Density')
    plt.xlabel('Time (s)')
    plt.title(plot_title)
    plt.show()

def load_retinal_ganglion_data(retinal_ganglion_path):
    retinal_ganglion_dict = loadmat(retinal_ganglion_path)
    data_keys = list(retinal_ganglion_dict.keys())
    data_names= [i for i in data_keys if '_' not in i]
    data_dict = {}
    for field_name in data_names:
        data_dict[field_name] = retinal_ganglion_dict[field_name][0]
    return data_dict
def make_raster_plot(spike_train, fig_title):
    N_figures= 1 +len(spike_train)//100
    N_spikes = len(spike_train)
    raster_start = 0
    raster_end   = 100
    fig, axs = plt.subplots(N_figures,1, figsize=(20, 10), facecolor='w', edgecolor='k')
    fig.subplots_adjust(hspace = 1.5, wspace=1)
    i = 0
    while raster_start < N_spikes:
        for n in range(raster_start, raster_end):
            curr_spike = spike_train[n]
            axs[i].plot([curr_spike,curr_spike],[0,1],'b')
            axs[i].set_yticks([],[])
        axs[i].set_xlabel('Time (ms)')
        raster_end += 100
        raster_start+= 100
        if raster_end > N_spikes:
            raster_end = N_spikes-1
        i += 1
    plt.suptitle(fig_title)
    plt.plot()
