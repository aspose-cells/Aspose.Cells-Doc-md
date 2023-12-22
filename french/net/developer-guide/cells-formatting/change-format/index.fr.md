---
title: Changer le format d'une cellule
description: Comment utiliser la bibliothèque Aspose.Cells dans C# pour modifier le formatage des cellules, notamment la police, la couleur, la bordure, etc. En ajustant ces propriétés, vous avez plus de contrôle sur l'apparence et l'apparence des cellules.
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /fr/net/how-to-change-format-of-cell/
---
##  **Scénarios d'utilisation possibles**
Lorsque vous souhaitez mettre en évidence certaines données, vous pouvez modifier le style des cellules.

##  **Comment changer le format d'une cellule dans Excel**

Pour modifier le format d'une seule cellule dans Excel, procédez comme suit :

1. Ouvrez Excel et ouvrez le classeur contenant la cellule que vous souhaitez formater.

2. Localisez la cellule que vous souhaitez formater.

3. Faites un clic droit sur la cellule et sélectionnez "Format Cells" dans le menu contextuel. Alternativement, vous pouvez sélectionner la cellule et accéder à l'onglet Accueil du ruban Excel, cliquer sur la liste déroulante « Format » dans le groupe « Cells » et sélectionner « Formater Cells ».

4. La boîte de dialogue "Formater Cells" apparaîtra. Ici, vous pouvez choisir différentes options de formatage à appliquer à la cellule sélectionnée. Par exemple, vous pouvez modifier le style de police, la taille de la police, la couleur de la police, le format des nombres, les bordures, la couleur d'arrière-plan, etc. Explorez les différents onglets de la boîte de dialogue pour accéder aux différentes options de formatage.

5. Après avoir apporté les modifications de formatage souhaitées, cliquez sur le bouton "OK" pour appliquer le formatage à la cellule sélectionnée.


##  **Comment changer le format d'une cellule en utilisant C#**

Pour modifier le format d'une cellule à l'aide de Aspose.Cells, vous pouvez utiliser Vous pouvez utiliser les méthodes suivantes :
1. [Cell.SetStyle(Style de style)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle (style de style, bool explicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Style de style, drapeau StyleFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **Exemple de code**
Dans cet exemple, nous créons un classeur Excel, ajoutons des exemples de données, accédons à la première feuille de calcul et obtenons deux cellules (« A2 » et « B3 »). Ensuite, nous obtenons le style de la cellule, définissons diverses options de formatage (par exemple, couleur de police, gras) et modifions le format de la cellule. Enfin, nous enregistrons le classeur dans un nouveau fichier.
![tâche : image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
