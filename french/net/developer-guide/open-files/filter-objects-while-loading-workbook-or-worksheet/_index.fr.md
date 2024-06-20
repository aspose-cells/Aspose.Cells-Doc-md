---
title: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul
type: docs
weight: 330
url: /fr/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Scénarios d'utilisation possibles**
Veuillez utiliser la propriété [LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) lors du filtrage des données du classeur. Mais si vous souhaitez filtrer les données des feuilles de calcul individuelles, vous devrez remplacer la méthode [LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet). Veuillez fournir la valeur appropriée de l'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) lors de la création ou du travail avec [LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

L'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) a les valeurs possibles suivantes.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtrer les objets lors du chargement de la feuille de calcul**
Le code d'exemple suivant charge le [fichier Excel source](5115255.xlsx) et filtre les données suivantes de ses feuilles de calcul en utilisant un filtre personnalisé.

- Il filtre les graphiques de la feuille de calcul nommée NoCharts.
- Il filtre les formes de la feuille de calcul nommée NoShapes.
- Il filtre la mise en forme conditionnelle de la feuille de calcul nommée NoConditionalFormatting.

Une fois, il charge le [fichier Excel source](5115255.xlsx) avec un filtre personnalisé, il prend les images de toutes les feuilles de calcul une par une. Voici les images de sortie pour votre référence. Comme vous pouvez le voir, la première image n'a pas de graphiques, la deuxième image n'a pas de formes et la troisième image n'a pas de mise en forme conditionnelle.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Voici comment utiliser la classe CustomLoadFilter en fonction des noms des feuilles de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
