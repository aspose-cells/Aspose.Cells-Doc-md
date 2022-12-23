---
title: Accesso a Cells in un foglio di lavoro
type: docs
weight: 10
url: /it/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

Finora abbiamo discusso dell'utilizzo di fogli di lavoro, righe e colonne, ma questo è il momento di approfondire e parlare di celle. Quindi, in questo argomento, inizieremo la nostra discussione sulle celle con una caratteristica di base per l'accesso alle celle.

{{% /alert %}} 
## **Accesso a Cells in un foglio di lavoro**
Possiamo accedere a qualsiasi cella di un foglio di lavoro utilizzando lo API di Aspose.Cells.GridDesktop. Ci potrebbero essere tre possibili modi per accedere alle celle come segue:

- **Utilizzando il nome Cell**
- **Utilizzo degli indici di riga e colonna di Cell**
- **Concentrarsi Cell**

Discutiamo tutti i tre approcci sopra uno per uno.
### **Utilizzando il nome Cell**
 Tutte le celle in un foglio di lavoro hanno un nome univoco. Ad esempio, A1, A2, B1, B2 ecc. Aspose.Cells.GridDesktop consente agli sviluppatori di accedere a qualsiasi cella desiderata utilizzando il nome della cella. Tutto quello che dobbiamo fare è semplicemente passare il nome della cella (come indice) al file**Cells** raccolta del**Foglio di lavoro**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Utilizzo degli indici di riga e colonna di Cell**
 Una cella in un foglio di lavoro può anche essere riconosciuta utilizzando la sua posizione in termini di indici di riga e colonna. Tutto quello che dobbiamo fare è semplicemente passare gli indici di riga e colonna della cella al file**Cells** raccolta del**Foglio di lavoro**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Concentrarsi Cell**
 Se non sai con precisione a quale cella accedere. Quindi Aspose.Cells.GridDesktop ti consente anche di accedere a una cella che è attualmente nel focus di un utente. Utilizzando questa funzione, puoi consentire a un utente di selezionare qualsiasi cella e quindi puoi accedere a quella cella nel back-end. Può essere ottenuto semplicemente utilizzando**GetFocusedCell** metodo del**Foglio di lavoro**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
