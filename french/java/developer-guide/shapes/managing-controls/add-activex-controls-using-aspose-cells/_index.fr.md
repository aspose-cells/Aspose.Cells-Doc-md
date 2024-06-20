---
title: Ajouter des contrôles ActiveX à l aide d Aspose.Cells
type: docs
weight: 720
url: /fr/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant la méthode [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)). Cette méthode prend un paramètre [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) qui indique le type de contrôle ActiveX à ajouter dans une feuille de calcul. Elle a les valeurs suivantes.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [BOUTON_TOURNANT](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [ZONE_DE_TEXTE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [BOUTON_DE_BASCULE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [INCONNU](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Une fois que vous avez ajouté le contrôle ActiveX dans la collection de formes, vous pouvez ensuite accéder à l'objet contrôle ActiveX via la propriété [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) et définir ses différentes propriétés.

{{% /alert %}} 
## **Ajouter un contrôle ActiveX de bouton bascule à l'aide d'Aspose.Cells**
Le code d'exemple suivant ajoute un contrôle ActiveX de bouton bascule à l'aide d'Aspose.Cells. Veuillez télécharger le [fichier Excel de sortie](5473427.xlsx) généré avec ce code pour votre référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
