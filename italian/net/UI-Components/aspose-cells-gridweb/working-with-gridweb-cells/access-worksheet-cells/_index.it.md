---
title: Accesso alla Cellula del Foglio di Lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: Questo articolo introduce come ottenere la cella (GridCell) in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento discute delle celle, analizzando la caratteristica più basilare di Aspose.Cells.GridWeb: l'accesso alle celle.

{{% /alert %}} 
## **Accesso alle Celle in un Foglio di Lavoro**
Ogni foglio di lavoro contiene una proprietà chiamata Cells che è effettivamente una collezione di oggetti GridCell dove un oggetto GridCell rappresenta una cella in Aspose.Cells.GridWeb. È possibile accedere a qualsiasi cella utilizzando Aspose.Cells.GridWeb. Ci sono due metodi preferiti, ognuno dei quali è discusso di seguito.


### **Utilizzo del nome della cella**
Tutte le celle hanno un nome univoco. Ad esempio, A1, A2, B1, B2, ecc. Aspose.Cells.GridWeb consente agli sviluppatori di accedere a qualsiasi cella desiderata utilizzando il nome della cella. Basta passare il nome della cella (come un indice) alla collezione Cells di GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Avviso**

Accedere a GridCell usando cells[cellName] può consumare più memoria. Creerà sempre un nuovo oggetto cella (GridCell) indipendentemente dal fatto che la cella sia nulla.


### **Utilizzo degli indici di riga e colonna**


Una cella può anche essere riconosciuta dalla sua posizione in termini di indici di riga e colonna. Basta passare gli indici di riga e colonna di una cella alla collezione Cells di GridWorksheet. Questo approccio è più veloce rispetto al precedente.

**Buone Pratiche**:

Se vogliamo ottenere il valore della cella o lo stile della cella e non vogliamo eseguire l'operazione di aggiornamento, possiamo utilizzare il metodo **CheckCell** che restituirà null se la cella non esiste. Questo **risparmierà memoria**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Buone Pratiche**:
### Iterare sulle celle
se vogliamo accedere a tutte le celle nel foglio di lavoro una per una, possiamo utilizzare **iteratori** per attraversare le celle esistenti. questo permetterà di **risparmiare memoria**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
confronta il seguente codice che è **cattivo**, questo creerà tutti gli oggetti delle celle indipendentemente che siano nulli, causando così problemi di memoria, quindi **non** usare in questo modo
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
