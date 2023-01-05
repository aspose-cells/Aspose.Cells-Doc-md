---
title: Lägg till ActiveX-kontroller med Aspose.Cells
type: docs
weight: 260
url: /sv/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 Du kan lägga till ActiveX-kontroller med Aspose.Cells med hjälp av[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) metod. Denna metod tar en parameter[**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)som talar om vilken typ av ActiveX-kontroll som måste läggas till i ett kalkylblad. Den har följande värden.

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
- ControlType.Okänd

 När du väl har lagt till ActiveX-kontrollen i formsamlingen kan du komma åt ActiveX-kontrollobjektet via[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) egenskap och ställ sedan in dess olika egenskaper.

{{% /alert %}}

Följande exempelkod lägger till Toggle Button ActiveX Control med Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
