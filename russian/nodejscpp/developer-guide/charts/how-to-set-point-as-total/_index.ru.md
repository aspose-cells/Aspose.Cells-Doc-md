---  
title: Как установить точку как сумму с помощью Node.js через C++  
linktitle: Как установить точку как сумму  
description: Научитесь устанавливать точки как сумму в водопадных диаграммах с помощью Aspose.Cells for Node.js via C++.  
keywords: Водопадная диаграмма, точка, Установить как сумму, Node.js через C++  
type: docs  
weight: 72  
url: /ru/nodejs-cpp/how-to-set-point-as-total/  
---  

## Что означает "Установить точку как сумму" в диаграмме Excel

В некоторых диаграммах Excel, например, водопадных, некоторые данные точек являются суммой предыдущих точек, и может понадобиться "установить точку как сумму". Мы покажем пример кода и иллюстрацию ниже.

## Водопадная диаграмма должна иметь функцию "Установить точку как сумму" 

![todo:image_alt_text](set-as-total1.png)

На этой картинке показана водопадная диаграмма в Excel. Мы видим четыре точки данных, начинающиеся с "Total", которые используются для подсчёта всех предыдущих данных. В этой картинке настройки не совсем правильные. Когда мы выбираем точку "Total 2024", видно, что опция "Set as total" не отмечена в Excel. Ниже приложен [пример файла Excel](SampleSheet.xlsx), который необходимо исправить, и мы используем Aspose.Cells for Node.js via C++ для правильной настройки.

## Используйте Aspose.Cells for Node.js via C++ для "установки точки как суммы" 

Мы используем следующий код для правильной настройки файла:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Вы можете получить следующий исправленный [выходной файл](output.xlsx)

Как видно на рисунке ниже, четыре точки "Total" настроены правильно, и вы можете заметить различия с предыдущей диаграммой.

![todo:image_alt_text](set-as-total2.png)  
