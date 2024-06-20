---
title: Ajouter des contrôles ActiveX à l aide d Aspose.Cells
type: docs
weight: 260
url: /fr/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant la méthode [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol). Cette méthode prend un paramètre [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) qui indique quel type de contrôle ActiveX doit être ajouté à l'intérieur d'une feuille de calcul. Voici les valeurs suivantes:

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

Une fois que vous avez ajouté le contrôle ActiveX à l'intérieur de la collection de formes, vous pouvez ensuite accéder à l'objet contrôle ActiveX via la propriété [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) et définir ensuite ses différentes propriétés.

{{% /alert %}}

Le code d'exemple suivant ajoute le contrôle ActiveX du bouton bascule à l'aide d'Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
