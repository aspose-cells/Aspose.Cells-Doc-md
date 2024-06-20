---
title: Convertir des données numériques sous forme de texte en nombre
type: docs
weight: 900
url: /fr/python-net/convert-text-numeric-data-to-number/
description: Apprenez à convertir des nombres stockés sous forme de texte dans Excel en nombres en utilisant l API Aspose.Cells pour Python via .NET.
keywords: python excel convertir le texte en nombre, python excel convertir le texte en nombre, python excel convertir des données numériques sous forme de texte en nombre, python excel convertir des données numériques sous forme de texte en nombre, python excel convertir du texte numérique en nombre, python excel convertir du texte numérique en nombre, excel convertir du texte numérique en nombre avec python, convertir du texte numérique en nombre dans excel avec python, convertir la chaîne numérique en nombre dans la bibliothèque excel python, python excel convertir des données numériques sous forme de texte en nombre, python excel convertir la chaîne numérique en nombre.
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez convertir des données numériques entrées sous forme de texte en nombres. Vous pouvez entrer des nombres sous forme de texte dans Microsoft Excel en plaçant un apostrophe avant un nombre, par exemple **'12345**. Excel traite alors le nombre comme une chaîne de caractères. Aspose.Cells pour Python via .NET vous permet de convertir des chaînes en nombres.


## **Comment convertir les nombres stockés sous forme de texte en nombres dans Excel**
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

## **Comment convertir les nombres stockés sous forme de texte en nombres en utilisant la bibliothèque Excel Aspose.Cells pour Python**
Aspose.Cells pour Python via .NET fournit la méthode [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) qui peut être utilisée pour convertir toutes les données numériques sous forme de chaînes ou de texte en nombres.

La capture d'écran suivante montre des nombres sous forme de chaînes dans les cellules **A1:A17**. Les nombres sous forme de chaînes sont alignés à gauche.
<br>
<img src="5.png" width=70% />

Ces nombres sous forme de chaînes ont été convertis en nombres en utilisant [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) dans la capture d'écran suivante. Comme vous pouvez le voir, ils sont maintenant alignés à droite.
<br>
<img src="6.png" width=70% />

## **Code Python pour convertir des données numériques en chaîne en nombres réels**

Le code d'exemple suivant illustre comment convertir toutes les données numériques en chaîne en nombres réels dans toutes les feuilles de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
