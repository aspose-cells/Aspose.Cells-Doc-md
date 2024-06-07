---
title: 设置内置文档属性的ScaleCrop和LinksUpToDate属性
type: docs
weight: 1050
url: /zh/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **可能的使用场景**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) 和 [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) 是 OpenXml 格式内部定义的两个扩展内置文档属性。这些属性的目的是以下内容
## **1) ScaleCrop**
此元素指示文档缩略图的显示模式。将此元素设置为 **true** 以启用将文档缩略图缩放到显示。将此元素设置为 **false** 以启用将文档缩略图裁剪为仅显示适合显示的部分。

该元素的可能值由W3C XML模式布尔数据类型定义。
## **2) LinksUpToDate**
此元素指示文档中的超链接是否为最新。将此元素设置为 **true** 表示超链接已更新。将此元素设置为 **false** 表示超链接已过时。

该元素的可能值由W3C XML模式布尔数据类型定义。
## **在app.xml文件中显示这些属性的屏幕截图**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **设置内置文档属性的ScaleCrop和LinksUpToDate属性**
以下示例代码设置了工作簿的 [ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) 和 [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) 扩展内置文档属性。请查看使用此代码生成的 [输出 excel 文件](5472494.xlsx)，将其扩展名更改为 .zip 并提取其中的内容，查看如上截图中所示的 aap.xml。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
