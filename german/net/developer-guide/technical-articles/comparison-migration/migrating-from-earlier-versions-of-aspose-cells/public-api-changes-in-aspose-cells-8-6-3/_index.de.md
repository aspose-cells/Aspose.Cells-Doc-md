---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.3
type: docs
weight: 220
url: /de/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.2 zu 8.6.3, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für HTML Parsing beim Importieren von Daten**
Diese Version von Aspose.Cells for .NET API hat die ImportTableOptions.IsHtmlString-Eigenschaft verfügbar gemacht, die API anweist, die HTML-Tags zu analysieren, während Daten in das Arbeitsblatt importiert werden, und das analysierte Ergebnis als Zellenwert festzulegen. Bitte beachten Sie, dass Aspose.Cells-APIs bereits den Cell.HtmlString bereitstellen, um diese Aufgabe für eine einzelne Zelle auszuführen. Beim Massenimport von Daten, z. B. aus einer DataTable, versucht die ImportTableOptions.IsHtmlString-Eigenschaft (wenn auf „true“ festgelegt) jedoch, alle unterstützten zu analysieren HTML markiert und setzt die geparsten Ergebnisse auf die entsprechenden Zellen.

Hier ist das einfachste Anwendungsszenario.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Methode Workbook.CreateBuiltinStyle Hinzugefügt**
 Aspose.Cells for .NET 8.6.3 hat die Workbook.CreateBuiltinStyle-Methode verfügbar gemacht, die verwendet werden kann, um ein Objekt der Style-Klasse zu erstellen, das einem der entspricht[integrierte Stile, die von der Excel-Anwendung angeboten werden](/cells/de/net/using-built-in-styles/)Die Workbook.CreateBuiltinStyle-Methode akzeptiert eine Konstante aus der Enumeration BuiltinStyleType. Bitte beachten Sie, dass mit früheren Versionen der Aspose.Cells-APIs dieselbe Aufgabe über die StyleCollection.CreateBuiltinStyle-Methode ausgeführt werden konnte, aber da die jüngsten Versionen der Aspose.Cells-APIs die StyleCollection-Klasse entfernt haben, kann die neu verfügbar gemachte Workbook.CreateBuiltinStyle-Methode als alternativer Ansatz in Betracht gezogen werden dasselbe erreichen.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Methode Cells.ImportGridView hinzugefügt**
Aspose.Cells for .NET 8.6.3 hat eine überladene Version von Cells.ImportGridView verfügbar gemacht, die jetzt eine Instanz von ImportTableOptions akzeptieren kann, um mehr Kontrolle über den Importprozess zu geben.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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


### **Eigenschaft ImportTableOptions.ConvertGridStyle hinzugefügt**
In Bezug auf die oben genannten Verbesserungen hat die neueste Version von Aspose.Cells for .NET API auch die ImportTableOptions.ConvertGridStyle-Eigenschaft verfügbar gemacht. Mit dieser booleschen Eigenschaft können die Entwickler das Erscheinungsbild der importierten Daten steuern, wobei das Festlegen der ImportTableOptions.ConvertGridStyle-Eigenschaft auf „true“ angibt, dass API den Stil der GridView auf die Zellen anwendet, in die Daten importiert wurden.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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


### **Eigenschaft LoadDataOption.OnlyVisibleWorksheet hinzugefügt**
 Aspose.Cells for .NET 8.6.3 hat die LoadDataOption.OnlyVisibleWorksheet-Eigenschaft verfügbar gemacht, die, wenn sie auf „true“ gesetzt wird, den Lademechanismus von Aspose.Cells for .NET API beeinflusst, sodass nur sichtbare Arbeitsblätter aus einer bestimmten Tabelle geladen werden. Bitte überprüfen Sie die[ausführlicher Artikel](/cells/de/net/different-ways-to-open-files/) zu diesem Thema.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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
### **Methode Worksheet.CopyConditionalFormatting Veraltet**
Als Alternative zur Methode Worksheet.CopyConditionalFormatting wird empfohlen, eine der Methoden Cells.CopyRows oder Range.Copy zu verwenden.
### **Eigenschaft Cells.Ende Veraltet**
Bitte verwenden Sie die Eigenschaft Cells.LastCell als Alternative zur Eigenschaft Cells.End.
