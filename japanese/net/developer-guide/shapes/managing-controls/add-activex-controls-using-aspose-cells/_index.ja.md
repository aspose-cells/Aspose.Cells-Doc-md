---
title: Aspose.Cells を使用して ActiveX コントロールを追加します
type: docs
weight: 260
url: /ja/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

を使用して、Aspose.Cells で ActiveX コントロールを追加できます。[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol)方法。このメソッドはパラメータを取ります[**コントロールタイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)これは、ワークシート内に追加する必要がある ActiveX コントロールの種類を示します。次の値があります。

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

シェイプ コレクション内に ActiveX コントロールを追加すると、次の方法で ActiveX コントロール オブジェクトにアクセスできます。[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol)プロパティを開き、さまざまなプロパティを設定します。

{{% /alert %}}

次のサンプル コードは、Aspose.Cells を使用してトグル ボタン ActiveX コントロールを追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
