---
title: PDFへ保存する際にコメントを印刷する
type: docs
weight: 10
url: /ja/net/print-comments-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Microsoft Excelでは、印刷またはPDF形式への保存時にコメントを印刷する機能が以下のオプションで提供されています

- なし
- シートの末尾
- シートに表示されている通り

Aspose.Cellsは同様の機能をサポートするために[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)列挙型を提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)列挙型には次のメンバーがあります

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **PDFへ保存する際にコメントを印刷する**

以下のサンプルコードは、[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)を使用してPDFに保存する際にコメントを印刷する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintCommentWhileSavingToPdf-PrintCommentWhileSavingToPdf.cs" >}}
