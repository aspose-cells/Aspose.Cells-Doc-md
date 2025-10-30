---
title: ActiveXコントロールを追加
type: docs
weight: 260
url: /ja/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETを使ってActiveXコントロールを追加するには、[**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control)メソッドを使用します。このメソッドはパラメータ[**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype)を受け取り、ワークシート内にどのタイプのActiveXコントロールを追加するかを指示します。この値は以下の通りです。

- ControlType.COMMAND_BUTTON
- ControlType.COMBO_BOX
- ControlType.CHECK_BOX
- ControlType.LIST_BOX
- ControlType.TEXT_BOX
- ControlType.SPIN_BUTTON
- ControlType.RADIO_BUTTON
- ControlType.LABEL
- ControlType.IMAGE
- ControlType.TOGGLE_BUTTON
- ControlType.SCROLL_BAR
- ControlType.BAR_CODE
- ControlType.UNKNOWN


シェイプコレクション内に ActiveX コントロールを追加したら、それから [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) プロパティを介して ActiveX コントロール オブジェクトにアクセスし、そのさまざまなプロパティを設定できます。

{{% /alert %}}

次のサンプルコードは、Aspose.Cells for Python via .NETを使用してActiveXコントロールのトグルボタンを追加します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
