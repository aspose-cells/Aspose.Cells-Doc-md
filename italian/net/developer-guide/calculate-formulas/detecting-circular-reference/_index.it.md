---
title: Rilevamento del riferimento circolare
type: docs
weight: 70
url: /it/net/detecting-circular-reference/
---
## **introduzione**

Le cartelle di lavoro possono avere riferimenti circolari e talvolta è necessario rilevare se i riferimenti circolari sono presenti o meno.

## **Concetto alla base del rilevamento del riferimento circolare**

I riferimenti circolari possono essere rilevati solo quando la formula viene calcolata perché i riferimenti di una formula dipendono comunemente dal risultato calcolato di altre parti o altre formule. Quindi forniamo nuove API per questo requisito (per raccogliere celle con riferimenti circolari) nel processo di calcolo della formula:

[**CalcoloCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Rappresenta il calcolo dei dati rilevanti su una cella calcolata

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): verrà richiamato dal motore di calcolo della formula quando incontra riferimenti circolari, l'elemento nell'enumeratore è[**CalcoloCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) oggetti che rappresentano tutte le celle in un cerchio. Il valore restituito indica se il motore delle formule deve calcolare tali celle in forma circolare dopo questa chiamata.

L'utente può raccogliere tali riferimenti circolari nell'attuazione di[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) metodo.

Il file di esempio sorgente può essere scaricato dal seguente link:

[Formule circolari.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

 Definizione di*Monitor circolare* classe da cui deriva[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) classe è la seguente:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
