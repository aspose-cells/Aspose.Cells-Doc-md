---
title: Formatage des cellules
type: docs
weight: 50
url: /fr/cpp/cells-formatting/
---

## **Format de cellule ou plage de cellules**
Si vous souhaitez formater une cellule ou une plage de cellules, Aspose.Cells fournit la classe [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Vous pouvez accomplir tout le formatage de la cellule ou de la plage de cellules en utilisant cette classe. Certaines des choses relatives au formatage qu'on peut accomplir avec la classe IStyle sont les suivantes

- Définir la couleur de remplissage de la cellule
- Définir le retour à la ligne du texte de la cellule
- Définir les bordures des cellules comme les bordures supérieure, gauche, inférieure et droite, etc.
- Définir la couleur de police, la taille de la police, le nom de la police, le souligné, le gras, l'italique, le souligné, etc.
- Définir l'alignement horizontal ou vertical du texte à droite, à gauche, en haut, en bas, au centre, etc.

Si vous voulez définir le style d'une seule cellule, utilisez la méthode [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) et si vous souhaitez définir le style d'une plage de cellules, utilisez la méthode [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).
## **Code d'exemple**
Le code d'exemple suivant formate la cellule C4 de la feuille de calcul de différentes manières et la capture d'écran montre le [fichier Excel de sortie](21266438.xlsx) généré par celui-ci pour votre référence.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
