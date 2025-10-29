---
title: Управление разрывами страниц с помощью Node.js через C++
linktitle: Управление разрывами страниц
type: docs
weight: 30
url: /ru/nodejs-cpp/managing-page-breaks/
description: Эта статья содержит пример кода и объясняет, как добавлять, очищать или удалять конкретные разрывы страниц в листах Excel программным способом с помощью Aspose.Cells for Node.js via C++.
keywords: разрывы страниц Node.js через C++, разрывы страниц Excel в Node.js через C++, очистка разрыва страницы Node.js через C++, удаление конкретного разрыва страницы Node.js через C++
---

{{% alert color="primary" %}}

Согласно определению, перерыв страницы - это место в текучем тексте, где заканчивается одна страница, и начинается другая. Microsoft Excel позволяет пользователям добавлять перерывы страницы в любую выбранную ячейку листа.

Местоположение ячейки, в которую добавлен перерыв страницы, страница заканчивается, и оставшиеся данные после перерыва странице печатаются на следующей странице во время печати. Проще говоря, перерывы страницы делят ваш лист на несколько страниц в соответствии с вашими спецификациями. Вы также можете добавлять перерывы страниц в свои листы во время выполнения с использованием Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два вида перерывов страницы:

- Горизонтальный перерыв страницы
- Вертикальный перерыв страницы

В остальной части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные перерывы страниц в свои листы с использованием Aspose.Cells.

{{% /alert %}}

## **Разрывы страниц**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), представляющий файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий спектр свойств и методов, используемых для управления листом.

Для добавления перерывов страниц используйте свойства класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) и методы [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) и [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--).

Свойства [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) и [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) являются коллекциями, которые могут содержать несколько перерывов страницы. Каждая коллекция содержит несколько методов для управления горизонтальными и вертикальными перерывами страниц.

### **Добавление разрывов страниц**

Чтобы добавить разрыв страницы в лист, вставьте вертикальные и горизонтальные разрывы страниц в указанную ячейку, вызвав методы [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) и [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-). Каждый метод **add** принимает название ячейки, в которую необходимо вставить разрыв.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

В режиме предварительного просмотра разрывов страниц или предварительного просмотра печати можно увидеть, как работают эти разрывы страниц.

{{% /alert %}}

### **Удаление определенного разрыва страницы**

Чтобы удалить конкретный разрыв страницы, вызовите методы [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) и [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-). Каждый метод **removeAt** принимает индекс разрыва страницы, который необходимо удалить.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Важно знать**

Когда вы устанавливаете свойства **fitToPages** (то есть [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) и [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) в настройках разметки страницы, настройки разрывов страниц оказывают влияние, поэтому при печати листа настройки разрывов страниц не учитываются, хотя они все еще установлены.
{{< app/cells/assistant language="nodejs-cpp" >}}
