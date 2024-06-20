---
title: ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用
type: docs
weight: 70
url: /ja/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **可能な使用シナリオ**

Aspose.Cells のAPIでは、スプレッドシートでサブトータルのカスタムラベルを使用したい場合に [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) クラスが公開されています。さらに、ワークシートまたはチャートをレンダリングする際に **Other** ラベルを変更するためにも [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) クラスを使用することができます。

## **GlobalizationSettingsクラスの紹介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスには現在以下の3つのメソッドが公開されており、カスタムクラスでこれらをオーバーライドして望ましいラベルを取得することができます。

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): 関数の合計名を取得します。
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): 関数のグランドトータル名を取得します。
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): 円グラフの "その他" ラベルの名前を取得します。

### **サブトータルのカスタムラベル**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスを使用してサブトータルのラベルをカスタマイズするには、上記で定義された**CustomSettings**クラスのインスタンスを作成し、シートにサブトータルを追加する前にこのプロパティを割り当てる必要があります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

カスタムラベルを挿入するには、新しいサブトータルを追加する必要があります。スプレッドシートにすでにサブトータルが含まれている場合は、そのラベルを変更することはできません。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスは、新しい小計を追加するためだけに動作します。スプレッドシートにすでに小計が含まれている場合、そのラベルは変更できません。

{{% /alert %}}

### **円グラフの他のラベルのカスタムテキスト**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) クラスは、"その他"の円グラフのラベルにカスタム値を与えるために便利な[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) メソッドを提供します。次のコードは、カスタムクラスを定義し、システムのカルチャ識別子に基づいてカスタムラベルを取得するために[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) メソッドをオーバーライドします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

次のコードは、円グラフを含む既存のスプレッドシートを読み込み、上記で作成した**CustomSettings** クラスを使用して画像にレンダリングします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
