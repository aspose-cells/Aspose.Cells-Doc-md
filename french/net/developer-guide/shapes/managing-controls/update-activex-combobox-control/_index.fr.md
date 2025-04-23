---
title: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 170
url: /fr/net/update-activex-combobox-control/
---

## **Scénarios d'utilisation possibles**
Vous pouvez lire ou écrire les valeurs du contrôle de zone de liste déroulante ActiveX à l'aide d'Aspose.Cells. Veuillez accéder au contrôle ActiveX via la propriété [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) et vérifier son type via la propriété [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type), cela devrait renvoyer la valeur [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) et ensuite le convertir en objet [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) et lire ou modifier ses différentes propriétés.

Veuillez télécharger le [fichier Excel exemple](5115124.xlsx) utilisé dans le code d'exemple suivant.
## **Mise à jour du contrôle ComboBox ActiveX**
La capture d'écran suivante montre l'effet du code d'exemple sur le [fichier Excel d'exemple](5115124.xlsx). Comme vous pouvez le constater, la valeur de la boîte combinée ActiveX a été mise à jour pour "Il s'agit d'un contrôle de boîte combinée".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Code d'exemple**
Le code d'exemple suivant met à jour la valeur du contrôle Boîte combi ActiveX présent dans le [fichier Excel d'exemple](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
{{< app/cells/assistant language="csharp" >}}
