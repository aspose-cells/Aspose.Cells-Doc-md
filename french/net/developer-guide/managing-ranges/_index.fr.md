---
title: Gestion des plages
linktitle: Gammes
type: docs
weight: 105
url: /fr/net/managing-ranges/
---
## **Introduction**

Dans Excel, vous pouvez sélectionner plusieurs cellules avec une boîte de sélection de la souris, l'ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer sur le bouton gauche de la souris dans Cell "A1" d'Excel, puis faire glisser vers la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells.

Voici comment créer une plage, mettre une valeur, définir un style et effectuer d'autres opérations sur l'objet "Range".

## **Gestion des gammes à l'aide de Aspose.Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil.

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1 : C4, vous pouvez utiliser le code suivant :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Mettez de la valeur dans le Cells de la Gamme**

Supposons que vous ayez une plage de cellules qui s'étend sur A1: C4. La matrice fait 4 * 3 = 12 cellules. Les cellules de plage individuelles sont disposées séquentiellement : Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Set style du Cells de la Gamme**

L'exemple suivant montre comment définir le style des cellules de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Sujets avancés**
- [Plage de remplissage automatique du fichier Excel](/cells/fr/net/autofill-ranges/)
- [Copier les plages d'Excel](/cells/fr/net/copy-ranges-of-Excel/)
- [Copier uniquement les données de plage](/cells/fr/net/copy-range-data-only/)
- [Copier les données de plage avec style](/cells/fr/net/copy-range-data-with-style/)
- [Copier le style de plage uniquement](/cells/fr/net/copy-range-style-only/)
- [Créer une plage d'union](/cells/fr/net/create-union-range/)
- [Couper et Coller Gamme](/cells/fr/net/cut-and-paste-cells/)
- [Supprimer des plages](/cells/fr/net/delete-ranges-from-Excel/)
- [Get Address Cell Count Offset Toute la colonne et toute la ligne de la plage](/cells/fr/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insérer des plages](/cells/fr/net/insert-ranges-to-Excel/)
- [Fusionner ou dissocier la plage de Cells](/cells/fr/net/merge-or-unmerge-range-of-cells/)
- [Déplacer la plage de Cells dans une feuille de calcul](/cells/fr/net/move-range-of-cells-in-a-worksheet/)
- [Créer des plages nommées d'étendue de classeur et de feuille de calcul](/cells/fr/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/net/search-and-replace-data-in-a-range/)
