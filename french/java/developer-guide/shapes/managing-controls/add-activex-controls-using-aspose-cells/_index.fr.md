---
title: Ajouter des contrôles ActiveX à l'aide de Aspose.Cells
type: docs
weight: 720
url: /fr/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

 Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant le[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ) méthode. Cette méthode prend un paramètre[Type de contrôle](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)qui indique quel type de contrôle ActiveX doit être ajouté dans une feuille de calcul. Il a les valeurs suivantes.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [BOÎTE COMBO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [BOUTON DE COMMANDE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [ÉTIQUETTE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [BOUTON RADIO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [BARRE DE DÉFILEMENT](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [ZONE DE TEXTE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [BOUTON À BASCULE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [INCONNUE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

 Une fois que vous avez ajouté le contrôle ActiveX à l'intérieur de la collection de formes, vous pouvez alors accéder à l'objet de contrôle ActiveX via[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) propriété, puis définissez ses différentes propriétés.

{{% /alert %}} 
## **Ajouter le contrôle ActiveX du bouton bascule en utilisant Aspose.Cells**
 L'exemple de code suivant ajoute le contrôle ActiveX du bouton bascule à l'aide de Aspose.Cells. Veuillez télécharger le[fichier excel de sortie](5473427.xlsx) généré avec ce code pour votre référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
