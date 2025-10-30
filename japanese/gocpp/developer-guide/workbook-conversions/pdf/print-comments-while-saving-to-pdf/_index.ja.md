---
title: C++経由のGolangでコメントをPDFに保存しながら印刷する
linktitle: PDFへ保存する際にコメントを印刷する
type: docs
weight: 10
url: /ja/go-cpp/print-comments-while-saving-to-pdf/
description: Aspose.Cells for C++を使用して、ExcelファイルをPDFに保存する際にコメントを印刷する方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、以下のオプションを使用してコメントの印刷やPDF保存時にコメントを印刷できます。

- なし
- シートの末尾
- シートに表示されている通り

Aspose.Cellsはこれと同じ機能をサポートするために、[**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/)列挙型を提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/)列挙型には以下のメンバーがあります：

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **PDFへ保存する際にコメントを印刷する**

次のサンプルコードは、コメントを印刷してPDFに保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PrintCommentsWhileSavingToPdf.go" >}}
