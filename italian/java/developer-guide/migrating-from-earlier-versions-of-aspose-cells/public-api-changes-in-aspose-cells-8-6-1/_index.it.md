---
title: Modifiche all API pubblica in Aspose.Cells 8.6.1
type: docs
weight: 210
url: /it/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.0 alla 8.6.1 che possono interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per il tipo di destinazione collegamento HTML**
Questa release dell'API Aspose.Cells for Java ha esposto un'enumerazione denominata HtmlLinkTargetType insieme a una nuova proprietà HtmlSaveOptions.LinkTargetType che insieme consente di [impostare il tipo di destinazione per i collegamenti nel foglio elettronico durante la conversione in formato HTML](/cells/it/java/change-the-html-link-target-type/). I valori possibili dell'enumerazione HtmlLinkTargetType sono i seguenti dove il valore predefinito è SELF.

1. HtmlLinkTargetType.BLANK: Apre il documento/pagina collegato in una nuova finestra o scheda.
1. HtmlLinkTargetType.PARENT: Apre il documento/pagina collegato nel frame parente.
1. HtmlLinkTargetType.SELF: Apre il documento/pagina collegato nello stesso frame in cui è stato cliccato il link.
1. HtmlLinkTargetType.TOP: Apre il documento/pagina collegato nell'intero corpo della finestra.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Metodo VbaModuleCollection.remove Aggiunto**
Aspose.Cells for Java 8.6.1 ha esposto un'altra sovraccarica del metodo VbaModuleCollection.remove che ora può accettare un'istanza di Worksheet per rimuovere tutti i moduli VBA associati al Worksheet specificato.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Metodo RangeCollection.add Aggiunto**
Aspose.Cells for Java 8.6.1 ha esposto il metodo RangeCollection.Add che può essere utilizzato per aggiungere oggetti Range alla collezione di intervalli per un determinato Foglio di lavoro.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Metodo Cell.setCharacters Aggiunto**
Il metodo Cell.setCharacters può essere utilizzato per aggiornare le porzioni del testo ricco di un determinato oggetto Cell. Il metodo Cell.getCharacters viene utilizzato per accedere alle porzioni del testo e quindi le modifiche possono essere fatte utilizzando il metodo Cell.setCharacters, mentre il metodo **get** restituisce un array di oggetti FontSetting che possono essere manipolati per impostare varie proprietà come il nome del font, il colore del font, il grassetto, ecc. e il metodo **set** può essere utilizzato per applicare le modifiche.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Proprietà VbaProject.isSigned Aggiunta**
Aspose.Cells for Java 8.6.1 ha esposto la proprietà VbaProject.isSigned che può essere utilizzata per verificare se un VbaProject in un Workbook è firmato o meno. La proprietà di tipo Boolean restituisce true se il progetto è firmato.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **API Modificate**
### **Metodo Cell.getFormatConditions Modificato**
Con il rilascio della v8.6.1, l'API Aspose.Cells for Java ha modificato il tipo di ritorno del metodo Cell.getFormatConditions che ora restituisce un array di tipo FormatConditionCollection.
## **API deprecate**
### **Metodo Workbook.checkWriteProtectedPassword Obsoleto**
Con il rilascio della v8.6.1, il metodo Workbook.checkWriteProtectedPassword è stato contrassegnato come deprecato. Si consiglia di utilizzare il metodo WorkbookSettings.WriteProtection.validatePassword che può accettare un valore Stringa come parametro e restituisce Boolean se la password corrisponde alla password preimpostata del foglio di calcolo.
{{< app/cells/assistant language="java" >}}
