---
title: Excel を Markdown に変換する
type: docs
weight: 30
url: /ja/python-java/convert-excel-to-markdown/
---
## **Excel を Markdown に変換する**
Aspose.Cells for Python via Java は、Excel ファイルの Markdown 形式への変換をサポートしています。アクティブなワークシートを Markdown にエクスポートするには、次を渡します。[SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN)の 2 番目のパラメータとして[Workbook.Save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)） 方法。また、[MarkdownSaveOptions](https://reference.aspose.com/cells/python/asposecells.api/MarkdownSaveOptions)クラスを使用して、ワークシートを Markdown にエクスポートするための追加設定を指定します。

次のコード例は、アクティブなワークシートを Markdown にエクスポートする方法を示しています。[SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN)列挙メンバー。をご覧ください[出力Markdownファイル](Book1.txt)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToMarkdownFiles.py" >}}
