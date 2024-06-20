---
title: Copia righe e colonne di GridWeb
type: docs
weight: 80
url: /it/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb,copia
description: Questo articolo introduce come copiare righe e colonne in GridWeb.
---

{{% alert color="primary" %}} 

Il componente Aspose.Cells.GridWeb offre il modo di copiare righe e colonne utilizzando la classe GridCells. Questo articolo dimostra l'uso delle API esposte da Aspose.Cells.GridWeb per copiare righe e colonne sull'interfaccia di GridWeb. 

I metodi GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows e GridCells.CopyColumns copieranno i contenuti, lo stile e le formule dalla riga e colonna di origine alla destinazione.

{{% /alert %}} 
## **Copia righe e colonne**
Se non sei già a conoscenza del componente Aspose.Cells.GridWeb, ti consigliamo vivamente di controllare l'[Introduzione a Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) e l'articolo dettagliato su [Come aggiungere il componente Aspose.Cells.GridWeb in un'applicazione WebForms](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/).
### **Copia di una singola riga**
Per mantenere l'esempio semplice, l'articolo utilizza un foglio di calcolo esistente con una singola riga e una semplice formula che somma tutti i valori nella riga. Ecco come il foglio di calcolo è visualizzato nell'interfaccia Aspose.Cells.GridWeb prima di copiare la riga.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

Il frammento di codice è semplice come dimostrato di seguito. Accede all'oggetto GridCells del foglio di lavoro attivo per fare una copia della prima riga alla riga successiva.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Ecco come appare Aspose.Cells.GridWeb dopo l'operazione di copia della riga.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Copia di una singola colonna**
Il seguente esempio utilizza un foglio di calcolo esistente con una singola colonna e una semplice formula che somma tutti i valori nella colonna. Ecco come il foglio di calcolo è visualizzato nell'interfaccia Aspose.Cells.GridWeb prima di copiare la colonna.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

Simile all'esempio precedente, il seguente frammento di codice accede all'oggetto GridCells del foglio di lavoro attivo per fare una copia della prima colonna alla colonna successiva.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Ecco come appare Aspose.Cells.GridWeb dopo l'operazione di copia della colonna.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Si può utilizzare i metodi GridCells.CopyRow & GridCells.CopyColumn in un loop per copiare la riga e la colonna di origine su più righe e colonne rispettivamente.

{{% /alert %}} 
### **Copia di più righe**
È anche possibile copiare più righe in una nuova destinazione utilizzando il metodo GridCells.CopyRows, che richiede un parametro aggiuntivo di tipo intero per specificare il numero di righe di origine da copiare.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Ecco come appare Aspose.Cells.GridWeb prima e dopo l'operazione di copia delle colonne.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Copia di più colonne**
La classe GridCells fornisce anche il metodo CopyColumns, che richiede un parametro aggiuntivo di tipo intero per specificare il numero di colonne di origine da copiare.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Ecco come appare Aspose.Cells.GridWeb prima e dopo l'operazione di copia delle colonne.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
