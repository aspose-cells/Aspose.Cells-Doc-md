---
title: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 170
url: /fr/python-net/update-activex-combobox-control/
---

## **Scénarios d'utilisation possibles**
Vous pouvez lire ou écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells pour Python via .NET. Accédez au contrôle ActiveX via la propriété [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) et vérifiez son type via la propriété [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/), qui doit renvoyer la valeur [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype), puis convertir en [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) pour lire ou modifier ses différentes propriétés.

Veuillez télécharger le [fichier Excel exemple](5115124.xlsx) utilisé dans le code d'exemple suivant.
## **Mise à jour du contrôle ComboBox ActiveX**
La capture d'écran suivante montre l'effet du code d'exemple sur le [fichier Excel d'exemple](5115124.xlsx). Comme vous pouvez le constater, la valeur de la boîte combinée ActiveX a été mise à jour pour "Il s'agit d'un contrôle de boîte combinée".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Code d'exemple**
Le code d'exemple suivant met à jour la valeur du contrôle Boîte combi ActiveX présent dans le [fichier Excel d'exemple](5115124.xlsx).



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
{{< app/cells/assistant language="python-net" >}}
