---
title: 将形状置于工作表的前端或后端
type: docs
weight: 3400
url: /zh/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当同一位置有多个形状时，它们的可见性由它们的z-order位置决定。 Aspose.Cells提供 [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) 方法来更改形状的z-order位置。 如果你想把形状发送到后面，你将使用一个负数，如-1、-2、-3等，如果你想把形状发送到前面，你将使用一个正数，如1、2、3等。

## **在工作表内将形状放到前面或后面**

以下示例代码说明了 [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) 方法的用法。请查看代码中使用的[示例Excel文件](sampleToFrontOrBack.xlsx)和由其生成的[输出Excel文件](50528331.xlsx)。截图显示了代码在执行后对示例Excel文件的效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
