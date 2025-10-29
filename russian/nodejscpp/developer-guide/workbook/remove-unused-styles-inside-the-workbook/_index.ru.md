---  
title: Удаление неиспользованных стилей внутри рабочей книги с помощью Node.js через C++  
linktitle: Удалить неиспользуемые стили внутри книги  
type: docs  
weight: 340  
url: /ru/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Узнайте, как удалить неиспользуемые стили из рабочей книги, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Неиспользуемые стили в Excel файлах занимают не только место, но и вызывают проблемы с производительностью при преобразовании в разные форматы, такие как PDF, HTML и др. Aspose.Cells предоставляет [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) для удаления всех неиспользуемых стилей внутри рабочей книги.  
{{% /alert %}}  

Следующий код показывает использование [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--). Код загружает [шаблон Excel файла](5115520.xlsx), который можно скачать по предоставленной ссылке. Он содержит неиспользуемый стиль под названием **AsposeStyle**; этот стиль и все остальные неиспользуемые стили будут удалены после выполнения кода.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
