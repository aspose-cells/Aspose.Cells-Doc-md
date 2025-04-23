---
title: Aggiungi controlli ActiveX
type: docs
weight: 260
url: /it/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Puoi aggiungere controlli ActiveX con Aspose.Cells per Python via .NET usando il metodo [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control). Questo metodo prende un parametro [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) che indica che tipo di controllo ActiveX deve essere aggiunto all'interno di un foglio di lavoro. Ha i seguenti valori.

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
- ControlType.SCONOSCIUTO


Una volta aggiunto il controllo ActiveX all'interno della raccolta delle forme, puoi accedere all'oggetto di controllo ActiveX tramite la proprietà [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) e quindi impostarne varie proprietà.

{{% /alert %}}

Il seguente esempio di codice aggiunge il controllo ActiveX Toggle Button usando Aspose.Cells per Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
