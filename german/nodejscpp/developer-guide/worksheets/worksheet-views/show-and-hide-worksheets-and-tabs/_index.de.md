---  
title: Zeigen und Verbergen von Arbeitsblättern und Registerkarten mit Node.js über C++  
linktitle: Arbeitsblätter und Registerkarten anzeigen und ausblenden  
type: docs  
weight: 10  
url: /de/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: Dieser Artikel enthält Beispielcode für die Verwendung der Node.js API oder Node.js Bibliothek, um ein Excel Arbeitsblatt programmatisch anzuzeigen und auszublenden. Außerdem wird gezeigt, wie man Excel Arbeitsmappen Registerkarten anzeigt und ausblendet.  
---  

{{% alert color="primary" %}}  
Aspose.Cells ermöglicht es dem Benutzer, Elemente einer Arbeitsmappe einschließlich Arbeitsblätter und Registerkarten anzuzeigen und auszublenden.  
{{% /alert %}}  

## **Arbeitsblatt anzeigen und ausblenden**  

Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Immer wenn wir eine Excel-Datei erstellen, fügen wir Arbeitsblätter hinzu, in denen wir arbeiten. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von anderen Arbeitsblättern und verfügt über eigene Daten- und Formatierungseinstellungen usw. Manchmal benötigen Entwickler möglicherweise, dass einige Arbeitsblätter in der Excel-Datei ausgeblendet und andere sichtbar sind, um ihre eigenen Interessen zu wahren. **Aspose.Cells** ermöglicht Entwicklern daher, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Klasse enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.  

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Sichtbarkeit eines Arbeitsblatts zu steuern, verwenden Sie die Eigenschaft [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Klasse. [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.  

### **Ein Arbeitsblatt sichtbar machen**  

Machen Sie ein Arbeitsblatt sichtbar, indem Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) der [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) Klasse auf **true** setzen.  

### **Arbeitsblatt ausblenden**  

Verstecken Sie ein Arbeitsblatt, indem Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) der [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) Klasse auf **false** setzen.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Registerkarten anzeigen und ausblenden**  

Wenn Sie am unteren Rand einer Microsoft Excel-Datei genau hinsehen, sehen Sie eine Reihe von Steuerelementen. Dazu gehören:  

- Registerkarten.  
- Registerkarten-Scrolltasten.  

Registerkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe sind, desto mehr Registerkarten gibt es. Wenn die Excel-Datei eine gute Anzahl von Arbeitsblättern hat, benötigen Sie Tasten, um zwischen ihnen zu navigieren. Daher bietet Microsoft Excel Registerkarten-Scrolltasten zum Scrollen durch die Registerkarten an.  

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Registerkarten und Bildlaufschaltflächen für Registerkarten in Excel-Dateien steuern.  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Registerkarten in einer Excel-Datei zu steuern, können Entwickler die Eigenschaft [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) der [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) Klasse verwenden. [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.  

### **Sichtbarkeit von Registerkarten**  

Machen Sie Registerkarten sichtbar, indem Sie die Eigenschaft [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) der [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) Klasse auf **true** setzen.  

### **Registerkarten ausblenden**  

Verstecken Sie Registerkarten in einer Excel-Datei, indem Sie die Eigenschaft [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) der [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) Klasse auf **false** setzen.  

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als Output.xls speichert. Nach der Codeausführung werden Sie feststellen, dass die Registerkarten der Arbeitsmappe ausgeblendet sind.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Steuerung der Registerkartenleistenbreite**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
