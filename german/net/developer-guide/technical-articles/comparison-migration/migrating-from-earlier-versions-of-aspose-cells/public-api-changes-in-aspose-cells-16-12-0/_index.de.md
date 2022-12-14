---
title: Öffentlich API Änderungen in Aspose.Cells 16.12.0
type: docs
weight: 360
url: /de/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.11.0 zu 16.12.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Objekte zur Ladezeit filtern**
Aspose.Cells 16.12.0 hat die LoadFilter-Klasse zusammen mit der LoadOptions.LoadFilter-Eigenschaft verfügbar gemacht, die zusammen den zu ladenden Datentyp steuern können, während eine Instanz von Workbook aus einer Vorlagendatei initialisiert wird.

Hier ist ein einfaches Anwendungsszenario, um nur die Dokumenteigenschaften aus einer Vorlagendatei zu laden.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Das folgende Snippet lädt alles aus einer vorhandenen Tabelle mit Ausnahme der Diagramme.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Der folgende Code lädt nur die Zellendaten (zusammen mit Formeln) und die Formatierung aus einer vorhandenen Tabelle.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Die LoadFilter-Klasse ermöglicht auch die Anpassung des Ladevorgangs gemäß den Eigenschaften des Arbeitsblatts. Um den Ladevorgang gemäß dem Arbeitsblatt anzupassen, muss die LoadFilter.StartSheet-Methode wie unten gezeigt überschrieben werden.

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



Das folgende Snippet verwendet die oben definierte CustomFilter-Klasse.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **FileFormatType.OTS-Enumeration hinzugefügt**
Aspose.Cells 16.12.0 hat den OTS-Eintrag zur FileFormatType-Enumeration hinzugefügt, um das Format von OTS-Dateien zu erkennen.

Das folgende Snippet verwendet FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **FontConfigs.PreferSystemFontSubstitutes-Eigenschaft hinzugefügt**
Aspose.Cells 16.12.0 hat die PreferSystemFontSubstitutes-Eigenschaft für die FontConfigs-Klasse verfügbar gemacht. Die Eigenschaft FontConfigs.PreferSystemFontSubstitutes ist vom Typ Boolean und gibt an, ob API zuerst den Schriftartersetzungsmechanismus des Systems verwenden soll, falls eine erforderliche Schriftart nicht vorhanden ist und keine Ersetzung für die bestimmte Schriftart definiert wurde. Der Standardwert der Eigenschaft FontConfigs.PreferSystemFontSubstitutes ist false.
### **BuiltInDocumentPropertyCollection.ScaleCrop-Eigenschaft hinzugefügt**
Aspose.Cells 16.12.0 hat die ScaleCrop-Eigenschaft zur BuiltInDocumentPropertyCollection-Klasse hinzugefügt. ScaleCrop gibt den Anzeigemodus des Dokument-Thumbnails an. Wenn dieses Element auf „true“ gesetzt wird, wird die Miniaturansicht des Dokuments gemäß der Anzeige skaliert, während die Einstellung auf „false“ das Zuschneiden der Miniaturansicht des Dokuments ermöglicht, um den Ausschnitt anzuzeigen, der in die Anzeige passt.
### **BuiltInDocumentPropertyCollection.LinksUpToDate-Eigenschaft hinzugefügt**
Aspose.Cells 16.12.0 hat auch die LinksUpToDate-Eigenschaft für die BuiltInDocumentPropertyCollection-Klasse verfügbar gemacht. Die Eigenschaft LinksUpToDate gibt an, ob die Hyperlinks in einem Dokument aktuell sind.
### **Workbook.ExportXml-Methode hinzugefügt**
Aspose.Cells 16.12.0 hat die Workbook.ExportXml-Methode verfügbar gemacht, die es ermöglicht, die XML-Zuordnungsdaten im angegebenen Dateipfad zu speichern. Die Workbook.ExportXml-Methode akzeptiert 2 Parameter, wobei der erste Parameter vom Typ Zeichenfolge der Name der XML-Zuordnung und der zweite Parameter der Dateipfad zum Speichern der XML-Daten sein sollte.
### **WorksheetCollection.CreateRange-Methode hinzugefügt**
Aspose.Cells 16.12.0 hat die WorksheetCollection.CreateRange-Methode hinzugefügt, die es ermöglicht, einen Bereich basierend auf einer Adresse (Zellbereichsreferenz) und einem Arbeitsblattindex zu erstellen.

Der folgende Codeausschnitt verwendet die WorksheetCollection.CreateRange-Methode, um einen Zellbereich zu erstellen, der sich über A1 bis A2 im ersten (Standard-)Arbeitsblatt erstreckt.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Veraltete APIs**
### **Veraltete LoadOptions.LoadDataOptions-Eigenschaft**
Bitte verwenden Sie alternativ die Eigenschaft LoadOptions.LoadFilter.
### **Veraltete LoadOptions.LoadDataFilterOptions-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft LoadOptions.LoadFilter.
### **Veraltete LoadOptions.OnlyLoadDocumentProperties-Eigenschaft**
Bitte verwenden Sie alternativ die Eigenschaft LoadOptions.LoadFilter.
### **Veraltete LoadOptions.LoadDataAndFormatting-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft LoadOptions.LoadFilter.

{{% alert color="primary" %}} 

Codeausschnitte für alle veralteten APIs wurden oben geteilt.

{{% /alert %}}
## **Gelöschte APIs**
### **Gelöschte DataLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die DataLabels.RotationAngle-Eigenschaft.
### **Gelöschte Title.Rotation-Eigenschaft**
Bitte verwenden Sie alternativ die Eigenschaft Title.RotationAngle.
### **Gelöschte DataLabels.Background-Eigenschaft**
Es wird empfohlen, stattdessen die DataLabels.BackgroundMode-Eigenschaft zu verwenden.
### **DisplayUnitLabel.Rotation-Eigenschaft gelöscht**
Bitte erwägen Sie die Verwendung der DisplayUnitLabel.RotationAngle-Eigenschaft, um dasselbe Ziel zu erreichen.
