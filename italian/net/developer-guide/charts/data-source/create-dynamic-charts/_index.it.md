---
title: Creazione di grafici dinamici
description: Scopri come creare grafici dinamici in Aspose.Cells for .NET. La nostra guida ti mostrerà come aggiornare dinamicamente i dati, le serie e la formattazione del grafico in base alle tue esigenze, consentendoti di presentare visivamente i dati in continua evoluzione nei tuoi fogli di lavoro.
keywords: Aspose.Cells for .NET, creazione di grafici dinamici, dati, serie, formattazione, fogli di lavoro, aggiornamento.
type: docs
weight: 240
url: /it/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

I grafici dinamici (o interattivi) hanno la capacità di cambiare quando si cambia l'ambito dei dati. In altre parole, i grafici dinamici possono riflettere automaticamente i cambiamenti quando viene modificata la fonte dati. Per innescare il cambiamento nella fonte dati, è possibile utilizzare l'opzione di filtraggio delle tabelle di Excel o utilizzare un controllo come ComboBox o elenco a discesa.

Questo articolo dimostra l'uso di Aspose.Cells for .NET API per creare grafici dinamici utilizzando entrambi gli approcci suddetti.

{{% /alert %}}

## **Utilizzo delle tabelle di Excel**

{{% alert color="primary" %}}

Le tabelle di Excel sono indicate come ListObjects in prospettiva di Aspose.Cells, quindi useremo il termine "ListObject" invece di "Tabella" per chiarezza. Si prega di leggere in dettaglio come [creare ListObjects](/cells/it/net/create-and-format-table/) con Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects fornisce la funzionalità integrata per ordinare e filtrare i dati all'interazione dell'utente. Entrambe le opzioni di ordinamento e filtraggio vengono fornite tramite elenchi a discesa che vengono automaticamente aggiunti alla riga dell'intestazione del [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject). A causa di queste caratteristiche (ordinamento e filtraggio), il [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) sembra essere il candidato perfetto per fungere da fonte dati per un grafico dinamico perché quando l'ordinamento o il filtraggio viene modificato, la rappresentazione dei dati nel grafico verrà modificata per riflettere lo stato attuale del [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) vuoto.
1. Accedere al [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primo [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nel [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserire alcuni dati nelle celle.
1. Creare [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) basato sui dati inseriti.
1. Creare [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basato sull'intervallo di dati di [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Salvare il risultato sul disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Utilizzo di Formule Dinamiche**

Nel caso in cui non si desideri utilizzare il [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) come fonte dati per il grafico dinamico, l'altra opzione è utilizzare le funzioni di Excel (o formule) per creare un intervallo dinamico di dati e un controllo (come ComboBox) per innescare il cambiamento dei dati. In questo scenario, utilizzeremo la funzione VLOOKUP per recuperare i valori appropriati in base alla selezione di ComboBox. Quando viene cambiata la selezione, la funzione VLOOKUP aggiornerà il valore della cella. Se un intervallo di celle sta utilizzando la funzione VLOOKUP, l'intero intervallo può essere aggiornato all'interazione dell'utente, quindi può essere utilizzato come fonte per il grafico dinamico.

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il Workbook da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) vuoto.
1. Accedere al [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primo [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nel [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserire alcuni dati nelle celle creando un Named Range. Questi dati fungeranno da serie per il grafico dinamico.
1. Creare [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) basato sul Named Range creato nel passo precedente.
1. Inserire ulteriori dati nelle celle che fungeranno da fonte per la funzione VLOOKUP.
1. Inserire la funzione VLOOKUP (con i parametri appropriati) in un intervallo di celle. Questo intervallo servirà come origine per il grafico dinamico.
1. Creare [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basato sull'intervallo creato nel passo precedente.
1. Salvare il risultato sul disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
