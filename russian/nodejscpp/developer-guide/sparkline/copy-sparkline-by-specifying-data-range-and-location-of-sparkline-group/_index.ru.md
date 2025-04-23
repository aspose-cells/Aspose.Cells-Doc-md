---  
title: Копирование Sparklines с указанием диапазона данных и положения группы Sparkline с помощью Node.js через C++  
linktitle: Копирование мини графиков, указав диапазон данных и расположение группы мини графиков  
type: docs  
weight: 300  
url: /ru/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Узнайте, как копировать диаграмму Sparkline в Excel, указав диапазон данных и расположение группы с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Microsoft Excel позволяет копировать минидиаграмму, указывая диапазон данных и местоположение группы минидиаграмм. Aspose.Cells поддерживает эту функцию.  
{{% /alert %}}  

Для копирования минидиаграммы в другие ячейки в Microsoft Excel:  

1. Выберите ячейку, содержащую минидиаграмму.  
1. Выберите **Edit Data** в разделе **Sparkline** вкладки **Design**.  
1. Выберите **Edit Group Location & Data**.  
1. Укажите диапазон данных и местоположение.  
1. Нажмите **ОК**.  

Aspose.Cells предоставляет метод `SparklineCollection.add(dataRange, row, column)` для указания диапазона данных и положения группы Sparkline. Следующий пример кода загружает исходный файл Excel, как показано на снимке выше, затем обращается к первой группе Sparkline и добавляет диапазоны данных и позиции в группу. В конце он сохраняет итоговый файл Excel на диск, как показано на снимке выше.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

