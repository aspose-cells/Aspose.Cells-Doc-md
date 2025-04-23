---
title: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul
type: docs
weight: 330
url: /fr/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Scénarios d'utilisation possibles**
Veuillez utiliser la propriété [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) lors du filtrage des données du classeur. Mais si vous souhaitez filtrer des données à partir de feuilles individuelles, vous devrez surcharger la méthode [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet). Veuillez fournir la valeur appropriée depuis l'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) lors de la création ou de l'utilisation de [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter).

L'énumération [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) a les valeurs possibles suivantes.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

