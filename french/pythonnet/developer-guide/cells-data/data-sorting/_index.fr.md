---
title: Tri des données
type: docs
weight: 130
url: /fr/python-net/sort-data-of-excel/
description: Apprenez à trier les données en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Trier les données en Python par ordre croissant ou décroissant, Trier les données en Python en fonction de la couleur de fond.
---

{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles d'Excel. Il permet aux utilisateurs de trier les données pour les rendre plus faciles à parcourir. Aspose.Cells pour Python via .NET permet aux développeurs de trier les données de feuille de calcul par ordre alphabétique ou numérique, ce qui fonctionne de la même manière qu'Excel pour trier les données.

{{% /alert %}}

## **Triage des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1. Sélectionnez **Données** dans le menu **Trier**. La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

En général, le tri est effectué sur une liste - définie comme un groupe de données contiguës où les données sont affichées dans des colonnes.

## **Tri de données avec la bibliothèque Aspose.Cells for Python Excel**

Aspose.Cells for for Python via .NET fournit la classe [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) utilisée pour trier les données par ordre croissant ou décroissant. La classe possède certains membres importants, par exemple, les propriétés Key1...Key3 et Order1...Order3. Ces membres sont utilisés pour définir les clés triées et spécifier l'ordre de tri des clés.

Vous devez définir les clés et définir l'ordre de tri avant de mettre en œuvre le tri des données. La classe fournit la méthode [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

La méthode [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) accepte les paramètres suivants :

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), les cellules de la feuille de calcul sous-jacente.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), la plage de cellules. Définissez la zone de cellules avant d'appliquer le tri des données.

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel. Après l'exécution du code ci-dessous, les données sont triées correctement.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

Si vous souhaitez trier *de gauche à droite*, utilisez l'attribut [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/).

{{% /alert %}}

### **Tri de données avec couleur de fond en utilisant la bibliothèque Aspose.Cells pour Python Excel**

Excel offre des fonctionnalités pour trier les données en fonction de la couleur de fond. La même fonctionnalité est fournie en utilisant Aspose.Cells for for Python via .NET en utilisant DataSorter où [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor peut être utilisé dans [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) pour trier les données en fonction de la couleur de fond. Toutes les cellules contenant la couleur spécifiée dans la [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any), la fonction sont placées en haut ou en bas selon le paramétrage de SortOrder et l'ordre du reste des cellules n'est pas du tout modifié.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Sujets avancés**
- [Trier les données dans une colonne avec une liste de tri personnalisée](/cells/fr/python-net/sort-data-in-column-with-custom-sort-list/)
- [Spécifier un avertissement de tri lors du tri des données](/cells/fr/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
