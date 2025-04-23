---
title: Définir la bordure de la plage
type: docs
weight: 600
url: /fr/java/set-range-border/
---

## **Scénarios d'utilisation possibles**
Lorsque vous souhaitez définir la bordure pour une plage, vous n'avez pas besoin de définir chaque cellule individuellement. Vous pouvez définir la bordure sur la plage. Aspose.Cells propose cette fonctionnalité.
Cet article fournit un code d'exemple qui utilise Aspose.Cells pour définir la bordure d'une plage.

## **Définir la bordure de la plage dans Excel**
Pour définir la bordure d'une plage dans Excel, vous pouvez suivre ces étapes :
1. Sélectionnez la plage de cellules sur laquelle vous souhaitez appliquer la bordure.
2. Dans l'onglet « Accueil » du ruban, localisez le groupe « Police ».
3. Dans le groupe « Police », cliquez sur le bouton déroulant « Bordures ».
<br>
<img src="border.png" />
4. Choisissez le type de bordure que vous souhaitez appliquer parmi les options du menu déroulant. Vous pouvez choisir parmi les styles de bordure prédéfinis ou personnaliser votre propre bordure.
5. Une fois que vous avez sélectionné le style de bordure souhaité, la bordure sera appliquée à la plage de cellules sélectionnée.

## **Définir la bordure de la plage en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Créer un classeur.
1. Ajouter des données aux cellules dans la première feuille de calcul.
1. Créer un [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/range/).
1. Définir la bordure interne de la plage.
1. Définir la bordure externe de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Range-set-border.java" >}}
{{< app/cells/assistant language="java" >}}
