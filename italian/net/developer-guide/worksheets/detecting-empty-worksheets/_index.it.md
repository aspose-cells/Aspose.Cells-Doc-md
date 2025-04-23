---
title: Rilevamento di fogli di lavoro vuoti
type: docs
weight: 410
url: /it/net/detecting-empty-worksheets/
description: Questo articolo ti mostra del codice che spiega come individuare i fogli di lavoro vuoti dei fogli di lavoro di Excel in modo programmato utilizzando l API C# con la libreria .NET.
keywords: individuare il foglio di lavoro vuoto c#, trovare il foglio di lavoro excel vuoto c#
---

## **Controllare le celle popolate**

I fogli di lavoro possono avere una o più celle popolate con valori in cui un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su formula. In tal caso, è facile individuare se un determinato foglio di lavoro è vuoto o meno. Tutto ciò che dobbiamo fare è controllare le proprietà [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn). Se le proprietà suddette restituiscono zero o valori positivi ciò significa che una o più celle sono state popolate, tuttavia, se una qualsiasi di queste proprietà restituisce -1 ciò indica che nessuna delle celle è stata popolata nel foglio di lavoro fornito.

{{% alert color="primary" %}}

Le raccolte righe e colonne hanno un indice a base zero quindi una cella nella riga 0 e colonna 0 significa la prima cella nel foglio di lavoro, che è A1.

{{% /alert %}}

## **Controllare le celle inizializzate vuote**

Tutte le celle che hanno valori vengono inizializzate automaticamente, tuttavia, c'è la possibilità che un foglio di lavoro abbia celle con solo la formattazione applicata. In uno scenario del genere, le proprietà [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) restituiranno -1 indicando l'assenza di valori popolati ma le celle inizializzate a causa della formattazione delle celle non possono essere individuate utilizzando questo approccio. Per verificare se un foglio di lavoro ha celle vuote inizializzate, si consiglia di utilizzare il metodo IEnumerator.MoveNext sull'enumeratore acquisito dalla raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Se il metodo IEnumerator.MoveNext restituisce **true** ciò significa che ci sono una o più celle inizializzate nel foglio di lavoro fornito.

## **Controllare le forme**

È possibile che un determinato foglio di lavoro non abbia celle popolate, tuttavia potrebbe contenere forme e oggetti come elementi di controllo, grafici, immagini e così via. Se abbiamo bisogno di verificare se un foglio di lavoro contiene una qualsiasi forma, possiamo farlo ispezionando la proprietà [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection). Qualsiasi valore positivo indica la presenza di una o più forme nel foglio di lavoro.

## **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
