---
title: 通过Node.js和C++提供导出工作表HTML文件路径的IFilePathProvider接口
linktitle: 通过IFilePathProvider接口提供导出的工作表HTML文件路径
type: docs
weight: 70
url: /zh/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能的使用场景**
假设你有一个包含多个工作表的Excel文件，想将每个工作表导出为单独的HTML文件。如果你的任何工作表中有指向其他工作表的链接，那么在导出的HTML中这些链接将会失效。为解决此问题，Aspose.Cells for Node.js via C++提供了[IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider)接口，你可以实现它来修复断裂的链接。

## **通过IFilePathProvider接口提供导出的工作表HTML文件路径**
请下载在以下代码中使用的[示例Excel文件](5115213.zip)及其导出的HTML文件。所有文件都在Temp目录中。你应将其解压到C盘，然后变成C:\Temp目录。然后在浏览器中打开Sheet1.html文件，点击其中的两个链接。这些链接指向C:\Temp\OtherSheets目录中的两个已导出HTML工作表。

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

以下截图显示了C:\Temp\Sheet1.html及其链接的外观

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下截图显示了HTML源代码。可以看到，链接现在指向C:\Temp\OtherSheets目录。这是通过使用[IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider)接口实现的。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **示例代码**
请注意，C:\Temp目录仅为说明用途。你可以使用任何自定义目录，把[示例Excel文件](5115211.xlsx)放在里面，然后执行提供的示例代码。它将在你的目录中创建一个OtherSheets子目录，并在里面导出第二和第三个工作表的HTML。请在执行前修改代码中的dirPath变量，指向你选择的目录。

{{% alert color="primary" %}} 

示例代码只有在设置了Aspose.Cells许可证后才有效。如果你在未设置许可证的情况下运行代码，会进入无限循环。因此，我们添加了一个检查，以在未设置许可证时打印消息并停止执行。你可以购买许可证或向Aspose.Purchase团队请求30天临时许可证。

{{% /alert %}} 

请注意，注释掉代码中的这些行将会破坏Sheet1.html中的链接，导致点击后无法打开Sheet2.html或Sheet3.html。

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

这里提供完整的示例代码，你可以结合提供的[示例Excel文件](5115211.xlsx)运行。

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
