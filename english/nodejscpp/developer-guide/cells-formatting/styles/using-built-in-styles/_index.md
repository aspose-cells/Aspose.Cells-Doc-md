---  
title: Using Built-in Styles with Node.js via C++  
linktitle: Using Built-in Styles  
type: docs  
weight: 80  
url: /nodejs-cpp/using-built-in-styles/  
description: Node.js code to use Excel built-in styles with Aspose.Cells for Node.js via C++.  
keywords: node.js use excel built in styles, node.js programmatically apply styles in workbook, programmatically apply styles in workbook, node.js apply built in styles in excel, node.js apply built in styles in workbook, node.js code apply built in styles in workbook, node.js code apply built in styles in excel workbook  
---  

{{% alert color="primary" %}}  
Aspose.Cells provides a vast collection of re-usable styles to format a cell in spreadsheet document. We can use built-in styles in our workbook and also create custom styles.  
{{% /alert %}}  

## **How to use Built-in Styles**  

The method [**Workbook.createBuiltinStyle**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createBuiltinStyle) and the enumeration [**BuiltinStyleType**](https://reference.aspose.com/cells/nodejs-cpp/builtinstyletype) make it convenient to use built-in styles. Here is a list of all possible built-in styles:  

- TWENTY_PERCENT_ACCENT_1  
- TWENTY_PERCENT_ACCENT_2  
- TWENTY_PERCENT_ACCENT_3  
- TWENTY_PERCENT_ACCENT_4  
- TWENTY_PERCENT_ACCENT_5  
- TWENTY_PERCENT_ACCENT_6  
- FORTY_PERCENT_ACCENT_1  
- FORTY_PERCENT_ACCENT_2  
- FORTY_PERCENT_ACCENT_3  
- FORTY_PERCENT_ACCENT_4  
- FORTY_PERCENT_ACCENT_5  
- FORTY_PERCENT_ACCENT_6  
- SIXTY_PERCENT_ACCENT_1  
- SIXTY_PERCENT_ACCENT_2  
- SIXTY_PERCENT_ACCENT_3  
- SIXTY_PERCENT_ACCENT_4  
- SIXTY_PERCENT_ACCENT_5  
- SIXTY_PERCENT_ACCENT_6  
- ACCENT_1  
- ACCENT_2  
- ACCENT_3  
- ACCENT_4  
- ACCENT_5  
- ACCENT_6  
- BAD  
- CALCULATION  
- CHECK_CELL  
- COMMA  
- COMMA_1  
- CURRENCY  
- CURRENCY_1  
- EXPLANATORY_TEXT  
- GOOD  
- HEADER_1  
- HEADER_2  
- HEADER_3  
- HEADER_4  
- HYPERLINK  
- FOLLOWED_HYPERLINK  
- INPUT  
- LINKED_CELL  
- NEUTRAL  
- NORMAL  
- NOTE  
- OUTPUT  
- PERCENT  
- TITLE  
- TOTAL  
- WARNING_TEXT  
- ROW_LEVEL  
- COLUMN_LEVEL  

## Node.js code to use built-in styles  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const output1Path = path.join(dataDir, "Output.xlsx");
const output2Path = path.join(dataDir, "Output.out.ods");

const workbook = new AsposeCells.Workbook();
const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

const cell = workbook.getWorksheets().get(0).getCells().get("A1");
cell.putValue("Aspose");
cell.setStyle(style);

const worksheet = workbook.getWorksheets().get(0);
worksheet.autoFitColumn(0);
worksheet.autoFitRow(0);

workbook.save(output1Path);
console.log(`File saved ${output1Path}`);
workbook.save(output2Path);
console.log(`File saved ${output2Path}`);
```  
  