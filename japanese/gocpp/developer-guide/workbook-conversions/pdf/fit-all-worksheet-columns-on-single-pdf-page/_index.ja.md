---
title: Golang経由のC++で単一のPDFページに全てのワークシート列をフィットさせる
linktitle: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 160
url: /ja/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.CellsとC++を使用して、すべてのワークシート列を単一ページに収めたPDFを生成します。
---

{{% alert color="primary" %}}

時には、すべてのワークシートの列を1ページに収めるPDFファイルを生成したい場合があります。[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) プロパティはこの機能を非常に簡単に提供します。出力されるPDFの高さと幅などの複雑な計算は内部で処理され、ワークシートのデータに基づいています。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) は、ワークシートのすべての列を1つのPDFページにレンダリングし、データに応じて行が複数ページにまたがる場合もあります。

以下のサンプルコードは、[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/)プロパティを使用して、大きな100列のワークシートをレンダリングする方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされたPDFファイルでは内容が非常に小さくなる場合があります。Acrobat Readerなどの閲覧アプリケーションで拡大するとまだ読める場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
