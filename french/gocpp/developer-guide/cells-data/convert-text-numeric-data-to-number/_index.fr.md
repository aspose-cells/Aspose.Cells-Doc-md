---
title: Convertir les données textuelles numériques en nombre avec Golang via C++
linktitle: Convertir des données numériques sous forme de texte en nombre
type: docs
weight: 900
url: /fr/go-cpp/convert-text-numeric-data-to-number/
description: Découvrez comment convertir des nombres stockés en tant que texte dans Excel en nombres en utilisant l’API Aspose.Cells for C++.
keywords: convertir texte en nombre Excel, convertir texte en nombre C++, convertir données numériques stockées en texte en nombre, convertir données numériques stockées en texte en nombre en C++, convertir texte numérique en nombre Excel, convertir texte numérique en nombre C++, convertir texte numérique en nombre avec C++, convertir texte numérique en nombre dans Excel en C++, convertir texte numérique en nombre dans Excel avec C++, convertir chaîne numérique en nombre dans Excel avec C++, convertir données textuelles numériques en nombre Excel, convertir chaîne numérique en nombre C++
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez convertir des données numériques saisies sous forme de texte en nombres. Vous pouvez saisir des nombres sous forme de texte dans Microsoft Excel en mettant une apostrophe avant un nombre, par exemple **'12345**. Excel traite alors le nombre comme une chaîne. Aspose.Cells vous permet de convertir des chaînes en nombres.

## Comment convertir des nombres stockés sous forme de texte en nombres dans Excel
Vous pouvez convertir les nombres stockés sous forme de texte en nombres en suivant quelques étapes simples.
1. Sélectionnez une cellule unique ou une plage de cellules comportant un indicateur d'erreur dans le coin supérieur gauche.
1. À côté de la cellule ou de la plage de cellules sélectionnée, cliquez sur le bouton d'erreur qui apparaît. Dans le menu, cliquez sur Convertir en nombre. 
<br>
<img src="4.png" width=70% />
1. Si le bouton d'alerte n'est pas disponible, sélectionnez une colonne présentant ce problème. Si vous ne voulez pas convertir toute la colonne, vous pouvez sélectionner une ou plusieurs cellules à la place. Assurez-vous simplement que les cellules que vous sélectionnez se trouvent dans la même colonne, sinon ce processus ne fonctionnera pas. Le bouton Texte en colonnes est généralement utilisé pour diviser une colonne, mais il peut également être utilisé pour convertir une seule colonne de texte en nombres. Sur l'onglet Données, cliquez sur Texte en colonnes.
<br>
<img src="1.png" width=70% />
1. Cliquez sur le bouton Terminer dans la boîte de dialogue.
<br>
<img src="2.png" width=70% />
1. Les nombres stockés sous forme de texte sont transformés en nombres.
<br>
<img src="3.png" width=70% />

## Comment convertir des nombres stockés sous forme de texte en nombres en utilisant Aspose.Cells for C++
Aspose.Cells fournit la méthode [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/go-cpp/cells/convertstringtonumericvalue/) qui peut être utilisée pour convertir toutes les données numériques sous forme de chaîne ou de texte en nombres.

La capture d'écran suivante montre des nombres sous forme de chaînes dans les cellules **A1:A17**. Les nombres sous forme de chaînes sont alignés à gauche.
<br>
<img src="5.png" width=70% />

Ces nombres sous forme de chaînes ont été convertis en nombres en utilisant [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/go-cpp/cells/convertstringtonumericvalue/) dans la capture d'écran suivante. Comme vous pouvez le voir, ils sont maintenant alignés à droite.
<br>
<img src="6.png" width=70% />

## Code C++ pour convertir des données numériques sous forme de chaîne en nombres réels

Le code d'exemple suivant illustre comment convertir toutes les données numériques en chaîne en nombres réels dans toutes les feuilles de calcul.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertTextNumericDataToNumber.go" >}}
