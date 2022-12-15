---
title: Aspose.Cells for Java 21.2 Notes de mise à jour
type: docs
weight: 11
url: /fr/java/aspose-cells-for-java-21-2-release-notes/
---
{{% alert color="primary" %}}

 Cette page contient des notes de version pour[Aspose.Cells for Java 21.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.2/).

{{% /alert %}}

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSJAVA-43382|La copie produit un classeur corrompu|
|CELLSJAVA-43364|Problème lors de l'enregistrement d'un graphique ayant une image dans le marqueur à l'image|
|CELLSJAVA-43389|Paramètres de protection par mot de passe du classeur/feuille de calcul perdus lors de l'enregistrement au format de fichier XLSB|
|CELLSJAVA-43392|La copie de la feuille produit un classeur corrompu|
|CELLSJAVA-43387|L'exportation d'une seule feuille au format HTML soulève une exception|

## **Public API et modifications incompatibles avec les versions antérieures**

Voici une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for Java. Si vous avez des inquiétudes concernant l'un des changements répertoriés, veuillez le signaler sur le forum d'assistance Aspose.Cells.

### **Modifie le comportement de Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

Dans les anciennes versions, nous supprimons tous les paramètres de colonne tout en supprimant les lignes vides si la feuille de calcul est vide (pas de données de cellules). Cela rend impossible pour l'utilisateur de supprimer uniquement les lignes vides et de conserver tous les paramètres de colonne. À partir de 21.2, nous n'effaçons plus les paramètres de colonne. Si l'utilisateur doit supprimer les paramètres de colonne pour une feuille de calcul vide, il doit vérifier qu'il n'y a pas de données dans la feuille, puis effacer manuellement la ColumnCollection.
Dans les anciennes versions, nous ne supprimons pas les lignes vides sous forme. Cela rend impossible pour l'utilisateur de supprimer toutes les lignes vides comme prévu. À partir de 12.2, nous supprimons ces lignes vides sous forme avec d'autres lignes vides communes.

### **Propriété Range.CellCount obsolète.**

Veuillez utiliser Range.RowCount et Range.ColumnCount pour obtenir le nombre total de cellules à la place.

### **Ajoute la propriété AutoFilter.ShowFilterButton.**

Indique si le bouton de filtre du filtre automatique est affiché.

### **Supprime la propriété SeriesCollection.SecondCatergoryData.**

Veuillez utiliser la propriété SeriesCollection.SecondCategoryData à la place.

### **Supprime l'énumération StyleModifyFlag.Spacing.**

Il n'est pas utilisé.
