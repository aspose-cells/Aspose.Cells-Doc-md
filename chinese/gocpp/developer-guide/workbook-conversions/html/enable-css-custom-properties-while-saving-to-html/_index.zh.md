---
title: 用 Golang 通过 C++ 在保存为 HTML 时启用 CSS 自定义属性
linktitle: 在保存为HTML时启用CSS自定义属性
type: docs
weight: 320
url: /zh/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: 学习如何在使用Aspose.Cells for C++保存Excel文件为HTML时启用CSS自定义属性。通过减少冗余的图片数据提高性能。
---

## **可能的使用场景**

当你将Excel文件保存为HTML时，对于同一基础64图片出现多次的场景，使用自定义属性后只需保存一次图片数据，从而提升生成HTML的性能。请在保存为HTML时使用[**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/)属性并将其设置为**true**。

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **在保存为HTML时启用CSS自定义属性**

以下示例代码展示了[**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/)属性的用法。截图显示了当未将此属性设置为**true**时的效果。请下载此代码中使用的[样本Excel文件](50528260.xlsx)以及它生成的[输出HTML](50528261.zip)作为参考。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}
