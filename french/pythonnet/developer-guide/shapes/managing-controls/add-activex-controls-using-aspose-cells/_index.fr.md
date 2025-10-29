---
title: Ajouter des contrôles ActiveX
type: docs
weight: 260
url: /fr/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells pour Python via .NET en utilisant la méthode [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control). Cette méthode prend un paramètre [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) qui indique le type de contrôle ActiveX à ajouter dans une feuille de calcul. Elle possède les valeurs suivantes.

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
- ControlType.INCONNU


Une fois que vous avez ajouté le contrôle ActiveX à l'intérieur de la collection de formes, vous pouvez ensuite accéder à l'objet contrôle ActiveX via la propriété [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) et définir ensuite ses différentes propriétés.

{{% /alert %}}

Le code d’exemple suivant ajoute un contrôle ActiveX de bouton de basculement en utilisant Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
