---
title: Agregar controles ActiveX
type: docs
weight: 260
url: /es/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Puedes agregar controles ActiveX con Aspose.Cells para Python via .NET usando el método [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control). Este método toma un parámetro [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) que indica qué tipo de control ActiveX necesita ser agregado dentro de una hoja de cálculo. Tiene los siguientes valores.

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
- ControlType.DESCONOCIDO


Una vez que hayas agregado el control ActiveX dentro de la colección de formas, puedes acceder al objeto control ActiveX a través de la propiedad [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) y luego configurar sus diferentes propiedades.

{{% /alert %}}

El siguiente código de ejemplo agrega un control ActiveX de Botón de Alternancia usando Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
