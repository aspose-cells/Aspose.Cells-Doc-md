---
title: Exportierten Arbeitsblatt HTML Dateipfad via IFilePathProvider Schnittstelle angeben mit Node.js via C++
linktitle: Exportierten Arbeitsblatt HTML Dateipfad über das IFilePathProvider Interface bereitstellen
type: docs
weight: 70
url: /de/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Mögliche Verwendungsszenarien**
Angenommen, Sie haben eine Excel-Datei mit mehreren Blättern und möchten jedes Blatt in eine separate HTML-Datei exportieren. Wenn eines Ihrer Blätter Links zu anderen Blättern enthält, werden diese beim Export in HTML zerbrochen. Um dieses Problem zu beheben, bietet Aspose.Cells for Node.js via C++ die [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider) Schnittstelle, die Sie implementieren können, um die kaputten Links zu reparieren.

## **Exportierten Arbeitsblatt-HTML-Dateipfad über das IFilePathProvider-Interface bereitstellen**
Laden Sie die [Beispieldatei Excel](5115213.zip) herunter, die im folgenden Code verwendet wird, sowie die exportierten HTML-Dateien. Alle Dateien befinden sich im Temp-Ordner. Sie sollten ihn auf Laufwerk C: entpacken. Dadurch wird daraus das Verzeichnis C:\Temp. Öffnen Sie dann die Sheet1.html im Browser und klicken Sie auf die beiden Links darin. Diese Links verweisen auf die beiden exportierten Arbeitsblatt-HTMLs, die im Verzeichnis C:\Temp\OtherSheets liegen.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Die folgende Abbildung zeigt, wie die C:\Temp\Sheet1.html und ihre Links aussehen

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Der folgende Screenshot zeigt die HTML-Quelle. Wie zu sehen ist, beziehen sich die Links jetzt auf das Verzeichnis C:\Temp\OtherSheets. Dies wurde mit der [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider) Schnittstelle erreicht.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Beispielcode**
Bitte beachten Sie, dass das Verzeichnis C:\Temp nur zu Illustrationszwecken dient. Sie können jedes Verzeichnis Ihrer Wahl verwenden und dort die [Beispieldatei Excel](5115211.xlsx) ablegen und den bereitgestellten Beispielcode ausführen. Dieser erstellt dann ein Unterverzeichnis OtherSheets in Ihrem Verzeichnis und exportiert die zweiten und dritten Arbeitsblätter als HTML darin. Ändern Sie vor der Ausführung die Variable dirPath im bereitgestellten Code entsprechend.

{{% alert color="primary" %}} 

Der Beispielcode funktioniert nur, wenn Sie die Lizenz für Aspose.Cells setzen. Wenn Sie versuchen, den Code ohne Lizenz auszuführen, läuft er in eine Endlosschleife. Daher haben wir eine Prüfung hinzugefügt, die eine Nachricht ausgibt und die Ausführung stoppt, wenn die Lizenz nicht gesetzt ist. Sie können entweder eine Lizenz erwerben oder eine 30-tägige temporäre Lizenz beim Aspose.Purchase-Team anfordern.

{{% /alert %}} 

Bitte beachten Sie, dass das Auskommentieren dieser Zeilen im Code die Links in Sheet1.html beschädigt. Sheet2.html oder Sheet3.html werden sich dann nicht öffnen, wenn Sie in Sheet1.html auf die Links klicken.

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

Hier ist der vollständige Beispielcode, den Sie mit der bereitgestellten [Beispieldatei Excel](5115211.xlsx) ausführen können.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
