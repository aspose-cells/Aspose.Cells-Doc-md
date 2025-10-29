---
title: 使用 Golang 通过 C++ 对字体应用上标和下标效果
linktitle: 在字体上应用上标和下标效果
type: docs
weight: 80
url: /zh/go-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: 使用 Aspose.Cells for C++ API，在 C++ 中对 Excel 中文本应用上标和下标效果的代码示例。
keywords: excel 上标 c++，excel 下标 c++，excel 上标和下标 c++，在 excel 中插入上标和下标 c++，向 excel 添加上标和下标，向 excel 添加上标和下标 c++，在 excel 中添加上标和下标，添加上标 c++，添加下标 c++
---

{{% alert color="primary" %}}

Aspose.Cells提供将文本应用上标（文本位于基线上方）和下标（文本位于基线下方）效果的功能。

{{% /alert %}}

## **处理上标和下标**

通过将[**Style.Font**](https://reference.aspose.com/cells/go-cpp/font/)对象的[**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/)属性设置为**true**来应用上标效果。要应用下标效果，将[**Style.Font**](https://reference.aspose.com/cells/go-cpp/font/)对象的[**IsSubscript**](https://reference.aspose.com/cells/go-cpp/font/issubscript/)属性设置为**true**。

以下代码示例展示了如何将上标和下标应用于文本。

### 用 C++ 应用上标效果的代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplySuperscriptAndSubscriptEffectsOnFonts.go" >}}
### 用 C++ 应用下标效果的代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplySuperscriptAndSubscriptEffectsOnFonts-1.go" >}}
