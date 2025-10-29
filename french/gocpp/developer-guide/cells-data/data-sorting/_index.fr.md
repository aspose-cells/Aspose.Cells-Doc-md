---
title: Tri des données avec Golang via C++
linktitle: Tri des données
type: docs
weight: 130
url: /fr/go-cpp/sort-data-of-excel/
description: Apprenez comment trier des données en utilisant l’API Aspose.Cells for C++.
keywords: Trier les données par ordre croissant ou décroissant, trier les données en fonction de la couleur de fond
---

{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Il permet aux utilisateurs d'ordonner les données pour les rendre plus faciles à scanner. Aspose.Cells permet aux développeurs de trier les données de la feuille de calcul par ordre alphabétique ou numérique, ce qui fonctionne de la même manière que Microsoft Excel pour trier les données.

{{% /alert %}}

## **Triage des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1. Sélectionnez **Données** dans le menu **Trier**. La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

En général, le tri est effectué sur une liste - définie comme un groupe de données contiguës où les données sont affichées dans des colonnes.

## **Trier les données avec Aspose.Cells**

Aspose.Cells fournit la classe [**DataSorter**](https://reference.aspose.com/cells/go-cpp/datasorter/) utilisée pour trier les données par ordre croissant ou décroissant. La classe a des membres importants, par exemple, des propriétés comme Key1 ... Key3 et Order1 ... Order3. Ces membres sont utilisés pour définir les clés triées et spécifier l'ordre de tri des clés.

Vous devez définir les clés et définir l'ordre de tri avant de mettre en œuvre le tri des données. La classe fournit la méthode [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

La méthode [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) accepte les paramètres suivants :

- [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), les cellules de la feuille de calcul sous-jacente.
- [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/), la plage de cellules. Définissez la zone de cellules avant d'appliquer le tri des données.

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel. Après l'exécution du code ci-dessous, les données sont triées correctement.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting.go" >}}
{{% alert color="primary" %}}

Si vous souhaitez trier *de gauche à droite*, utilisez l'attribut [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Tri des données avec couleur de fond**

Excel propose des fonctionnalités pour trier les données en fonction de la couleur de fond. La même fonctionnalité est fournie en utilisant Aspose.Cells en utilisant DataSorter où [**SortOnType**](https://reference.aspose.com/cells/go-cpp/sortontype/).CellColor peut être utilisé dans [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) pour trier les données en fonction de la couleur de fond. Toutes les cellules qui contiennent la couleur spécifiée dans le [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), la fonction sont placées en haut ou en bas en fonction du paramètre SortOrder et l'ordre des autres cellules n'est pas du tout modifié.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting-1.go" >}}
## **Sujets avancés**
- [Trier les données dans une colonne avec une liste de tri personnalisée](/cells/fr/cpp/sort-data-in-column-with-custom-sort-list/)
- [Spécifier un avertissement de tri lors du tri des données](/cells/fr/cpp/specifying-sort-warning-while-sorting-data/)
