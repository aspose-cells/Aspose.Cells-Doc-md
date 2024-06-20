---
title: Öffentliche API Änderungen in Aspose.Cells 8.9.1
type: docs
weight: 310
url: /de/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.9.0 auf 8.9.1, die für Modul- / Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Konfigurierbare Schriftquellen**
Aspose.Cells for .NET hat eine Reihe von Klassen freigegeben, um die Unterstützung für konfigurierbare Schriftquellen zur Darstellung von Tabellenkalkulationen bereitzustellen. Hier ist die Liste der Klassen, die mit Aspose.Cells for .NET 8.9.1 hinzugefügt wurden.

1. Die Klasse FontConfigs gibt die Schrifteinstellungen an.
1. Die Klasse FontSourceBase ist eine abstrakte Basisklasse für die Klassen, die es dem Benutzer ermöglichen, verschiedene Schriftquellen anzugeben.
1. Die Klasse FileFontSource repräsentiert die einzelne TrueType-Schriftartdatei, die im Dateisystem gespeichert ist.
1. Die Klasse FolderFontSource repräsentiert den Ordner, der TrueType-Schriftartdateien enthält.
1. Die Klasse MemoryFontSource repräsentiert die einzelne TrueType-Schriftartdatei, die im Speicher gespeichert ist.
1. Die Enumeration FontSourceType gibt den Typ einer Schriftquelle an.

Mit den oben genannten Änderungen ermöglicht Aspose.Cells for .NET das Festlegen der Schriften wie unten beschrieben.

1. Festlegen eines benutzerdefinierten Schriftordners unter Verwendung der Methode FontConfigs.SetFontFolder.
1. Festlegen mehrerer benutzerdefinierter Schriftordner unter Verwendung der Methode FontConfigs.SetFontFolders.
1. Festlegen von Schriftquellen aus einem benutzerdefinierten Schriftordner, einer einzelnen Schriftartdatei oder Schriftartdaten aus einem Byte-Array unter Verwendung der Methode FontConfigs.SetFontSources.

Hier ist ein einfaches Anwendungsszenario für die oben genannten Methoden.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Die Methoden FontConfigs.SetFontFolder und FontConfigs.SetFontFolders akzeptieren beide einen booleschen Typ als zweiten Parameter. Das Übergeben von true als zweiten Parameter wird die Aspose.Cells-APIs anweisen, nach Schriftordnern in den Unterordnern zu suchen.

{{% /alert %}} 

Aspose.Cells for .NET ermöglicht auch die Konfiguration der Schriftart-Substitution. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schriftart auf dem Rechner, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste von Schriftartnamen als Alternative zur ursprünglich erforderlichen Schriftart bereitstellen. Um dies zu erreichen, haben die Aspose.Cells-APIs die Methode FontConfigs.SetFontSubstitutes freigegeben, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ string und sollte der Name der Schriftart sein, die substituiert werden soll. Der zweite Parameter ist ein Array vom Typ string. Benutzer können eine Liste von Schriftartnamen als Ersatz für den ursprünglichen Schriftartnamen bereitstellen (der im ersten Parameter angegeben ist).

Hier ist ein einfaches Anwendungsszenario für die Methode FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET hat auch Mittel bereitgestellt, um Informationen darüber zu sammeln, welche Quellen und Substitutionen festgelegt wurden.

1. Die Methode FontConfigs.GetFontSources gibt ein Array vom Typ FontSourceBase zurück, das die Liste der angegebenen Schriftquellen enthält. Falls keine Quellen festgelegt wurden, gibt die Methode FontConfigs.GetFontSources ein leeres Array zurück.
1. Die Methode FontConfigs.GetFontSubstitutes akzeptiert einen Parameter vom Typ string, mit dem der Schriftartname angegeben werden kann, für den eine Substitution festgelegt wurde. Falls keine Substitution für den angegebenen Schriftartnamen festgelegt wurde, gibt die Methode FontConfigs.GetFontSubstitutes null zurück.

{{% alert color="primary" %}} 

Für weitere Details zu FontConfigs lesen Sie bitte den Artikel über [Konfigurieren von Schriftarten für das Rendern von Tabellenkalkulationen](/cells/de/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Hinzugefügt: IFilePathProvider-Schnittstelle & HtmlSaveOptions.FilePathProvider-Eigenschaft**
Aspose.Cells for .NET 8.9.1 ermöglicht das Setzen/Abfragen des IFilePathProvider zum Exportieren von Tabellenkalkulationen in separate HTML-Dateien. Diese neuen APIs sind hilfreich in Szenarien, in denen Hyperlinks in einer Tabelle auf einen Ort in einer anderen Tabelle verweisen, und die Anwendungsanforderung ist, jede Tabelle in eine separate HTML-Datei zu rendert. Die Implementierung des IFilePathProvider ermöglicht das Beibehalten der genannten Hyperlinks, unabhhängig davon, ob sie auf einen Ort in einer separaten resultierenden HTML-Datei verweisen.

Im Folgenden wird das einfache Anwendungsszenario der Eigenschaft HtmlSaveOptions.FilePathProvider beschrieben.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



So implementiert man das IFilePathProvider-Interface.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Für weitere Details zu dieser Optimierung lesen Sie bitte den Artikel über [Implementierung des IFilePathProvider-Interfaces](/cells/de/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Hinzugefügte CopyOptions.ReferToDestinationSheet Eigenschaft & Überladung für Cells.CopyRows Methode**
Die Aspose.Cells for .NET-API hat die Boolean-Typen CopyOptions.ReferToDestinationSheet Eigenschaft freigegeben, zusammen mit einer Überladung der Cells.CopyRows Methode, um den Kopiervorgang von Zeilen zu erleichtern, wenn die zu kopierenden Zeilen auch ein Diagramm und seine Datenquelle enthalten. Entwickler können diese neuen APIs nutzen, um die Datenquelle des Diagramms auf die Quell- oder Zielarbeitsblätter zu verweisen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den Artikel über [Steuerung der Datenquelle des Diagramms beim Kopieren von Zeilen](/cells/de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Hinzugefügt: CalculationOptions.Recursive-Eigenschaft**
Aspose.Cells for .NET 8.9.1 hat die Boolean-Typen CalculationOptions.Recursive Eigenschaft freigegeben. Durch Setzen der CalculationOptions.Recursive Eigenschaft auf true und Übergeben des Objekts an die Workbook.CalculateFormula Methode wird die Aspose.Cells-API angewiesen, die abhängigen Zellen rekursiv zu berechnen, wenn Zellen berechnet werden, die von anderen Zellen abhängen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Für weitere Details zu dieser Optimierung lesen Sie bitte den Artikel über [Optimierung der Berechnungszeit](/cells/de/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Veraltete APIs**
### **Veraltete Eigenschaft CellsHelper.FontDir**
Es wird empfohlen, die FontConfigs.SetFontFolder(string, bool) Methode mit rekursivem Ordner auf false zu verwenden.
### **Veraltete Eigenschaft CellsHelper.FontDirs**
Verwenden Sie die FontConfigs.SetFontFolders(string[], bool) Methode mit rekursivem Ordner auf false stattdessen.
### **Veraltete Eigenschaft CellsHelper.FontFiles**
Verwenden Sie die Methode FontConfigs.SetFontSources(FontSourceBase[]) stattdessen.
