---
title: Creazione di grafici dinamici
description: Scopri come creare grafici dinamici in Aspose.Cells per Python via .NET. La nostra guida ti mostrerà come aggiornare dinamicamente i dati del grafico, le serie e la formattazione in base alle tue esigenze, permettendoti di presentare dati mutevoli visivamente nei tuoi fogli di lavoro.
keywords: Aspose.Cells per Python via .NET, diagrammi, grafici dinamici, dati, serie, formattazione, fogli di lavoro, aggiornamenti.
type: docs
weight: 240
url: /it/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

I grafici dinamici (o interattivi) hanno la capacità di cambiare quando si cambia l'ambito dei dati. In altre parole, i grafici dinamici possono riflettere automaticamente i cambiamenti quando viene modificata la fonte dati. Per innescare il cambiamento nella fonte dati, è possibile utilizzare l'opzione di filtraggio delle tabelle di Excel o utilizzare un controllo come ComboBox o elenco a discesa.

Questo articolo dimostra l’utilizzo delle API di Aspose.Cells per Python via .NET per creare grafici dinamici usando entrambi gli approcci sopra menzionati.

{{% /alert %}}

## **Utilizzo delle tabelle di Excel**

{{% alert color="primary" %}}

Le tabelle Excel sono chiamate ListObjects in prospettiva di Aspose.Cells, pertanto utilizzeremo il termine "ListObject" invece di "Tabella" per chiarezza. Leggi in dettaglio come [creare ListObjects](/cells/it/python-net/create-and-format-table/) con le API di Aspose.Cells per Python via .NET.

{{% /alert %}}

ListObjects fornisce la funzionalità integrata per ordinare e filtrare i dati tramite interazione dell'utente. Entrambe le opzioni di ordinamento e filtro sono fornite attraverso i menu a tendina che vengono aggiunti automaticamente alla riga di intestazione. Grazie a queste funzionalità (ordinamento e filtro), il [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) sembra essere il candidato ideale per fungere da sorgente dati per un grafico dinamico perché, quando si cambia l'ordinamento o il filtro, la rappresentazione dei dati nel grafico verrà modificata per riflettere lo stato attuale del  .

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) vuoto.
1. Accedere al [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) del primo [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) nel [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Inserire alcuni dati nelle celle.
1. Creare [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) basato sui dati inseriti.
1. Creare [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basato sull'intervallo di dati di [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject).
1. Salvare il risultato sul disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **Utilizzo di Formule Dinamiche**

Nel caso in cui non si desideri utilizzare il [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) come fonte dati per il grafico dinamico, l'altra opzione è utilizzare le funzioni di Excel (o formule) per creare un intervallo dinamico di dati e un controllo (come ComboBox) per innescare il cambiamento dei dati. In questo scenario, utilizzeremo la funzione VLOOKUP per recuperare i valori appropriati in base alla selezione di ComboBox. Quando viene cambiata la selezione, la funzione VLOOKUP aggiornerà il valore della cella. Se un intervallo di celle sta utilizzando la funzione VLOOKUP, l'intero intervallo può essere aggiornato all'interazione dell'utente, quindi può essere utilizzato come fonte per il grafico dinamico.

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il Workbook da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) vuoto.
1. Accedere al [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) del primo [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) nel [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Inserire alcuni dati nelle celle creando un Named Range. Questi dati fungeranno da serie per il grafico dinamico.
1. Creare [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) basato sul Named Range creato nel passo precedente.
1. Inserire ulteriori dati nelle celle che fungeranno da fonte per la funzione VLOOKUP.
1. Inserire la funzione VLOOKUP (con i parametri appropriati) in un intervallo di celle. Questo intervallo servirà come origine per il grafico dinamico.
1. Creare [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basato sull'intervallo creato nel passo precedente.
1. Salvare il risultato sul disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
{{< app/cells/assistant language="python-net" >}}
