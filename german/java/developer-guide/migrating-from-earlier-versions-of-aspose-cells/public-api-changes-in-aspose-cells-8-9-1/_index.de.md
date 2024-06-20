---
title: Öffentliche API Änderungen in Aspose.Cells 8.9.1
type: docs
weight: 320
url: /de/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.9.0 auf 8.9.1, die für Modul- / Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Konfigurierbare Schriftquellen**
Aspose.Cells for Java hat eine Reihe von Klassen freigegeben, um die Unterstützung für konfigurierbare Schriftquellen für die Darstellung von Tabellenkalkulationen bereitzustellen. Hier ist die Liste der Klassen, die mit Aspose.Cells for Java 8.9.1 hinzugefügt wurden.

1. Die Klasse FontConfigs gibt die Schrifteinstellungen an.
1. Die Klasse FontSourceBase ist eine abstrakte Basisklasse für die Klassen, die es dem Benutzer ermöglichen, verschiedene Schriftquellen anzugeben.
1. Die Klasse FileFontSource repräsentiert die einzelne TrueType-Schriftartdatei, die im Dateisystem gespeichert ist.
1. Die Klasse FolderFontSource repräsentiert den Ordner, der TrueType-Schriftartdateien enthält.
1. Die Klasse MemoryFontSource repräsentiert die einzelne TrueType-Schriftartdatei, die im Speicher gespeichert ist.
1. Die Enumeration FontSourceType gibt den Typ einer Schriftquelle an.

Mit den oben genannten Änderungen ermöglicht Aspose.Cells for Java das Festlegen der Schriften wie folgt.

1. Legen Sie einen benutzerdefinierten Schriftordner fest, während Sie die Methode FontConfigs.setFontFolder verwenden.
1. Legen Sie mehrere benutzerdefinierte Schriftordner fest, während Sie die Methode FontConfigs.setFontFolders verwenden.
1. Legen Sie Schriftquellen aus einem benutzerdefinierten Schriftordner, einer einzelnen Schriftartdatei oder Schriftendaten aus einem Byte-Array fest, während Sie die Methode FontConfigs.setFontSources verwenden.

Hier ist ein einfaches Anwendungsszenario für die oben genannten Methoden.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Die Methoden FontConfigs.setFontFolder und FontConfigs.setFontFolders akzeptieren beide einen zweiten Parameter vom Typ Boolean. Wenn true als zweiter Parameter übergeben wird, werden die Aspose.Cells APIs angewiesen, nach den Schriftartdateien in den Unterordnern zu suchen. 

{{% /alert %}} 

Aspose.Cells for Java ermöglicht auch die Konfiguration der Schriftarten-Substitution. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schriftart auf dem Computer, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste von Schriftartnamen als Alternative zur ursprünglich benötigten Schriftart angeben. Um dies zu ermöglichen, haben die Aspose.Cells APIs die Methode FontConfigs.setFontSubstitutes freigegeben, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ String und sollte der Name der Schriftart sein, die ersetzt werden muss. Der zweite Parameter ist ein Array vom Typ String. Benutzer können eine Liste von Schriftartnamen als Ersatz für den ursprünglichen Schriftartnamen angeben (der im ersten Parameter angegeben ist).

Hier ist ein einfaches Anwendungsszenario für die Methode FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java hat auch Mittel bereitgestellt, um Informationen darüber zu sammeln, welche Quellen und Substitutionen festgelegt wurden.

1. Die Methode FontConfigs.getFontSources gibt ein Array vom Typ FontSourceBase zurück, das die Liste der angegebenen Schriftquellen enthält. Falls keine Quellen festgelegt wurden, wird die Methode FontConfigs.getFontSources ein leeres Array zurückgeben.
1. Die Methode FontConfigs.getFontSubstitutes akzeptiert einen Parameter vom Typ String, mit dem der Schriftname angegeben werden kann, für den eine Substitution festgelegt wurde. Falls keine Substitution für den angegebenen Schriftname festgelegt wurde, gibt die Methode FontConfigs.getFontSubstitutes null zurück.

{{% alert color="primary" %}} 

Weitere Details zu FontConfigs finden Sie im Artikel über die [Konfiguration von Schriftarten für das Rendern von Tabellenkalkulationen](/cells/de/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Hinzugefügt: IFilePathProvider-Schnittstelle & HtmlSaveOptions.FilePathProvider-Eigenschaft**
Aspose.Cells for Java 8.9.1 ermöglicht das Abrufen/Festlegen des IFilePathProvider zum Exportieren von Tabellenkalkulationen in separate HTML-Dateien. Diese neuen APIs sind in Szenarien hilfreich, in denen Hyperlinks in einer Arbeitsmappe auf einen Speicherort in einer anderen Arbeitsmappe verweisen und jede Arbeitsmappe in eine separate HTML-Datei gerendert werden soll. Durch Implementierung des IFilePathProvider bleiben die genannten Hyperlinks unabhängig von der Tatsache, dass sie auf einen Speicherort in einer separaten resultierenden HTML-Datei verweisen, intakt.

Im Folgenden wird das einfache Anwendungsszenario der Eigenschaft HtmlSaveOptions.FilePathProvider beschrieben.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Weitere Details zu dieser Verbesserung finden Sie im Artikel über die [Implementierung des IFilePathProvider Interface](/cells/de/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Hinzugefügt: CopyOptions.ReferToDestinationSheet-Eigenschaft & Überladung für Cells.copyRows-Methode**
Aspose.Cells for Java API hat die Eigenschaft CopyOptions.ReferToDestinationSheet vom Typ Boolean und eine Überladung der Cells.copyRows-Methode freigegeben, um die Kopiervorgänge von Zeilen zu erleichtern, wenn die zu kopierenden Zeilen auch ein Diagramm und seine Datenquelle enthalten. Entwickler können diese neuen APIs verwenden, um die Datenquelle des Diagramms auf die Quell- oder Zielarbeitsblätter zu verweisen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Weitere Details zu diesem Feature finden Sie im Artikel über die [Steuerung der Datenquelle des Diagramms beim Kopieren von Zeilen](/cells/de/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Hinzugefügt: CalculationOptions.Recursive-Eigenschaft**
Aspose.Cells for Java 8.9.1 hat die Eigenschaft CalculationOptions.Recursive vom Typ Boolean freigegeben. Durch Setzen der Eigenschaft CalculationOptions.Recursive auf true und Übergeben des Objekts an die Workbook.calculateFormula-Methode weisen Sie die Aspose.Cells APIs an, die abhängigen Zellen rekursiv zu berechnen, wenn Zellen berechnet werden, die von anderen Zellen abhängen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Weitere Details zu diesem Feature finden Sie im Artikel über die [Optimierung der Berechnungszeit](/cells/de/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Veraltete APIs**
### **Veraltete Eigenschaft CellsHelper.FontDir**
Es wird empfohlen, die Methode FontConfigs.setFontFolder(String, boolean) mit rekursivem Ordner auf false zu verwenden.
### **Veraltete Eigenschaft CellsHelper.FontDirs**
Verwenden Sie die Methode FontConfigs.setFontFolders(String[], boolean) mit rekursivem Ordner auf false.
### **Veraltete Eigenschaft CellsHelper.FontFiles**
Verwenden Sie stattdessen die Methode FontConfigs.setFontSources(FontSourceBase[]).
