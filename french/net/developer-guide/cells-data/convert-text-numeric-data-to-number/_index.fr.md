---
title: Convertir des données numériques texte en nombre
type: docs
weight: 900
url: /fr/net/convert-text-numeric-data-to-number/
description: Apprenez à convertir des nombres stockés sous forme de texte dans Excel en nombres en utilisant le Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **Scénarios d'utilisation possibles**
Parfois, vous souhaitez convertir des données numériques saisies sous forme de texte en nombres. Vous pouvez saisir des nombres sous forme de texte dans Excel Microsoft en mettant une apostrophe devant un nombre, par exemple *'12345**. Excel traite ensuite le nombre comme une chaîne. Aspose.Cells vous permet de convertir des chaînes en nombres.


##  Comment convertir des nombres stockés sous forme de texte en nombres dans Excel
Vous pouvez convertir des nombres stockés sous forme de texte en nombres en suivant quelques étapes simples.
1. Sélectionnez n’importe quelle cellule ou plage de cellules comportant un indicateur d’erreur dans le coin supérieur gauche.
1.  À côté de la cellule ou de la plage de cellules sélectionnée, cliquez sur le bouton d'erreur qui apparaît. Dans le menu, cliquez sur Convertir en nombre.
<br>
<img src="4.png" width=70% />
1. Si le bouton d'alerte n'est pas disponible, sélectionnez une colonne présentant ce problème. Si vous ne souhaitez pas convertir la colonne entière, vous pouvez sélectionner une ou plusieurs cellules à la place. Assurez-vous simplement que les cellules que vous sélectionnez se trouvent dans la même colonne, sinon ce processus ne fonctionnera pas. Le bouton Texte en colonnes est généralement utilisé pour diviser une colonne, mais il peut également être utilisé pour convertir une seule colonne de texte en nombres. Sous l’onglet Données, cliquez sur Texte en colonnes.
<br>
<img src="1.png" width=70% />
1. Cliquez sur le bouton Terminer dans la boîte contextuelle.
<br>
<img src="2.png" width=70% />
1. Les nombres stockés sous forme de texte sont transformés en nombres.
<br>
<img src="3.png" width=70% />

## Comment convertir des nombres stockés sous forme de texte en nombres en utilisant Aspose.Cells for .NET
Aspose.Cells fournit le[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)méthode qui peut être utilisée pour convertir toutes les données numériques de chaîne ou de texte en nombres.

La capture d'écran suivante montre les numéros de chaîne dans les cellules *A1:A17**. Les numéros de chaîne sont alignés à gauche.
<br>
<img src="5.png" width=70% />

 Ces numéros de chaîne ont été convertis en nombres à l'aide de[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)dans la capture d'écran suivante. Comme vous pouvez le constater, ils sont désormais alignés à droite.
<br>
<img src="6.png" width=70% />

##  Code C# pour convertir les données numériques de chaîne en nombres réels

L'exemple de code suivant illustre comment convertir toutes les données numériques de chaîne en nombres réels dans toutes les feuilles de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
