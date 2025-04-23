---
title: 画像やグラフが含まれる XLS ファイルを PDF ドキュメントに変換する
type: docs
weight: 50
url: /ja/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、画像やチャートを含むXLSファイルをPDFドキュメントに変換するサポートがあります。Aspose.Cells for .NETはスプレッドシートをPDFに変換するために独立して動作できます。 Aspose.PDF for .NETは変換に必要ありません。そのため、大きなExcelファイル、例えば、画像やチャート、その他の描画オブジェクトを含むファイルも迅速かつ効率的に変換できます。

{{% /alert %}} 
## **サンプルコード**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、PDF にレンダリングする直前に [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) メソッドを呼び出すことが最適です。これにより、数式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
