---
title: ピボット テーブルのグローバリゼーション設定のカスタマイズ
type: docs
weight: 50
url: /ja/net/customize-globalization-settings-for-pivot-table/
---
## **考えられる使用シナリオ**

カスタマイズしたいときもある*ピボット合計、小計、総計、すべてのアイテム、複数のアイテム、列ラベル、行ラベル、空白の値*あなたの条件に従ってテキスト。 Aspose.Cells を使用すると、ピボット テーブルのグローバリゼーション設定をカスタマイズして、このようなシナリオに対処できます。この機能を使用して、ラベルをアラビア語、ヒンディー語、ポーランド語などの他の言語に変更することもできます。

## **ピボット テーブルのグローバリゼーション設定のカスタマイズ**

次のサンプル コードは、ピボット テーブルのグローバリゼーション設定をカスタマイズする方法を説明しています。クラスを作成します*CustomPivotTableGlobalizationSettings*基本クラスから派生[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)必要なすべてのメソッドをオーバーライドします。これらのメソッドは、*ピボット合計、小計、総計、すべてのアイテム、複数のアイテム、列ラベル、行ラベル、空白の値*.次に、このクラスのオブジェクトを[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)財産。コードは[ソースエクセルファイル](40468488.xlsx)ピボット テーブルを含むデータを更新して計算し、名前を付けて保存します。[出力 PDF](40468487.pdf)ファイル。次のスクリーンショットは、出力 PDF に対するサンプル コードの効果を示しています。スクリーンショットでわかるように、ピボット テーブルのさまざまな部分に、オーバーライドされた[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラス。

![todo:画像_代替_文章](customize-globalization-settings-for-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
