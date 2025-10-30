---
title: Olika sätt att öppna filer med Node.js via C++
linktitle: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/nodejs-cpp/different-ways-to-open-files/
description: Denna artikel förklarar hur man öppnar en Excel fil med Aspose.Cells for Node.js via C++ API.
keywords: Node.js öppnar en Excel fil utan Excel, hur öppnar jag en Excel fil med Node.js.
---

{{% alert color="primary" %}}

 Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data eller använda en designermall för att snabba på utvecklingsprocessen.

{{% /alert %}}

## **Så öppnar du en Excel-fil via en sökväg**

 Utvecklare kan öppna en Microsoft Excel-fil genom att specificera dess sökväg på den lokala datorn i [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassens konstruktor. Ange helt enkelt sökvägen som en *sträng* i konstruktorn. Aspose.Cells upptäcker automatiskt filformatet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Så öppnar du en Excel-fil via en ström**

Det är också enkelt att öppna en Excel-fil som en ström. Använd en överlagrad version av konstruktorn som tar emot *Stream* objektet som innehåller filen.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Så öppnar du en fil med endast data**

För att öppna en fil med endast data, använd klasserna [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) och [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) för att ställa in relaterade attribut och alternativ för klassernas mallfil.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Så lastar du bara synliga ark**

När du laddar en [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) kan du ibland bara behöva data i synliga arbetsblad i en arbetsbok. Aspose.Cells gör det möjligt att hoppa över data i osynliga arbetsblad vid inläsning av en arbetsbok. Skapa en anpassad funktion som ärvder [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) klassen och passera dess instans till [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) egenskapen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Här är implementeringen av *CustomLoad* klassen som nämns i ovanstående kod.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Ett undantag kommer att kastas om du försöker öppna icke-native Excel-filer eller andra filformat (t.ex. PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

Det finns rättvisa chanser att [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-konstruktören kan kasta *OutOfMemoryError* när stora kalkylblad laddas. Detta undantag tyder på att tillgängligt minne är otillräckligt för att helt ladda kalkylbladet i minnet; därför måste kalkylbladet laddas medan minnesinställningarna är aktiverade.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
