---
title: Modifiche all'API pubblica in Aspose.Cells 8.6.1
type: docs
weight: 200
url: /it/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.0 alla 8.6.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per il tipo di destinazione del collegamento HTML**
Questa versione dell'API Aspose.Cells for .NET ha esposto un'enumerazione denominata HtmlLinkTargetType insieme a una nuova proprietà HtmlSaveOptions.LinkTargetType che insieme consente di[impostare il tipo di destinazione per i collegamenti nel foglio di calcolo durante la conversione in formato HTML](/cells/it/net/change-the-html-link-target-type/). Di seguito sono riportati i possibili valori dell'enumerazione HtmlLinkTargetType, dove il valore predefinito è Self.

1. HtmlLinkTargetType.Blank: apre il documento/la pagina collegata in una nuova finestra o scheda.
1. HtmlLinkTargetType.Parent: apre il documento/la pagina collegata nel frame principale.
1. HtmlLinkTargetType.Self: apre il documento/la pagina collegata nello stesso frame in cui è stato fatto clic sul collegamento.
1. HtmlLinkTargetType.Top: apre il documento/la pagina collegata nel corpo intero della finestra.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Metodo VbaModuleCollection.Remove Aggiunto**
Aspose.Cells for .NET 8.6.1 ha esposto un altro overload del metodo VbaModuleCollection.Remove che ora può accettare un'istanza di Worksheet per rimuovere tutti i moduli VBA associati al foglio di lavoro specificato.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Metodo RangeCollection.Add Aggiunto**
Aspose.Cells for .NET 8.6.1 ha esposto il metodo RangeCollection.Add che può essere utilizzato per aggiungere oggetti Range alla raccolta di intervalli per un particolare foglio di lavoro.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Metodo Cell.SetCharacters Aggiunto**
 Il metodo Cell.SetCharacters può essere utilizzato per[aggiornare le parti del rich text](/cells/it/net/access-and-update-the-portions-of-rich-text-of-cell/) di un dato oggetto Cell. Il metodo Cell.GetCharacters deve essere utilizzato per accedere alle porzioni di testo e quindi le modifiche possono essere apportate utilizzando il metodo Cell.SetCharacters mentre il**Ottenere** metodo restituisce un array di oggetti FontSetting che possono essere manipolati per impostare varie proprietà nome carattere, colore carattere, grassetto ecc. e**Impostare** metodo può essere utilizzato per applicare le modifiche.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Proprietà VbaProject.IsSigned Aggiunta**
 Aspose.Cells for .NET 8.6.1 ha esposto la proprietà VbaProject.IsSigned che può essere utilizzata per[verificare se un VbaProject in una cartella di lavoro è firmato o meno](/cells/it/net/check-if-vba-project-in-a-workbook-is-signed/). La proprietà di tipo booleano restituisce true se il progetto è firmato.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **API modificate**
### **Metodo Cell.GetFormatConditions modificato**
Con il rilascio della v8.6.1, l'API Aspose.Cells for .NET ha modificato il tipo restituito del metodo Cell.GetFormatConditions che ora restituisce un array di tipo FormatConditionCollection.
## **API obsolete**
### **Metodo Workbook.CheckWriteProtectedPassword Obsoleto**
Con la versione v8.6.1, il metodo Workbook.CheckWriteProtectedPassword è stato contrassegnato come deprecato. Si consiglia di utilizzare il metodo WorkbookSettings.WriteProtection.ValidatePassword che può accettare un valore stringa come parametro e restituire Boolean se la password corrisponde alla password preimpostata del foglio di calcolo.
