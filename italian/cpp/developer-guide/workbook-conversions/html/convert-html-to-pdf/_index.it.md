---
title: Come Convertire HTML in PDF con C++
linktitle: Converti HTML in PDF
type: docs
weight: 80
url: /it/cpp/convert-html-to-pdf/
description: Questo argomento mostra come convertire HTML nel formato di salvataggio PDF e MHTML in formato di salvataggio PDF usando Aspose.Cells for C++.
keywords: Converti HTML in PDF e MHTML in PDF con C++.
---

## **Panoramica**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>converti HTML in PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML in PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">Converti HTML in PDF con C++</a></li>
<li><a href="#cpp-convert-html-to-pdf">Come convertire HTML in PDF con C++</a></li>
</ul>

## **Conversione di HTML in PDF in C++**
Come convertire HTML in PDF? Con la libreria [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) puoi convertire facilmente HTML in PDF programmaticamente con pochi righi di codice. Aspose.Cells for C++ è in grado di costruire applicazioni multipiattaforma con la capacità di generare, modificare, convertire, renderizzare e stampare tutti i file Excel.

## **Converti HTML in PDF con C++**
Il seguente esempio di codice C++ mostra come convertire un documento HTML in PDF usando [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. Crea un'istanza della classe [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/).
1. Inizializza l’oggetto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Salvare il documento PDF di output chiamando il metodo Workbook.Save().

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

## **Prova a convertire HTML in PDF online**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML to PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
