---
title: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 900
url: /fr/java/update-activex-combobox-control/
---

## **Scénarios d'utilisation possibles**
Vous pouvez lire ou écrire les valeurs du contrôle ComboBox ActiveX à l'aide d'Aspose.Cells. Veuillez accéder au contrôle ActiveX via la propriété [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) et vérifiez son type via la propriété [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type), cela devrait renvoyer la valeur [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) et puis effectuez une conversion de type en objet [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) et lisez ou modifiez ses différentes propriétés.

Veuillez télécharger le [fichier excel d'exemple](5473374.xlsx) utilisé dans le code d'exemple suivant et le [fichier excel de sortie](5473375.xlsx) généré par celui-ci.
## **Mise à jour du contrôle ComboBox ActiveX**
La capture d'écran suivante montre l'effet du code d'exemple sur le [fichier excel d'exemple](5473374.xlsx). Comme vous pouvez le voir, la valeur du ComboBox ActiveX a été mise à jour à "Ceci est un contrôle de liste déroulante".

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **Code d'exemple**
Le code d'exemple suivant met à jour la valeur du contrôle ComboBox ActiveX présent dans le [fichier Excel d'exemple](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
