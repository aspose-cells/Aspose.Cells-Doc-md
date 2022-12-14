---
title: Agregue controles ActiveX usando Aspose.Cells
type: docs
weight: 260
url: /es/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 Puede agregar controles ActiveX con Aspose.Cells usando el[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) método. Este método toma un parámetro[**Tipo de control**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)que indica qué tipo de control ActiveX debe agregarse dentro de una hoja de trabajo. Tiene los siguientes valores.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Imagen
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Desconocido

 Una vez que haya agregado el control ActiveX dentro de la colección de formas, puede acceder al objeto de control ActiveX a través de[**Forma.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) propiedad y luego establecer sus diversas propiedades.

{{% /alert %}}

El siguiente código de ejemplo agrega el control ActiveX del botón de alternancia mediante Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
