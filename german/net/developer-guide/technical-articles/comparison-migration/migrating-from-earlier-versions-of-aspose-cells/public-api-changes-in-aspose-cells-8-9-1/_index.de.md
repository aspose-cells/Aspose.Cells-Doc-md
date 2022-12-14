---
title: Öffentlich API Änderungen in Aspose.Cells 8.9.1
type: docs
weight: 310
url: /de/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.9.0 zu 8.9.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Konfigurierbare Schriftartquellen**
Aspose.Cells for .NET hat eine Reihe von Klassen verfügbar gemacht, um die Unterstützung für konfigurierbare Schriftartquellen zum Rendern von Tabellenkalkulationen bereitzustellen. Hier ist die Liste der Klassen, die mit Aspose.Cells for .NET 8.9.1 hinzugefügt wurden.

1. Die FontConfigs-Klasse gibt die Schriftarteinstellungen an.
1. Die FontSourceBase-Klasse ist eine abstrakte Basisklasse für die Klassen, die es dem Benutzer ermöglichen, verschiedene Schriftartquellen anzugeben.
1. Die FileFontSource-Klasse stellt die einzelne TrueType-Schriftartdatei dar, die im Dateisystem gespeichert ist.
1. Die FolderFontSource-Klasse stellt den Ordner dar, der TrueType-Schriftartdateien enthält.
1. Die MemoryFontSource-Klasse stellt die einzelne TrueType-Schriftartdatei dar, die im Arbeitsspeicher gespeichert ist.
1. Die Aufzählung FontSourceType gibt den Typ einer Schriftartquelle an.

Mit den oben genannten Änderungen ermöglicht die Aspose.Cells for .NET die Einstellung der Schriftarten wie unten beschrieben.

1. Legen Sie einen benutzerdefinierten Schriftartenordner fest, während Sie die Methode FontConfigs.SetFontFolder verwenden.
1. Legen Sie mehrere Ordner für benutzerdefinierte Schriftarten fest, während Sie die Methode FontConfigs.SetFontFolders verwenden.
1. Legen Sie Schriftartquellen aus einem benutzerdefinierten Schriftartordner, einer einzelnen Schriftartdatei oder Schriftartdaten aus einem Array von Bytes fest, während Sie die FontConfigs.SetFontSources-Methode verwenden.

Hier ist ein einfaches Anwendungsszenario der oben genannten Methoden.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Beide FontConfigs.SetFontFolder- und FontConfigs.SetFontFolders-Methoden akzeptieren einen zweiten Parameter vom Typ Boolean. Die Übergabe von true als zweiten Parameter weist die Aspose.Cells-APIs an, die Unterordner nach den Schriftartdateien zu durchsuchen.

{{% /alert %}} 

Aspose.Cells for .NET ermöglicht auch die Konfiguration der Schriftersetzung. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schriftart auf dem Computer, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste mit Schriftartnamen als Alternative zur ursprünglich erforderlichen Schriftart bereitstellen. Um dies zu erreichen, haben die Aspose.Cells-APIs die FontConfigs.SetFontSubstitutes-Methode verfügbar gemacht, die zwei Parameter akzeptiert. Der erste Parameter ist vom Typ string, der der Name der Schriftart sein sollte, die ersetzt werden muss. Der zweite Parameter ist ein Array vom Typ String. Benutzer können eine Liste mit Schriftartnamen als Ersatz für den ursprünglichen Schriftartnamen (angegeben im ersten Parameter) bereitstellen.

Hier ist ein einfaches Nutzungsszenario der Methode FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Die Aspose.Cells for .NET hat auch Mittel bereitgestellt, um Informationen darüber zu sammeln, welche Quellen und Substitutionen eingestellt wurden.

