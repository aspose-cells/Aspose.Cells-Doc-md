---
title: Öffentliche API Änderungen in Aspose.Cells 8.0.0
type: docs
weight: 10
url: /de/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Diese Seite listet öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.0 eingeführt wurden. Es umfasst nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung von Änderungen im Verhalten im Hintergrund von Aspose.Cells, die den vorhandenen Code beeinflussen können.

{{% /alert %}} 
## **MemorySetting zu LoadOptions & WorkbookSettings hinzugefügt**
Ab Version 8.0.0 von Aspose.Cells for .NET haben wir die Speichernutzungsoptionen aus Leistungsgründen bereitgestellt. Die MemorySetting Eigenschaft ist jetzt in den Klassen LoadOptions & WorkbookSettings verfügbar.
##### **Beispiel**
Zeigt, wie eine Excel-Datei (mit großer Größe) im optimierten Modus gelesen wird.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Zeigt, wie ein großes Dataset im optimierten Modus in ein Arbeitsblatt geschrieben wird.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Optimierung des Speichers beim Arbeiten mit großen Dateien](/cells/de/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Implementierungen von Zeile & Zelle wurden geändert**
In früheren Versionen wurden Zeilen- und Zellenobjekte im Speicher gehalten, um die entsprechende Zeile und Zelle in einem Arbeitsblatt darzustellen. Die gleiche Instanz wurde zurückgegeben, wann immer **RowCollection[int index]** oder **Cells[int row, int column]** abgerufen wurde. Aus Gründen der Speicherleistung werden jetzt nur noch Eigenschaften und Daten von Zeile und Zelle im Speicher behalten. Daher sind das Zeilen- und Zellenobjekt nun die Wrapper für die genannten Eigenschaften.
### **Beispiel**
Zeigt, wie man die Zellen- und Zeilenobjekte von jetzt an vergleicht.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Da die Zeilen- und Zellenobjekte je nach Aufruf instanziiert werden, werden sie nicht vom Zellenkomponenten im Speicher behalten und verwaltet. Daher können nach einigen Einfüge- und Löschvorgängen die Zeilen- und Spaltenindizes nicht aktualisiert werden oder diese Objekte werden ungültig.
### **Beispiel**
Beispielsweise gibt der folgende Codeausschnitt ab Version 8.0.0 und höher ungültige Ergebnisse zurück,

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Mit der neuen Version wird das Zellenobjekt ungültig oder verweist auf A2 mit einem unerwünschten Wert. Um eine solche Situation zu vermeiden, holen Sie die Zeilen- oder Zellenobjekte erneut aus der Zellensammlung, um das korrekte Ergebnis zu erhalten.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection erbt nicht mehr von CollectionBase, da es kein Zeilenobjekt in seiner internen Liste gibt.

{{% /alert %}}
## **Cell.StringValue-Verhalten geändert**
In früheren Versionen wurde das Sondermuster _ beim Formatieren von Zellenwerten ignoriert, während das Sonderzeichen * immer ein Zeichen in das formatierte Ergebnis einfügte. Ab dieser Version haben wir die Logik geändert, um Sonderzeichen _ und * zu behandeln, um das formatierte Ergebnis so zu gestalten, wie es die Excel-Anwendung macht. Beispielsweise ergab das benutzerdefinierte Zellenformat "_(\$* #,##0.00_)" für den Wert 123 das Ergebnis "$ 123.00". Mit neuen Versionen enthält Cell.StringValue das Ergebnis als "$123.00", was dasselbe Verhalten ist wie die Excel-Anwendung beim Kopieren der Zelle in Text oder beim Export in CSV.
## **Erstellungszeit zu PdfSaveOptions hinzugefügt**
Nutzer können nun die Erstellungszeit von PDF beim Speichern des Tabellenblatts in PDF mithilfe der Klasse PdfSaveOptions festlegen oder abrufen.
## **ShowFormulas zu Arbeitsblatt hinzugefügt**
Ab sofort können Benutzer die Boolesche Eigenschaft ShowFormulas, die von Worksheet angeboten wird, verwenden, um die Ansicht von Formel zu Wert in einem bestimmten Arbeitsblatt zu ändern.
## **Ooxml zu FileFormatType hinzugefügt**
Eine neue Konstante Ooxml wurde der Klasse FileFormatType hinzugefügt, um die verschlüsselten Office Open XML-Dateien wie XLSX, DOCX, PPTX und mehr zu repräsentieren.
## **FilterColumnCollection von AutoFilter veraltet**
Mit Aspose.Cells for Java wurde die Eigenschaft FilterColumnCollection als veraltet markiert. Es wird empfohlen, stattdessen die Eigenschaft AuotFilter.FilterColumns zu verwenden.
## **Ersetzte SeriesCollection.SecondCatergoryData durch SeriesCollection.SecondCategoryData**
Wir haben den Tippfehler im Eigenschaftsnamen von SeriesCollection.SecondCatergoryData korrigiert. Sie verwenden nun die Eigenschaft SeriesCollection.SecondCategoryData, während die ursprüngliche Eigenschaft SeriesCollection.SecondCatergoryData als veraltet markiert wurde.
