---
title: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 170
url: /fr/net/update-activex-combobox-control/
---
## **Scénarios d'utilisation possibles**
 Vous pouvez lire ou écrire les valeurs du contrôle ActiveX ComboBox à l'aide de Aspose.Cells. Veuillez accéder au contrôle ActiveX via[Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) propriété et vérifier son type via[ActiveXControl.TypeActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type) propriété, il devrait retourner[ControlType.ComboBoxControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) valeur, puis transtypez-la dans[ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)objet et lire ou modifier ses différentes propriétés.

 Veuillez télécharger le[exemple de fichier excel](5115124.xlsx) utilisé dans l'exemple de code suivant.
## **Mettre à jour le contrôle ComboBox ActiveX**
 La capture d'écran suivante montre l'effet de l'exemple de code sur le[exemple de fichier excel](5115124.xlsx)Comme vous pouvez le voir, la valeur ActiveX ComboBox a été mise à jour en "Ceci est un contrôle de zone de liste déroulante".

|![tâche : image_autre_texte](update-activex-combobox-control_1.png)|
|:- |
## **Exemple de code**
 L'exemple de code suivant met à jour la valeur du contrôle ActiveX ComboBox présent dans le[exemple de fichier excel](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
