---
title: Fornire il percorso del file HTML del foglio esportato tramite l interfaccia IFilePathProvider con Node.js tramite C++
linktitle: Fornire il percorso del file HTML del foglio esportato tramite l interfaccia IFilePathProvider
type: docs
weight: 70
url: /it/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Possibili Scenari di Utilizzo**
Supponi di avere un file Excel con più fogli e desideri esportare ogni foglio in un file HTML separato. Se alcuni dei tuoi fogli contengono link ad altri fogli, tali link si romperanno nell'HTML esportato. Per risolvere questo problema, Aspose.Cells for Node.js via C++ fornisce l'interfaccia [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider), che puoi implementare per correggere i link rotti.

## **Fornire il percorso del file HTML del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider**
Scarica il [file Excel di esempio](5115213.zip) utilizzato nel seguente codice e i relativi file HTML esportati. Tutti questi file sono all’interno della directory Temp. Devi estrarlo nel drive C:. Così diventerà la directory C:\Temp. Poi apri il file Sheet1.html nel browser e clicca sui due link al suo interno. Questi collegamenti fanno riferimento ai due fogli HTML esportati che si trovano nella directory C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Lo screenshot seguente mostra come appaiono il C:\Temp\Sheet1.html e i suoi collegamenti

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La schermata seguente mostra la sorgente HTML. Come puoi vedere, i link ora fanno riferimento alla directory C:\Temp\OtherSheets. Questo è stato ottenuto utilizzando l'interfaccia [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Codice di Esempio**
Si noti che la directory C:\Temp è solo a scopo illustrativo. Puoi usare qualsiasi directory a tua scelta e posizionare il [file Excel di esempio](5115211.xlsx) all’interno e eseguire il codice di esempio fornito. Questo creerà una sottocartella OtherSheets all’interno della tua directory e l’esporterà come secondo e terzo foglio HTML. Modifica la variabile dirPath nel codice fornito e puntala alla directory di tua scelta prima di eseguire.

{{% alert color="primary" %}} 

Il codice di esempio funzionerà solo se imposti la licenza di Aspose.Cells. Se provi a eseguire il codice senza impostare la licenza, entrerà in un ciclo infinito. Per questo motivo, abbiamo aggiunto un controllo che stampa un messaggio e interrompe l’esecuzione se la licenza non è impostata. Puoi acquistare una licenza o chiedere una licenza temporanea di 30 giorni al team di Aspose.Purchase.

{{% /alert %}} 

Tieni presente che commentare queste righe nel codice interromperà i link in Sheet1.html, e Sheet2.html o Sheet3.html non si apriranno quando vengono cliccati i link all’interno di Sheet1.html.

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

Ecco il codice di esempio completo che puoi eseguire con il [file Excel di esempio](5115211.xlsx) fornito.

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
