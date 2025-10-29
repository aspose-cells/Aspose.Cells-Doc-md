---  
title: Установка шрифта по умолчанию при отображении электронной таблицы в HTML с помощью Node.js через C++  
linktitle: Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML  
type: docs  
weight: 370  
url: /ru/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells позволяет установить шрифт по умолчанию при рендеринге электронной таблицы в HTML. Пожалуйста, используйте [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) для этой цели. Это свойство полезно, если в электронной таблице есть ячейки с недопустимыми или несуществующими шрифтами. Тогда эти ячейки будут отображаться шрифтом, указанным в свойстве [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  
{{% /alert %}}  

## Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML  

Следующий образец кода создает книгу и добавляет некоторый текст в ячейку B4 первого листа и устанавливает ее шрифт на неизвестный/не существующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman, и т. д.  

На снимке экрана показан эффект установки разных шрифтов по умолчанию через свойство [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

Код генерирует [выходной файл HTML с Courier New](5115516), [выходной HTML с Arial](5115518) и [выходной файл HTML с Times New Roman](5115517).  

## Образец кода  

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
