---
title: Cómo convertir HTML a PDF con C++
linktitle: Convertir HTML a PDF
type: docs
weight: 80
url: /es/cpp/convert-html-to-pdf/
description: Este tema muestra cómo convertir HTML a formato de guardado PDF y MHTML a formato de guardado PDF usando Aspose.Cells for C++.
keywords: Convertir HTML a PDF y MHTML a PDF con C++.
---

## **Visión general**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convertir HTML a PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">HTML a PDF con C++</a></li>
<li><a href="#cpp-convert-html-to-pdf">Convertir HTML a PDF en C++</a></li>
<li><a href="#cpp-convert-html-to-pdf"> Cómo convertir HTML a PDF con C++</a></li>
</ul>

## **Conversión de HTML a PDF en C++**
¿Cómo convertir HTML a PDF? Con la biblioteca [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/), puedes convertir fácilmente HTML a PDF automáticamente con unas pocas líneas de código. Aspose.Cells for C++ es capaz de crear aplicaciones multiplataforma con la capacidad de generar, modificar, convertir, renderizar e imprimir todos los archivos de Excel.

## **Convertir HTML a PDF en C++**
El siguiente ejemplo en C++ muestra cómo convertir un documento HTML a PDF usando [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. Crear una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/).
1. Inicializar el objeto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Guarda el documento PDF de salida llamando al método Workbook.Save().

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

## **Intenta convertir HTML a PDF en línea**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML a PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
