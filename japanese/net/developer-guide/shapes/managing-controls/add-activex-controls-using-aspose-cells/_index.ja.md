---
title: Aspose.Cells を使用して ActiveX コントロールを追加する
type: docs
weight: 260
url: /ja/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) メソッドを使用して Aspose.Cells で ActiveX コントロールを追加することができます。 このメソッドは、ワークシート内に追加する ActiveX コントロールの種類を伝えるパラメータ [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) を取ります。 次の値があります。

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

シェイプコレクション内に ActiveX コントロールを追加したら、それから [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) プロパティを介して ActiveX コントロール オブジェクトにアクセスし、そのさまざまなプロパティを設定できます。

{{% /alert %}}

Aspose.Cellsを使用してToggle Button ActiveXコントロールを追加するサンプルコードは、次のとおりです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
