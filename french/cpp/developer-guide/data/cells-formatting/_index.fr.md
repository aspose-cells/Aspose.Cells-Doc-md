---
title: Cells Formatage
type: docs
weight: 50
url: /fr/cpp/cells-formatting/
---
##  **Format Cell ou Plage de Cells**
 Si vous souhaitez formater une cellule ou une plage de cellules, Aspose.Cells fournit le[Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/)classe. Vous pouvez effectuer tout le formatage de la cellule ou de la plage de cellules en utilisant cette classe. Certaines des choses liées au formatage qui peuvent être accomplies avec la classe IStyle sont les suivantes

- Définir la couleur de remplissage de la cellule
- Définir l'habillage du texte de la cellule
- Définissez les bordures des cellules comme les bordures supérieure, gauche, inférieure et droite, etc.
- Définissez la couleur de la police, la taille de la police, le nom de la police, la frappe, le gras, l'italique, le souligné, etc.
- Définissez l'alignement horizontal ou vertical du texte à droite, à gauche, en haut, en bas, au centre, etc.

 Si vous souhaitez définir le style d'une seule cellule, veuillez utiliser[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) méthode et si vous souhaitez définir le style d'une plage de cellules, veuillez utiliser[Plage->AppliquerStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)méthode.
##  **Exemple de code**
 L'exemple de code suivant formate la cellule C4 de la feuille de calcul de différentes manières et la capture d'écran montre le[sortie du fichier Excel](21266438.xlsx) généré par celui-ci pour votre référence.

![tâche : image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
