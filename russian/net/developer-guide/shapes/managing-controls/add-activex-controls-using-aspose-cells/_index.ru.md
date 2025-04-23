---
title: Добавление элементов ActiveX с помощью Aspose.Cells
type: docs
weight: 260
url: /ru/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Вы можете добавлять элементы ActiveX с помощью Aspose.Cells, используя метод [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol). Этот метод принимает параметр [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype), который указывает, какой тип элемента ActiveX должен быть добавлен внутри листа. У него следующие значения.

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

После добавления элемента ActiveX в коллекцию форм, вы можете получить доступ к объекту элемента ActiveX через свойство [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) и установить его различные свойства.

{{% /alert %}}

В следующем примере кода добавляется элемент Управления переключением с помощью элемента ActiveX Toggle Button, используя Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
