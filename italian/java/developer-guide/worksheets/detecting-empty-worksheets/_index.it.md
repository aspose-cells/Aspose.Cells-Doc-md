---
title: Rilevamento di fogli di lavoro vuoti
type: docs
weight: 710
url: /it/java/detecting-empty-worksheets/
---

## **Controllare le celle popolate**
I fogli di lavoro possono avere una o più celle popolate con valori in cui un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su una formula. In tal caso, è facile rilevare se un dato foglio di lavoro è vuoto o meno. Tutto ciò che dobbiamo controllare sono le proprietà [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) o [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn). Se le suddette proprietà restituiscono zero o valori positivi, ciò significa che una o più celle sono state popolate, tuttavia, se una qualsiasi di queste proprieta restituisce -1, ciò indica che nessuna delle celle è stata popolata nel dato foglio di lavoro.

{{% alert color="primary" %}} 

Le collezioni di righe e colonne hanno un indice in base zero, quindi una cella alla riga 0 e colonna 0 significa la prima cella nel foglio di lavoro, che corrisponde ad A1.

{{% /alert %}} 
## **Controllare le celle inizializzate vuote**
Tutte le celle con valori vengono automaticamente inizializzate, tuttavia, c'è la possibilità che un foglio di lavoro abbia celle con solo formattazione applicata. In uno scenario del genere, le proprietà [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) o [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) restituiranno -1 indicando l'assenza di valori popolati ma le celle inizializzate a causa della formattazione delle celle non possono essere rilevate tramite questo approccio. Per verificare se un foglio di lavoro ha celle inizializzate vuote, è consigliabile utilizzare il metodo *Iterator.hasNext* sull'iteratore acquisito dalla collezione Cells. Se il metodo *iterator.hasNext* restituisce true, ciò significa che ci sono una o più celle inizializzate nel dato foglio di lavoro.

{{% alert color="primary" %}} 

Ci sono diverse modalità per acquisire l'enumeratore delle celle come dettagliato in [Come e dove utilizzare gli iteratori](/cells/it/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Controllare le forme**
È possibile che un dato foglio di lavoro non abbia alcune celle popolate, tuttavia, potrebbe contenere forme e oggetti come controlli, grafici, immagini e così via. Se è necessario verificare se un foglio di lavoro contiene qualche forma, è possibile farlo ispezionando la proprietà [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count). Qualsiasi valore positivo indica la presenza di forma(e) nel foglio di lavoro.
## **Esempio di programmazione**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
