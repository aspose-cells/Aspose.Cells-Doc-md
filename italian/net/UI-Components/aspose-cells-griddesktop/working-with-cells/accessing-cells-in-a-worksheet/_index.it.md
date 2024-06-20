---
title: Accesso alla cella della griglia in un foglio di lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: Questo articolo introduce come ottenere l oggetto cella (GridCell) nel foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

Abbiamo parlato finora di come lavorare con i fogli di lavoro, le righe e le colonne, ma è ora di approfondire e parlare delle celle. Quindi, in questo argomento, inizieremo la nostra discussione sulle celle con una funzionalità di base per accedere alle celle.

{{% /alert %}} 
## **Accesso alla cella in un foglio di lavoro**
Possiamo accedere a qualsiasi cella di un foglio di lavoro utilizzando l'API di Aspose.Cells.GridDesktop. Potrebbero esserci tre possibili modi per accedere alla cella come segue:

- **Utilizzando il Nome della Cella**
- **Utilizzando gli Indici di Riga e Colonna**
- **Ottener una Cellula Focalizzata**

Discutiamo uno per uno tutti i tre approcci sopra.
### **Utilizzo del nome della cella**
Tutte le celle in un foglio di lavoro hanno un nome univoco. Ad esempio, A1, A2, B1, B2 ecc. Aspose.Cells.GridDesktop consente agli sviluppatori di accedere a qualsiasi cella desiderata utilizzando il suo nome di cella. Tutto quello che dobbiamo fare è passare il nome della cella (come un indice) alla collezione **Cells** del **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Avviso**

Accedere a GridCell usando cells[cellName] può consumare più memoria. Creerà sempre un nuovo oggetto cella (GridCell) indipendentemente dal fatto che la cella sia nulla.

### **Utilizzo degli Indici di Riga e Colonna della Cellula**

**Buone Pratiche**:

Se vogliamo ottenere il valore della cella o lo stile della cella e non vogliamo eseguire l'operazione di aggiornamento, possiamo utilizzare il metodo **CheckCell** che restituirà null se la cella non esiste. Questo **risparmierà memoria**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accedere a una cella utilizzando gli indici di riga e colonna
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

Una cella in un foglio di lavoro può essere riconosciuta anche utilizzando la sua posizione in termini di indici di riga e colonna. Tutto ciò che dobbiamo fare è passare gli indici di riga e colonna della cella alla raccolta **Cells** del **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Avviso**

Accedere a GridCell utilizzando cells[rowIndex, columnIndex] può consumare più memoria. Creerà sempre un nuovo oggetto cella (GridCell) indipendentemente dal fatto che la cella sia nulla.


### **Ottenere la cella focalizzata**
Se non sai con precisione quale cella accedere. Allora Aspose.Cells.GridDesktop ti consente anche di accedere a una cella che è attualmente al centro dell'attenzione di un utente. Utilizzando questa funzionalità, puoi consentire a un utente di selezionare qualsiasi cella e quindi puoi accedere a quella cella sul backend. Può essere semplicemente ottenuto utilizzando il metodo **GetFocusedCell** del **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Buone Pratiche**:
### Iterare sulle celle
se vogliamo accedere a tutte le celle nel foglio di lavoro una per una, possiamo utilizzare **iteratori** per attraversare le celle esistenti. questo permetterà di **risparmiare memoria**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
confronta il seguente codice che è **cattivo**, questo creerà tutti gli oggetti delle celle indipendentemente che siano nulli, causando così problemi di memoria, quindi **non** usare in questo modo
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

