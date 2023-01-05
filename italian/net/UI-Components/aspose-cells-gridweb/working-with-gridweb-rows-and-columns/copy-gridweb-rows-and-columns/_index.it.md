---
title: Copia righe e colonne GridWeb
type: docs
weight: 80
url: /it/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Il componente Aspose.Cells.GridWeb offre i mezzi per copiare riga e colonna durante l'utilizzo della classe GridCells. Questo articolo illustra l'utilizzo delle API esposte da Aspose.Cells.GridWeb per copiare righe e colonne nell'interfaccia GridWeb.

I metodi GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows e GridCells.CopyColumns copieranno il contenuto, lo stile e le formule dalla riga e dalla colonna di origine alla destinazione.

{{% /alert %}} 
## **Copia di righe e colonne**
 Se non conosci già il componente Aspose.Cells.GridWeb, ti consigliamo vivamente di controllare il[Introduzione a Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) e articolo dettagliato su[Come aggiungere il componente Aspose.Cells.GridWeb in un'applicazione WebForms](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Copia di una singola riga**
Per semplificare l'esempio, l'articolo utilizza un foglio di calcolo esistente con una riga e una semplice formula che somma tutti i valori nella riga. Ecco come viene visualizzato il foglio di calcolo nell'interfaccia Aspose.Cells.GridWeb prima di copiare la riga.

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_1.png)

Il frammento di codice è semplice come dimostrato di seguito. Accede all'oggetto GridCells dell'ordine del foglio di lavoro attivo per eseguire una copia della prima riga nella riga successiva.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Ecco come Aspose.Cells.GridWeb si occupa dell'operazione di copia riga.

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_2.png)
### **Copia di una singola colonna**
L'esempio seguente utilizza un foglio di calcolo esistente con una colonna e una formula semplice che somma tutti i valori nella colonna. Ecco come viene visualizzato il foglio di calcolo nell'interfaccia Aspose.Cells.GridWeb prima di copiare la colonna.

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_3.png)

Analogamente all'esempio precedente, il seguente frammento di codice accede all'oggetto GridCells dell'ordine del foglio di lavoro attivo per creare una copia della prima colonna nella colonna successiva.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Ecco come Aspose.Cells.GridWeb si occupa dell'operazione di copia della colonna.

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

È possibile utilizzare i metodi GridCells.CopyRow e GridCells.CopyColumn in loop per copiare rispettivamente la riga e la colonna di origine su più righe e colonne.

{{% /alert %}} 
### **Copia di più righe**
È anche possibile copiare più righe in una nuova destinazione utilizzando il metodo GridCells.CopyRows, che accetta un parametro aggiuntivo di tipo integer per specificare il numero di righe di origine da copiare.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Ecco come appare Aspose.Cells.GridWeb prima e dopo l'operazione di copia delle righe.

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_5.png)

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_6.png)
### **Copia di più colonne**
La classe GridCells fornisce anche il metodo CopyColumns, che accetta un parametro aggiuntivo di tipo integer per specificare il numero di colonne di origine da copiare.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Ecco come appare Aspose.Cells.GridWeb prima e dopo l'operazione di copia delle righe.

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_7.png)

![cose da fare:immagine_alt_testo](copy-gridweb-rows-and-columns_8.png)
