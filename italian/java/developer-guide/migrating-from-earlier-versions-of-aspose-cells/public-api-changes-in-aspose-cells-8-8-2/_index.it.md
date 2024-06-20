---
title: Modifiche all API pubblica in Aspose.Cells 8.8.2
type: docs
weight: 290
url: /it/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.8.1 alla 8.8.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiornamento automatico dei riferimenti durante l'eliminazione delle righe e colonne vuote**
Aspose.Cells for Java 8.8.2 ha esposto le versioni sovraccaricate dei metodi Cells.deleteBlankRows & Cells.deleteBlankColumns. I nuovi metodi possono accettare un'istanza della classe DeleteOptions e possono essere utilizzati per superare le situazioni che potrebbero sorgere a causa dei riferimenti spezzati nelle formule, nei dati delle serie dei grafici e così via. La classe DeleteOptions ha attualmente un solo membro, una proprietà di tipo Boolean di nome UpdateReference. Se la suddetta proprietà è impostata su true e l'istanza della classe DeleteOptions viene passata ai metodi Cells.deleteBlankRows & Cells.deleteBlankColumns, l'API regolerà internamente i riferimenti delle formule (se presenti) per accomodare le modifiche. 

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Eliminazione delle righe e colonne vuote con riferimenti aggiornati](/cells/it/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
