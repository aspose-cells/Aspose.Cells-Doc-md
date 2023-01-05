---
title: Filtrer les objets lors du chargement du classeur dans GridDesktop
type: docs
weight: 1060
url: /fr/net/aspose-cells-griddesktop/loading-filter
description: Cet article décrit comment utiliser le filtre de chargement pour la bibliothèque Aspose.Cells.GridDesktop.
---
## **Scénarios d'utilisation possibles**
 Veuillez utiliser[GridDesktop.LoadDataFilterGridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)propriété lors du filtrage des données du classeur.

 Le[GridLoadDataFilterOptionsGridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)énumération a les valeurs suivantes.
- Tout
- Paramètres du livre
- CelluleVide
- CellBool
- CellData
- CellErreur
- CellNumérique
- CellString
- ValeurCellule
- Graphique
- Mise en forme conditionnelle
- La validation des données
- NomsDéfinis
- Propriétés du document
- Formule
- Hyperliens
- Zone fusionnée
- Tableau croisé dynamique
- Réglages
- Façonner
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap
## **Filtrer les données lors du chargement du classeur**
 L'exemple de code suivant montre comment filtrer le dessin à partir du classeur. S'il vous plaît, vérifiez le[exemple de fichier excel](5472489.xlsx) . Comme vous pouvez le voir, tous les graphiques/formes/images ont été filtrés du classeur.
![classeur sans image](nodrawing.png)
### **Exemple de code**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}
 