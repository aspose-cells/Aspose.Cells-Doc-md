---
title: Agregar controles ActiveX usando Aspose.Cells
type: docs
weight: 260
url: /es/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Puedes agregar controles ActiveX con Aspose.Cells usando el método [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol). Este método toma un parámetro [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) que indica qué tipo de control ActiveX se debe agregar dentro de una hoja de cálculo. Tiene los siguientes valores.

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

Una vez que hayas agregado el control ActiveX dentro de la colección de formas, puedes acceder al objeto control ActiveX a través de la propiedad [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) y luego configurar sus diferentes propiedades.

{{% /alert %}}

El siguiente código de ejemplo agrega el control de botón de alternancia ActiveX utilizando Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
