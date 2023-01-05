---
title: Ajouter des contrôles ActiveX à l'aide de Aspose.Cells
type: docs
weight: 260
url: /fr/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant le[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) méthode. Cette méthode prend un paramètre[**Type de contrôle**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)qui indique quel type de contrôle ActiveX doit être ajouté dans une feuille de calcul. Il a les valeurs suivantes.

- ControlType.CheckBoxControlType.CheckBox
- ControlType.ComboBoxControlType.ComboBox
- ControlType.CommandButtonControlType.CommandButtonControlType.CommandButtonControlType.CommandButton
- ControlType.Image
- ControlType.LabelControlType.Label
- ControlType.ListBoxControlType.ListBox
- ControlType.RadioButtonControlType.RadioButtonControlType.RadioButtonControlType.RadioButton
- ControlType.ScrollBarControlType.ScrollBar
- ControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButtonControlType.ToggleButtonControlType.ToggleButton
- ControlType.UnknownControlType.Unknown

 Une fois que vous avez ajouté le contrôle ActiveX à l'intérieur de la collection de formes, vous pouvez alors accéder à l'objet de contrôle ActiveX via[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) propriété, puis définissez ses différentes propriétés.

{{% /alert %}}

L'exemple de code suivant ajoute le contrôle ActiveX du bouton bascule à l'aide de Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
