---
title: Creazione dei subtotali
type: docs
weight: 800
url: /it/python-net/creating-subtotals/
description: Scopri come creare subtotali per qualsiasi valore ripetuto in un foglio di calcolo utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Applica subtotali, Imposta subtotali, Aggiungi subtotali, Crea subtotali, Come aggiungere subtotali a un foglio di lavoro 
---

{{% alert color="primary" %}}

Puoi creare automaticamente subtotali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells per Python via .NET fornisce funzionalità API che ti aiutano ad aggiungere subtotali ai fogli di calcolo in modo programmato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiungere subtotali in Microsoft Excel:

1. Crea una semplice lista di dati nel primo foglio di lavoro del documento (come mostrato nella figura qui sotto) e salva il file come Book1.xls.
1. Seleziona una qualsiasi cella all'interno della tua lista.
1. Dal menu **Dati**, seleziona **Subtotali**. Verrà visualizzata la finestra di dialogo Subtotali. Definisci quale funzione utilizzare e dove inserire i subtotali.

## **Utilizzando l'API Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta di [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente l'accesso a ogni foglio di lavoro nel file di Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro e di altri oggetti. Ogni foglio di lavoro è composto da una raccolta di [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Per aggiungere subtotali a un foglio di lavoro, utilizza il metodo [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) della classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Fornisci valori di parametro al metodo per specificare come il totale parziale deve essere calcolato e posizionato.

Nei seguenti esempi, abbiamo aggiunto subtotali al primo foglio di lavoro del file di modello (Book1.xls) utilizzando l'API Aspose.Cells per Python via .NET. Quando il codice viene eseguito, viene creato un foglio di lavoro con i subtotali.

I frammenti di codice seguenti mostrano come aggiungere subtotali a un foglio di lavoro con Aspose.Cells per Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **Argomenti avanzati**
- [Applicazione Subtotale e Modifica della Direzione delle Righe di Riepilogo dell'Outline sotto i Dettagli](/cells/it/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
{{< app/cells/assistant language="python-net" >}}
