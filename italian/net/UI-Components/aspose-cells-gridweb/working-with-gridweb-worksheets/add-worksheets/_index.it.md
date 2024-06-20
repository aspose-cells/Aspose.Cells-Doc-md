---
title: Aggiungere Fogli di Lavoro
type: docs
weight: 20
url: /it/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: Questo articolo introduce come aggiungere un foglio di lavoro (GridWorksheet) in GridWeb.
---

{{% alert color="primary" %}} 

I fogli di lavoro sono una parte integrante di Aspose.Cells.GridWeb. Tutti i dati sono gestiti e memorizzati sotto forma di fogli di lavoro. Aspose.Cells.GridWeb consente agli sviluppatori di aggiungere uno o più fogli di lavoro al controllo Aspose.Cells.GridWeb. Questo argomento mostra approcci semplici per aggiungere fogli di lavoro ad Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Aggiunta di un Foglio di Lavoro**
### **Senza specificare il nome del foglio**
Il modo più semplice per aggiungere un foglio di lavoro ad Aspose.Cells.GridWeb è chiamare il metodo Aggiungi della collezione GridWorksheetCollection nel controllo GridWeb. Ciò crea fogli di lavoro che utilizzano nomi predefiniti (come Foglio1, Foglio2, Foglio3 e così via) e li aggiunge al controllo GridWeb.

**Output: è stato aggiunto un foglio di lavoro con un nome predefinito a GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Il metodo Aggiungi restituisce l'indice del nuovo foglio di lavoro che può essere utilizzato per accedere all'istanza di questo foglio di lavoro. Per ulteriori dettagli su come accedere ai fogli di lavoro, leggere [Accesso ai Fogli di Lavoro](/cells/it/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **Con nome del foglio specificato**
Per aggiungere un foglio di lavoro con un nome specifico al controllo GridWeb anziché utilizzare lo schema di denominazione predefinito, chiamare una versione sovraccaricata del metodo Aggiungi che prende il nome del Foglio specificato. Ad esempio, l'esempio sottostante aggiunge un foglio di lavoro chiamato Fattura.

**Output: è stato aggiunto un foglio di lavoro con un nome specificato a GridWeb** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Il metodo Aggiungi che accetta il nome del foglio di lavoro come stringa restituisce un'istanza di GridWorksheet.

{{% /alert %}}
