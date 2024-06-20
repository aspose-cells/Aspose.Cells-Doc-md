---
title: ピボットテーブルのグローバリゼーション設定のカスタマイズ
type: docs
weight: 20
url: /ja/java/customize-globalization-settings-for-pivot-table/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、*Pivot Total、Sub Total、Grand Total、All Items、Multiple Items、Column Labels、Row Labels、Blank Values*のテキストをカスタマイズして要件に合わせることができます。この機能を使用して、ピボットテーブルのグローバリゼーション設定をカスタマイズしたり、ラベルをアラビア語、ヒンディー語、ポーランド語など他言語に変更したりすることができます。

## **ピボットテーブルのグローバリゼーション設定のカスタマイズ**

次のサンプルコードは、ピボットテーブルのグローバリゼーション設定をカスタマイズする方法を説明しています。これにより、[**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)から派生した*CustomPivotTableGlobalizationSettings*クラスを作成し、必要なメソッドをオーバーライドします。これらのメソッドは、*Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*のカスタマイズされたテキストを返します。その後、このクラスのオブジェクトを[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)プロパティに割り当てます。コードは、ピボットテーブルを含む[ソースExcelファイル](40468491.xlsx)をロードし、そのデータを更新して計算し、[出力PDFファイル](40468490.pdf)として保存します。以下のスクリーンショットは、出力PDF上でサンプルコードの効果を示しています。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
