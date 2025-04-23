---
title: Wie konvertiert man HTML mit C++ in PDF
linktitle: HTML in PDF konvertieren
type: docs
weight: 80
url: /de/cpp/convert-html-to-pdf/
description: Dieses Thema zeigt, wie Sie HTML in das saveformat PDF und MHTML in das saveformat PDF mithilfe von Aspose.Cells for C++ konvertieren.
keywords: C++ Konvertierung von HTML in PDF Format und MHTML in PDF Format.
---

## **Übersicht**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>konvertieren Sie HTML in das PDF-Saveformat</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML zu PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML in PDF konvertieren</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ Wie man HTML in PDF umwandelt</a></li>
</ul>

## **HTML in PDF-Konvertierung in C++**
Wie konvertiere ich HTML in PDF? Mit der [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) Bibliothek können Sie HTML einfach programmatisch in PDF konvertieren, mit nur wenigen Codezeilen. Aspose.Cells for C++ ist in der Lage, plattformübergreifende Anwendungen zu erstellen, die in der Lage sind, alle Excel-Dateien zu generieren, zu modifizieren, zu konvertieren, anzuzeigen und zu drucken.

## **C++ HTML in PDF konvertieren**
Das folgende C++-Codebeispiel zeigt, wie man ein HTML-Dokument mit [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) in ein PDF umwandelt.

1. Erstellen Sie eine Instanz der [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/) Klasse.
1. Initialisieren Sie das [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekt.
1. Speichern Sie das Ausgabe-PDF-Dokument, indem Sie die Methode Workbook.Save() aufrufen.

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

## **Versuchen Sie, HTML online in PDF zu konvertieren**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">„HTML in PDF“</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
