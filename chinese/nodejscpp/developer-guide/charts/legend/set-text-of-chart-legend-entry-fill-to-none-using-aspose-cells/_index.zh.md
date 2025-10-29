---
title: 使用Aspose.Cells for Node.js via C++设置图表图例条目的填充为无
linktitle: 使用Aspose.Cells将图例条目填充的文本设置为无
description: 学习如何使用Aspose.Cells for Node.js via C++将图表图例条目的填充设置为无。本指南将演示如何修改Microsoft Excel图表中图例条目的填充颜色，以实现更好的可视化和自定义。
keywords: Aspose.Cells for Node.js via C++，图表图例条目填充，微软Excel，可视化，自定义。
type: docs
weight: 320
url: /zh/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

如果你想将图表图例条目的填充文本设置为无，以便它不在图例内显示，请将[**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--)设置为**true**。

{{% /alert %}}

以下示例代码将图表的第二个图例条目填充的文本设置为无色。请下载这段代码中使用的[sample excel file](5115219.xlsx)和由此生成的[output excel file](5115217.xlsx)进行参考。

以下截图突出显示了此代码对[示例Excel文件](5115219.xlsx)的效果。

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
