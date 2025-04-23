---
title: テンプレートファイルからワークブックをロードする際にデータの種類をフィルタリングする
type: docs
weight: 400
url: /ja/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

時には、テンプレートファイルからワークブックを作成するときに、どの種類のデータをロードすべきかを指定したい場合があります。ローディングされたデータのフィルタリングは、パフォーマンスの向上に役立ちます。この目的に[**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter)プロパティを使用してください。

{{% /alert %}}

[指定されたリンク](5115552.xlsx)からダウンロードできるテンプレートファイルを使用して、ワークブックをロードする際にシェイプオブジェクトのみをロードするサンプルコードを以下に示します。以下のスクリーンショットには[テンプレートファイル](5115552.xlsx)の内容と、赤色および黄色の背景のデータがロードされないことを説明したものが表示されています。これは[**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter)プロパティが[**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)に設定されているためです。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

[指定されたリンク](5115555.pdf)からダウンロードできる出力PDFです。ここでは、赤色および黄色の背景のデータが存在しない一方、すべての形状が存在することが分かります。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

