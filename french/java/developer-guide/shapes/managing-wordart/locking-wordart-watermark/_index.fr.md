---
title: Verrouiller le filigrane WordArt
type: docs
weight: 160
url: /fr/java/locking-wordart-watermark/
---

{{% alert color="primary" %}}

Les API Aspose.Cells permettent d'ajouter des filigranes WordArt sur la feuille de calcul de manière à ce que le WordArt devienne un objet qui peut être déplacé et positionné sur la feuille de calcul. Il est également possible de verrouiller l'objet WordArt pour toute interaction telle que l'édition, le déplacement et la sélection. Cet article explique l'utilisation de la méthode [**Shape.setLockedProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#setLockedProperty(int,%20boolean)) pour verrouiller quelques aspects du filigrane.

{{% /alert %}}

## **Verrouillage du filigrane WordArt**

Les API Aspose.Cells permettent de verrouiller certains aspects du filigrane afin que l'interaction de l'utilisateur soit limitée ou complètement bloquée. L'extrait de code suivant montre l'utilisation de l'API Aspose.Cells for Java pour créer un filigrane pour chaque feuille de calcul dans la feuille de calcul chargée et verrouiller la sélection, le déplacement, l'édition et le redimensionnement du filigrane.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LockWordArtWatermark-LockWordArtWatermark.java" >}}
