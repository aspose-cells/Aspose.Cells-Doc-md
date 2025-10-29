---
title: كيفية تحويل HTML إلى PDF باستخدام C++
linktitle: تحويل HTML إلى PDF
type: docs
weight: 80
url: /ar/cpp/convert-html-to-pdf/
description: يظهر لك هذا الموضوع كيفية تحويل HTML إلى تنسيق حفظ PDF و MHTML إلى تنسيق حفظ PDF باستخدام Aspose.Cells for C++.
keywords: تحويل C++ من HTML إلى PDF و MHTML إلى PDF.
---

## **نظرة عامة**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>تحويل HTML إلى PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">HTML إلى PDF باستخدام C++</a></li>
<li><a href="#cpp-convert-html-to-pdf">تحويل C++ من HTML إلى PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">كيف يتم تحويل HTML إلى PDF باستخدام C++</a></li>
</ul>

## **تحويل HTML إلى PDF في C++**
كيف تحول HTML إلى PDF؟ مع مكتبة [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) ، يمكنك بسهولة تحويل HTML إلى PDF برمجياً ببضع خطوط من الكود. Aspose.Cells for C++ قادر على بناء تطبيقات متعددة المنصات مع القدرة على إنشاء، تعديل، تحويل، عرض وطباعة جميع ملفات Excel.

## **تحويل C++ من HTML إلى PDF**
يوضح المثال التالي بكود C++ كيفية تحويل مستند HTML إلى PDF باستخدام [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. إنشاء نسخة من فئة [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/).
1. تهيئة كائن [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. حفظ مستند PDF الناتج عن طريق استدعاء طريقة Workbook.Save().

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

## **محاولة تحويل HTML إلى PDF عبر الإنترنت**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML إلى PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="cpp" >}}
