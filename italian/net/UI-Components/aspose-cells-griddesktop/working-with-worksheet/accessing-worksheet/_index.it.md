---
title: Accesso al Foglio di Lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop, foglio di lavoro
description: Questo articolo introduce come lavorare con i fogli di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

Un foglio di lavoro è una parte integrante di un file Excel. Infatti, un file Excel è composto da uno o più fogli di lavoro. Ogni foglio di lavoro può essere composto solo da un massimo di 65.536 righe e 256 colonne. È il foglio di lavoro che contiene i dati in un file Excel.

Aspose.Cells.GridDesktop può creare e manipolare file Excel esistenti e nuovi, quindi ovviamente c'è un modo per accedere ai fogli di lavoro utilizzando Aspose.Cells.GridDesktop. Questo argomento ne discute.

{{% /alert %}} 
## **Utilizzando l'indice del foglio di lavoro**
Gli sviluppatori possono accedere a un'istanza di qualsiasi Foglio di Lavoro utilizzando l'indice del foglio di lavoro desiderato come mostrato nell'esempio seguente. Questo approccio è utile per iterare tra un certo numero di fogli di lavoro in un file Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Utilizzando il nome del foglio di lavoro**
Se si conosce il nome del foglio di lavoro, è possibile accedere a un foglio di lavoro utilizzando il suo nome come mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accesso a un Foglio di Lavoro Attivo**
È possibile che un file Excel abbia più di un foglio di lavoro. Quello su cui un utente sta lavorando viene chiamato foglio di lavoro attivo. È possibile accedere al foglio di lavoro attivo.

Per accedere a un foglio di lavoro attivo, Aspose.Cells.GridDesktop offre due approcci:
### **Utilizzando la proprietà AcriveSheetIndex**
Un modo per accedere a un foglio di lavoro attivo utilizzando il controllo Aspose.Cells.GridDesktop è utilizzare la proprietà ActiveSheetIndex del controllo GridDesktop. Utilizzando questa proprietà, è possibile ottenere l'indice del foglio di lavoro attivo nel controllo Aspose.Cells.GridDesktop. Quell'indice può quindi essere utilizzato per accedere al foglio di lavoro in modo tradizionale come mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Utilizzando il metodo GetActiveWorksheet**
L'altro approccio è richiamare il metodo GetActiveWorksheet del controllo GridDesktop. Questo metodo fornisce un riferimento al foglio di lavoro attualmente attivo nel controllo Aspose.Cells.GridDesktop come mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
