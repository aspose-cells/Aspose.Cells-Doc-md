---
title: Resize Chart's Data Label Shape To Fit Text
type: docs
weight: 190
url: /java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

Excel application provides the **Resize shape to fit text** option for Chart's DataLabels in order to increase the size of the shape so that the text fits inside of it. This option can be accessed on Excel interface by selecting any of the data labels on the chart. Right click and select **Format DataLabels** menu. On **Size & Properties** tab, expand **Alignment** to reveal the related properties including the **Resize shape to fix text** option.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Resize Chart's Data Label Shape To Fit Text**

In order to mimic Excel's feature of resizing data label shapes to fit the text, the Aspose.Cells APIs have exposed the Boolean type [**DataLabels.ResizeShapeToFitText**](https://apireference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText) property. The following piece of code shows the simple usage scenario of [**DataLabels.ResizeShapeToFitText**](https://apireference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText) property.

The chart looks as follows before executing the code.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

The chart looks as follows after executing the code.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
