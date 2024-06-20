---
title: ExcelをMarkdownに変換する
type: docs
weight: 30
url: /ja/python-java/convert-excel-to-markdown/
---

## **ExcelをMarkdownに変換**
Aspose.Cells for Python via Javaは、ExcelファイルをMarkdown形式に変換する操作をサポートしています。アクティブなワークシートをMarkdownにエクスポートするには、[Workbook.Save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\))メソッドの第2パラメータとして[SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN)を渡します。さらに、[MarkdownSaveOptions](https://reference.aspose.com/cells/python/asposecells.api/MarkdownSaveOptions)クラスを使用して、ワークシートをMarkdownにエクスポートする追加設定を指定することもできます。

次のコード例は、[SaveFormat.Markdown](https://reference.aspose.com/cells/python/asposecells.api/saveformat#MARKDOWN)列挙型メンバーを使用して、アクティブなワークシートをMarkdownにエクスポートする方法を示しています。参照のために、コードによって生成された[Markdownファイル](Book1.txt)をご覧ください。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToMarkdownFiles.py" >}}
