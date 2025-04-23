---
title: Comment convertir HTML en PDF avec C++
linktitle: Convertir HTML en PDF
type: docs
weight: 80
url: /fr/cpp/convert-html-to-pdf/
description: Ce sujet vous montre comment convertir HTML en format de sauvegarde PDF et MHTML en format de sauvegarde PDF en utilisant Aspose.Cells for C++.
keywords: Conversion C++ de HTML en PDF et MHTML en PDF.
---

## **Vue d'ensemble**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convertir du HTML en PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML vers PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">Conversion C++ de HTML en PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">Comment convertir HTML en PDF avec C++</a></li>
</ul>

## **Conversion HTML en PDF en C++**
Comment convertir HTML en PDF ? Avec la bibliothèque [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/), vous pouvez facilement convertir HTML en PDF de manière programmatique avec quelques lignes de code. Aspose.Cells for C++ est capable de créer des applications multiplateformes avec la capacité de générer, modifier, convertir, rendre et imprimer tous les fichiers Excel.

## **Conversion C++ de HTML en PDF**
L'exemple de code C++ suivant montre comment convertir un document HTML en PDF en utilisant [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/).
1. Initialisez l'objet [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Enregistrez le document PDF de sortie en appelant la méthode Workbook.Save().

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

## **Essayez de convertir du HTML en PDF en ligne**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML en PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
