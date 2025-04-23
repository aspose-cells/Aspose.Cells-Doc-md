---
title: 在形状内作为纹理平铺图片
type: docs
weight: 50
url: /zh/java/tile-picture-as-a-texture-inside-the-shape/
---

## **可能的使用场景**

当图片较小且不覆盖整个形状表面而又不失真时，可以选择将其平铺。平铺会通过重复小图像来填充形状表面，就像它们是瓷砖一样。

## **在形状内部将图片作为纹理平铺**

您可以使用 [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/java/com.aspose.cells/texturefill#IsTiling) 属性并将其设置为 **true**，将某个图像填充到形状表面并进行平铺。请参阅以下示例代码，其[示例Excel文件](46465055.xlsx)，[输出Excel文件](46465056.xlsx)以及截图作为参考。

## **屏幕截图**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-TilePictureAsTextureInsideShape.java" >}}
{{< app/cells/assistant language="java" >}}
