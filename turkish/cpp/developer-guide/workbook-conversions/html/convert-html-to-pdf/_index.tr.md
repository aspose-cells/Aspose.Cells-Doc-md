---
title: HTML den PDF ye C++ ile nasıl dönüştürülür
linktitle: HTML yi PDF ye dönüştür
type: docs
weight: 80
url: /tr/cpp/convert-html-to-pdf/
description: Bu konu, Aspose.Cells for C++ kullanarak HTML den PDF ve MHTML den PDF ye dönüştürmeyi gösterir.
keywords: C++ kullanarak HTML yi PDF ye ve MHTML yi PDF ye dönüştürme.
---

## **Genel Bakış**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>HTML'i PDF'e dönüştür</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML'den PDF'ye dönüştürme</a></li>
<li><a href="#cpp-convert-html-to-pdf"> C++ HTML'yi PDF'ye dönüştürme</a></li>
<li><a href="#cpp-convert-html-to-pdf"> C++ ile HTML'den PDF'ye dönüştürme nasıl yapılır</a></li>
</ul>

## **HTML'yi PDF'ye dönüştürme C++ ile**
HTML'yi PDF'ye nasıl dönüştürürüm? [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) kütüphanesi ile, HTML'yi birkaç satır kodla programlı olarak PDF'ye kolayca dönüştürebilirsiniz. Aspose.Cells for C++, tüm Excel dosyalarını oluşturma, değiştirme, dönüştürme, görüntüleme ve yazdırma yeteneği ile çapraz platform uygulamaları geliştirme kapasitesine sahiptir.

## ** C++ HTML'yi PDF'ye dönüştürme**
 Aşağıdaki C++ kod örneği, [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) kullanarak bir HTML belgesini PDF'ye nasıl dönüştüreceğinizi gösterir.

1. [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/) sınıfının bir örneğini oluşturun.
1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesini başlatın.
1. Workbook.Save() yöntemini çağırarak çıktı PDF belgesini kaydedin.

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

## **HTML'i PDF'e çevirmeyi deneyin**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML'den PDF'e”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
