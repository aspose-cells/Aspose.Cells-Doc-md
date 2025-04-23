---
title: 特定のスタイルのセルを見つける
type: docs
weight: 80
url: /ja/java/find-cells-with-specific-style/
description: この記事では、MS ExcelとAspose.Cells for Java APIを使用して特定のスタイルのセルを見つける方法を示しています。
keywords: 特定のスタイルのセルを見つける、特定のスタイルのセルを検索、特定のスタイルのセルを検索するExcel、特定のスタイルのセルを見つけるExcel Java、特定のスタイルのセルを検索するExcel Java、特定のスタイルのセルを検索する方法、特定のスタイルのセルを検索する方法Excel、特定のスタイルのセルを検索する方法Excel Java、特定のスタイルのセルを見つける方法、特定のスタイルのセルを見つける方法Excel、特定のスタイルのセルを見つける方法Excel Java
---

{{% alert color="primary" %}}

時々、特定のスタイルのセルを見つける必要があります。この記事では、Microsoft ExcelおよびAspose.Cells for Java APIを使用してこれを実現する方法を示します。

{{% /alert %}}

**Microsoft Excelを使用する**

MS Excelで特定のスタイルのセルを検索するために必要な手順は以下のとおりです。

1. **ホームタブ**で**検索と選択**を選択します。
1. **検索**を選択します。
1. 高度なオプションが表示されていない場合は**オプション**を選択します。
1. **書式**ドロップダウンから**セルから書式を選択**を選択します。
1. 検索したいスタイルのセルを選択します。
1. すべてを見つけるをクリックします。選択したセルと似たスタイルを持つすべてのセルを見つけます。

Aspose.Cells for Java の使用

Aspose.Cells for Java は、ワークシート内の特定のスタイルでセルを検索する機能を提供します。このため、API は [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) プロパティを提供します。

### サンプルコード

次のコードスニペットは、セル **A1** と同じスタイルのすべてのセルを見つけ、それらのセル内のテキストを変更します。出力ファイルのスクリーンショットを見て、サンプルコードの出力を分析してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

コードの実行後、セル A1 と同じスタイルを持つすべてのセルにテキスト "Found" が追加されます。

スクリーンショット

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**図:** スタイルを持つセルを含むソースファイル

以下のコードによって生成された出力ファイルです。セル **A1** と同じスタイルを持つすべてのセルにテキスト "Found" が追加されています。

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**図:** **A1** スタイルで検索後に見つかったセルを含む出力ファイル
{{< app/cells/assistant language="java" >}}
