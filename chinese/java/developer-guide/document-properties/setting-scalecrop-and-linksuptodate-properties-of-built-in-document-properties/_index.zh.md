---
title: 设置内置文档属性的 ScaleCrop 和 LinksUpToDate 属性
type: docs
weight: 1050
url: /zh/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **可能的使用场景**
[鳞片作物](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)和[最新链接](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)是在 OpenXml 格式中定义的两个扩展的内置文档属性。这些属性的用途如下
## **1) 鳞片作物**
该元素表示文档缩略图的显示方式。将此元素设置为**真的**启用文档缩略图缩放到显示。将此元素设置为**错误的**启用文档缩略图的裁剪以仅显示适合显示的部分。

该元素的可能值由 W3C XML Schema 布尔数据类型定义。
## **2) 链接更新**
此元素指示文档中的超链接是否是最新的。将此元素设置为**真的**表示超链接已更新。将此元素设置为**错误的**表示超链接已过时。

该元素的可能值由 W3C XML Schema 布尔数据类型定义。
## **显示 app.xml 文件中这些属性的屏幕截图**
![待办事项：图片_替代_文本](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **设置内置文档属性的 ScaleCrop 和 LinksUpToDate 属性**
下面的示例代码设置[鳞片作物](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)和[最新链接](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)扩展了工作簿的内置文档属性。请检查[输出excel文件](5472494.xlsx)使用此代码生成，将其扩展名更改为 .zip 并提取其内容并查看 aap.xml，如上面的屏幕截图所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
