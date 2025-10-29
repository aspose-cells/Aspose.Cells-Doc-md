---
title: Настройка XML ленты с помощью Node.js через C++
linktitle: Настроить меню Excel
type: docs
weight: 1500
url: /ru/nodejs-cpp/customizing-the-ribbon-xml/
description: Узнайте, как настраивать XML ленты в Excel с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office заменил меню и панели инструментов на ленту в верхней части окна приложения с момента выпуска офиса 2007 года. Лента является настраиваемой. 
Aspose.Cells for Node.js via C++ позволяет вам

- Сохранить Ribbon XML без его разбора,
- Читать и записывать Ribbon XML без его разбора,
- Получать и устанавливать данные Ribbon XML.

Если вы хотите изменить XML-ленту, вам нужно его проанализировать с помощью парсера XML или другого инструмента для работы с XML-лентой.

{{% /alert %}} 

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
workbook.setRibbonXml(ribbonXml);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
