---
title: 设置内置文档属性的ScaleCrop和LinksUpToDate属性
type: docs
weight: 320
url: /zh/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **可能的使用场景**
 [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) 和 [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) 是OpenXml格式中定义的两个扩展内置文档属性。这些属性的用途如下：
## **1) ScaleCrop**
此元素指示文档缩略图的显示模式。将此元素设置为**TRUE**以启用文档缩略图的缩放以进行显示。将此元素设置为**FALSE**以启用文档缩略图的裁剪，以仅显示适合显示器的部分。

此元素的可能值由W3C XML Schema布尔数据类型定义。
## **2) LinksUpToDate**
此元素指示文档中的超链接是否为最新状态。将此元素设置为**TRUE**表示超链接已更新。将此元素设置为**FALSE**表示超链接已过时。

此元素的可能值由W3C XML Schema布尔数据类型定义。
## **截图显示了app.xml文件中的这些属性**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **设置内置文档属性的ScaleCrop和LinksUpToDate属性**
 以下示例代码设置工作簿的 [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) 和 [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) 扩展内置文档属性。请检查此代码生成的 [输出Excel文件](5115500.xlsx)，将扩展名改为 .zip，解压后查看 app.xml 如上方截图所示。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
