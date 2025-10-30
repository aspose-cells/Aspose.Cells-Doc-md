---
title: GO言語とC++経由でテンプレートファイルからワークブックを読み込む際に特定のデータタイプをフィルタリングします
linktitle: ワークブック読み込み時のデータフィルタリング
type: docs
weight: 400
url: /ja/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Aspose.Cellsを使用してGO言語とC++経由でテンプレートファイルからワークブックを読み込む際に特定のデータタイプをフィルタリングする方法を学びます。
---

{{% alert color="primary" %}}

Excelファイル結合の効率的な方法

{{% /alert %}}

[指定されたリンク](5115552.xlsx)からダウンロードできるテンプレートファイルを使用して、ワークブックをロードする際にシェイプオブジェクトのみをロードするサンプルコードを以下に示します。以下のスクリーンショットには[テンプレートファイル](5115552.xlsx)の内容と、赤色および黄色の背景のデータがロードされないことを説明したものが表示されています。これは[**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/)プロパティが[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)に設定されているためです。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

[指定されたリンク](5115555.pdf)からダウンロードできる出力PDFです。ここでは、赤色および黄色の背景のデータが存在しない一方、すべての形状が存在することが分かります。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
