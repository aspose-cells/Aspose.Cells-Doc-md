---
title: Lägg till ActiveX kontroller
type: docs
weight: 260
url: /sv/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Du kan lägga till ActiveX-kontroller med Aspose.Cells för Python via .NET med hjälp av [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control)-metoden. Denna metod tar en parameter [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) som talar om vilken typ av ActiveX-kontroll som ska läggas till i ett arbetsblad. Den har följande värden.

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


När du har lagt till ActiveX-kontrollen inuti formuppsättningen kan du sedan få åtkomst till ActiveX-kontrollobjektet via [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) egenskapen och sedan ställa in dess olika egenskaper.

{{% /alert %}}

Följande kod exempel lägger till Toggle Button ActiveX-kontroll med Aspose.Cells för Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
