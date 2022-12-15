---
title: Cells Formatage
type: docs
weight: 50
url: /fr/cpp/cells-formatting/
---
## **Format Cell ou Plage de Cells**
 Si vous souhaitez formater une cellule ou une plage de cellules, Aspose.Cells fournit le[IStyle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)classer. Vous pouvez effectuer tout le formatage de la cellule ou de la plage de cellules à l'aide de cette classe. Certaines des choses relatives au formatage qui peuvent être accomplies avec la classe IStyle sont les suivantes

- Définir la couleur de remplissage de la cellule
- Définir l'habillage du texte de la cellule
- Définissez les bordures des cellules comme les bordures supérieure, gauche, inférieure et droite, etc.
- Définissez la couleur de la police, la taille de la police, le nom de la police, la barre, le gras, l'italique, le souligné, etc.
- Réglez l'alignement horizontal ou vertical du texte sur droite, gauche, haut, bas, centre, etc.

 Si vous souhaitez définir le style d'une seule cellule, veuillez utiliser[ICell->SetIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) méthode et si vous souhaitez définir le style d'une plage de cellules, veuillez utiliser[IRange->AppliquerIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)méthode.
## **Exemple de code**
 L'exemple de code suivant met en forme la cellule C4 de la feuille de calcul de différentes manières et la capture d'écran montre le[fichier excel de sortie](21266438.xlsx) généré par celui-ci pour votre référence.

![tâche : image_autre_texte](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
