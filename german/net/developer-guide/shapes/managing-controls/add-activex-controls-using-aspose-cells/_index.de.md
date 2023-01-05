---
title: Fügen Sie ActiveX-Steuerelemente mit Aspose.Cells hinzu
type: docs
weight: 260
url: /de/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 Sie können ActiveX-Steuerelemente mit Aspose.Cells hinzufügen, indem Sie die verwenden[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) Methode. Diese Methode akzeptiert einen Parameter[**Steuerungstyp**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)die angibt, welche Art von ActiveX-Steuerelement in einem Arbeitsblatt hinzugefügt werden muss. Es hat die folgenden Werte.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.Befehlsschaltfläche
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unbekannt

 Sobald Sie das ActiveX-Steuerelement in der Formensammlung hinzugefügt haben, können Sie über auf das ActiveX-Steuerelementobjekt zugreifen[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) -Eigenschaft und legen Sie dann ihre verschiedenen Eigenschaften fest.

{{% /alert %}}

Der folgende Beispielcode fügt das Toggle Button ActiveX-Steuerelement mit Aspose.Cells hinzu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
