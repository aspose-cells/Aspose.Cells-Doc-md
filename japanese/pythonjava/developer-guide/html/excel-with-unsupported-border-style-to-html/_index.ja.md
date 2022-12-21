---
title: HTML へのサポートされていない境界線スタイルを持つ Excel
type: docs
weight: 80
url: /ja/python-java/excel-with-unsupported-border-style-to/
---
## **HTML へのサポートされていない境界線スタイルを持つ Excel**
Microsoft Excel は、Web ブラウザーでサポートされていないある種の破線枠をサポートしています。このようなファイルが Aspose.Cells を使用して HTML に変換されると、それらの境界線は削除されます。ただし、 Aspose.Cells for Python via Java は、同様の境界線の表示をサポートしています[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)財産。の値を設定できます。[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)プロパティへ**真実**サポートされていない境界線をエクスポートします。

次のサンプル コードは、[サンプル Excel ファイル](sampleExportSimilarBorderStyle.xlsx)次のスクリーンショットに示すように、サポートされていない境界線が含まれています。スクリーンショットは、[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)内部のプロパティ[出力HTML](outputExportSimilarBorderStyle.zip).

![todo:画像_代替_文章](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
