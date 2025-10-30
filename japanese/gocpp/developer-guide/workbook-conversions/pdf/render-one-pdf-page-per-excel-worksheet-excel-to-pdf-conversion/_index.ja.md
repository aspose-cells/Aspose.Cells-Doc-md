---
title: Golang経由のC++でExcelの各ワークシートごとに1ページのPDFをレンダリング
type: docs
weight: 100
url: /ja/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aspose.Cellsを使用してGolang経由でC++で各ワークシートを1ページとしたPDF形式にExcelワークシートを変換します。
---

{{% alert color="primary" %}} 

多くのシートを持つ大きなMicrosoft Excelファイル（例：各シートに50列以上、300行以上のデータ）を扱う場合、サイズに関係なく各ワークシートを1ページとしてPDF出力したいことがあります。これにより、各ページは大きく異なるページサイズになる可能性があります。これはAspose.Cells for C++を使用して実現できます。

{{% /alert %}} 

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

[PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/)オプションが**true**に設定されている場合、すべてのシートの内容が1つのPDFページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、[Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)をPDFにレンダリングする直前に呼び出すのが最適です。これにより、数式に依存する値が再計算され、正しい値がPDFに描画されます。

{{% /alert %}}
