---
title: Tillhandahåll sökväg till exporterad arbetsblads HTML fil via IFilePathProvider gränssnittet i Node.js via C++
linktitle: Tillhandahålla sökväg för exporterad kalkylblads HTML fil via IFilePathProvider gränssnitt
type: docs
weight: 70
url: /sv/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Möjliga användningsscenario**
Anta att du har en Excel-fil med flera blad och du vill exportera varje blad till en individuell HTML-fil. Om något av dina blad har länkar till andra blad, kommer dessa länkar att gå sönder i den exporterade HTML:en. För att hantera detta problem ger Aspose.Cells for Node.js via C++ gränssnittet [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider), vilket du kan implementera för att fixa de brutna länkarna.

## **Tillhandahålla sökväg för exporterad kalkylblads-HTML-fil via IFilePathProvider-gränssnitt**
Vänligen ladda ner [exempel Excel-fil](5115213.zip) som används i koden nedan och dess exporterade HTML-filer. Alla dessa filer är inne i Temp-katalogen. Extrahera den till C: -driven. Då blir den C:\Temp-mappen. Du öppnar Sheet1.html i webbläsaren och klickar på de två länkarna inuti den. Dessa länkar hänvisar till dessa två exporterade HTML-arbetsblad som finns i C:\Temp\OtherSheets-katalogen.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Den följande skärmbilden visar hur C:\Temp\Sheet1.html och dess länkar ser ut

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Följande skärmbild visar HTML-koden. Som du kan se hänvisar länkarna nu till katalogen C:\Temp\OtherSheets. Detta uppnåddes med hjälp av [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider)-gränssnittet.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Exempelkod**
Vänligen notera att katalogen C:\Temp bara är för illustration. Du kan använda vilken katalog du vill och placera [exempel Excel-filen](5115211.xlsx) där och köra den medföljande exempel koden. Den kommer att skapa en underkatalog OtherSheets i din katalog och exportera andra och tredje arbetsbladets HTML inuti den. Ändra variabeln dirPath i koden innan du kör den och hänvisa till den katalog du önskar.

{{% alert color="primary" %}} 

Exempelkoden fungerar endast när du har satt Aspose.Cells-licensen. Om du försöker köra koden utan att ange licensen, kommer den att hamna i en oändlig loop. Därför har vi lagt till en kontroll för att skriva ut ett meddelande och stoppa exekveringen när licensen inte är inställd. Du kan antingen köpa en licens eller begära ett 30-dagars tillfälligt licens från Aspose.Purchase-teamet.

{{% /alert %}} 

Vänligen notera att kommentera ut dessa rader i koden kommer att bryta länkarna i Sheet1.html, och Sheet2.html eller Sheet3.html kommer inte att öppnas när deras länkar klickas i Sheet1.html.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// If you will comment this line, then hyperlinks will be broken
const options = new AsposeCells.HtmlSaveOptions();
options.setFilePathProvider(new FilePathProvider());
```

Här är den kompletta exempel koden som du kan köra med den tillhandahållna [exempel Excel-filen](5115211.xlsx).

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// This is the directory path which contains the sample.xlsx file
const dirPath = path.join(__dirname, "data");

// because Aspose.Cells will always make the warning worksheet as active sheet in Evaluation mode.
//setLicense();

// Check if license is set, otherwise do not proceed
const wb = new AsposeCells.Workbook();
if (!wb.isLicensed()) {
console.log("You must set the license to execute this code successfully.");
} else {
// Test IFilePathProvider interface
testFilePathProvider();
}

function setLicense() {
const licPath = "Aspose.Cells.lic";

const lic = new AsposeCells.License();
lic.setLicense(licPath);

console.log(AsposeCells.CellsHelper.getVersion());
console.debug(AsposeCells.CellsHelper.getVersion());

process.chdir(dirPath);
}

function testFilePathProvider() {
// Create subdirectory for second and third worksheets
const otherSheetsDir = path.join(dirPath, "OtherSheets");
if (!fs.existsSync(otherSheetsDir)) {
fs.mkdirSync(otherSheetsDir);
}

// Load sample workbook from your directory
const wb = new AsposeCells.Workbook(path.join(dirPath, "Sample_filepath.xlsx"));

// Save worksheets to separate html files
// Because of IFilePathProvider, hyperlinks will not be broken.
for (let i = 0; i < wb.getWorksheets().getCount(); i++)
{
// Set the active worksheet to current value of variable i
wb.getWorksheets().setActiveSheetIndex(i);

// Create html save option
const options = new AsposeCells.HtmlSaveOptions();
options.setExportActiveWorksheetOnly(true);
// If you will comment this line, then hyperlinks will be broken
options.setFilePathProvider(new FilePathProvider());
// Sheet actual index which starts from 1 not from 0
const sheetIndex = i + 1;

let filePath = "";

// Save first sheet to same directory and second and third worksheets to subdirectory
if (i === 0) 
{
filePath = path.join(dirPath, "Sheet1.html");
} 
else 
{
filePath = path.join(otherSheetsDir, `Sheet${sheetIndex}_out.html`);
}

// Save the worksheet to html file
wb.save(filePath, options);
}
}
```
