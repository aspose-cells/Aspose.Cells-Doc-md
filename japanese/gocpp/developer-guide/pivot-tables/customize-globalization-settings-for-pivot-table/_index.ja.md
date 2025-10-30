---
title: Golang経由でC++を使ったピボットテーブルのグローバリゼーション設定のカスタマイズ
linktitle: ピボットテーブルのグローバリゼーション設定のカスタマイズ
type: docs
weight: 50
url: /ja/go-cpp/customize-globalization-settings-for-pivot-table/
description: Aspose.Cells for C++ を使ったピボットテーブルのグローバリゼーション設定のカスタマイズ方法を学びます。
---

## **可能な使用シナリオ**

時には、「合計、サブ合計、総合計、すべてのアイテム、複数アイテム、列ラベル、行ラベル、空の値」等のテキストを要件に応じてカスタマイズしたいことがあります。Aspose.Cells for C++ はこれらのシナリオに対処するためにピボットテーブルのグローバリゼーション設定をカスタマイズできるようにします。また、この機能を使ってラベルをアラビア語、ヒンディー語、ポーランド語など他の言語に変更することも可能です。

## **ピボットテーブルのグローバリゼーション設定のカスタマイズ**

以下のサンプルコードはC++でピボットテーブルのグローバリゼーション設定をカスタマイズする方法を示しています。ベースクラス [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) から派生した `CustomPivotTableGlobalizationSettings` クラスを作成し、すべての必要なメソッドをオーバーライドします。これらのメソッドはさまざまなピボットテーブルの要素に対してカスタマイズされたテキストを返します。次に、この実装を [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) プロパティに割り当てます。例として [ソースExcelファイル](40468488.xlsx) を読み込み、ピボットデータを更新し、[出力PDF](40468487.pdf)として保存します。以下のスクリーンショットにはカスタマイズされたラベルが表示されています。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
