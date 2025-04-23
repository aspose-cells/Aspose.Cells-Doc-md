---  
title: Seitenlayoutoptionen mit Node.js via C++ einstellen  
linktitle: Seite einrichten  
type: docs  
weight: 10  
url: /de/nodejs-cpp/setting-page-options/  
description: Dieser Artikel bietet Beispielcode, um die Seiteneinstellungen von Excel Arbeitsblättern programmatisch mit Node.js via C++ festzulegen. Seitenorientierung, Skalierungsfaktor, FitToPages Optionen, Papiergröße, Druckqualität, erste Seitennummer.  
keywords: Seitenorientierung in Excel mit Node.js via C++ einstellen, Skalierungsfaktor in Excel mit Node.js via C++ festlegen, Papiergröße in Excel Arbeitsblättern mit Node.js via C++ festlegen  
---  

{{% alert color="primary" %}}  
Manchmal ist es notwendig, Seiteneinrichtungseinstellungen für Arbeitsblätter zu konfigurieren, um den Druck zu steuern. Diese Seiteneinrichtungseinstellungen bieten verschiedene Optionen.  
{{% /alert %}}  

## **Seiteneinstellungen**  

Seiteneinrichtungsoptionen werden vollständig in Aspose.Cells unterstützt. Dieser Artikel erläutert, wie Seiteneinstellungen mit Aspose.Cells festgelegt werden, und zeigt Codebeispiele für die Einstellung von:  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert.  

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) stellt die Eigenschaft [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) bereit, mit der die Seitenlayoutsoptionen des Arbeitsblatts eingestellt werden. Tatsächlich ist diese Eigenschaft [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) ein Objekt der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup), das es ermöglicht, verschiedene Seitenlayout-Optionen für ein gedrucktes Arbeitsblatt festzulegen. Die Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) bietet verschiedene Eigenschaften, um die Seiteneinrichtung zu steuern. Einige dieser Eigenschaften werden unten erläutert.  

### **Seitenausrichtung**  

