---
title: Gestion des plages
linktitle: Plages
type: docs
weight: 105
url: /fr/net/managing-ranges/
---

## **Introduction**

Dans Excel, vous pouvez sélectionner plusieurs cellules avec une sélection de zone à la souris, l'ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer sur le bouton gauche de la souris dans la cellule "A1" d'Excel, puis faire glisser jusqu'à la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells.

Voici comment créer une plage, mettre une valeur, définir un style et effectuer d'autres opérations sur l'objet "Plage".

## **Gestion des plages à l'aide de Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1:C4, vous pouvez utiliser le code suivant :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Placer une valeur dans les cellules de la plage**

Imaginons que vous avez une plage de cellules qui s'étend sur A1:C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées de manière séquentielle : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Définir le style des cellules de la plage**

L'exemple suivant montre comment définir le style des cellules de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Obtenir la région actuelle de la plage**

CurrentRegion est une propriété qui renvoie un objet Range qui représente la région actuelle. 

La région actuelle est une plage délimitée par une combinaison de lignes vierges et de colonnes vierges. En lecture seule.

Dans Excel, vous pouvez obtenir la région actuelle en :
1. Sélectionnez une zone (plage1) avec la boîte de souris.
2. Cliquez sur "Accueil - Modification - Recherche et sélection - Atteindre une spécificité - Région actuelle", ou utilisez "Ctrl+Maj+*", vous verrez qu'Excel vous aide automatiquement à sélectionner une zone (plage2), maintenant vous l'avez fait, la plage2 est la région actuelle de la plage1.

En utilisant Aspose.Cells, vous pouvez utiliser la propriété "Range.CurrentRegion" pour effectuer la même fonction.

Veuillez télécharger le fichier de test suivant, l'ouvrir dans Excel, utiliser la boîte de souris pour sélectionner une zone "A1:D7", puis cliquer sur "Ctrl+Maj+*", vous verrez que la zone "A1:C3" est sélectionnée.

[current_region.xlsx](current_region.xlsx)

Veuillez exécuter l'exemple suivant pour voir comment cela fonctionne dans Aspose.Cells :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Sujets avancés**
- [Plage AutoFill du fichier Excel](/cells/fr/net/autofill-ranges/)
- [Copier des plages de cellules d'Excel](/cells/fr/net/copy-ranges-of-Excel/)
- [Copier uniquement les données de la plage](/cells/fr/net/copy-range-data-only/)
- [Copier les données de la plage avec le style](/cells/fr/net/copy-range-data-with-style/)
- [Copier uniquement le style de la plage](/cells/fr/net/copy-range-style-only/)
- [Créer l'union de la plage](/cells/fr/net/create-union-range/)
- [Couper et coller la plage](/cells/fr/net/cut-and-paste-cells/)
- [Supprimer les plages](/cells/fr/net/delete-ranges-from-Excel/)
- [Obtenir le nombre de cellules, le décalage de la plage entière de colonne et de ligne entière](/cells/fr/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insérer des plages](/cells/fr/net/insert-ranges-to-Excel/)
- [Fusionner ou séparer la plage de cellules](/cells/fr/net/merge-or-unmerge-range-of-cells/)
- [Déplacer une plage de cellules dans une feuille de calcul](/cells/fr/net/move-range-of-cells-in-a-worksheet/)
- [Créer des plages nommées en fonction du classeur et de la feuille de calcul](/cells/fr/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/net/search-and-replace-data-in-a-range/)
