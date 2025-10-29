---
title: Вычисление массивной формулы таблицы данных с Node.js через C++
linktitle: Вычисление массивной формулы таблиц данных
description: Как использовать библиотеку Aspose.Cells для вычисления массивных формул таблицы данных в Microsoft Excel с помощью Node.js через C++. Загрузите или создайте файл Excel, вычислите массивную формулу и сохраните изменённый файл.
keywords: Aspose.Cells, Excel, таблицы данных, массивные формулы, вычисления Node.js через C++
type: docs
weight: 70
url: /ru/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Вы можете создать Таблицу данных в Microsoft Excel, используя Data > What-If Analysis > Data Table.... Сейчас Aspose.Cells позволяет вычислять массивные формулы таблицы данных. Пожалуйста, используйте [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) как обычно для вычисления любых типов формул.

{{% /alert %}}

В следующем образце кода мы использовали [исходный файл Excel](5115535.xlsx). Если вы измените значение ячейки B1 на 100, значения Таблицы данных, заполненные желтым цветом, станут равными 120, как показано на следующих изображениях. Образец кода генерирует [выходной PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Вот образец кода, используемый для генерации [выходного PDF](5115538.pdf) из [исходного файла Excel](5115535.xlsx). Пожалуйста, прочитайте комментарии для получения дополнительной информации.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
