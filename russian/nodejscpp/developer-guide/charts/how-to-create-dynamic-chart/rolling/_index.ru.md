---
title: Как создать динамическую скользящую диаграмму с помощью Node.js через C++
linktitle: Как создать динамическую катящуюся диаграмму
description: Узнайте, как создать динамическую скользящую диаграмму с использованием Aspose.Cells for Node.js via C++. Наш гид покажет, как реализовать плавные переходы данных и скользящие средние для постоянного и актуального отображения.
keywords: Aspose.Cells для Node.js, динамическая скользящая диаграмма, переходы данных, плавные средние, непрерывное отображение, обновление визуализации.
type: docs
weight: 74
url: /ru/nodejs-cpp/create-dynamic-rolling-chart/
---

## **Возможные сценарии использования**
Динамическая катящаяся диаграмма относится к графическому представлению данных, которое постоянно смещается и обновляется с течением времени. Это тип диаграммы, который постоянно обновляется, показывая катящееся окно последних данных, отбрасывая старые данные по мере поступления новых.

Динамические катящиеся диаграммы часто используются для визуализации тенденций и закономерностей в реальном времени или потоковых данных. Они особенно полезны в сценариях, где временные аспекты и изменения со временем критичны, таких как анализ фондового рынка, мониторинг погоды или отслеживание живой производительности.

Эти диаграммы обычно используют анимацию или автоматическую прокрутку, чтобы обеспечить обновление наиболее актуальной информации. Длина катящегося окна может быть настроена для отображения определенного временного периода, такого как последний час, день или неделя.

В заключение, динамическая катящаяся диаграмма представляет собой непрерывно обновляемое графическое представление, отображающее последние данные и отбрасывающее старые, что позволяет пользователям наблюдать тенденции и закономерности в реальном времени.

## **Используйте Aspose Cells для создания динамической катящейся диаграммы**
В следующих абзацах мы покажем вам, как создать динамическую катящуюся диаграмму с использованием Aspose.Cells. Мы покажем вам код для примера, а также созданный этим кодом файл Excel.

## **Образец кода**
Приведенный ниже образец кода сгенерирует файл [Динамической Карты Прокрутки](DynamicRollingChart.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **Примечания**
В сгенерированном файле вы можете продолжать добавлять данные в столбцах A и B, в то время как диаграмма динамически подсчитывает последние 5 наборов данных. Это делается с использованием формулы "СМЕЩЕНИЕ" в образцовом коде:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Вы можете попробовать изменить число "-5" на "-10" в формуле, и динамическая диаграмма будет подсчитывать последние 10 наборов данных. Теперь мы успешно создали динамическую прокручивающуюся диаграмму с использованием Aspose.Cells.
