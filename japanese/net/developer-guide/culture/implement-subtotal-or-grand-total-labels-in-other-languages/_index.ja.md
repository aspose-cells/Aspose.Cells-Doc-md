---
title: 他の言語でサブトータルまたはグランドトータルラベルを実装する
type: docs
weight: 50
url: /ja/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **可能な使用シナリオ**

時には、中国語、日本語、アラビア語、ヒンディ語などの非英語の言語でサブトータルとグランドトータルのラベルを表示したいことがあります。Aspose.Cells を使用すると、[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスと[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)プロパティを使用してこれを行うことができます。[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスの使用方法については、この記事を参照してください。

- [ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用](/cells/ja/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **他の言語でサブトータルまたはグランドトータルラベルを実装する**

以下のサンプルコードでは、中国語でサブトータルとグランドトータル名を実装し、このコードによって生成された [出力Excelファイル](5115152.xlsx) をご参照ください。まず、[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスを作成し、その後コードで使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

上記で作成したクラスを以下のようにコードで使用します:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
