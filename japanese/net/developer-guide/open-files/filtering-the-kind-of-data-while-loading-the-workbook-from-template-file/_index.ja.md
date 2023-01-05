---
title: テンプレート ファイルからワークブックを読み込む際のデータの種類のフィルタリング
type: docs
weight: 400
url: /ja/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

テンプレート ファイルからワークブックを作成するときに、どの種類のデータを読み込むかを指定したい場合があります。ロードされたデータをフィルタリングすると、特別な目的のためにパフォーマンスを向上させることができます。[LightCell API](/cells/ja/net/using-lightcells-api/) .をご利用ください[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)この目的のためのプロパティ。

{{% /alert %}}

次のサンプル コードは、ワークブックを[テンプレートファイル](5115552.xlsx)指定されたリンクからダウンロードできます。次のスクリーンショットは、[テンプレートファイル](5115552.xlsx)また、赤と黄色の背景のデータはロードされないことも説明されています。[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)プロパティはに設定されています[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:画像_代替_文章](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

次のスクリーンショットは、[出力 PDF](5115555.pdf)指定されたリンクからダウンロードできます。ここでわかるように、赤色と黄色の背景のデータは存在しませんが、すべての形状が存在します。

![todo:画像_代替_文章](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
