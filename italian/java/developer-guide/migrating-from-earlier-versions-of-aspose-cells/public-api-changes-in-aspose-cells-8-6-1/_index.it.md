---
title: Pubblico API Modifiche Aspose.Cells 8.6.1
type: docs
weight: 210
url: /it/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.6.0 alla 8.6.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per il tipo di destinazione del collegamento HTML**
Questa versione di Aspose.Cells for Java API ha esposto un'enumerazione HtmlLinkTargetType insieme a una nuova proprietà HtmlSaveOptions.LinkTargetType che insieme consente di[impostare il tipo di destinazione per i collegamenti nel foglio di calcolo durante la conversione in formato HTML](/cells/it/java/change-the-html-link-target-type/). Di seguito sono riportati i possibili valori dell'enumerazione HtmlLinkTargetType, dove il valore predefinito è SELF.

1. HtmlLinkTargetType.BLANK: apre il documento/la pagina collegata in una nuova finestra o scheda.
1. HtmlLinkTargetType.PARENT: apre il documento/la pagina collegata nel frame principale.
1. HtmlLinkTargetType.SELF: apre il documento/la pagina collegata nello stesso frame in cui è stato fatto clic sul collegamento.
1. HtmlLinkTargetType.TOP: Apre il documento/la pagina collegata nel corpo intero della finestra.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.6.1 ha esposto un altro overload del metodo VbaModuleCollection.remove che ora può accettare un'istanza di Worksheet per rimuovere tutti i moduli VBA associati al Worksheet specificato.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Metodo RangeCollection.add Aggiunto**
Aspose.Cells for Java 8.6.1 ha esposto il metodo RangeCollection.Add che può essere utilizzato per aggiungere oggetti Range alla raccolta di intervalli per un particolare foglio di lavoro.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Metodo Cell.setCaratteri aggiunti**
 Il metodo Cell.setCharacters può essere utilizzato per[aggiornare le parti del rich text](/cells/it/java/access-and-update-the-portions-of-rich-text-of-cell/) di un dato oggetto Cell. Il metodo Cell.getCharacters deve essere utilizzato per accedere alle porzioni di testo e quindi le modifiche possono essere apportate utilizzando il metodo Cell.setCharacters mentre il**ottenere** metodo restituisce un array di oggetti FontSetting che possono essere manipolati per impostare varie proprietà nome carattere, colore carattere, grassetto ecc. e**impostare** metodo può essere utilizzato per applicare le modifiche.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Proprietà VbaProject.isSigned Aggiunta**
 Aspose.Cells for Java 8.6.1 ha esposto la proprietà VbaProject.isSigned che può essere utilizzata per[verificare se un VbaProject in una cartella di lavoro è firmato o meno](/cells/it/java/check-if-vba-project-in-a-workbook-is-signed/). La proprietà di tipo booleano restituisce true se il progetto è firmato.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
## **API modificate**
### **Metodo Cell.getFormatConditions modificato**
Con il rilascio della v8.6.1, il Aspose.Cells for Java API ha modificato il tipo restituito del metodo Cell.getFormatConditions che ora restituisce un array di tipo FormatConditionCollection.
## **API obsolete**
### **Metodo Workbook.checkWriteProtectedPassword Obsoleto**
Con la versione v8.6.1, il metodo Workbook.checkWriteProtectedPassword è stato contrassegnato come deprecato. Si consiglia di utilizzare il metodo WorkbookSettings.WriteProtection.validatePassword che può accettare un valore String come parametro e restituire Boolean se la password corrisponde alla password preimpostata del foglio di calcolo.
