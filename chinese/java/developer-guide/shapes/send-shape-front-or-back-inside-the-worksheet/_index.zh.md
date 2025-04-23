---
title: 在工作表内部发送形状到前面或后面
type: docs
weight: 600
url: /zh/java/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当同一位置存在多个形状时，它们的可见性由它们的z-顺序位置决定。Aspose.Cells提供了[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-)方法，该方法可以更改形状的z-顺序位置。如果要将形状发送到后面，将使用像-1、-2、-3等的负数，如果要将形状移到前面，则使用像1、2、3等的正数。

## **在工作表内发送形状到最前或最后**

以下示例代码解释了[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-)方法的用法。请查看代码中使用的[样本Excel文件](50528362.xlsx)和由其生成的[输出Excel文件](50528361.xlsx)。屏幕截图显示了代码对样本Excel文件的影响。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
