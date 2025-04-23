---
title: Modifiche all API pubblica in Aspose.Cells 8.6.1
type: docs
weight: 200
url: /it/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.6.0 alla 8.6.1 che possono interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per il tipo di destinazione collegamento HTML**
Questa versione di Aspose.Cells for .NET API ha esposto un'enumerazione chiamata HtmlLinkTargetType insieme a una nuova proprietà HtmlSaveOptions.LinkTargetType che consente di [impostare il tipo di destinazione per i collegamenti nello spreadsheet durante la conversione nel formato HTML](/cells/it/net/change-the-html-link-target-type/). I valori possibili dell'enumerazione HtmlLinkTargetType sono i seguenti dove il valore predefinito è Self.

1. HtmlLinkTargetType.Blank: Apre il documento/pagina collegato in una nuova finestra o scheda.
1. HtmlLinkTargetType.Parent: Apre il documento/pagina collegato nel frame padre.
1. HtmlLinkTargetType.Self: Apre il documento/pagina collegato nello stesso frame in cui è stato fatto clic sul collegamento.
1. HtmlLinkTargetType.Top: Apre il documento/pagina collegato nell'intero corpo della finestra.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Aggiunto Metodo Remove di VbaModuleCollection**
Aspose.Cells for .NET 8.6.1 ha esposto un'altra sovraccarica del metodo VbaModuleCollection.Remove che può ora accettare un'istanza di Foglio di lavoro per rimuovere tutti i moduli VBA associati al Foglio di lavoro specificato.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Aggiunto Metodo Add di RangeCollection**
Aspose.Cells for .NET 8.6.1 ha esposto il metodo RangeCollection.Add che può essere utilizzato per aggiungere oggetti Range alla collezione di intervalli per un particolare Foglio di lavoro.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Aggiunto Metodo SetCharacters di Cell**
Il metodo Cell.SetCharacters può essere utilizzato per aggiornare le porzioni del testo formattato di un oggetto Cell specificato. Il metodo Cell.GetCharacters deve essere utilizzato per accedere alle porzioni del testo e quindi le modifiche possono essere apportate utilizzando il metodo Cell.SetCharacters mentre il metodo **Get** restituisce un array di oggetti FontSetting che possono essere manipolati per impostare diverse proprietà come il nome del font, il colore del font, il grassetto, ecc. e il metodo **Set** può essere utilizzato per applicare le modifiche.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Aggiunta Proprietà IsSigned di VbaProject**
Aspose.Cells for .NET 8.6.1 ha esposto la proprietà VbaProject.IsSigned che può essere utilizzata per verificare se un progetto VbaProject in un Workbook è firmato o meno. La proprietà di tipo Boolean restituisce true se il progetto è firmato.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

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
## **API Modificate**
### **Metodo Cell.GetFormatConditions Modificato**
Con il rilascio della v8.6.1, l'API Aspose.Cells for .NET ha modificato il tipo di ritorno del metodo Cell.GetFormatConditions che ora restituisce un array di tipo FormatConditionCollection.
## **API deprecate**
### **Metodo Workbook.CheckWriteProtectedPassword Obsoleto**
Con il rilascio della v8.6.1, il metodo Workbook.CheckWriteProtectedPassword è stato contrassegnato come deprecato. Si consiglia di utilizzare il metodo WorkbookSettings.WriteProtection.ValidatePassword che può accettare una stringa come parametro e restituisce Boolean se la password corrisponde alla password predefinita del foglio di calcolo.
{{< app/cells/assistant language="csharp" >}}
