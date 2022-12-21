---
title: 小計または総計のラベルを他の言語で実装する
type: docs
weight: 50
url: /ja/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **考えられる使用シナリオ**

中国語、日本語、アラビア語、ヒンディー語など、英語以外の言語で小計と総計のラベルを表示したい場合があります。Aspose.Cells を使用すると、[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスと[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)財産。利用方法はこちらの記事をご覧ください[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラス

- [カスタム小計ラベルおよび円グラフのその他のラベルに GlobalizationSettings クラスを使用する](/cells/ja/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **小計または総計のラベルを他の言語で実装する**

次のサンプル コードは、[サンプルエクセルファイル](5115151.xlsx)小計と総計の名前を中国語で実装します。を確認してください[出力エクセルファイル](5115152.xlsx)参照用にこのコードによって生成されます。最初にクラスを作成します[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)コードで使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

上記で作成したクラスを以下のコードで使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
