---
title: Aspose.Cellsを使用してGolangを使ったC++でActiveXコントロールを追加
linktitle: ActiveXコントロールを追加
type: docs
weight: 260
url: /ja/go-cpp/add-activex-controls-using-aspose-cells/
description: Aspose.Cells for C++を使ってExcelシートにプログラムでActiveXコントロールを追加する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsの[**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/)メソッドを使ってActiveXコントロールを追加できます。このメソッドはパラメータ[**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/)を受け取り、シート内に追加するActiveXコントロールの種類を指定します。以下の値があります：

- ControlType::CheckBox
- ControlType::ComboBox
- ControlType::CommandButton
- ControlType::Image
- ControlType::Label
- ControlType::ListBox
- ControlType::RadioButton
- ControlType::ScrollBar
- ControlType::SpinButton
- ControlType::TextBox
- ControlType::ToggleButton
- ControlType::Unknown

ActiveXコントロールをシェイプコレクションに追加したら、[**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/)メソッドを通じてActiveXコントロールオブジェクトにアクセスし、さまざまなプロパティを設定できます。

{{% /alert %}}

以下のサンプルコードはAspose.Cells for C++を使ってトグルボタンActiveXコントロールを追加します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
