def codonSelection(str:inputA, str:inputT,str:inputG, str:inputC, str:plot): -> list[str]
    codonA = [i for i in codon if i.startswith("A")]
    codonT = [i for i in codon if i.startswith("T")]
    codonT = [i for i in codon if i.startswith("G")]
    codonG = [i for i in codon if i.startswith("C")]
    plot_type = ['box', 'violin', 'swarm']
    selectedA =[]
    for i in range(len(codonA)):
        if codonA[i] == inputA:
            selectedA.append(inputA)
    selectedT =[]
    for i in range(len(codonT)):
        if codonT[i] == inputT:
            selectedT.append(inputT)
    selectedG =[]
    for i in range(len(codonG)):
        if codonG[i] == inputG:
            selectedG.append(inputT)
    selectedC =[]
    for i in range(len(codonC)):
        if codonC[i] == inputC:
            selectedC.append(inputC)   
    final_matrix = [selectedA, selectedT, selectedG, selectedC]
    bicodon_rates = [[i for i in bicodonA if bicodonA],\
          [i for i in bicodonT if bicodonT],\
          [i for i in bicodonG if bicodonG], \
          [i for i in bicodonC if bicodonC]]
    for i in plot_type:
        if i and plot == "box":
            upset = UpSetPlotly(samples=bicodon_rates, 
                sample_names=final_matrix, 
                order_by='decreasing',plot_type='box')
                usp.plot()
        elif i and plot == "violin":
            upset = UpSetPlotly(samples=bicodon_rates, 
                sample_names=final_matrix, 
                order_by='decreasing',plot_type='violin')
                usp.plot()
        elif i and plot == "swarm":
            upset = UpSetPlotly(samples=bicodon_rates, 
                sample_names=final_matrix, 
                order_by='decreasing',plot_type='swarm')
                usp.plot()
        else:
            None
