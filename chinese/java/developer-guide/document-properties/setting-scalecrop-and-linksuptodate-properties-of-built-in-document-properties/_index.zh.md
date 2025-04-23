---
title: 设置内置文档属性的ScaleCrop和LinksUpToDate属性
type: docs
weight: 1050
url: /zh/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **可能的使用场景**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)和[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)是OpenXml格式内定义的两个扩展内置文档属性。这些属性的目的如下：
## **1) ScaleCrop**
此元素指示文档缩略图的显示模式。将此元素设置为**true**以启用对文档缩略图进行缩放以进行显示。将此元素设置为**false**以启用对文档缩略图进行裁剪，以显示仅适合显示的部分。

此元素的可能值由W3C XML Schema布尔数据类型定义。
## **2) LinksUpToDate**
此元素指示文档中的超链接是否是最新的。将此元素设置为**true**表示超链接已更新。将此元素设置为**false**表示超链接已过时。

此元素的可能值由W3C XML Schema布尔数据类型定义。
## **截图显示了app.xml文件中的这些属性**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **设置内置文档属性的ScaleCrop和LinksUpToDate属性**
以下示例代码设置Workbook的[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)和[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)扩展内置文档属性。请查看使用此代码生成的[输出Excel文件](5472494.xlsx)，将其扩展名更改为.zip并提取其内容，并查看上述屏幕截图中的app.xml。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
{{< app/cells/assistant language="java" >}}
