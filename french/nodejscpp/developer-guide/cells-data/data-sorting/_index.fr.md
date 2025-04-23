---
title: Tri des données
type: docs
weight: 130
url: /fr/nodejs-cpp/sort-data-of-excel/
description: Apprenez comment trier des données en utilisant l API Aspose.Cells for Node.js via C++.
keywords: Trier les données par ordre croissant ou décroissant, trier les données en fonction de la couleur de fond
---

{{% alert color="primary" %}}

Le tri des données est une des nombreuses fonctionnalités utiles de Microsoft Excel. Il permet aux utilisateurs de classer les données pour faciliter leur visualisation. L'API Aspose.Cells for Node.js via C++ permet aux développeurs de trier les données de la feuille de calcul par ordre alphabétique ou numérique, de la même manière que Microsoft Excel.

{{% /alert %}}

## **Triage des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1. Sélectionnez **Données** dans le menu **Trier**. La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

En général, le tri est effectué sur une liste - définie comme un groupe de données contiguës où les données sont affichées dans des colonnes.

## **Trier les données avec Aspose.Cells**

Aspose.Cells for Node.js via C++ fournit la classe [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) utilisée pour trier les données par ordre croissant ou décroissant. La classe possède des membres importants, par exemple, des propriétés comme Key1 ... Key3 et Order1 ... Order3. Ces membres sont utilisés pour définir les clés triées et spécifier l'ordre de tri des clés.

Vous devez définir les clés et définir l'ordre de tri avant de mettre en œuvre le tri des données. La classe fournit la méthode [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

La méthode [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) accepte les paramètres suivants :

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), les cellules de la feuille de calcul sous-jacente.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), la plage de cellules. Définissez la zone de cellules avant d'appliquer le tri des données.

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel. Après l'exécution du code ci-dessous, les données sont triées correctement.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

Si vous souhaitez trier *de gauche à droite*, utilisez l'attribut [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-).

{{% /alert %}}

### **Tri des données avec couleur de fond**

Excel propose des fonctionnalités pour trier les données en fonction de la couleur de fond. La même fonctionnalité est fournie via Aspose.Cells for Node.js via C++ en utilisant DataSorter où [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor peut être utilisé dans [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) pour trier les données en fonction de la couleur de fond. Toutes les cellules contenant la couleur spécifiée dans la fonction [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) sont placées en haut ou en bas selon le paramètre SortOrder, et l'ordre des autres cellules n'est pas modifié.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Sujets avancés**
- [Trier les données dans une colonne avec une liste de tri personnalisée](/cells/fr/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Spécifier un avertissement de tri lors du tri des données](/cells/fr/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

