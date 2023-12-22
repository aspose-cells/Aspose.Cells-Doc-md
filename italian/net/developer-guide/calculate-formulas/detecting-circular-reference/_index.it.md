---
title: Rilevamento del riferimento circolare
description: Questo articolo illustra come utilizzare la libreria Aspose.Cells per rilevare riferimenti circolari in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare il metodo fornito da Aspose.Cells per rilevare i riferimenti circolari e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /it/net/detecting-circular-reference/
---
##  **introduzione**

Le cartelle di lavoro possono avere riferimenti circolari e talvolta è necessario rilevare se sono presenti o meno riferimenti circolari.

##  **Concetto alla base del rilevamento del riferimento circolare**

riferimenti circolari possono essere rilevati solo quando la formula viene calcolata poiché i riferimenti di una formula dipendono comunemente dal risultato calcolato di altre parti o altre formule. Pertanto forniamo nuove API per questo requisito (per raccogliere celle con riferimenti circolari) nel processo di calcolo della formula:

[**CalcoloCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Rappresenta il calcolo dei dati rilevanti su una cella da calcolare

[**AbstractCalculationMonitor.OnCircular(IEnumerator circolareCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): verrà richiamato dal motore di calcolo delle formule quando si incontrano riferimenti circolari, l'elemento nell'enumeratore è[**CalcoloCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) oggetti che rappresentano tutte le celle in un cerchio. Il valore restituito indica se il motore della formula deve calcolare quelle celle in circolare dopo questa chiamata.

 L'utente può raccogliere tali riferimenti circolari nell'implementazione di[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) metodo.

Il file di esempio sorgente può essere scaricato dal seguente collegamento:

[Formule circolari.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definizione di*CircularMonitor* classe da cui deriva[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) la classe è la seguente:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
