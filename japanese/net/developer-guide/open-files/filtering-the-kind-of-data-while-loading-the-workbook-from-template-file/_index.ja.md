---
title: テンプレートファイルからワークブックをロードする際にデータの種類をフィルタリングする
type: docs
weight: 400
url: /ja/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

時々、テンプレートファイルからワークブックを作成する際にロードされるデータの種類を指定したい場合があります。ロードされるデータをフィルタリングすることで、特に[LightCells API](/cells/ja/net/using-lightcells-api/)を使用する際に、特定の目的に向けてパフォーマンスを向上させることができます。この目的のために[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)プロパティを使用してください。

{{% /alert %}}

[指定されたリンク](5115552.xlsx)からダウンロードできるテンプレートファイルを使用して、ワークブックをロードする際にシェイプオブジェクトのみをロードするサンプルコードを以下に示します。以下のスクリーンショットには[テンプレートファイル](5115552.xlsx)の内容と、赤色および黄色の背景のデータがロードされないことを説明したものが表示されています。これは[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)プロパティが[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)に設定されているためです。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

[指定されたリンク](5115555.pdf)からダウンロードできる出力PDFです。ここでは、赤色および黄色の背景のデータが存在しない一方、すべての形状が存在することが分かります。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
