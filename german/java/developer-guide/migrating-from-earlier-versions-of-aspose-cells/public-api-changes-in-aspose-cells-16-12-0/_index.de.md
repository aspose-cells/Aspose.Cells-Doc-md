---
title: Öffentliche API Änderungen in Aspose.Cells 16.12.0
type: docs
weight: 370
url: /de/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 16.11.0 auf 16.12.0, die für Modul-/Anwendungsentwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Filterobjekte beim Laden**
Aspose.Cells 16.12.0 hat die LoadFilter-Klasse zusammen mit der LoadOptions.LoadFilter-Eigenschaft freigegeben, die gemeinsam steuern können, welche Art von Daten beim Initialisieren einer Instanz von Workbook aus einer Vorlagendatei geladen werden sollen.

Hier ist ein einfaches Anwendungsszenario, um nur die Dokumenteigenschaften aus einer Vorlagendatei zu laden.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Das folgende Snippet lädt alles aus einer vorhandenen Tabellenkalkulation, außer den Diagrammen.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Der folgende Code lädt nur die Zelldaten (zusammen mit Formeln) und das Formatieren aus einer vorhandenen Tabellenkalkulation.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Hinzugefügter FileFormatType.OTS-Aufzählung**
Aspose.Cells 16.12.0 hat den OTS-Eintrag zur FileFormatType-Aufzählung hinzugefügt, um das Format von OTS-Dateien zu erkennen.

Das folgende Snippet verwendet die FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Hinzugefügtes BuiltInDocumentPropertyCollection.ScaleCrop-Eigenschaft**
Aspose.Cells 16.12.0 hat die ScaleCrop-Eigenschaft zur BuiltInDocumentPropertyCollection-Klasse hinzugefügt. ScaleCrop gibt den Anzeigemodus des Dokumentminiaturbilds an. Wenn dieses Element auf true gesetzt ist, wird das Dokumentminiaturbild entsprechend der Anzeige skaliert, während es bei false ist, das Zuschneiden des Dokumentminiaturbilds aktiviert, um den Bereich anzuzeigen, der zur Anzeige passt.
### **Hinzugefügte BuiltInDocumentPropertyCollection.LinksUpToDate-Eigenschaft**
Aspose.Cells 16.12.0 hat auch die LinksUpToDate-Eigenschaft für die BuiltInDocumentPropertyCollection-Klasse freigegeben. Die LinksUpToDate-Eigenschaft gibt an, ob die Hyperlinks in einem Dokument auf dem neuesten Stand sind. 
### **Hinzugefügte Workbook.exportXml-Methode**
Aspose.Cells 16.12.0 hat die Workbook.exportXml-Methode freigegeben, die es ermöglicht, die XML-Zuordnungsdaten an einem angegebenen Dateipfad zu speichern. Die Workbook.exportXml-Methode akzeptiert 2 Parameter, wobei der erste Parameter vom Typ String der XML-Zuordnungsname sein sollte und der zweite Parameter der Dateipfad zur Speicherung der XML-Daten sein sollte.
### **Hinzugefügte WorksheetCollection.createRange-Methode**
Aspose.Cells 16.12.0 hat die WorksheetCollection.createRange-Methode hinzugefügt, die es ermöglicht, einen Bereich anhand einer Adresse (Zellbereichsreferenz) & des Arbeitsblatt-Index zu erstellen.

Der folgende Codeausschnitt verwendet die WorksheetCollection.createRange-Methode, um einen Zellenbereich von A1 bis A2 im ersten (Standard-) Arbeitsblatt zu erstellen.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Gelöschte Title.getCharacters Methode**
Bitte verwenden Sie die Methode Title.characters stattdessen.
{{< app/cells/assistant language="java" >}}
