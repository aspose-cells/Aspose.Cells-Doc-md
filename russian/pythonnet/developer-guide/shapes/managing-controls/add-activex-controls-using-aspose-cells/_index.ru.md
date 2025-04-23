---
title: Добавить элементы ActiveX
type: docs
weight: 260
url: /ru/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Вы можете добавлять элементы управления ActiveX с помощью Aspose.Cells для Python via .NET, используя метод [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control). Этот метод принимает параметр [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype), который указывает тип элемента управления ActiveX, который необходимо добавить внутри листа. Он имеет следующие значения.

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


После добавления элемента ActiveX в коллекцию форм, вы можете получить доступ к объекту элемента ActiveX через свойство [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) и установить его различные свойства.

{{% /alert %}}

Следующий пример кода добавляет переключатель ActiveX с помощью Aspose.Cells для Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
