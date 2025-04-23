---
title: Lägg till ActiveX kontroller med hjälp av Aspose.Cells
type: docs
weight: 260
url: /sv/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Du kan lägga till ActiveX-kontroller med Aspose.Cells med hjälp av [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) metoden. Denna metod tar en parameter [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) som anger vilken typ av ActiveX-kontroll som behöver läggas till i ett kalkylblad. Den har följande värden.

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

När du har lagt till ActiveX-kontrollen inuti formuppsättningen kan du sedan få åtkomst till ActiveX-kontrollobjektet via [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) egenskapen och sedan ställa in dess olika egenskaper.

{{% /alert %}}

Följande exempelkod lägger till Toggle-knappen ActiveX-kontroll med hjälp av Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
