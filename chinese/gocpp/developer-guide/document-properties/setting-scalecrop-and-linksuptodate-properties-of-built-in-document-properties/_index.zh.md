---
title: 使用C++中的Golang设置内置文档属性的ScaleCrop和LinksUpToDate属性
linktitle: 设置 ScaleCrop 和 LinksUpToDate 属性
type: docs
weight: 320
url: /zh/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: 学习如何使用 Aspose.Cells for C++ 设置内置文档属性的 ScaleCrop 和 LinksUpToDate 属性。
---

## **可能的使用场景**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) 和 [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/)是OpenXml格式中定义的两个扩展内置文档属性。这些属性的用途如下：

## **1) ScaleCrop**
此元素指示文档缩略图的显示模式。将此元素设置为**TRUE**以启用文档缩略图的缩放以进行显示。将此元素设置为**FALSE**以启用文档缩略图的裁剪，以仅显示适合显示器的部分。

此元素的可能值由W3C XML Schema布尔数据类型定义。

## **2) LinksUpToDate**
此元素指示文档中的超链接是否为最新状态。将此元素设置为**TRUE**表示超链接已更新。将此元素设置为**FALSE**表示超链接已过时。

此元素的可能值由W3C XML Schema布尔数据类型定义。

## **截图显示了app.xml文件中的这些属性**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **设置内置文档属性的 ScaleCrop 和 LinksUpToDate 属性**
 以下示例代码设置了工作簿的[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/)和[GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/)扩展内置文档属性。请检查用此代码生成的[输出Excel文件](5115500.xlsx)，将其扩展名改为.zip并解压内容，查看app.xml，如上方截图所示。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
