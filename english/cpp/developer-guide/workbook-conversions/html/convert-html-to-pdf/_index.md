---
title: How to Convert HTML to PDF with C++
linktitle: Convert HTML to PDF
type: docs
weight: 80
url: /cpp/convert-html-to-pdf/
description: This topic shows you how to convert HTML to PDF saveformat and MHTML to PDF saveformat using Aspose.Cells for C++.
keywords: C++ convert HTML to PDF saveformat and MHTML to PDF saveformat.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Overview**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convert HTML to PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML to PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ Convert HTML to PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ How to convert HTML to PDF</a></li>
</ul>

## **HTML to PDF Conversion in C++**
How to convert HTML to PDF? With [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) library, you can easily convert HTML to PDF programmatically with a few lines of code. Aspose.Cells for C++ is capable of building cross‑platform applications with the ability to generate, modify, convert, render, and print all Excel files.

## **C++ Convert HTML to PDF**
The following C++ code sample shows how to convert an HTML document to a PDF using [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/) class.  
2. Initialize a Workbook object.  
3. Save the output PDF document by calling the `Workbook.Save()` method.

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

## **Try to convert HTML to PDF online**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) provides a free online application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML to PDF”</a>, where you can try the functionality and see how well it works.  
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="cpp" >}}
