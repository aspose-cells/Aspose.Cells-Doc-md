---
title: Объединение нескольких рабочих книг в одну с помощью Node.js через C++
linktitle: Слияние книг
type: docs
weight: 66
url: /ru/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Узнайте, как объединить несколько рабочих книг в одну с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Иногда нужно объединить рабочие книги с различным содержимым, таким как изображения, графики и данные, в одну книгу. Aspose.Cells for Node.js via C++ поддерживает эту функцию. В этой статье показано, как создать консольное приложение и объединить рабочие книги с помощью всего нескольких строк кода в Aspose.Cells.

{{% /alert %}}

## **Объединение книг с изображениями и диаграммами**

Пример кода объединяет две рабочие книги в одну с помощью Aspose.Cells for Node.js via C++. Код загружает исходные рабочие книги, использует метод [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) для их объединения и сохраняет итоговую рабочую книгу.

### **Исходные книги**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Выходные книги**

- [combined.xlsx](5473095.xlsx)

### **Скриншоты**

Ниже приведены скриншоты исходной и выходной книг.

{{% alert color="primary" %}}

Вы можете использовать любые исходные книги. Эти изображения приведены только в целях иллюстрации.

{{% /alert %}}

**Первый лист книги с диаграммами - столбцы** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Второй лист книги с диаграммами - линейный** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Первый лист книги с картинками - изображение** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Все три листа в объединенной книге - столбцы, линейный, изображение** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **Продвинутые темы**
- [Объединение нескольких листов в один](/cells/ru/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Объединение файлов](/cells/ru/nodejs-cpp/merge-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
