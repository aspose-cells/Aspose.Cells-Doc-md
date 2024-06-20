---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.3
type: docs
weight: 230
url: /de/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.6.2 auf 8.6.3, die für Modul-/Anwendungsentwickler interessant sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden und hinzugefügte Klassen, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für HTML-Parser beim Importieren von Daten**
In dieser Version von Aspose.Cells for Java API wurde das Attribut ImportTableOptions.setHtmlString freigelegt, das die API anweist, die HTML-Tags beim Importieren von Daten auf das Arbeitsblatt zu analysieren und das analysierte Ergebnis als Zellwert festzulegen. Bitte beachten Sie, dass die Aspose.Cells-APIs bereits das Attribut Cell.setHtmlString bereitstellen, um diese Aufgabe für eine einzelne Zelle auszuführen. Beim Importieren von Daten in großem Umfang versucht das Attribut ImportTableOptions.setHtmlString (wenn auf true gesetzt) alle unterstützten HTML-Tags zu analysieren und die analysierten Ergebnisse in die entsprechenden Zellen zu setzen.

Hier ist das einfachste Anwendungsszenario.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Hinzugefügte Workbook.createBuiltinStyle-Methode**
Aspose.Cells for Java 8.6.3 hat die Workbook.createBuiltinStyle-Methode freigelegt, die verwendet werden kann, um ein Objekt der Style-Klasse zu erstellen, das einem der von der Excel-Anwendung angebotenen [eingebauten Stile](/cells/de/java/using-built-in-styles/) entspricht. Die Workbook.createBuiltinStyle-Methode akzeptiert eine Konstante aus der Aufzählung BuiltinStyleType. Bitte beachten Sie, dass mit früheren Versionen der Aspose.Cells-APIs dieselbe Aufgabe über die StyleCollection.createBuiltinStyle-Methode ausgeführt werden konnte, jedoch da die neueren Versionen der Aspose.Cells-APIs die StyleCollection-Klasse entfernt haben, kann die neu freigelegte Workbook.createBuiltinStyle-Methode als alternativer Ansatz betrachtet werden, um dasselbe zu erreichen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Hinzugefügte LoadDataOption.OnlyVisibleWorksheet-Eigenschaft**
Aspose.Cells for Java 8.6.3 hat die LoadDataOption.OnlyVisibleWorksheet-Eigenschaft freigelegt, die bei Einstellung auf true den Lademechanismus von Aspose.Cells for Java API beeinflusst, wodurch nur sichtbare Arbeitsblätter aus einer gegebenen Tabellenkalkulation geladen werden.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Veraltete APIs**
### **Veraltete Worksheet.copyConditionalFormatting-Methode**
Anstelle der Worksheet.copyConditionalFormatting-Methode wird empfohlen, eine der Cells.copyRows- oder Range.copy-Methoden zu verwenden.
### **Veraltete Cells.End Property**
Bitte verwenden Sie die Cells.LastCell-Eigenschaft als Alternative zur Cells.End-Eigenschaft.
