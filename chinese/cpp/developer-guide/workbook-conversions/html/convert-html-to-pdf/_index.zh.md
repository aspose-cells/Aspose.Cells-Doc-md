---
title: 如何使用C++将HTML转换为PDF
linktitle: 转换HTML为PDF
type: docs
weight: 80
url: /zh/cpp/convert-html-to-pdf/
description: 本主题展示如何使用Aspose.Cells for C++将HTML转换为PDF以及MHTML转换为PDF。
keywords: C++将HTML转换为PDF和MHTML转换为PDF。
---

## **概述**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>将 HTML 转换为 PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML转PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++将HTML转换为PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ 如何将HTML转换为PDF</a></li>
</ul>

## **C++中的HTML转PDF转换**
 如何将HTML转换为PDF？使用[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/)库，您可以轻松通过几行代码实现HTML到PDF的程序转换。Aspose.Cells for C++具有构建跨平台应用的能力，能够生成、修改、转换、渲染和打印所有Excel文件。

## **C++将HTML转换为PDF**
以下C++代码示例演示如何使用[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/)将HTML文档转换为PDF。

1. 创建[HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/)类的实例。
1. 初始化[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象。
1. 通过调用Workbook.Save()方法保存输出PDF文档。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create HTML load options
    HtmlLoadOptions options(LoadFormat::Html);

    // Load the HTML file into a workbook
    U16String inputFilePath(u"sample.html");
    Workbook book(inputFilePath, options);

    // Save the workbook as PDF
    U16String outputFilePath(u"out.pdf");
    book.Save(outputFilePath);

    std::cout << "HTML file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **尝试在线将HTML转换为PDF**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML转PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
