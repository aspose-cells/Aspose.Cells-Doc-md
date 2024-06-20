---
title: HTMLへのサポートされていないボーダースタイルを持つExcel
type: docs
weight: 80
url: /ja/python-java/excel-with-unsupported-border-style-to/
---

## **HTMLへのサポートされていないボーダースタイルを持つExcel**
Microsoft ExcelはWebブラウザーでサポートされていない一部の点線ボーダーをサポートしています。そのようなファイルをAspose.Cellsを使用してHTMLに変換すると、それらのボーダーが削除されます。ただし、Aspose.Cells for Python via Javaは[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)プロパティで同様のボーダーを表示するサポートを提供しています。[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)プロパティの値を**True**に設定すると、サポートされていないボーダーがエクスポートされます。

以下のサンプルコードは、次のスクリーンショットに示すように、いくつかのサポートされていないボーダーを含む[sample Excel file](sampleExportSimilarBorderStyle.xlsx)をロードします。スクリーンショットはまた、[output HTML](outputExportSimilarBorderStyle.zip)内の[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)プロパティの効果を説明しています。

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
