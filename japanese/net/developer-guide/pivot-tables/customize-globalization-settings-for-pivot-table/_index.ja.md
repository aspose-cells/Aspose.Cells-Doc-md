---
title: ピボットテーブルのグローバリゼーション設定をカスタマイズする
type: docs
weight: 50
url: /ja/net/customize-globalization-settings-for-pivot-table/
---
##  **考えられる使用シナリオ**

カスタマイズしたい場合があります。*ピボット合計、小計、総計、すべてのアイテム、複数のアイテム、列ラベル、行ラベル、空白値*要件に応じてテキストを入力します。 Aspose.Cells を使用すると、このようなシナリオに対処するためにピボット テーブルのグローバリゼーション設定をカスタマイズできます。この機能を使用して、ラベルをアラビア語、ヒンディー語、ポーランド語などの他の言語に変更することもできます。

##  **ピボットテーブルのグローバリゼーション設定をカスタマイズする**

次のサンプル コードでは、ピボット テーブルのグローバリゼーション設定をカスタマイズする方法を説明します。クラスを作成します*カスタムピボットテーブルグローバリゼーション設定*基本クラスから派生した[**ピボットグローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)そして必要なメソッドをすべてオーバーライドします。これらのメソッドは、*ピボット合計、小計、総計、すべてのアイテム、複数のアイテム、列ラベル、行ラベル、空白値*のカスタマイズされたテキストを返します。次に、このクラスのオブジェクトを次のように割り当てます。[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/)財産。コードは、[ソースエクセルファイル](40468488.xlsx)ピボット テーブルが含まれており、そのデータを更新して計算し、次のように保存します。[出力PDF](40468487.pdf)ファイル。次のスクリーンショットは、出力 PDF に対するサンプル コードの効果を示しています。スクリーンショットでわかるように、ピボット テーブルのさまざまな部分には、オーバーライドされたメソッドによって返されるカスタマイズされたテキストが含まれています。[**ピボットグローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)クラス。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
