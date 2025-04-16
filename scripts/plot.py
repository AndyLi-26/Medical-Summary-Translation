import numpy as np
import matplotlib.pyplot as plt

# Sample data
categories = ['BLEU', 'CHR-F', 'METEOR']
models = ['GPT', 'LLAMA', 'GEMMA', 'MS', 'GTrans', 'DL']
value1 =[
[0.6535880223, 0.594651762, 0.6051478851, 0.6404740013, 0.6528038142, 0.6522730427 ],
[0.5063892422, 0.4562358983, 0.4692732105, 0.507806089, 0.5151491002, 0.5155593379 ],
[0.3166049423, 0.2568037157, 0.2809734945, 0.328892702, 0.3398578304, 0.3048132733 ]
]

value2=[
[0.6300378261, 0.6028503223, 0.6005968566, 0.6148840764, 0.6786785139, 0.6692481909],
[0.4956742543, 0.472642631, 0.4768190131, 0.5004898567, 0.5907404444, 0.5422944268],
[0.3342921863, 0.3575409986, 0.368236762, 0.4011563899, 0.498790895, 0.4171445194]
]

value3=[
[0.4265599202, 0.4164106729, 0.5226994167, 0.5017766035, 0.4358197828, 0.4321728751],
[0.4165222201, 0.3909694784, 0.43919699, 0.419342954, 0.370945107, 0.384362597],
[0.4698167041, 0.5033136853, 0.5678417998, 0.5169138528, 0.4564426512, 0.5096587199]
]

value4=[
[0.2661694444, 0.2421856219, 0.2466107012, 0.2392866375, 0.2595962692, 0.2603372181],
#[0.4165222201, 0.3909694784, 0.43919699, 0.419342954, 0.370945107, 0.384362597],
[0.2870905816457497, 0.23866044094215164, 0.25756932208195893, 0.2426979175708668, 0.272898818208975, 0.252581298979798],
[0.3055361212, 0.3347215544, 0.3394492593, 0.3294170887, 0.3348786882, 0.3331397524]
]

value5=[
[0.7187980562, 0.7516993263, 0.7457576096, 0.7463707256, 0.7718824345],
[0.5956111067, 0.5978711947, 0.5956753335, 0.5864217125, 0.6184064952],
[0.5566201054, 0.5893869532, 0.5488933473, 0.5372961879, 0.5908364986]
]

value6=[
[0.685745816, 0.744072695, 0.7118488173, 0.7059234392, 0.7325217087],
[0.5493715543, 0.6054525741, 0.6129926929, 0.5861539087, 0.625168901],
[0.4652498297, 0.4787032853, 0.539867683, 0.5221585821, 0.574383188]
]

values_list=[value1,value3,value5,value2, value4,value6]
lan=["Arabic","Simplified Chinese","Vietnamese"]



# Bar width and positions
x = np.arange(len(categories))
width = 0.1  # Adjust for spacing

# Define colors
colors = ['darkred', 'red', 'orange', 'blue', 'dodgerblue', 'cadetblue']

fig, axs = plt.subplots(2, 3, figsize=(18, 10), sharey=True)
axs = axs.flatten()

for idx, ax in enumerate(axs):
    values = values_list[idx]
    x = np.arange(len(categories))
    width = 0.12

    # Plot each model
    for i, model in enumerate(models):
        #print(idx,i)
        if idx in [2,5] and i==5: continue
        ax.bar(x + (i - len(models)/2) * width, [values[j][i] for j in range(len(categories))],
               width*0.9, label=model, color=colors[i])

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.set_ylim(0, 0.8)
    temp1="Simple" if idx<=2 else "Complex"
    ax.set_title(f'{temp1} Summary in {lan[idx%3]}', fontsize=16)
    if idx==0:
        ax.legend()


# Create a single legend at the bottom
handles, labels = axs[0].get_legend_handles_labels()
#fig.legend(handles,labels)
#fig.legend(handles, labels, loc='lower center',
#           bbox_to_anchor=(0.5, 0.02), ncol=len(models), fontsize=14)

plt.tight_layout(rect=[0, 0.05, 1, 1])  # Leave space for legend
plt.show()
