---
title: Gestion des plages
linktitle: Gammes
type: docs
weight: 75
url: /fr/java/managing-ranges/
---
## **Introduction**

Dans Excel, vous pouvez sélectionner plusieurs cellules avec une boîte de sélection de la souris, l'ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer sur le bouton gauche de la souris dans Cell "A1" d'Excel, puis faire glisser vers la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells.

Voici comment créer une plage, mettre une valeur, définir un style et effectuer d'autres opérations sur l'objet "Range".

## **Gestion des gammes à l'aide de Aspose.Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil.

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1 : C4, vous pouvez utiliser le code suivant :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Mettez de la valeur dans le Cells de la Gamme**

Supposons que vous ayez une plage de cellules qui s'étend sur A1: C4. La matrice fait 4 * 3 = 12 cellules. Les cellules de plage individuelles sont disposées séquentiellement : Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Set style du Cells de la Gamme**

L'exemple suivant montre comment définir le style des cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **Obtenir la région actuelle de la plage**

 CurrentRegion est une propriété qui renvoie un objet Range qui représente la région actuelle.

La région actuelle est une plage délimitée par n'importe quelle combinaison de lignes vides et de colonnes vides. Lecture seulement.

Dans Excel, vous pouvez obtenir la zone CurrentRegion en :
1. Sélectionnez une zone (range1) avec la boîte de la souris.
2. Cliquez sur "Accueil - Édition - Rechercher et sélectionner - Aller à Spécial - Région actuelle", ou utilisez "Ctrl + Maj + *", vous verrez qu'Excel vous aide automatiquement à sélectionner une zone (range2), maintenant vous l'avez fait, range2 est la CurrentRegion de range1.

En utilisant Aspose.Cells, vous pouvez utiliser la propriété "Range.CurrentRegion" pour exécuter la même fonction.

Veuillez télécharger le fichier de test suivant, ouvrez-le dans Excel, utilisez la souris pour sélectionner une zone "A1:D7", puis cliquez sur "Ctrl+Maj+*", vous verrez la zone "A1:C3" sélectionnée.

[région_actuelle.xlsx](current_region.xlsx)

Veuillez maintenant exécuter l'exemple suivant, voir comment cela fonctionne dans Aspose.Cells :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Sujets avancés**
- [Plage de remplissage automatique du fichier Excel](/cells/fr/java/autofill-ranges/)
- [Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage](/cells/fr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Copier les plages d'Excel](/cells/fr/java/copy-ranges-of-Excel/)
- [Copier uniquement les données de plage](/cells/fr/java/copy-range-data-only/)
- [Copier les données de plage avec style](/cells/fr/java/copy-range-data-with-style/)
- [Copier le style de plage uniquement](/cells/fr/java/copy-range-style-only/)
- [Copier les hauteurs de ligne de la plage source dans la plage de destination](/cells/fr/java/copy-row-heights-of-source-range-to-destination-range/)
- [Créer une plage d'union](/cells/fr/java/create-union-range/)
- [Couper et coller des plages](/cells/fr/java/cut-and-paste-cells/)
- [Supprimer des plages](/cells/fr/java/delete-ranges-from-Excel/)
- [Détecter fusionné Cells dans une feuille de calcul](/cells/fr/java/detect-merged-cells-in-a-worksheet/)
- [Get Address Cell Count Offset Toute la colonne et toute la ligne de la plage](/cells/fr/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Obtenir la portée avec des liens externes](/cells/fr/java/get-range-with-external-links/)
- [Implémentation de plages non séquentielles](/cells/fr/java/implementing-non-sequential-ranges/)
- [Insérer des plages](/cells/fr/java/insert-ranges-to-Excel/)
- [Fusionner ou dissocier la plage de Cells](/cells/fr/java/merge-or-unmerge-range-of-cells/)
- [Déplacer la plage de Cells dans une feuille de calcul](/cells/fr/java/move-range-of-cells-in-a-worksheet/)
- [Plages nommées](/cells/fr/java/named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/java/search-and-replace-data-in-a-range/)

