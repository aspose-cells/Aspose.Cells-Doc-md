---
title: Accedi al foglio di lavoro Cells
type: docs
weight: 10
url: /it/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

Questo argomento discute le celle, esaminando la funzionalità più basilare di Aspose.Cells.GridWeb: l'accesso alle celle.

{{% /alert %}} 
## **Accesso a Cells in un foglio di lavoro**
Ogni foglio di lavoro contiene una proprietà con il nome di Cells che è in realtà una raccolta di oggetti GridCell in cui un oggetto GridCell rappresenta una cella in Aspose.Cells.GridWeb. È possibile accedere a qualsiasi cella utilizzando Aspose.Cells.GridWeb. Ci sono due metodi preferiti, ognuno dei quali è discusso di seguito.


### **Utilizzando il nome Cell**
Tutte le celle hanno un nome univoco. Ad esempio, A1, A2, B1, B2 ecc. Aspose.Cells.GridWeb consente agli sviluppatori di accedere a qualsiasi cella desiderata utilizzando il nome della cella. Basta passare il nome della cella (come indice) alla raccolta Cells del GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Utilizzo degli indici di riga e colonna**
Una cella può anche essere riconosciuta dalla sua posizione in termini di indici di riga e colonna. Basta passare gli indici di riga e colonna di una cella alla raccolta Cells di GridWorksheet. Questo approccio è più veloce di quello precedente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
