---  
title: Преобразование диаграммы в изображение в формате SVG с помощью Node.js через C++  
linktitle: Преобразование диаграммы в изображение в формате SVG  
type: docs  
weight: 240  
url: /ru/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Узнайте, как преобразовать диаграмму в изображение в формате SVG, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Масштабируемая векторная графика (SVG) - это формат векторных изображений на основе XML для двумерной графики, который также поддерживает интерактивность и анимацию. Спецификация SVG является открытым стандартом, разработанным Консорциумом Всемирной паутины (W3C) с 1999 года.  

Изображения SVG и их поведение определены в XML-текстовых файлах. Это означает, что их можно искать, индексировать, сценаризировать и сжимать. Как XML-файлы, изображения SVG могут быть созданы и отредактированы с использованием любого текстового редактора, но их чаще создают с помощью графического программного обеспечения.  

Aspose.Cells может сохранять диаграммы в изображения в различных форматах, таких как BMP, JPEG, PNG, GIF, SVG и др. В этой статье объясняется, как сохранить диаграмму в формате SVG.  

{{% /alert %}}  

В следующем образце кода объясняется, как использовать Aspose.Cells для преобразования диаграммы в изображение в формате SVG. Код загружает исходный файл Microsoft Excel, а затем сохраняет первую найденную диаграмму на первом листе в SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
