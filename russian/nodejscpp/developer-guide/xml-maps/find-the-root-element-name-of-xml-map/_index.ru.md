---
title: Найдите имя корневого элемента XML карты с помощью Node.js через C++
linktitle: Поиск имени корневого элемента XML схемы
type: docs
weight: 30
url: /ru/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Узнайте, как найти имя корневого элемента XML карты в Excel, используя Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Вы можете найти *Имя корневого элемента XML-карты* с помощью Aspose.Cells for Node.js via C++ и свойства [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Следующий скриншот показывает имя корневого элемента XML-карты в Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Образец кода**

Следующий пример кода загружает [пробный Excel-файл](55541789.xlsx) и получает доступ к первой XML-карте, выводя его свойство [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Ниже приведен вывод в консоль примера кода.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **Вывод в консоль**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
