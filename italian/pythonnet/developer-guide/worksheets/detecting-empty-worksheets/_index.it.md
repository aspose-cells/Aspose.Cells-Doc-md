---
title: Rilevamento di fogli di lavoro vuoti
type: docs
weight: 410
url: /it/python-net/detecting-empty-worksheets/
description: Questo articolo ti mostra i codici che spiegano come rilevare i fogli di lavoro vuoti dei fogli di lavoro di Excel in modo programmato utilizzando la libreria Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, rileva il foglio di lavoro vuoto utilizzando Python, trova il foglio di lavoro Excel vuoto in Python.
---

## **Controllare le celle popolate**

I fogli di lavoro possono avere una o più celle popolate con valori in cui un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su formula. In tal caso, è facile individuare se un determinato foglio di lavoro è vuoto o meno. Tutto ciò che dobbiamo fare è controllare le proprietà [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) o [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/). Se le proprietà suddette restituiscono zero o valori positivi ciò significa che una o più celle sono state popolate, tuttavia, se una qualsiasi di queste proprietà restituisce -1 ciò indica che nessuna delle celle è stata popolata nel foglio di lavoro fornito.

{{% alert color="primary" %}}

Le raccolte righe e colonne hanno un indice a base zero quindi una cella nella riga 0 e colonna 0 significa la prima cella nel foglio di lavoro, che è A1.

{{% /alert %}}

## **Controllare le celle inizializzate vuote**

Tutte le celle che hanno valori vengono inizializzate automaticamente, tuttavia, c'è la possibilità che un foglio di lavoro abbia celle a cui è stata applicata solo la formattazione. In questo caso, le proprietà [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) o [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) restituiranno -1 indicando l'assenza di valori popolati ma celle inizializzate a causa della formattazione delle celle non possono essere rilevate utilizzando questo approccio. Per verificare se un foglio di lavoro ha celle inizializzate vuote, è consigliabile utilizzare il metodo IEnumerator.MoveNext sull'enumeratore acquisito dalla raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Se il metodo IEnumerator.MoveNext restituisce **vero** significa che ci sono una o più celle inizializzate nel foglio di lavoro dato.

## **Controllare le forme**

È possibile che un determinato foglio di lavoro non abbia celle popolate, tuttavia, potrebbe contenere forme e oggetti come controlli, grafici, immagini e così via. Se abbiamo bisogno di verificare se un foglio di lavoro contiene una forma, possiamo farlo ispezionando gli elementi [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection). Qualsiasi valore positivo indica la presenza di forme nel foglio di lavoro.

## **Esempio di programmazione**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
