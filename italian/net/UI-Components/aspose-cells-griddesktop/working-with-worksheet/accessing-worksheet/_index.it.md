---
title: Accesso al foglio di lavoro
type: docs
weight: 10
url: /it/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Un foglio di lavoro è parte integrante di un file Excel. Infatti, un file Excel è composto da uno o più fogli di lavoro. Ogni foglio di lavoro può essere composto solo da un massimo di 65.536 righe e 256 colonne. È il foglio di lavoro che contiene i dati in un file Excel.

Aspose.Cells.GridDesktop può creare e manipolare file Excel esistenti e nuovi, quindi esiste, ovviamente, un modo per accedere ai fogli di lavoro utilizzando Aspose.Cells.GridDesktop. Questo argomento discute come.

{{% /alert %}} 
## **Utilizzo dell'indice del foglio di lavoro**
Gli sviluppatori possono accedere a un'istanza di qualsiasi foglio di lavoro utilizzando l'indice del foglio di lavoro di qualsiasi foglio di lavoro desiderato, come mostrato di seguito nell'esempio. Questo approccio è utile per l'iterazione di un numero di fogli di lavoro in un file Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Utilizzo del nome del foglio di lavoro**
Se il nome del foglio di lavoro è noto, è possibile accedere a un foglio di lavoro utilizzando il suo nome come mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accesso a un foglio di lavoro attivo**
È possibile che un file Excel contenga più di un foglio di lavoro. Quello su cui sta lavorando un utente è chiamato foglio di lavoro attivo. E' possibile accedere al foglio attivo.

Per accedere a un foglio di lavoro attivo, Aspose.Cells.GridDesktop offre due approcci:
### **Utilizzo della proprietà AcriveSheetIndex**
Un modo per accedere a un foglio di lavoro attivo utilizzando il controllo Aspose.Cells.GridDesktop consiste nell'utilizzare la proprietà ActiveSheetIndex del controllo GridDesktop. Utilizzando questa proprietà, è possibile ottenere l'indice del foglio di lavoro attivo nel controllo Aspose.Cells.GridDesktop. Quindi quell'indice può essere utilizzato per accedere al foglio di lavoro in modo tradizionale come mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Utilizzando il metodo GetActiveWorksheet**
L'altro approccio consiste nel chiamare il metodo GetActiveWorksheet del controllo GridDesktop. Questo metodo fornisce un riferimento al foglio di lavoro attualmente attivo nel controllo Aspose.Cells.GridDesktop come mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
