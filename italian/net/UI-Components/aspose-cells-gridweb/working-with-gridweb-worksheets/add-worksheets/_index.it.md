---
title: Aggiungi fogli di lavoro
type: docs
weight: 20
url: /it/net/add-worksheets/
---
{{% alert color="primary" %}} 

fogli di lavoro sono parte integrante di Aspose.Cells.GridWeb. Tutti i dati vengono gestiti e archiviati sotto forma di fogli di lavoro. Aspose.Cells.GridWeb consente agli sviluppatori di aggiungere uno o più fogli di lavoro al controllo Aspose.Cells.GridWeb. Questo argomento illustra approcci semplici per l'aggiunta di fogli di lavoro a Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Aggiunta di un foglio di lavoro**
### **Senza specificare il nome del foglio**
Il modo più semplice per aggiungere un foglio di lavoro a Aspose.Cells.GridWeb consiste nel chiamare il metodo Add della raccolta GridWorksheetCollection nel controllo GridWeb. Questo crea fogli di lavoro che utilizzano nomi predefiniti (ovvero Foglio1, Foglio2, Foglio3 e così via) e li aggiunge al controllo GridWeb.

**Output: un foglio di lavoro con nome predefinito è stato aggiunto a GridWeb** 

![cose da fare:immagine_alt_testo](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 Il metodo Add restituisce l'indice del nuovo foglio di lavoro che può essere utilizzato per accedere all'istanza di questo foglio di lavoro. Per maggiori dettagli su come accedere ai fogli di lavoro, leggi[Accedi ai fogli di lavoro](/cells/it/net/access-worksheets/).

{{% /alert %}} 
### **Con il nome del foglio specificato**
Per aggiungere un foglio di lavoro con un nome specifico al controllo GridWeb invece di usare lo schema di denominazione predefinito, chiamare una versione di overload del metodo Add che accetta il SheetName specificato. Ad esempio, l'esempio seguente aggiunge un foglio di lavoro denominato Invoice.

**Output: un foglio di lavoro con un nome specificato è stato aggiunto a GridWeb** 

![cose da fare:immagine_alt_testo](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Il metodo Add che accetta il nome del foglio di lavoro come stringa restituisce un'istanza di GridWorksheet.

{{% /alert %}}
