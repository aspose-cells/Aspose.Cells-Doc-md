---  
title: 在Node.js和C++中设置默认字体以渲染电子表格为HTML  
linktitle: 在将电子表格渲染为HTML时设置默认字体  
type: docs  
weight: 370  
url: /zh/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells允许在将电子表格渲染为HTML时设置默认字体. 请使用[**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--)来实现此目的. 当电子表格中有一些单元格具有无效或不存在的字体时, 特定于[**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--)属性指定的字体将进行渲染.  
{{% /alert %}}  

## 在将电子表格渲染为HTML时设置默认字体  

以下示例代码创建一个工作簿，并在第一个工作表的B4单元格中添加了一些文本，并将其字体设置为某个未知/不存在的字体。然后，它通过设置不同的默认字体名称，如Courier New、Arial、Times New Roman等，将工作簿保存为HTML。  

截图显示通过[**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--)属性设置不同默认字体名的效果。  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

该代码生成了使用Courier New的[output HTML文件](5115516), 使用Arial的[output HTML文件](5115518), 以及使用Times New Roman的[output HTML文件](5115517).  

## 示例代码  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
