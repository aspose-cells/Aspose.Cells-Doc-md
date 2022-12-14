---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.3
type: docs
weight: 230
url: /de/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.2 zu 8.6.3, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für HTML-Parsing beim Importieren von Daten**
Diese Version von Aspose.Cells for Java API hat das ImportTableOptions.setHtmlString-Attribut bereitgestellt, das API anweist, die HTML-Tags zu analysieren, während Daten in das Arbeitsblatt importiert werden, und das analysierte Ergebnis als Zellenwert festzulegen. Bitte beachten Sie, dass Aspose.Cells-APIs bereits das Attribut Cell.setHtmlString bereitstellen, um diese Aufgabe für eine einzelne Zelle auszuführen. Beim Massenimport von Daten versucht das Attribut ImportTableOptions.setHtmlString jedoch (wenn es auf „true“ gesetzt ist), alle unterstützten HTML-Tags und -Sätze zu analysieren die geparsten Ergebnisse in die entsprechenden Zellen.

Hier ist das einfachste Anwendungsszenario.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Methode Workbook.createBuiltinStyle Hinzugefügt**
Aspose.Cells for Java 8.6.3 hat die Workbook.createBuiltinStyle-Methode verfügbar gemacht, die verwendet werden kann, um ein Objekt der Style-Klasse zu erstellen, das einem der entspricht[integrierte Stile, die von der Excel-Anwendung angeboten werden](/cells/de/java/using-built-in-styles/). Die Workbook.createBuiltinStyle-Methode akzeptiert eine Konstante aus der Enumeration BuiltinStyleType. Bitte beachten Sie, dass mit früheren Versionen der Aspose.Cells-APIs dieselbe Aufgabe über die StyleCollection.createBuiltinStyle-Methode ausgeführt werden konnte, aber da die jüngsten Versionen der Aspose.Cells-APIs die StyleCollection-Klasse entfernt haben, kann die neu verfügbar gemachte Workbook.createBuiltinStyle-Methode als alternativer Ansatz in Betracht gezogen werden dasselbe erreichen.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Eigenschaft LoadDataOption.OnlyVisibleWorksheet hinzugefügt**
Aspose.Cells for Java 8.6.3 hat die LoadDataOption.OnlyVisibleWorksheet-Eigenschaft verfügbar gemacht, die, wenn sie auf „true“ gesetzt wird, den Lademechanismus von Aspose.Cells for Java API beeinflusst, sodass nur sichtbare Arbeitsblätter aus einer bestimmten Tabelle geladen werden.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

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
### **Methode Worksheet.copyConditionalFormatting Veraltet**
Als Alternative zur Methode Worksheet.copyConditionalFormatting wird empfohlen, eine der Methoden Cells.copyRows oder Range.copy zu verwenden.
### **Eigenschaft Cells.Ende Veraltet**
Bitte verwenden Sie die Eigenschaft Cells.LastCell als Alternative zur Eigenschaft Cells.End.
