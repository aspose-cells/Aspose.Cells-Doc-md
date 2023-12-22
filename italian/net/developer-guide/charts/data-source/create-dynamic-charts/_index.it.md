---
title: Crea grafici dinamici
description: Scopri come creare grafici dinamici al numero Aspose.Cells for .NET. La nostra guida ti mostrerà come aggiornare dinamicamente i dati, le serie e la formattazione del grafico in base alle tue esigenze, consentendoti di presentare visivamente i dati che cambiano nei tuoi fogli di lavoro.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /it/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

I grafici dinamici (o interattivi) hanno la possibilità di cambiare quando si modifica l'ambito dei dati. In altre parole, i grafici dinamici possono riflettere automaticamente le modifiche quando viene modificata l'origine dati. Per attivare la modifica nell'origine dati, è possibile utilizzare l'opzione di filtro delle tabelle Excel o utilizzare un controllo come ComboBox o elenco a discesa.

Questo articolo dimostra l'utilizzo delle API Aspose.Cells for .NET per creare grafici dinamici utilizzando entrambi gli approcci sopra menzionati.

{{% /alert %}}

##  **Utilizzo di tabelle Excel**

{{% alert color="primary" %}}

 Le tabelle di Excel vengono chiamate ListObjects nella prospettiva Aspose.Cells, pertanto utilizzeremo il termine "ListObject" anziché "Tabella" per chiarezza. Si prega di leggere in dettaglio come farlo[creare ListObjects](/cells/it/net/create-and-format-table/)con Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects fornisce la funzionalità integrata per ordinare e filtrare i dati in base all'interazione dell'utente. Entrambe le opzioni di ordinamento e filtro vengono fornite tramite gli elenchi a discesa che vengono aggiunti automaticamente alla riga di intestazione del file[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . A causa di queste funzionalità (ordinamento e filtraggio), il file[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) sembra essere il candidato perfetto per fungere da origine dati per un grafico dinamico perché quando si modifica l'ordinamento o il filtro, la rappresentazione dei dati nel grafico verrà modificata per riflettere lo stato corrente del[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Per mantenere la dimostrazione semplice da comprendere, creeremo il file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)da zero e procedere passo dopo passo come descritto di seguito.

1.  Crea un vuoto[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Accedi al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primo[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nel[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserisci alcuni dati nelle celle.
1.  Creare[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)in base ai dati inseriti.
1.  Creare[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) in base all'intervallo di dati di[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Salvare il risultato sul disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **Utilizzo di formule dinamiche**

Nel caso in cui non desideri utilizzare il file[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)come origine dati per il grafico dinamico, l'altra opzione è utilizzare le funzioni (o formule) di Excel per creare un intervallo dinamico di dati e un controllo (come ComboBox) per attivare la modifica dei dati. In questo scenario, utilizzeremo la funzione CERCA.VERT per recuperare i valori appropriati in base alla selezione di ComboBox. Quando la selezione viene modificata, la funzione CERCA.VERT aggiornerà il valore della cella. Se un intervallo di celle utilizza la funzione CERCA.VERT, l'intero intervallo può essere aggiornato dopo l'interazione dell'utente, quindi può essere utilizzato come origine per il grafico dinamico.

Per mantenere la dimostrazione semplice da comprendere, creeremo la cartella di lavoro da zero e procederemo passo dopo passo come indicato di seguito.

1.  Crea un vuoto[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Accedi al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primo[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nel[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserisci alcuni dati nelle celle creando un intervallo denominato. Questi dati serviranno come una serie per il grafico dinamico.
1.  Creare[**Casella combinata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)in base all'intervallo denominato creato nel passaggio precedente.
1. Inserisci altri dati nelle celle che fungeranno da fonte per la funzione CERCA.VERT.
1. Inserisci la funzione CERCA.VERT (con parametri appropriati) in un intervallo di celle. Questo intervallo servirà come fonte per il grafico dinamico.
1.  Creare[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)in base all'intervallo creato nel passaggio precedente.
1. Salvare il risultato sul disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
