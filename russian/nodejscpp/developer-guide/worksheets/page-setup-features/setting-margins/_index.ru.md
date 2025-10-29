---
title: Настройка полей с помощью Node.js через C++
linktitle: Настройка полей
type: docs
weight: 20
url: /ru/nodejs-cpp/setting-margins/
description: В этой статье вы узнаете, как задать поля листа Excel с помощью примеров кода. Также изучите, как программно установить поля по центру страницы, в заголовке и в нижнем колонтитуле, используя API Node.js через C++.
keywords: установить поля листа Excel по центру с помощью Node.js через C++, установить поля заголовка и нижнего колонтитула листа с помощью Node.js через C++
---

{{% alert color="primary" %}}

Aspose.Cells полностью поддерживает параметры настройки страниц Microsoft Excel. Разработчики могут настраивать параметры страницы для листов, чтобы контролировать процесс печати. В данном разделе рассматривается, как использовать Aspose.Cells для настройки полей страницы.

{{% /alert %}}

## **Установка полей**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), представляющий файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет свойство [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--), используемое для установки параметров настройки страницы для листа. Атрибут [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) — это объект класса [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--), который позволяет разработчикам задавать различные параметры макета страницы для распечатываемого листа. Класс [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) содержит различные свойства и методы для установки параметров настройки страницы.

### **Поля страницы**

Установка полей страницы (слева, справа, сверху, снизу) с помощью элементов класса [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--). Ниже приведены некоторые методы, используемые для указания полей страницы:

- [**PageSetup.getLeftMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getLeftMargin--)
- [**PageSetup.getRightMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getRightMargin--)
- [**PageSetup.getTopMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getTopMargin--)
- [**PageSetup.getBottomMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBottomMargin--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Set bottom, left, right and top page margins
pageSetup.setBottomMargin(2);
pageSetup.setLeftMargin(1);
pageSetup.setRightMargin(1);
pageSetup.setTopMargin(3);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetMargins_out.xls"));
```

### **Центрирование на странице**

Можно разместить что-либо по горизонтали и вертикали по центру страницы. Для этого существуют полезные элементы класса [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--), [**PageSetup.getCenterHorizontally()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterHorizontally--) и [**PageSetup.getCenterVertically()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterVertically--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Center on page Horizontally and Vertically
pageSetup.setCenterHorizontally(true);
pageSetup.setCenterVertically(true);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```

### **Поля верхнего и нижнего колонтитулов**

Установка полей заголовка и подвала с помощью элементов класса [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--), таких как [**PageSetup.getHeaderMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeaderMargin--) и [**PageSetup.getFooterMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooterMargin--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Header / Footer margins
pageSetup.setHeaderMargin(2);
pageSetup.setFooterMargin(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
