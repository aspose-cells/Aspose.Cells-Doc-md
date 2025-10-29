---  
title: Изменение размера формы метки данных диаграммы, чтобы она поместилась в текст с помощью Node.js через C++  
linktitle: Изменение формы метки данных диаграммы для подгонки текста  
description: Научитесь изменять размер формы метки данных на диаграмме, чтобы она соответствовала тексту, в Aspose.Cells for Node.js via C++. Наш гид покажет, как настроить размер и форму контейнера метки для правильного отображения текста без усечения или перекрытия.  
keywords: Aspose.Cells for Node.js via C++, создание диаграмм, метки данных, изменение формы, фиксация текста, усечение, перекрытие.  
type: docs  
weight: 220  
url: /ru/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
Приложение Excel предлагает опцию **Изменить форму для подгонки текста** для подписей данных диаграммы, чтобы увеличить размер формы так, чтобы текст помещался внутри нее  
{{% /alert %}}  

## **Как изменить форму подписей данных в диаграмме, чтобы они соответствовали тексту в Microsoft Excel**  

Этот параметр можно получить в интерфейсе Excel, выбрав любую метку данных на диаграмме. Щелкните правой кнопкой мыши и выберите меню **Формат меток данных**. На вкладке **Размер и свойства** разверните раздел **Выравнивание**, чтобы открыть связанные свойства, включая опцию **Изменить форму для фиксации текста**.  

## **Как изменить размер формы метки данных диаграммы, чтобы она соответствовала тексту, с помощью Aspose.Cells for Node.js via C++**  

Чтобы имитировать функцию Excel по изменению размера форм меток данных для соответствия текста, API Aspose.Cells предоставил булевое свойство [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--). В следующем примере показано простое использование сценария свойства [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
