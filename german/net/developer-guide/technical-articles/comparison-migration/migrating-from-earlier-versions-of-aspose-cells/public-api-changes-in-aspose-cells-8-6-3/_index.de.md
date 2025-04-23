---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.3
type: docs
weight: 220
url: /de/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.6.2 auf 8.6.3, die für Modul-/Anwendungsentwickler interessant sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden und hinzugefügte Klassen, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für HTML-Parser beim Importieren von Daten**
Diese Version der Aspose.Cells for .NET-API hat das ImportTableOptions.IsHtmlString-Eigenschaft freigelegt, die die API anweist, die HTML-Tags beim Importieren von Daten auf das Arbeitsblatt zu parsen und das geparste Ergebnis als Zellwert festzulegen. Bitte beachten Sie, dass Aspose.Cells-APIs bereits die Cell.HtmlString bereitstellen, um diese Aufgabe für eine einzelne Zelle auszuführen. Während jedoch das Importieren von Daten in größerem Umfang, wie z. B. aus einem DataTable, versucht die ImportTableOptions.IsHtmlString-Eigenschaft (wenn auf true gesetzt) alle unterstützten HTML-Tags zu parsen und die geparsten Ergebnisse in die entsprechenden Zellen zu setzen.

Hier ist das einfachste Anwendungsszenario.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Hinzugefügter Workbook.CreateBuiltinStyle-Methode**
Aspose.Cells for .NET 8.6.3 hat die Workbook.CreateBuiltinStyle-Methode freigelegt, die verwendet werden kann, um ein Objekt der Klasse Style zu erstellen, das einem der [von der Excel-Anwendung angebotenen integrierten Stile](/cells/de/net/using-built-in-styles/) entspricht. Die Workbook.CreateBuiltinStyle-Methode akzeptiert eine Konstante aus der Aufzählung BuiltinStyleType. Bitte beachten Sie, dass mit früheren Versionen der Aspose.Cells-APIs dieselbe Aufgabe über die StyleCollection.CreateBuiltinStyle-Methode erledigt werden konnte. Da jedoch die neueren Versionen der Aspose.Cells-APIs die Klasse StyleCollection entfernt haben, kann die neu freigelegte Workbook.CreateBuiltinStyle-Methode als alternative Möglichkeit angesehen werden, um das gleiche zu erreichen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Hinzugefügte Cells.ImportGridView-Methode**
Aspose.Cells for .NET 8.6.3 hat eine überladene Version der Cells.ImportGridView freigelegt, die nun eine Instanz von ImportTableOptions akzeptieren kann, um mehr Kontrolle über den Importprozess zu ermöglichen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Hinzugefügtes ImportTableOptions.ConvertGridStyle-Eigenschaft**
In Bezug auf die oben genannten Verbesserungen hat die neueste Version der Aspose.Cells for .NET-API auch die ImportTableOptions.ConvertGridStyle-Eigenschaft freigelegt. Diese Eigenschaft vom Typ Boolean ermöglicht es den Entwicklern, das Erscheinungsbild der importierten Daten zu steuern, wobei das Setzen der ImportTableOptions.ConvertGridStyle-Eigenschaft auf true anzeigt, dass die API den Stil des GridView auf die Zellen anwendet, in die die Daten importiert wurden.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Hinzugefügte LoadDataOption.OnlyVisibleWorksheet-Eigenschaft**
Aspose.Cells for .NET 8.6.3 hat die LoadDataOption.OnlyVisibleWorksheet-Eigenschaft freigelegt, die bei Einstellung auf true den Ladevorgang der Aspose.Cells for .NET-API beeinflussen wird. Als Ergebnis werden nur sichtbare Arbeitsblätter aus einer gegebenen Tabellenkalkulation geladen. Bitte lesen Sie den [ausführlichen Artikel](/cells/de/net/different-ways-to-open-files/) zu diesem Thema.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Veraltete APIs**
### **Veraltete Worksheet.CopyConditionalFormatting-Methode**
Als Alternative zur Worksheet.CopyConditionalFormatting-Methode wird empfohlen, eine der Cells.CopyRows- oder Range.Copy-Methoden zu verwenden.
### **Veraltete Cells.End Property**
Bitte verwenden Sie die Cells.LastCell-Eigenschaft als Alternative zur Cells.End-Eigenschaft.
{{< app/cells/assistant language="csharp" >}}
