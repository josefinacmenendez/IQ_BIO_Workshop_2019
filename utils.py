from scipy.io import loadmat
from scipy.stats import norm
from scipy.special import gamma, factorial, gammainc
from matplotlib import pyplot as plt

def plot_ISIs(ISIs, n_bins, plot_title):
    plt.hist(ISIs,n_bins, density=True)
    plt.ylabel('Counts')
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

def plot_exponential_dist( pdf_or_cdf_fun, x_vals, lambdas,pdf):
    for lam in lambdas:
        curr_pdf_or_cdf = pdf_or_cdf_fun(x_vals, lam)
        plt.plot(x_vals, curr_pdf_or_cdf)
    legend_vals = ['lambda: ' + str(lam) for lam in lambdas]
    plt.legend(legend_vals)
    plt.xlabel('x')
    if pdf:
        y_label = 'Probability Density'
        fig_title = 'PDF for the exponential distribution'
    else:
        y_label = '$P(X \leq x)$'
        fig_title = 'CDF for the exponential distribution'
    plt.title(fig_title)
    plt.ylabel(y_label)
    plt.show()

def plot_gamma_dist(gamma_pdf_or_cdf, x_vals, ths, ks, pdf, yrange):
    dist_vals = []
    for i in range(len(ths)):
        th = ths[i]
        k  = ks[i]
        curr_dist = gamma_pdf_or_cdf(x_vals, th, k)
        plt.plot(x_vals, curr_dist)
        dist_vals.append(curr_dist[0])
    legend_vals = ['k: ' + str(ks[i]) + r', $\theta$ : ' + str(ths[i]) for i in range(len(ths))]
    plt.legend(legend_vals)
    if pdf:
        fig_title = 'PDF for the Gamma Distribution'
        y_lab     = 'Density'
        ylimrange = [0, 0.5]
    else:
        fig_title = 'CDF for the Gamma Distribution'
        y_lab     = '$P(X \leq x)$'
        ylimrange = [0,1]
    plt.title(fig_title)
    plt.ylabel(y_lab)
    plt.xlabel('x')
    plt.ylim(yrange)
    plt.xlim([0, max(x_vals)])
    plt.show()

def plot_igauss_dist(igauss_pdf_or_cdf, x_vals, lambdas, muvals, pdf, yrange):
    dist_vals = []
    for i in range(len(lambdas)):
        lam = lambdas[i]
        mu  = muvals[i]
        curr_dist = igauss_pdf_or_cdf(x_vals, lam, mu)
        plt.plot(x_vals, curr_dist)
        dist_vals.append(curr_dist[0])
    legend_vals = [r'$\lambda$: ' + str(lambdas[i]) + r', $\mu$ : ' + str(muvals[i]) for i in range(len(muvals))]
    plt.legend(legend_vals)
    if pdf:
        fig_title = 'PDF for the Inverse Gaussian Distribution'
        y_lab     = 'Density'
    else:
        fig_title = 'CDF for the Inverse Gaussian Distribution'
        y_lab     = '$P(X \leq x)$'
        yrange    = [0,1]
    plt.title(fig_title)
    plt.ylabel(y_lab)
    plt.xlabel('x')
    plt.ylim(yrange)
    plt.xlim([0, max(x_vals)])
    plt.show()
