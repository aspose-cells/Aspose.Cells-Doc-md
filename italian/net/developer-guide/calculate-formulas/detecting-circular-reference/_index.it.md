---
title: Rilevamento del riferimento circolare
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per rilevare i riferimenti circolari in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare il metodo fornito da Aspose.Cells per rilevare i riferimenti circolari e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, riferimenti circolari, rilevamento
type: docs
weight: 70
url: /it/net/detecting-circular-reference/
---

## **Introduzione**

I workbooks possono avere riferimenti circolari e a volte c'è la necessità di rilevare se ci sono o meno riferimenti circolari.

## **Concetto alla base del rilevamento del riferimento circolare**

I riferimenti circolari possono essere rilevati solo quando la formula viene calcolata poiché i riferimenti di una formula dipendono comunemente dal risultato calcolato di altre parti o altre formule. Quindi forniamo nuove API per questo requisito (per raccogliere celle con riferimenti circolari) nel processo di calcolo delle formule:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Rappresenta il calcolo dei dati pertinenti su una cella in fase di calcolo

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): verrà invocato dall'interprete di calcolo della formula quando si incontrano riferimenti circolari, l'elemento nell'enumeratore è [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) oggetti che rappresentano tutte le celle in un cerchio. Il valore restituito indica se il motore di formule deve calcolare queste celle in modo circolare dopo questa chiamata.

L'utente può raccogliere quei riferimenti circolari nell'implementazione del metodo [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular).

Il file di esempio di origine può essere scaricato dal seguente link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

La definizione della classe *CircularMonitor*, derivata dalla classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor), è la seguente:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
