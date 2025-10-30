---
title: エクスポートされたワークシートのHTMLファイルパスをIFilePathProviderインターフェースで提供
linktitle: IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する
type: docs
weight: 70
url: /ja/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能な使用シナリオ**
複数シートのExcelファイルを各シートごとに個別のHTMLファイルとしてエクスポートしたい場合、リンクの切断を避けるために、Aspose.Cells for Node.js via C++は[ IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider)インターフェースを提供しています。

## **IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する**
次のコードで使用されるサンプルExcelファイル([sample excel file](5115213.zip))とエクスポートされたHTMLファイルをダウンロードしてください。これらのファイルはすべてTempディレクトリ内にあります。C:ドライブに解凍してください。その後、C:\Tempディレクトリになります。その後、ブラウザでSheet1.htmlファイルを開き、中のリンクを2つクリックします。これらのリンクは、C:\Temp\OtherSheetsディレクトリ内にあるこれらの2つのエクスポートされたHTMLワークシートを参照しています。

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

次のスクリーンショットは、C:\Temp\Sheet1.htmlおよびそのリンクの外観を示しています。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

次のスクリーンショットはHTMLソースを示しています。ご覧のとおり、リンクは現在C:\Temp\OtherSheetsディレクトリを参照しています。これは[IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider)インターフェースを使用して実現しました。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **サンプルコード**
C:\Tempディレクトリはあくまで例示用です。好きなディレクトリを使用し、[サンプルExcelファイル](5115211.xlsx)をそこに配置して、提供されたサンプルコードを実行できます。すると、そのディレクトリ内にOtherSheetsサブディレクトリを作成し、その中に2番目と3番目のワークシートのHTMLをエクスポートします。コード内のdirPath変数を変更し、実行前に任意のディレクトリを指定してください。

{{% alert color="primary" %}} 

サンプルコードは、ライセンスが設定されている場合のみ動作します。ライセンスを設定せずにコードを実行すると、無限ループに入ります。そのため、ライセンスが設定されていない場合はメッセージを表示し、実行を停止するチェックを追加しています。ライセンスを購入するか、Aspose.Purchaseチームから30日間の一時ライセンスをリクエストしてください。

{{% /alert %}} 

これらの行をコード内でコメントアウトすると、Sheet1.htmlのリンクが壊れ、リンクをクリックしてもSheet2.htmlやSheet3.htmlが開きません。

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

こちらは、提供された[サンプルExcelファイル](5115211.xlsx)を実行できる完全なサンプルコードです。

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
