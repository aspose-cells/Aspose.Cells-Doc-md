---
title: Rilevamento di fogli di lavoro vuoti
type: docs
weight: 410
url: /it/net/detecting-empty-worksheets/
---
## **Controlla Popolato Cells**

 fogli di lavoro possono avere una o più celle popolate con valori in cui un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su una formula. In tal caso, è facile rilevare se un determinato foglio di lavoro è vuoto o meno. Tutto quello che dobbiamo controllare è il[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) o[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)proprietà. Se le suddette proprietà restituiscono valori zero o positivi, significa che una o più celle sono state popolate, tuttavia, se una di queste proprietà restituisce -1 che indica che nessuna delle celle è stata popolata nel foglio di lavoro specificato.

{{% alert color="primary" %}}

Le raccolte di righe e colonne hanno un indice in base zero, quindi una cella alla riga 0 e alla colonna 0 indica la prima cella nel foglio di lavoro, che è A1.

{{% /alert %}}

## **Verificare la presenza di vuoto inizializzato Cells**

 Tutte le celle che hanno valori vengono inizializzate automaticamente, tuttavia, esiste la possibilità che un foglio di lavoro abbia celle con solo la formattazione applicata. In uno scenario del genere, il[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)o[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) properties restituirà -1 che indica l'assenza di valori popolati ma le celle inizializzate a causa della formattazione delle celle non possono essere rilevate utilizzando questo approccio. Per verificare se un foglio di lavoro ha celle inizializzate vuote, si consiglia di utilizzare il metodo IEnumerator.MoveNext sull'enumeratore acquisito da[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Se il metodo IEnumerator.MoveNext restituisce**VERO** ciò significa che ci sono una o più celle inizializzate nel foglio di lavoro specificato.

## **Controlla le forme**

 È possibile che un determinato foglio di lavoro non contenga celle popolate, tuttavia potrebbe contenere forme e oggetti come controlli, grafici, immagini e così via. Se dobbiamo verificare se un foglio di lavoro contiene una forma, possiamo farlo ispezionando il file[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)proprietà. Qualsiasi valore positivo indica la presenza di forme nel foglio di lavoro.

## **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
