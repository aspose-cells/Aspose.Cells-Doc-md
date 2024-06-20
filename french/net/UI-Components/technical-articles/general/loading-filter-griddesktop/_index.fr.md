---
title: Filtrer les objets lors du chargement du classeur dans GridDesktop
type: docs
weight: 1060
url: /fr/net/aspose-cells-griddesktop/loading-filter
description: Cet article décrit comment utiliser le filtre de chargement dans GridDesktop.
keywords: GridDesktop,loading,loading filter,filter
---

## **Scénarios d'utilisation possibles**
Veuillez utiliser la propriété [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter) lors du filtrage des données du classeur.

L'énumération [GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) a les valeurs suivantes.
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
## **Filtrer les données lors du chargement du classeur**
Le code d'exemple suivant illustre comment filtrer le dessin du classeur. Veuillez vérifier le [fichier Excel d'exemple](5472489.xlsx). Comme vous pouvez le voir, tous les graphiques/formes/images ont été filtrés hors du classeur.
![classeur sans image](nodrawing.png)
### **Code d'exemple**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}

