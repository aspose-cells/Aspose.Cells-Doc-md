---
title: Définir la bordure de la plage avec Golang via C++
type: docs
weight: 600
url: /fr/go-cpp/set-range-border/
description: Apprenez comment définir les bordures de la plage en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**
Lorsque vous souhaitez définir la bordure d’une plage, vous n’avez pas besoin de définir chaque cellule individuellement. Vous pouvez définir la bordure sur toute la plage. Aspose.Cells offre cette fonctionnalité. Cet article fournit un exemple de code utilisant Aspose.Cells pour définir la bordure de plage.

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
2. Ajouter des données aux cellules de la première feuille de calcul.
3. Créer un [**Range**](https://reference.aspose.com/cells/go-cpp/range).
4. Définir la bordure intérieure de la plage.
5. Définir la bordure extérieure de la plage.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetBorder.go" >}}
