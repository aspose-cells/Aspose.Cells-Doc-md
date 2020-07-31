---
title : "Disable Text Wrapping for Data Labels of the Chart" 
description : "" 
weight : 16464 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngchartsandshapes/disable+text+wrapping+for+data+labels+of+the+chart/
---

# Aspose.Cells for Java : Disable Text Wrapping for Data Labels of the Chart


Microsoft Excel 2013 allows users to wrap or unwrap text inside a chart's data labels. By default, the data label text is wrapped.

Aspose.Cells provides the [DataLabels.setTextWrapped()](https://apireference.aspose.com/java/cells/com.aspose.cells/datalabels#IsTextWrapped) method. Set to **True** or **False** to enable or disable text wrapping on data labels respectively.

Similarly, use the [DataLabels.isTextWrapped()](https://apireference.aspose.com/java/cells/com.aspose.cells/datalabels#IsTextWrapped) method to find out if a data label is already wrapped.

This screenshot shows a sample Microsoft Excel file containing a chart in which the text of the data labels are wrapped. As you can see, you can check or clear the **Wrap text in shape** option in the ALIGNMENT section of the Format Datalabels panel in Microsoft Excel 2013.

**Wrapping data labels**  
![](https://docs2.aspose.com/cells/java/attachments/5276457/5472863.png)

The sample code that follows loads the sample Microsoft Excel file using Aspose.Cells and disables data label text wrapping using the [DataLabels.setTextWrapped()](https://apireference.aspose.com/java/cells/com.aspose.cells/datalabels#IsTextWrapped) method. When the code is executed, the chart looks like this. The previously wrapped text is now unwrapped.

**Showing data labels on one line only**  
![](https://docs2.aspose.com/cells/java/attachments/5276457/5472864.png)


