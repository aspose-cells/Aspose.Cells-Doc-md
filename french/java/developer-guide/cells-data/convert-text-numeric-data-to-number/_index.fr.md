---
title: Convertir des données numériques sous forme de texte en nombre
type: docs
weight: 150
url: /fr/java/convert-text-numeric-data-to-number/
description: Apprenez comment convertir des nombres stockés sous forme de texte en nombres en utilisant l API Aspose.Cells for Java.
keywords: excel convertir du texte en nombre, excel convertir du texte en nombre en java, excel convertir des données numériques en texte en nombre, excel convertir des données numériques en texte en nombre en java, excel convertir un texte numérique en nombre, excel convertir un texte numérique en nombre en java, excel convertir un texte numérique en nombre avec java, convertir un texte numérique en nombre dans excel avec java, convertir un texte numérique en nombre dans excel avec java, convertir une chaîne numérique en nombre dans excel avec java, excel convertir des données numériques en texte en nombre java, excel convertir une chaîne numérique en nombre en java
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez convertir des données numériques saisies sous forme de texte en nombres. Vous pouvez saisir des nombres sous forme de texte dans Microsoft Excel en mettant une apostrophe avant un nombre, par exemple **'12345**. Excel traite alors le nombre comme une chaîne. Aspose.Cells vous permet de convertir des chaînes en nombres.


## Convertir des nombres stockés sous forme de texte en nombres dans Excel
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

## Convertir des nombres stockés sous forme de texte en nombres en utilisant Aspose.Cells pour JAVA
L'API Aspose.Cells for Java fournit la méthode [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) qui peut être utilisée pour convertir toutes les données numériques de type texte en nombres.

La capture d'écran suivante montre des nombres sous forme de chaînes dans les cellules **A1:A17**. Les nombres sous forme de chaînes sont alignés à gauche.
<br>
<img src="5.png" width=70% />

Ces nombres sous forme de chaînes ont été convertis en nombres en utilisant [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) dans la capture d'écran suivante. Comme vous pouvez le voir, ils sont maintenant alignés à droite.
<br>
<img src="6.png" width=70% />

## Code Java pour convertir des données numériques de type texte en nombres réels
Le code d'exemple suivant illustre comment convertir toutes les données numériques en chaîne en nombres réels dans toutes les feuilles de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
