---
title: Formater les plages
type: docs
weight: 105
url: /fr/net/how-to-format-a-range/
---

## **Scénarios d'utilisation possibles**
Lorsque vous devez appliquer un style à une plage, vous pouvez utiliser le formatage des plages.

## **Comment formater une plage dans Excel**

Pour formater une plage de cellules dans Excel, vous pouvez utiliser les options de formatage intégrées fournies par Excel. Voici comment vous pouvez formater une plage de cellules directement dans Excel:

1. Ouvrez Excel et ouvrez le classeur qui contient la plage que vous souhaitez formater.

2. Sélectionnez la plage de cellules que vous souhaitez formater. Vous pouvez cliquer et faire glisser pour sélectionner la plage, ou vous pouvez utiliser des raccourcis clavier comme Maj + touches de direction pour étendre la sélection.

3. Une fois la plage sélectionnée, faites un clic droit sur la plage sélectionnée et choisissez "Format de cellule" dans le menu contextuel. Alternativement, vous pouvez aller dans l'onglet Accueil dans le ruban Excel, cliquer sur la liste déroulante "Format" dans le groupe "Cellules", et sélectionner "Format de cellule".

4. La boîte de dialogue "Format de cellule" apparaîtra. Ici, vous pouvez choisir différentes options de formatage à appliquer à la plage sélectionnée. Par exemple, vous pouvez changer le style de police, la taille de police, la couleur de police, le format de nombre, les bordures, la couleur de fond, etc. Explorez les différents onglets de la boîte de dialogue pour accéder à diverses options de formatage.

5. Après avoir apporté les modifications de formatage souhaitées, cliquez sur le bouton "OK" pour appliquer le formatage à la plage sélectionnée.


## **Comment formater une plage en utilisant C#**

Pour formater une plage en utilisant Aspose.Cells, vous pouvez utiliser les méthodes suivantes:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


## **Code d'exemple**
Dans cet exemple, nous créons un classeur Excel, ajoutons des données d'exemple, accédons à la première feuille de calcul, et définissons deux plages("A1:C3" et "A4:C5"). Ensuite, nous créons de nouveaux styles, définissons diverses options de formatage (par exemple, couleur de police, gras), et appliquons le style à la plage. Enfin, nous enregistrons le classeur dans un nouveau fichier.
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
{{< app/cells/assistant language="csharp" >}}
