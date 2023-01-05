---
title: Rilevamento del riferimento circolare
type: docs
weight: 70
url: /it/java/detecting-circular-reference/
---
## **introduzione**

Le cartelle di lavoro possono avere riferimenti circolari e talvolta è necessario rilevare se i riferimenti circolari sono presenti o meno.

## **Concetto alla base del rilevamento del riferimento circolare**

riferimenti circolari possono essere rilevati solo quando la formula viene calcolata perché i riferimenti di una formula dipendono comunemente dal risultato calcolato di altre parti o altre formule. Quindi forniamo nuove API per questo requisito (per raccogliere celle con riferimenti circolari) nel processo di calcolo della formula:

[**CalcoloCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Rappresenta il calcolo dei dati rilevanti su una cella calcolata

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): verrà richiamato dal motore di calcolo della formula quando incontra riferimenti circolari, l'elemento nell'enumeratore è[**CalcoloCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) oggetti che rappresentano tutte le celle in un cerchio. Il valore restituito indica se il motore delle formule deve calcolare tali celle in forma circolare dopo questa chiamata.

 L'utente può raccogliere tali riferimenti circolari nell'attuazione di[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) metodo.

Il file di esempio sorgente può essere scaricato dal seguente link:

[Formule circolari.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Definizione di*Monitor circolare* classe da cui deriva[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) classe è la seguente:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