Die Seitenorientierung kann mit der Eigenschaft [**getOrientation()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrientation--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) auf Hochformat oder Querformat eingestellt werden. Die Eigenschaft [**getOrientation()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrientation--) akzeptiert einen der vordefinierten Werte im [**PageOrientationType**](https://reference.aspose.com/cells/nodejs-cpp/pageorientationtype) Enumeration, die unten aufgeführt sind.  

|**Seitenausrichtungstypen**|**Beschreibung**|  
| :- | :- |  
|Landscape|Hochformat-Ausrichtung|  
|Portrait|Porträtmodus|  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageOrientation_out.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Save the Workbook.
workbook.save(filePath);
```  

### **Maßstab**  

Es ist möglich, die Größe eines Arbeitsblatts zu verkleinern oder zu vergrößern, indem der Skalierungsfaktor mit der Eigenschaft [**PageSetup.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getZoom--) eingestellt wird.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the scaling factor to 100
worksheet.getPageSetup().setZoom(100);

// Save the workbook.
workbook.save(path.join(dataDir, "ScalingFactor_out.xls"));
```  

### **FitToPages-Optionen**  

Um den Inhalt des Arbeitsblatts auf eine bestimmte Anzahl von Seiten anzupassen, verwenden Sie die Eigenschaften [**getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) und [**getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Diese Eigenschaften werden auch zum Skalieren von Arbeitsblättern verwendet.  

{{% alert color="primary" %}}  
Sie können entweder die Eigenschaften [**getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--)/[**getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) oder [**getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getZoom--) auswählen, aber nicht beide gleichzeitig.  
{{% /alert %}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook.
workbook.save(path.join(dataDir, "FitToPagesOptions_out.xls"));
```  

### **Papierformat**  

Legen Sie die Papiergröße fest, auf der die Arbeitsblätter gedruckt werden sollen, mit der Eigenschaft [**getPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperSize--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Die Eigenschaft [**getPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperSize--) akzeptiert einen der vordefinierten Werte im [**PaperSizeType**](https://reference.aspose.com/cells/nodejs-cpp/papersizetype) Enumeration, unten aufgeführt.  

|**Papierformattypen**|**Beschreibung**|  
| :- | :- |  
|PaperLetter|Letter (8-1/2 in. x 11 in.)|  
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|  
|PaperTabloid|Tabloid (11 in. x 17 in.)|  
|PaperLedger|Ledger (17 in. x 11 in.)|  
|PaperLegal|Legal (8-1/2 in. x 14 in.)|  
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|  
|PaperExecutive|Executive (7-1/4 in. x 10-1/2 in.)|  
|PaperA3|A3 (297 mm x 420 mm)|  
|PaperA4|A4 (210 mm x 297 mm)|  
|PaperA4Small|A4 Small (210 mm x 297 mm)|  
|PaperA5|A5 (148 mm x 210 mm)|  
|PaperB4|JIS B4 (257 mm x 364 mm)|  
|PaperB5|JIS B5 (182 mm x 257 mm)|  
|PaperFolio|Folio (8-1/2 in. x 13 in.)|  
|PaperQuarto|Quarto (215 mm x 275 mm)|  
|Paper10x14|10 in. x 14 in.|  
|Paper11x17|11 in. x 17 in.|  
|PaperNote|Note (8-1/2 in. x 11 in.)|  
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|  
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|  
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|  
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|  
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|  
|PaperCSheet|C size sheet|  
|PaperDSheet|D size sheet|  
|PaperESheet|E size sheet|  
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|  
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|  
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|  
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|  
|PaperEnvelopeC6 |Envelope C6 (114 mm x 162 mm)|  
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|  
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|  
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|  
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|  
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|  
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|  
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|  
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|  
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|  
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|  
|PaperISOB4|B4 (ISO) 250 x 353 mm|  
|PaperJapanesePostcard|Japanese Postcard (100mm x 148mm)|  
|Paper9x11|9 in. x 11 in.|  
|Paper10x11|10 in. x 11 in.|  
|Paper15x11|15 in. x 11 in.|  
|PaperEnvelopeInvite|Envelope Invite(220mm x 220mm)|  
|PaperLetterExtra|US Letter Extra 9 \275 x 12 in|  
|PaperLegalExtra|US Legal Extra 9 \275 x 15 in|  
|PaperTabloidExtra|US Tabloid Extra 11.69 x 18 in|  
|PaperA4Extra|A4 Extra 9.27 x 12.69 in|  
|PaperLetterTransverse|Letter Transverse 8 \275 x 11 in|  
|PaperA4Transverse|A4 Transverse 210 x 297 mm|  
|PaperLetterExtraTransverse|Letter Extra Transverse 9\275 x 12 in|  
|PaperSuperA|SuperA/SuperA/A4 227 x 356 mm|  
|PaperSuperB|SuperB/SuperB/A3 305 x 487 mm|  
|PaperLetterPlus|US Letter Plus 8.5 x 12.69 in|  
|PaperA4Plus|A4 Plus 210 x 330 mm|  
|PaperA5Transverse|A5 Transverse 148 x 210 mm|  
|PaperJISB5Transverse|B5 (JIS) Transverse 182 x 257 mm|  
|PaperA3Extra|A3 Extra 322 x 445 mm|  
|PaperA5Extra|A5 Extra 174 x 235 mm|  
|PaperISOB5Extra|B5 (ISO) Extra 201 x 276 mm|  
|PaperA2|A2 420 x 594 mm|  
|PaperA3Transverse|A3 Transverse 297 x 420 mm|  
|PaperA3ExtraTransverse|A3 Extra Transverse 322 x 445 mm|  
|PaperJapaneseDoublePostcard|Japanese Double Postcard 200 x 148 mm|  
|PaperA6|A6 105 x 148 mm|  
|PaperJapaneseEnvelopeKaku2|Japanese Envelope Kaku #2|  
|PaperJapaneseEnvelopeKaku3|Japanese Envelope Kaku #3|  
|PaperJapaneseEnvelopeChou3|Japanese Envelope Chou #3|  
|PaperJapaneseEnvelopeChou4|Japanese Envelope Chou #4|  
|PaperLetterRotated|11in x 8.5in|  
|PaperA3Rotated|420mm x 297mm|  
|PaperA4Rotated|297mm x 210mm|  
|PaperA5Rotated|210mm x 148mm|  
|PaperJISB4Rotated|B4 (JIS) Rotated 364 x 257 mm|  
|PaperJISB5Rotated|B5 (JIS) Rotated 257 x 182 mm|  
|PaperJapanesePostcardRotated|Japanese Postcard Rotated 148 x 100 mm|  
|PaperJapaneseDoublePostcardRotated|Double Japanese Postcard Rotated 148 x 200 mm|  
|PaperA6Rotated|A6 Rotated 148 x 105 mm|  
|PaperJapaneseEnvelopeKaku2Rotated|Japanese Envelope Kaku #2 Rotated|  
|PaperJapaneseEnvelopeKaku3Rotated|Japanese Envelope Kaku #3 Rotated|  
|PaperJapaneseEnvelopeChou3Rotated|Japanese Envelope Chou #3 Rotated|  
|PaperJapaneseEnvelopeChou4Rotated|Japanese Envelope Chou #4 Rotated|  
|PaperJISB6|B6 (JIS) 128 x 182 mm|  
|PaperJISB6Rotated|B6 (JIS) Rotated 182 x 128 mm|  
|Paper12x11|12 x 11 in|  
|PaperJapaneseEnvelopeYou4|Japanese Envelope You #4|  
|PaperJapaneseEnvelopeYou4Rotated|Japanese Envelope You #4 Rotated|  
|PaperPRC16K|PRC 16K 146 x 215 mm|  
|PaperPRC32K|PRC 32K 97 x 151 mm|  
|PaperPRCBig32K|PRC 32K(Big) 97 x 151 mm|  
|PaperPRCEnvelope1|PRC Envelope #1 102 x 165 mm|  
|PaperPRCEnvelope2|PRC Envelope #2 102 x 176 mm|  
|PaperPRCEnvelope3|PRC Envelope #3 125 x 176 mm|  
|PaperPRCEnvelope4|PRC Envelope #4 110 x 208 mm|  
|PaperPRCEnvelope5|PRC Envelope #5 110 x 220 mm|  
|PaperPRCEnvelope6|PRC Envelope #6 120 x 230 mm|  
|PaperPRCEnvelope7|PRC Envelope #7 160 x 230 mm|  
|PaperPRCEnvelope8|PRC Envelope #8 120 x 309 mm|  
|PaperPRCEnvelope9|PRC Envelope #9 229 x 324 mm|  
|PaperPRCEnvelope10|PRC Envelope #10 324 x 458 mm|  
|PaperPRC16KRotated|PRC 16K Rotated|  
|PaperPRC32KRotated|PRC 32K Rotated|  
|PaperPRCBig32KRotated|PRC 32K(Big) Rotated|  
|PaperPRCEnvelope1Rotated|PRC Envelope #1 Rotated 165 x 102 mm|  
|PaperPRCEnvelope2Rotated|PRC Envelope #2 Rotated 176 x 102 mm|  
|PaperPRCEnvelope3Rotated|PRC Envelope #3 Rotated 176 x 125 mm|  
|PaperPRCEnvelope4Rotated|PRC Envelope #4 Rotated 208 x 110 mm|  
|PaperPRCEnvelope5Rotated|PRC Envelope #5 Rotated 220 x 110 mm|  
|PaperPRCEnvelope6Rotated|PRC Envelope #6 Rotated 230 x 120 mm|  
|PaperPRCEnvelope7Rotated|PRC Envelope #7 Rotated 230 x 160 mm|  
|PaperPRCEnvelope8Rotated|PRC Envelope #8 Rotated 309 x 120 mm|  
|PaperPRCEnvelope9Rotated|PRC Envelope #9 Rotated 324 x 229 mm|  
|PaperPRCEnvelope10Rotated|PRC Envelope #10 Rotated 458 x 324 mm|  
|PaperB3|usual B3(13.9 x 19.7 in)|  
|PaperBusinessCard|Business Card(90mm x 55 mm)|  
|PaperThermal|Thermal(3 x 11 in)|  
|Custom|Represents the custom paper size.|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Save the Workbook.
workbook.save(path.join(dataDir, "ManagePaperSize_out.xls"));
```  

### **Druckqualität**  

Stellen Sie die Druckqualität der Arbeitsblätter mit der Eigenschaft [**getPrintQuality()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintQuality--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) ein. Die Einheit für die Druckqualität ist Dots Per Inches (DPI).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the print quality of the worksheet to 180 dpi
worksheet.getPageSetup().setPrintQuality(180);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetPrintQuality_out.xls"));
```  

### **Erste Seitenzahl**  

Beginnen Sie die Nummerierung der Arbeitsblätter mit der Eigenschaft [**getFirstPageNumber()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFirstPageNumber--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Die Eigenschaft [**getFirstPageNumber()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFirstPageNumber--) legt die Seitennummer des ersten Arbeitsblattabschnitts fest, danach werden die Seiten aufsteigend nummeriert.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetFirstPageNumber_out.xls"));
```  

