---
title: Gestion des plages
linktitle: Plages
type: docs
weight: 75
url: /fr/java/managing-ranges/
---

## **Introduction**

Dans Excel, vous pouvez sélectionner plusieurs cellules avec une sélection de zone à la souris, l'ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer sur le bouton gauche de la souris dans la cellule "A1" d'Excel, puis faire glisser jusqu'à la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells.

Voici comment créer une plage, mettre une valeur, définir un style et effectuer d'autres opérations sur l'objet "Plage".

## **Gestion des plages à l'aide de Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1:C4, vous pouvez utiliser le code suivant :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Placer une valeur dans les cellules de la plage**

Imaginons que vous avez une plage de cellules qui s'étend sur A1:C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées de manière séquentielle : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Définir le style des cellules de la plage**

L'exemple suivant montre comment définir le style des cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Sujets avancés**
- [Plage AutoFill du fichier Excel](/cells/fr/java/autofill-ranges/)
- [Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage](/cells/fr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Copier des plages de cellules d'Excel](/cells/fr/java/copy-ranges-of-Excel/)
- [Copier uniquement les données de la plage](/cells/fr/java/copy-range-data-only/)
- [Copier les données de la plage avec le style](/cells/fr/java/copy-range-data-with-style/)
- [Copier uniquement le style de la plage](/cells/fr/java/copy-range-style-only/)
- [Copier les hauteurs de ligne de la plage source vers la plage de destination](/cells/fr/java/copy-row-heights-of-source-range-to-destination-range/)
- [Créer l'union de la plage](/cells/fr/java/create-union-range/)
- [Couper et coller des plages](/cells/fr/java/cut-and-paste-cells/)
- [Supprimer les plages](/cells/fr/java/delete-ranges-from-Excel/)
- [Détecter les cellules fusionnées dans une feuille de calcul](/cells/fr/java/detect-merged-cells-in-a-worksheet/)
- [Obtenir le nombre de cellules, le décalage de la plage entière de colonne et de ligne entière](/cells/fr/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Obtenir une plage avec des liens externes](/cells/fr/java/get-range-with-external-links/)
- [Mise en œuvre de plages non séquentielles](/cells/fr/java/implementing-non-sequential-ranges/)
- [Insérer des plages](/cells/fr/java/insert-ranges-to-Excel/)
- [Fusionner ou séparer la plage de cellules](/cells/fr/java/merge-or-unmerge-range-of-cells/)
- [Déplacer une plage de cellules dans une feuille de calcul](/cells/fr/java/move-range-of-cells-in-a-worksheet/)
- [Plages nommées](/cells/fr/java/named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/java/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="java" >}}
