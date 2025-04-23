---
title: Öffentliche API Änderungen in Aspose.Cells 16.12.0
type: docs
weight: 360
url: /de/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 16.11.0 auf 16.12.0, die für Modul-/Anwendungsentwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Filterobjekte beim Laden**
Aspose.Cells 16.12.0 hat die LoadFilter-Klasse zusammen mit der LoadOptions.LoadFilter-Eigenschaft freigegeben, die gemeinsam steuern können, welche Art von Daten beim Initialisieren einer Instanz von Workbook aus einer Vorlagendatei geladen werden sollen.

Hier ist ein einfaches Anwendungsszenario, um nur die Dokumenteigenschaften aus einer Vorlagendatei zu laden.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Das folgende Snippet lädt alles aus einer vorhandenen Tabellenkalkulation, außer den Diagrammen.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Der folgende Code lädt nur die Zelldaten (zusammen mit Formeln) und das Formatieren aus einer vorhandenen Tabellenkalkulation.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Die Klasse LoadFilter ermöglicht es auch, den Ladevorgang anhand der Eigenschaften des Arbeitsblatts anzupassen. Um den Ladevorgang entsprechend des Arbeitsblatts anzupassen, muss die Methode LoadFilter.StartSheet wie unten demonstriert überschrieben werden.

**C#**

{{< highlight csharp >}}

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



Der folgende Ausschnitt verwendet die oben definierte CustomFilter-Klasse.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Hinzugefügter FileFormatType.OTS-Aufzählung**
Aspose.Cells 16.12.0 hat den OTS-Eintrag zur FileFormatType-Aufzählung hinzugefügt, um das Format von OTS-Dateien zu erkennen.

Das folgende Snippet verwendet die FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Hinzugefügte Eigenschaft FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 hat die Eigenschaft PreferSystemFontSubstitutes für die Klasse FontConfigs freigelegt. Die Eigenschaft FontConfigs.PreferSystemFontSubstitutes ist vom Typ Boolean und gibt an, ob die API zunächst den Systemschriften-Ersatzmechanismus verwenden soll, falls eine benötigte Schriftart nicht vorhanden ist und keine Ersatzschriftart für die jeweilige Schriftart definiert wurde. Der Standardwert der Eigenschaft FontConfigs.PreferSystemFontSubstitutes ist false.
### **Hinzugefügtes BuiltInDocumentPropertyCollection.ScaleCrop-Eigenschaft**
Aspose.Cells 16.12.0 hat die ScaleCrop-Eigenschaft zur BuiltInDocumentPropertyCollection-Klasse hinzugefügt. ScaleCrop gibt den Anzeigemodus des Dokumentminiaturbilds an. Wenn dieses Element auf true gesetzt ist, wird das Dokumentminiaturbild entsprechend der Anzeige skaliert, während es bei false ist, das Zuschneiden des Dokumentminiaturbilds aktiviert, um den Bereich anzuzeigen, der zur Anzeige passt.
### **Hinzugefügte BuiltInDocumentPropertyCollection.LinksUpToDate-Eigenschaft**
Aspose.Cells 16.12.0 hat auch die LinksUpToDate-Eigenschaft für die BuiltInDocumentPropertyCollection-Klasse freigegeben. Die LinksUpToDate-Eigenschaft gibt an, ob die Hyperlinks in einem Dokument auf dem neuesten Stand sind.
### **Hinzugefügte Methode Workbook.ExportXml**
Aspose.Cells 16.12.0 hat die Methode Workbook.ExportXml freigelegt, die es ermöglicht, die XML-Mappendaten an einen angegebenen Dateipfad zu speichern. Die Methode Workbook.ExportXml akzeptiert 2 Parameter, wobei der erste Parameter vom Typ String der Name der XML-Map sein sollte und der zweite Parameter der Dateipfad sein sollte, an dem die XML-Daten gespeichert werden sollen.
### **Hinzugefügter WorksheetCollection.CreateRange Methode**
Aspose.Cells 16.12.0 hat die WorksheetCollection.CreateRange Methode hinzugefügt, die es ermöglicht, Bereich auf der Grundlage einer Adresse (Zellbereichsreferenz) & Arbeitsblattindex zu erstellen.

Der folgende Codeausschnitt verwendet die WorksheetCollection.CreateRange Methode, um einen Zellenbereich von A1 bis A2 im ersten (Standard-) Arbeitsblatt zu erstellen.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Veraltete APIs**
### **Veraltete LoadOptions.LoadDataOptions-Eigenschaft**
Bitte verwenden Sie stattdessen die LoadOptions.LoadFilter-Eigenschaft.
### **Veraltete LoadOptions.LoadDataFilterOptions-Eigenschaft**
Bitte verwenden Sie stattdessen die LoadOptions.LoadFilter-Eigenschaft.
### **Veraltete LoadOptions.OnlyLoadDocumentProperties-Eigenschaft**
Bitte verwenden Sie stattdessen die LoadOptions.LoadFilter-Eigenschaft.
### **Veraltete LoadOptions.LoadDataAndFormatting-Eigenschaft**
Bitte verwenden Sie stattdessen die LoadOptions.LoadFilter-Eigenschaft.

{{% alert color="primary" %}} 

Codeausschnitte für alle veralteten APIs wurden oben geteilt.

{{% /alert %}}
## **Gelöschte APIs**
### **Gelöschte DataLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die DataLabels.RotationAngle-Eigenschaft.
### **Gelöschte Title.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die Title.RotationAngle-Eigenschaft als Alternative.
### **Gelöschte DataLabels.Background-Eigenschaft**
Es wird empfohlen, stattdessen die DataLabels.BackgroundMode-Eigenschaft zu verwenden.
### **Gelöschte DisplayUnitLabel.Rotation-Eigenschaft**
Bitte ziehen Sie in Betracht, die DisplayUnitLabel.RotationAngle-Eigenschaft zu verwenden, um das gleiche Ziel zu erreichen.
{{< app/cells/assistant language="csharp" >}}
