---
title: ピボット テーブルのグローバリゼーション設定のカスタマイズ
type: docs
weight: 20
url: /ja/java/customize-globalization-settings-for-pivot-table/
---
## **考えられる使用シナリオ**

カスタマイズしたいときもある*ピボット合計、小計、総計、すべてのアイテム、複数のアイテム、列ラベル、行ラベル、空白の値*あなたの条件に従ってテキスト。 Aspose.Cells を使用すると、ピボット テーブルのグローバリゼーション設定をカスタマイズして、このようなシナリオに対処できます。この機能を使用して、ラベルをアラビア語、ヒンディー語、ポーランド語などの他の言語に変更することもできます。

## **ピボット テーブルのグローバリゼーション設定のカスタマイズ**

次のサンプル コードは、ピボット テーブルのグローバリゼーション設定をカスタマイズする方法を説明しています。クラスを作成します*CustomPivotTableGlobalizationSettings*基本クラスから派生[**グローバリゼーション設定**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)必要なすべてのメソッドをオーバーライドします。これらのメソッドは、*ピボット合計、小計、総計、すべてのアイテム、複数のアイテム、列ラベル、行ラベル、空白の値* .次に、このクラスのオブジェクトを[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)財産。コードは[ソースエクセルファイル](40468491.xlsx)ピボット テーブルを含むデータを更新して計算し、名前を付けて保存します。[出力PDFファイル](40468490.pdf).次のスクリーンショットは、出力 PDF に対するサンプル コードの効果を示しています。スクリーンショットでわかるように、ピボット テーブルのさまざまな部分に、オーバーライドされたメソッドによって返されるカスタマイズされたテキストがあります。[**グローバリゼーション設定**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)クラス。

![todo:画像_代替_文章](customize-globalization-settings-for-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
