---
title: Modifiche all API pubblica in Aspose.Cells 8.8.2
type: docs
weight: 280
url: /it/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.8.1 alla 8.8.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiornamento automatico dei riferimenti durante l'eliminazione di righe e colonne vuote**
Aspose.Cells for .NET 8.8.2 ha esposto le versioni sovraccaricate dei metodi Cells.DeleteBlankRows e Cells.DeleteBlankColumns. I nuovi metodi possono accettare un'istanza della classe DeleteOptions e possono essere utilizzati per superare le situazioni che potrebbero sorgere a causa dei riferimenti interrotti nelle formule, nei dati delle serie del grafico e così via. Al momento, la classe DeleteOptions ha solo un membro, una proprietà di tipo Booleano chiamata UpdateReference. Se tale proprietà è impostata su true e l'istanza della classe DeleteOptions viene passata ai metodi Cells.DeleteBlankRows e Cells.DeleteBlankColumns, l'API regolerà internamente i riferimenti della formula (se presenti) per accomodare le modifiche.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Eliminazione di Righe e Colonne Vuote con Riferimenti Aggiornati](/cells/it/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
