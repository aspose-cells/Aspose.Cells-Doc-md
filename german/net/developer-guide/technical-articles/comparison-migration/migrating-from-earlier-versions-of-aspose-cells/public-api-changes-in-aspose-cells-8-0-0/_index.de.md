---
title: Öffentlich API Änderungen in Aspose.Cells 8.0.0
type: docs
weight: 10
url: /de/net/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Diese Seite listet öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.0 eingeführt wurden. Es enthält nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells, die sich auf den vorhandenen Code auswirken können.

{{% /alert %}} 
## **MemorySetting zu LoadOptions & WorkbookSettings hinzugefügt**
Ab v8.0.0 von Aspose.Cells for .NET haben wir die Speichernutzungsoptionen aus Leistungsgründen bereitgestellt. Die Eigenschaft „MemorySetting“ ist jetzt in den Klassen „LoadOptions“ und „WorkbookSettings“ verfügbar.
##### **Beispiel**
Demonstriert, wie eine Excel-Datei (mit großer Größe) im optimierten Modus gelesen wird.

**C#**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Veranschaulicht, wie ein großes Dataset im optimierten Modus in ein Arbeitsblatt geschrieben wird.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Optimieren des Arbeitsspeichers beim Arbeiten mit großen Dateien](/cells/de/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Implementierungen von Zeile & Cell wurden geändert**
 In früheren Versionen wurden Row- und Cell-Objekte im Arbeitsspeicher gehalten, um entsprechende Zeilen und Zellen in einem Arbeitsblatt darzustellen. Es wurde immer dieselbe Instanz zurückgegeben**RowCollection[int index]** oder**Cells[int-Zeile, int-Spalte]** wurden abgerufen. Aus Gründen der Speicherleistung werden ab sofort nur noch die Eigenschaften und Daten von Row und Cell im Speicher gehalten. Daher wurde das Objekt Row & Cell zum Wrapper der oben genannten Eigenschaften.
### **Beispiel**
Demonstriert, wie von nun an die Objekte Cell und Row verglichen werden.

**C#**

{{< highlight "csharp" >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Da die Row- und Cell-Objekte gemäß dem Aufruf instanziiert werden, werden sie nicht von der Cells-Komponente im Arbeitsspeicher gehalten und verwaltet. Daher werden nach einigen Einfüge- und Löschvorgängen die Zeilen- und Spaltenindizes möglicherweise nicht aktualisiert oder noch schlimmer, diese Objekte werden ungültig.
### **Beispiel**
Beispielsweise gibt das folgende Code-Snippet mit 8.0.0 und höher ungültige Ergebnisse zurück.

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Mit der neuen Version wird das Objekt Cell ungültig oder verweist mit einem unerwünschten Wert auf A2. Um eine solche Situation zu vermeiden, rufen Sie die Row- oder Cell-Objekte erneut aus der Cells-Sammlung ab, um das korrekte Ergebnis abzurufen.

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection erbt CollectionBase nicht mehr, da es kein Row-Objekt in seiner inneren Liste gibt.

{{% /alert %}}
## **Cell.StringValue-Verhalten geändert**
 In früheren Versionen spezielles Muster_wurde beim Formatieren von Zellenwerten ignoriert, wobei das Sonderzeichen * immer ein Zeichen im formatierten Ergebnis erzeugte. Ab dieser Version haben wir die Logik geändert, um Sonderzeichen zu behandeln_ und* um das formatierte Ergebnis gleich wie bei der Excel-Anwendung zu machen. Das benutzerdefinierte Zellenformat „_(\$* #,##0.00_)" verwendet, um den Wert 123 darzustellen, erzeugte das Ergebnis als "$ 123,00". In neuen Versionen enthält Cell.StringValue das Ergebnis als "$ 123,00", was das gleiche Verhalten ist, das die Excel-Anwendung beim Kopieren der Zelle zeigt als Text oder als CSV exportieren.
## **CreatedTime zu PdfSaveOptions hinzugefügt**
Jetzt können Benutzer die PDF-Erstellungszeit abrufen oder festlegen, während sie die Tabelle als PDF speichern, während sie die PdfSaveOptions-Klasse verwenden.
## **ShowFormulas zum Arbeitsblatt hinzugefügt**
Von nun an können Benutzer die von Worksheet angebotene boolesche Eigenschaft ShowFormulas verwenden, um die Ansicht von der Formel zum Wert eines bestimmten Arbeitsblatts zu ändern.
## **Ooxml zu FileFormatType hinzugefügt**
Der FileFormatType-Klasse wurde eine neue Konstante Ooxml hinzugefügt, um die verschlüsselte Office Open XML-Datei wie XLSX, DOCX, PPTX und mehr darzustellen.
## **Veraltete FilterColumnCollection von AutoFilter**
Mit Aspose.Cells for Java wurde die FilterColumnCollection-Eigenschaft als veraltet markiert. Es wird empfohlen, stattdessen die Eigenschaft AuotFilter.FilterColumns zu verwenden.
## **SeriesCollection.SecondCatergoryData durch SeriesCollection.SecondCategoryData ersetzt**
Wir haben den Tippfehler im Eigenschaftsnamen für SeriesCollection.SecondCatergoryData grundsätzlich korrigiert. Sie können die Eigenschaft SeriesCollection.SecondCategoryData jetzt weiter verwenden, während die ursprüngliche Eigenschaft SeriesCollection.SecondCatergoryData als veraltet markiert wurde.
