---
title: Hur konverterar man HTML till PDF med C++
linktitle: Konvertera HTML till PDF
type: docs
weight: 80
url: /sv/cpp/convert-html-to-pdf/
description: Detta ämne visar hur du konverterar HTML till saveformat PDF och MHTML till saveformat PDF med Aspose.Cells for C++.
keywords: C++ konverterar HTML till PDF saveformat och MHTML till PDF saveformat.
---

## **Översikt**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>konvertera HTML till PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML till PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ Konvertera HTML till PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ Hur konverterar man HTML till PDF</a></li>
</ul>

## **Konvertering av HTML till PDF i C++**
Hur konverterar man HTML till PDF? Med [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) bibliotek kan du enkelt konvertera HTML till PDF programmässigt med några få kodrader. Aspose.Cells for C++ kan bygga plattformsövergripande applikationer med möjlighet att generera, modifiera, konvertera, rendera och skriva ut alla Excel-filer.

## **C++ Konvertera HTML till PDF**
Följande C++-kod visar hur man konverterar ett HTML-dokument till PDF med [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. Skapa en instans av klassen [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/).
1. Initiera [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektet.
1. Spara utdata PDF-dokument genom att anropa Workbook.Save() metoden.

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

## **Försök att konvertera HTML till PDF online**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML till PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="cpp" >}}
