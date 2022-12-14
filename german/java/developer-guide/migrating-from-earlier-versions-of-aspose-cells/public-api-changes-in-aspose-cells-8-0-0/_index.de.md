---
title: Öffentlich API Änderungen in Aspose.Cells 8.0.0
type: docs
weight: 20
url: /de/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Diese Seite listet öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.0 eingeführt wurden. Es enthält nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells, die sich auf den vorhandenen Code auswirken können.

{{% /alert %}} 
## **MemorySetting zu LoadOptions & WorkbookSettings hinzugefügt**
Ab v8.0.0 von Aspose.Cells for Java haben wir die Speichernutzungsoptionen aus Leistungsgründen bereitgestellt. Die Eigenschaft „MemorySetting“ ist jetzt in den Klassen „LoadOptions“ und „WorkbookSettings“ verfügbar.
### **Beispiel**
Demonstriert, wie eine Excel-Datei (mit großer Größe) im optimierten Modus gelesen wird.

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Veranschaulicht, wie ein großes Dataset im optimierten Modus in ein Arbeitsblatt geschrieben wird.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Optimieren des Arbeitsspeichers beim Arbeiten mit großen Dateien](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)s.

{{% /alert %}}
## **Implementierungen von Zeile & Cell wurden geändert**
 In früheren Versionen wurden Row- und Cell-Objekte im Arbeitsspeicher gehalten, um entsprechende Zeilen und Zellen in einem Arbeitsblatt darzustellen. Es wurde immer dieselbe Instanz zurückgegeben**RowCollection[int index]** oder**Cells[int-Zeile, int-Spalte]** wurden abgerufen. Aus Gründen der Speicherleistung werden ab sofort nur noch die Eigenschaften und Daten von Row und Cell im Speicher gehalten. Daher wurde das Objekt Row & Cell zum Wrapper der oben genannten Eigenschaften.
### **Beispiel**
Demonstriert, wie von nun an die Objekte Cell und Row verglichen werden.

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Da die Row- und Cell-Objekte gemäß dem Aufruf instanziiert werden, werden sie nicht von der Cells-Komponente im Arbeitsspeicher gehalten und verwaltet. Daher werden nach einigen Einfüge- und Löschvorgängen die Zeilen- und Spaltenindizes möglicherweise nicht aktualisiert oder noch schlimmer, diese Objekte werden ungültig.
### **Beispiel**
Beispielsweise gibt das folgende Code-Snippet mit 8.0.0 und höher ungültige Ergebnisse zurück,

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Mit der neuen Version wird das Objekt Cell ungültig oder verweist mit einem unerwünschten Wert auf A2. Um eine solche Situation zu vermeiden, rufen Sie die Row- oder Cell-Objekte erneut aus der Cells-Sammlung ab, um das korrekte Ergebnis abzurufen.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection erbt CollectionBase nicht mehr, da es kein Row-Objekt in seiner inneren Liste gibt.

{{% /alert %}}
## **Cell.StringValue-Verhalten geändert**
 In früheren Versionen spezielles Muster_wurde beim Formatieren von Zellenwerten ignoriert, wobei das Sonderzeichen * immer ein Zeichen im formatierten Ergebnis erzeugte. Ab dieser Version haben wir die Logik geändert, um Sonderzeichen zu behandeln_ und* um das formatierte Ergebnis gleich wie bei der Excel-Anwendung zu machen. Das benutzerdefinierte Zellenformat „_(\$* #,##0.00_)" verwendet, um den Wert 123 darzustellen, erzeugte das Ergebnis als "$ 123,00". In neuen Versionen enthält Cell.StringValue das Ergebnis als "$ 123,00", was das gleiche Verhalten ist, das die Excel-Anwendung beim Kopieren der Zelle zeigt als Text oder als CSV exportieren.
## **CreatedTime zu PdfSaveOptions hinzugefügt**
Jetzt können Benutzer die PDF-Erstellungszeit abrufen oder festlegen, während sie die Tabelle als PDF speichern, während sie die PdfSaveOptions-Klasse verwenden.
## **ShowFormulas zum Arbeitsblatt hinzugefügt**
Von nun an können Benutzer die von Worksheet angebotene boolesche Eigenschaft ShowFormulas verwenden, um die Ansicht zwischen Formel und Wert eines bestimmten Arbeitsblatts umzuschalten.
## **Ooxml zu FileFormatType hinzugefügt**
Der FileFormatType-Klasse wurde eine neue Konstante Ooxml hinzugefügt, um die verschlüsselte Office Open XML-Datei wie XLSX, DOCX, PPTX und mehr darzustellen.
## **Veraltete FilterColumnCollection von AutoFilter**
Mit Aspose.Cells for Java wurde die Methode getFilterColumnCollection als veraltet markiert. Es wird empfohlen, stattdessen die Methode AuotFilter.getFilterColumns zu verwenden.
## **SeriesCollection.SecondCatergoryData durch SeriesCollection.SecondCategoryData ersetzt**
Wir haben den Tippfehler im Methodennamen für SeriesCollection.getSecondCatergoryData grundsätzlich korrigiert. Sie können die Methode SeriesCollection.getSecondCategoryData jetzt weiter verwenden, während die ursprüngliche Methode SeriesCollection.getSecondCatergoryData als veraltet markiert wurde.
