---
title: Aggiungi controlli ActiveX usando Aspose.Cells
type: docs
weight: 260
url: /it/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Puoi aggiungere controlli ActiveX con Aspose.Cells usando il metodo [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol). Questo metodo richiede un parametro [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) che indica che tipo di controllo ActiveX deve essere aggiunto all'interno di un foglio di lavoro. Ha i seguenti valori.

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

Una volta aggiunto il controllo ActiveX all'interno della raccolta delle forme, puoi accedere all'oggetto di controllo ActiveX tramite la proprietà [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) e quindi impostarne varie proprietà.

{{% /alert %}}

Il seguente codice di esempio aggiunge il pulsante di controllo ActiveX utilizzando Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
