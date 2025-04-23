---
title: Обеспечьте путь к экспортированному HTML файлу рабочего листа с помощью интерфейса IFilePathProvider в Node.js через C++
linktitle: Предоставьте путь к экспортированному файлу HTML рабочего листа через интерфейс IFilePathProvider
type: docs
weight: 70
url: /ru/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Возможные сценарии использования**
Предположим, у вас есть файл Excel с несколькими листами, и вы хотите экспортировать каждый лист в отдельный HTML-файл. Если некоторые листы содержат ссылки на другие листы, то при экспорте эти ссылки будут сломаны. Для решения этой проблемы Aspose.Cells for Node.js via C++ предоставляет интерфейс [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider), который можно реализовать для исправления сломанных ссылок.

## **Предоставьте путь к экспортированному файлу HTML рабочего листа через интерфейс IFilePathProvider**
Пожалуйста, скачайте [образец файла Excel](5115213.zip), используемый в следующем коде, и его экспортированные HTML файлы. Все они находятся внутри директории Temp. Распакуйте ее в диск C:. Тогда получится папка C:\Temp. После этого откройте файл Sheet1.html в браузере и кликните по двум ссылкам внутри него. Эти ссылки ведут к двум экспортированным листам HTML, находящимся внутри папки C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Ниже показано, как выглядят C:\Temp\Sheet1.html и его ссылки

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Следующий скриншот показывает исходный код HTML. Как видно, ссылки теперь ведут к директории C:\Temp\OtherSheets. Это было достигнуто с помощью интерфейса [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Образец кода**
Обратите внимание, что директория C:\Temp предназначена только для иллюстрационных целей. Вы можете использовать любую выбранную вами директорию и разместить внутри неё файл [образец файла Excel](5115211.xlsx), затем выполнить предоставленный пример кода. Он создаст внутри вашей директории поддиректорию OtherSheets и экспортирует HTML для второго и третьего листов внутрь нее. Пожалуйста, измените переменную dirPath внутри кода перед выполнением, указав директорию по вашему выбору.

{{% alert color="primary" %}} 

Этот пример кода будет работать только при установке лицензии Aspose.Cells. Если попытаться запустить код без установки лицензии, он войдет в бесконечный цикл. Поэтому мы добавили проверку, которая выводит сообщение и останавливает выполнение при отсутствии лицензии. Вы можете приобрести лицензию или запросить временную лицензию на 30 дней у команды Aspose.Purchase.

{{% /alert %}} 

Обратите внимание, что закомментировав эти строки в коде, вы нарушите ссылки в файлах Sheet1.html, и файлы Sheet2.html или Sheet3.html не откроются при нажатии на соответствующие ссылки в Sheet1.html.

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

Вот полный пример кода, который можно выполнить с помощью предоставленного [образца файла Excel](5115211.xlsx).

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
