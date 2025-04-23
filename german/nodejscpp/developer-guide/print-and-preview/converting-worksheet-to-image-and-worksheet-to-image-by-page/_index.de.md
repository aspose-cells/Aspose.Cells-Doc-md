---  
title: Arbeitsblatt in Bild umwandeln und Arbeitsblatt nach Seite in Bild umwandeln mit Node.js über C++  
linktitle: Arbeitsblatt in Bild und Arbeitsblatt in Bild pro Seite konvertieren  
type: docs  
weight: 80  
url: /de/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Dieses Dokument soll Entwicklern ein detailliertes Verständnis darüber vermitteln, wie ein Arbeitsblatt in eine Bilddatei umgewandelt werden kann und wie man mehrere Seiten eines Arbeitsblatts in eine Bilddatei pro Seite umwandelt.  

Manchmal müssen Arbeitsblätter als Bilder präsentiert werden, zum Beispiel um sie in Anwendungen oder Webseiten zu verwenden. Sie müssen die Bilder möglicherweise in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Im Grunde genommen möchten Sie das Arbeitsblatt als Bild rendern. Aspose.Cells unterstützt die Umwandlung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Umwandlung eines Arbeitsmappen in mehrere Bilddateien, eine pro Seite.  

Möglicherweise verwenden Sie Office Automation, um dies zu erreichen, aber Office-Automation hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, beispielsweise Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von der Verwendung von Office-Automation abrät.  
{{% /alert %}}  

## **Mit Aspose.Cells for Node.js via C++ Arbeitsblatt in Bilddatei umwandeln**  

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, ein Arbeitsblatt in ein Bild umwandelt und ein Arbeitsblatt in ein Bild für jedes Arbeitsblatt mit wenigen und einfachen Zeilen Code mit der Aspose.Cells API übersetzt.  

Sie müssen mehrere wertvolle Klassen im Zusammenhang mit Render-Funktionen in Ihr Programm oder Projekt importieren, z.B. [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/) usw. Die Klasse [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) stellt ein Arbeitsblatt dar, um Bilder für das Arbeitsblatt zu rendern, und hat eine überladene Methode [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-), die ein Arbeitsblatt direkt in Bilddateien umwandeln kann, wobei alle Attribute oder Optionen eingestellt sind. Es kann ein Bildobjekt zurückgeben, und Sie können eine Bilddatei auf Festplatte/Stream speichern. Mehrere Bildformate werden unterstützt, z.B. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF und andere.  

Dieser Artikel erklärt, wie:  

- Ein Arbeitsblatt in ein Bild konvertiert wird  
- Jede Seite in einem Arbeitsblatt in ein Bild konvertiert wird  

Diese Aufgabe zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe in eine Bilddatei zu konvertieren.  

### **Setup-Projekt**  

1. Zuerst [laden Sie Aspose.Cells for Node.js via C++ herunter](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installieren Sie es auf Ihrem Entwicklungssystem. Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in die produzierten Dokumente ein. Starten Sie nun Ihre Entwicklungsumgebung und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine Node.js-Konsolenanwendung, aber Sie können jede Konfiguration verwenden, die mit Node.js integriert ist. Fügen Sie der erstellten Projektdatei einen Verweis auf Aspose.Cells hinzu.  

### **Arbeitsblatt in Bilddatei konvertieren**  

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook.xlsx** (1 Arbeitsblatt). Konvertieren Sie als Nächstes das Arbeitsblatt Sheet1 der Vorlagendatei in eine Bilddatei namens SheetImage.jpg.  

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in **Testbook.xlsx** in eine Bilddatei, um zu erklären, wie einfach diese Konvertierung ist.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Mit Aspose.Cells for Node.js via C++ Arbeitsblatt in Bilddatei nach Seite umwandeln**  

Dieses Beispiel zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe, die mehrere Seiten hat, in eine Bilddatei pro Seite zu konvertieren.  

### **Arbeitsblatt seitenweise in Bild umwandeln**  

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook2.xlsx** (1 Arbeitsblatt).  

Konvertieren Sie jetzt das Arbeitsblatt Sheet1 der Vorlagendatei in Bilddateien (eine Datei pro Seite). Da ich die Konsolenanwendung bereits erstellt habe, um die Kopieraufgabe auszuführen, werde ich diese Schritte zur Erstellung der Konsolenanwendung überspringen und direkt zu den Arbeitsblattkonvertierungsschritten übergehen.  

Der folgende Code wird vom Component zum Erreichen der Aufgabe verwendet. Er wandelt Sheet1 in Testbook2.xlsx in Bilder nach Seitenzahl um.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


