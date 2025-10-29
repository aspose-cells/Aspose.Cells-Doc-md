---
title: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul avec Golang via C++
linktitle: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul
type: docs
weight: 330
url: /fr/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Apprenez à filtrer des objets comme des graphiques, formes et mise en forme conditionnelle lors du chargement des classeurs ou feuilles de calcul en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
Veuillez utiliser la propriété [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) lors du filtrage des données du classeur. Mais si vous souhaitez filtrer les données d'une feuille spécifique, vous devrez remplacer la méthode [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Veuillez fournir une valeur appropriée à partir de l'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) lors de la création ou de l'utilisation de [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

L'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) a les valeurs possibles suivantes.

- Tous
- Paramètres du classeur
- Cellule vide
- Cellule booléenne
- Données de la cellule
- Erreur de la cellule
- Numérique de la cellule
- Chaîne de la cellule
- Valeur de la cellule
- Chart
- Formatage conditionnel
- Validation des données
- Noms définis
- Propriétés du document
- Formule
- Liens hypertexte
- Zone de fusion
- Tableau croisé dynamique
- Paramètres
- Forme
- Données de feuille
- Paramètres de feuille
- Structure
- Style
- Tableau
- VBA
- XmlMap

## **Filtrer les objets lors du chargement du classeur**
Le code d'exemple suivant illustre comment filtrer les graphiques du classeur. Veuillez vérifier le [fichier Excel exemple](5115258.xlsx) utilisé dans ce code et le [PDF de sortie](5115257.pdf) généré par celui-ci. Comme vous pouvez le voir dans le PDF de sortie, tous les graphiques ont été filtrés du classeur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **Filtrer les objets lors du chargement de la feuille de calcul**
Le code d'exemple suivant charge le [fichier Excel source](5115255.xlsx) et filtre les données suivantes de ses feuilles de calcul en utilisant un filtre personnalisé.

- Il filtre les graphiques de la feuille de calcul nommée NoCharts.
- Il filtre les formes de la feuille de calcul nommée NoShapes.
- Il filtre la mise en forme conditionnelle de la feuille de calcul nommée NoConditionalFormatting.

Une fois, il charge le [fichier Excel source](5115255.xlsx) avec un filtre personnalisé, il prend les images de toutes les feuilles de calcul une par une. Voici les images de sortie pour votre référence. Comme vous pouvez le voir, la première image n'a pas de graphiques, la deuxième image n'a pas de formes et la troisième image n'a pas de mise en forme conditionnelle.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
Voici comment utiliser la classe CustomLoadFilter en fonction des noms des feuilles de calcul.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
