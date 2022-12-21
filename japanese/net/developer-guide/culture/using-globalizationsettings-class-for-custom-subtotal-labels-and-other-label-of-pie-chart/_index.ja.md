---
title: カスタム小計ラベルおよび円グラフのその他のラベルに GlobalizationSettings クラスを使用する
type: docs
weight: 70
url: /ja/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **考えられる使用シナリオ**

 Aspose.Cells API が[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスを使用して、ユーザーがスプレッドシートの小計にカスタム ラベルを使用したいシナリオに対処します。さらに、[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスを使用して変更することもできます**他の**ワークシートまたはグラフのレンダリング中の円グラフのラベル。

## **GlobalizationSettings クラスの紹介**

の[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスは現在、カスタム クラスでオーバーライドして、小計の目的のラベルを取得したり、**他の**円グラフのラベル。

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): 関数の完全な名前を取得します。
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): 関数の総計名を取得します。
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): 円グラフの「その他」ラベルの名前を取得します。

### **小計のカスタム ラベル**

の[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスをオーバーライドして、小計ラベルをカスタマイズするために使用できます。[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)先に示した方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

カスタム ラベルを挿入するには、[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)のインスタンスへのプロパティ**カスタム設定**小計をワークシートに追加する前に、上で定義したクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

の[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスは、新しい小計を追加する場合にのみ機能します。スプレッドシートにすでに小計が含まれている場合、そのラベルは変更できません。

{{% /alert %}}

### **円グラフの他のラベルのカスタム テキスト**

の[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスオファー[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)円グラフの「その他」ラベルにカスタム値を与えるのに役立つメソッド。次のスニペットは、カスタム クラスを定義し、[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)システムのカルチャ識別子に基づいてカスタム ラベルを取得するメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

次のスニペットは、円グラフを含む既存のスプレッドシートを読み込み、グラフを画像にレンダリングします。**カスタム設定**上記で作成したクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
