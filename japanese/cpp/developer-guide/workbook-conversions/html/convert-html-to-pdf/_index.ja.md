---
title: C++を用いたHTMLからPDFへの変換方法
linktitle: HTMLをPDFに変換する
type: docs
weight: 80
url: /ja/cpp/convert-html-to-pdf/
description: このトピックは、Aspose.Cells for C++を使用してHTMLをPDF保存形式およびMHTMLをPDF保存形式に変換する方法を示します。
keywords: C++でHTMLをPDF保存形式およびMHTMLをPDF保存形式に変換する
---

## **概要**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>HTMLをPDFに変換する</b>. It covers the following topics.

<ul>
<li><a href="#cpp-convert-html-to-pdf">C++ HTMLからPDFへ</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++でHTMLをPDFに変換</a></li>
<li><a href="#cpp-convert-html-to-pdf">C++でHTMLをPDFに変換する方法</a></li>
</ul>

## **C++におけるHTMLからPDFへの変換**
HTMLをPDFに変換する方法： [Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/)ライブラリを使えば、数行のコードでHTMLをPDFに簡単に変換できます。Aspose.Cells for C++は、クロスプラットフォームアプリケーションの構築や、すべてのExcelファイルの生成・修正・変換・レンダリング・印刷を可能にします。

## **C++でHTMLをPDFに変換**
以下のC++コード例は、[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/)を使用してHTMLドキュメントをPDFに変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/)クラスのインスタンスを作成します。
1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトを初期化します。
1. Workbook.Save() メソッドを呼び出して出力PDFドキュメントを保存します。

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

## **オンラインでHTMLをPDFに変換してみてください**

[Aspose.Cells for C++](https://releases.aspose.com/cells/cpp/) presents you with an online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">「HTMLをPDFに」</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="cpp" >}}
