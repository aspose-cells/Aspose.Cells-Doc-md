---
title: Aggiungi controlli ActiveX utilizzando Aspose.Cells
type: docs
weight: 260
url: /it/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 È possibile aggiungere controlli ActiveX con Aspose.Cells utilizzando il file[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) metodo. Questo metodo accetta un parametro[**Tipo di controllo**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)che indica quale tipo di controllo ActiveX deve essere aggiunto all'interno di un foglio di lavoro. Ha i seguenti valori.

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

 Dopo aver aggiunto il controllo ActiveX all'interno della raccolta delle forme, è possibile accedere all'oggetto del controllo ActiveX tramite[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) property e quindi impostarne le varie proprietà.

{{% /alert %}}

Il codice di esempio seguente aggiunge il controllo ActiveX del pulsante di attivazione/disattivazione utilizzando Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
