---
title: Rilevamento del riferimento circolare
type: docs
weight: 70
url: /it/java/detecting-circular-reference/
---

## **Introduzione**

I workbooks possono avere riferimenti circolari e a volte c'è la necessità di rilevare se ci sono o meno riferimenti circolari.

## **Concetto alla base del rilevamento del riferimento circolare**

I riferimenti circolari possono essere rilevati solo quando la formula viene calcolata poiché i riferimenti di una formula dipendono comunemente dal risultato calcolato di altre parti o altre formule. Quindi forniamo nuove API per questo requisito (per raccogliere celle con riferimenti circolari) nel processo di calcolo delle formule:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Rappresenta il calcolo dei dati pertinenti su una cella in fase di calcolo

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): verrà invocato dall'interprete di calcolo della formula quando si incontrano riferimenti circolari, l'elemento nell'enumeratore è [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) oggetti che rappresentano tutte le celle in un cerchio. Il valore restituito indica se il motore di formule deve calcolare queste celle in modo circolare dopo questa chiamata.

L'utente può raccogliere quei riferimenti circolari nell'implementazione del metodo [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-).

Il file di esempio di origine può essere scaricato dal seguente link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

La definizione della classe *CircularMonitor*, derivata dalla classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor), è la seguente:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
