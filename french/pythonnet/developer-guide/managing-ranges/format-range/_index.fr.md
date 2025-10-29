---
title: Formater les plages
type: docs
weight: 105
url: /fr/python-net/how-to-format-a-range/
description: Cet article décrit comment formater des plages avec Aspose.Cells pour la bibliothèque Python via .NET.
keywords: Bibliothèque Python Excel, Comment formater une plage en Python, Comment formater des plages en Python.
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
1. [Range.apply_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)
2. [Range.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style)
3. [Range.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style-bool)


## **Code d'exemple**
Dans cet exemple, nous créons un classeur Excel, ajoutons des données d'exemple, accédons à la première feuille de calcul, et définissons deux plages("A1:C3" et "A4:C5"). Ensuite, nous créons de nouveaux styles, définissons diverses options de formatage (par exemple, couleur de police, gras), et appliquons le style à la plage. Enfin, nous enregistrons le classeur dans un nouveau fichier.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-FormatRanges.py" >}}
{{< app/cells/assistant language="python-net" >}}