1. Die Methode FontConfigs.GetFontSources gibt ein Array vom Typ FontSourceBase zurück, das die Liste der angegebenen Schriftartquellen enthält. Falls keine Quellen festgelegt wurden, gibt die Methode FontConfigs.GetFontSources ein leeres Array zurück.
1. Die Methode „FontConfigs.GetFontSubstitutes“ akzeptiert einen Parameter vom Typ „String“, mit dem der Schriftartname angegeben werden kann, für den eine Ersetzung festgelegt wurde. Falls für den angegebenen Schriftartnamen keine Ersetzung festgelegt wurde, gibt die Methode FontConfigs.GetFontSubstitutes null zurück.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu FontConfigs finden Sie im Artikel unter[Konfigurieren von Schriftarten zum Rendern von Tabellenkalkulationen](/cells/de/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **IFilePathProvider Interface & HtmlSaveOptions.FilePathProvider-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.9.1 ermöglicht das Abrufen/Setzen des IFilePathProvider zum Exportieren von Arbeitsblättern in separate HTML-Dateien. Diese neuen APIs sind in Szenarien hilfreich, in denen Hyperlinks in einem Arbeitsblatt auf eine Position in einem anderen Arbeitsblatt verweisen, in denen die Anwendungsanforderung darin besteht, jedes Arbeitsblatt in eine separate HTML-Datei zu rendern. Das Implementieren des IFilePathProvider ermöglicht es, die oben erwähnten Hyperlinks intakt zu halten, ungeachtet der Tatsache, dass sie auf einen Ort in einer separaten resultierenden HTML-Datei zeigen.

Im Folgenden ist das einfache Verwendungsszenario der HtmlSaveOptions.FilePathProvider-Eigenschaft dargestellt.

**C#**

{{< highlight "csharp" >}}

 // Eine Tabelle in eine Instanz von Workbook laden

var book = new Workbook(dir + "sample.xlsx");

// Speichern Sie jedes Arbeitsblatt in einer separaten HTML-Datei

 für (int i = 0; i< book.Worksheets.Count; i++)

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



So implementieren Sie die IFilePathProvider-Schnittstelle.

**C#**

{{< highlight "csharp" >}}

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

 Weitere Einzelheiten zu dieser Verbesserung finden Sie im Artikel auf[Implementieren der IFilePathProvider-Schnittstelle](/cells/de/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheet-Eigenschaft und Überladung für Cells.CopyRows-Methode hinzugefügt**
Aspose.Cells for .NET API hat die CopyOptions.ReferToDestinationSheet-Eigenschaft des booleschen Typs zusammen mit der Überladung der Cells.CopyRows-Methode verfügbar gemacht, um den Vorgang zum Kopieren von Zeilen zu vereinfachen, wenn zu kopierende Zeilen auch ein Diagramm und seine Datenquelle enthalten. Entwickler können diese neuen APIs verwenden, um die Datenquelle des Diagramms auf die Quell- oder Zielarbeitsblätter zu verweisen.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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

 Weitere Einzelheiten zu dieser Funktion finden Sie im Artikel auf[Steuern Sie die Datenquelle des Diagramms beim Kopieren von Zeilen](/cells/de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **CalculationOptions.Recursive-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.9.1 hat die CalculationOptions.Recursive-Eigenschaft des booleschen Typs verfügbar gemacht. Durch Festlegen der Eigenschaft „CalculationOptions.Recursive“ auf „true“ und Übergeben des Objekts an die Methode „Workbook.CalculateFormula“ werden die Aspose.Cells-APIs angewiesen, die abhängigen Zellen rekursiv zu berechnen, wenn Zellen berechnet werden, die von anderen Zellen abhängen.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im Artikel auf[Berechnungszeit optimieren](/cells/de/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Veraltete APIs**
### **Veraltete CellsHelper.FontDir-Eigenschaft**
Es wird empfohlen, stattdessen die Methode FontConfigs.SetFontFolder(string, bool) zu verwenden, wobei der Ordner rekursiv zu „false“ wird.
### **Veraltete CellsHelper.FontDirs-Eigenschaft**
Verwenden Sie stattdessen die Methode „FontConfigs.SetFontFolders(string[], bool)“, wobei der Ordner rekursiv zu „false“ wird.
### **Veraltete CellsHelper.FontFiles-Eigenschaft**
Verwenden Sie stattdessen die Methode FontConfigs.SetFontSources(FontSourceBase[]).
