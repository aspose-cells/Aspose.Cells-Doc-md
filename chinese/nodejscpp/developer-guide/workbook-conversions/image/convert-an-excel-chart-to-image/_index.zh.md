---  
title: 使用 C++ 通过 Node.js 将 Excel 图表转换为图像  
linktitle: 将Excel图表转换成图像  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/convert-an-excel-chart-to-image/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将 Excel 图表转换为图像。  
---  

{{% alert color="primary" %}}  

图表在视觉上很吸引人，可以帮助用户轻松地观察数据的比较、模式和趋势。例如，与分析工作表数字列相比，图表能够一眼看出销售额是下降还是上升，以及实际销售额与预期销售额的比较如何。人们经常需要以易于理解和维护的方式呈现统计和图形信息。图片有助于解释。  

有时，应用程序或网页中需要图表。或者可能需要在 Word 文档、PDF 文件、PowerPoint 演示文稿或其他应用程序中使用。在每种情况下，你都希望将图表呈现为图像，以便在其他地方使用。  

{{% /alert %}}  

## **将图表转换为图像**  

在此示例中，饼图和柱状图被转换为图像。  

### **将饼图转换为图像文件**  

首先，在 Microsoft Excel 中创建一个饼图，然后使用 Aspose.Cells for Node.js via C++ 将其转换为图像文件。此示例中的代码基于模板 Microsoft Excel 文件中的饼图创建了一个 EMF 图像。  

|**输出：饼图图像**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. 在Microsoft Excel中创建饼图：  
   1. 在Microsoft Excel中打开一个新的工作簿。  
   1. 在工作表输入一些数据。  
   1. 根据数据创建饼图。  
   1. 保存文件。  

|**输入文件。**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. 下载并安装 Aspose.Cells：  
   [下载Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp)。  
   1. 在您的开发计算机上安装它。  

在首次安装时，所有[Aspose](http://www.aspose.com/)组件均以评估模式运行。 评估模式没有时间限制，只会向输出文档中注入水印。  

1. 创建一个项目：  
   1. 启动你偏好的 IDE。  
   1. 创建一个新的控制台应用程序。本示例使用 Node.js 应用程序，但你也可以使用任何 JavaScript 运行环境创建它。  
   1. 添加引用。本项目使用 Aspose.Cells，因此请添加对 Aspose.Cells for Node.js via C++ 的引用。  
   1. 编写查找并转换图表的代码。 以下是组件用于完成任务的代码。 使用的代码行很少。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **将柱状图转换为图像文件**  

首先，在Microsoft Excel中创建柱状图并转换为图像文件，如上所述。执行示例代码后，将根据模板Excel文件中的柱状图生成一个JPEG文件。  

|**输出文件：柱状图图像。**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. 在Microsoft Excel中创建柱状图：  
   1. 在Microsoft Excel中打开一个新的工作簿。  
   1. 在工作表输入一些数据。  
   1. 根据数据创建柱状图。  
   1. 保存文件。  

|**输入文件。**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. 配置项目及引用，如上所述。  
1. 动态将图表转换为图像。 以下是组件用于完成任务的代码。 该代码与先前的代码类似。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
