---
title: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 900
url: /fr/java/update-activex-combobox-control/
---
## **Scénarios d'utilisation possibles**
 Vous pouvez lire ou écrire les valeurs du contrôle ActiveX ComboBox à l'aide de Aspose.Cells. Veuillez accéder au contrôle ActiveX via[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) propriété et vérifier son type via[ActiveXControl.TypeActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type) propriété, il devrait retourner[ControlType.ComboBoxControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) valeur, puis transtypez-la dans[ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl)objet et lire ou modifier ses différentes propriétés.

 Veuillez télécharger le[exemple de fichier excel](5473374.xlsx) utilisé dans l'exemple de code suivant et le[fichier excel de sortie](5473375.xlsx) généré par celui-ci.
## **Mettre à jour le contrôle ComboBox ActiveX**
 La capture d'écran suivante montre l'effet de l'exemple de code sur le[exemple de fichier excel](5473374.xlsx)Comme vous pouvez le voir, la valeur ActiveX ComboBox a été mise à jour en "Ceci est un contrôle de zone de liste déroulante".

![tâche : image_autre_texte](update-activex-combobox-control_1.png)
## **Exemple de code**
 L'exemple de code suivant met à jour la valeur du contrôle ActiveX ComboBox présent dans le[exemple de fichier excel](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
