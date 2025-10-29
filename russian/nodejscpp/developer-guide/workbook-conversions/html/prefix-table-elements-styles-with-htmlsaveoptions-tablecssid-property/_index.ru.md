---
title: Добавление префикса для стилей элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId в Node.js через C++
linktitle: Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /ru/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Узнайте, как добавлять префикс к стилям элементов таблицы в HTML с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

Aspose.Cells позволяет добавлять префикс к стилям элементов таблицы с помощью свойства [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Например, если вы установите это свойство в значение **MyTest_TableCssId**, то стили таблицы будут выглядеть следующим образом:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

На следующем скриншоте показано влияние использования свойства [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) на выходной HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId**

Следующий образец кода демонстрирует, как использовать свойство [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Пожалуйста, проверьте [выходной HTML](60489790.zip), сгенерированный кодом, для справки.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
