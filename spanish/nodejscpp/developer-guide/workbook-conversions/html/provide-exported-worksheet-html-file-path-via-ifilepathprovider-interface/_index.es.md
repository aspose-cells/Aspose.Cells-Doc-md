---
title: Proporcionar la ruta del archivo HTML exportado mediante la interfaz IFilePathProvider en Node.js mediante C++
linktitle: Proporcionar la ruta del archivo HTML de la hoja de cálculo exportada a través de la interfaz IFilePathProvider
type: docs
weight: 70
url: /es/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Escenarios de uso posibles**
Supón que tienes un archivo de Excel con varias hojas y quieres exportar cada hoja a un archivo HTML individual. Si alguna de tus hojas tiene enlaces a otras hojas, estos enlaces se romperán en el HTML exportado. Para solucionar este problema, Aspose.Cells for Node.js via C++ proporciona la interfaz [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider), que puedes implementar para arreglar los enlaces rotos.

## **Proporcione la ruta del archivo HTML de hoja de cálculo exportado a través de la interfaz IFilePathProvider**
Descarga el [archivo de Excel de ejemplo](5115213.zip) usado en el siguiente código y sus archivos HTML exportados. Todos estos archivos están en el directorio Temp. Debes extraerlo en la unidad C:. Luego, se convertirá en el directorio C:\Temp. Después, abrirás el archivo Sheet1.html en el navegador y harás clic en los dos enlaces dentro de él. Estos enlaces se refieren a estas dos hojas de Excel exportadas, que están en el directorio C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

La siguiente captura de pantalla muestra cómo se ven los enlaces en C:\Temp\Sheet1.html y sus vínculos

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La siguiente captura de pantalla muestra el código fuente HTML. Como puedes ver, los enlaces ahora refieren al directorio C:\Temp\OtherSheets. Esto se logró usando la interfaz [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Código de muestra**
Ten en cuenta que el directorio C:\Temp es solo para fines ilustrativos. Puedes usar cualquier directorio de tu elección y colocar allí el [archivo de Excel de ejemplo](5115211.xlsx) y ejecutar el código de ejemplo proporcionado. Luego creará una subcarpeta OtherSheets dentro de tu directorio y exportará como HTML las segundas y terceras hojas de cálculo en ella. Cambia la variable dirPath en el código proporcionado y refiérelo al directorio que elijas antes de ejecutarlo.

{{% alert color="primary" %}} 

El código de ejemplo solo funcionará cuando configures la licencia de Aspose.Cells. Si intentas ejecutar el código sin establecer la licencia, entrará en un ciclo infinito. Por eso, hemos añadido una comprobación para mostrar un mensaje y detener la ejecución si la licencia no está establecida. Puedes comprar una licencia o solicitar una licencia temporal de 30 días al equipo de Aspose.Purchase.

{{% /alert %}} 

Ten en cuenta que comentar estas líneas en el código romperá los enlaces en Sheet1.html, y Sheet2.html o Sheet3.html no se abrirán cuando hagas clic en sus enlaces dentro de Sheet1.html.

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

Aquí tienes el código completo de ejemplo que puedes ejecutar con el [archivo de Excel de ejemplo](5115211.xlsx) proporcionado.

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
