---
title: Добавьте элементы управления ActiveX, используя Aspose.Cells.
type: docs
weight: 260
url: /ru/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 Вы можете добавить элементы управления ActiveX с номером Aspose.Cells, используя команду[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) метод. Этот метод принимает параметр[**тип управления**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)который сообщает, какой тип элемента управления ActiveX необходимо добавить на рабочий лист. Он имеет следующие значения.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ТипКонтроля.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

 После того, как вы добавили элемент управления ActiveX в коллекцию фигур, вы можете получить доступ к объекту элемента управления ActiveX через[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) свойство, а затем установить его различные свойства.

{{% /alert %}}

В следующем примере кода добавляется элемент управления ActiveX Toggle Button с использованием Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
