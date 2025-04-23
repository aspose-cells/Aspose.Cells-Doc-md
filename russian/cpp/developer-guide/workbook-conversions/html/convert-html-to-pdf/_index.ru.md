---
title: Как конвертировать HTML в PDF с помощью C++
linktitle: Конвертация HTML в PDF
type: docs
weight: 80
url: /ru/cpp/convert-html-to-pdf/
description: Этот раздел показывает, как конвертировать HTML в формат PDF и MHTML в формат PDF с помощью Aspose.Cells for C++.
keywords: Конвертация HTML в PDF и MHTML в PDF с помощью C++.
---

## **Обзор**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>конвертировать HTML в PDF</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTML в PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ Конвертация HTML в PDF</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++ Как конвертировать HTML в PDF</a></li>
</ul>

## **Конвертация HTML в PDF в C++**
Как конвертировать HTML в PDF? С помощью библиотеки [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) вы легко можете автоматически преобразовать HTML в PDF с помощью нескольких строк кода. Aspose.Cells for C++ способен создавать кросс-платформенные приложения с возможностью генерации, изменения, преобразования, отображения и печати всех файлов Excel.

## **C++ Конвертация HTML в PDF**
Следующий пример кода C++ показывает, как конвертировать HTML-документ в PDF с помощью [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/).

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/).
1. Инициализируйте объект [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Сохранить выходной PDF-документ, вызвав метод Workbook.Save().

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

## **Попробуйте конвертировать HTML в PDF онлайн**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">«HTML в PDF»</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
