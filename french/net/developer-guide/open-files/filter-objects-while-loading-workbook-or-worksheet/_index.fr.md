---
title: Filtrer les objets lors du chargement du classeur ou de la feuille de calcul
type: docs
weight: 330
url: /fr/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Scénarios d'utilisation possibles**
Veuillez utiliser[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)propriété lors du filtrage des données du classeur. Mais si vous souhaitez filtrer les données de feuilles de calcul individuelles, vous devrez remplacer le[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)méthode. Veuillez fournir une valeur appropriée à partir du[LoadDataFilterOptionsLoadDataFilterOptionsLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)énumération lors de la création ou de l'utilisation[ChargerFiltre](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 La[LoadDataFilterOptionsLoadDataFilterOptionsLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)énumération a les valeurs possibles suivantes.

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
- Forme
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap
## **Filtrer les objets lors du chargement du classeur**
 L'exemple de code suivant montre comment filtrer les graphiques du classeur. S'il vous plaît, vérifiez le[exemple de fichier excel](5115258.xlsx) utilisé dans ce code et le[PDF de sortie](5115257.pdf)généré par celui-ci. Comme vous pouvez le voir dans le PDF de sortie, tous les graphiques ont été filtrés du classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtrer les objets lors du chargement de la feuille de calcul**
 L'exemple de code suivant charge le[fichier excel source](5115255.xlsx) et filtre les données suivantes à partir de ses feuilles de calcul à l'aide d'un filtre personnalisé.

- Il filtre les graphiques de la feuille de calcul nommée NoCharts.
- Il filtre les formes de la feuille de calcul nommée NoShapes.
- Il filtre la mise en forme conditionnelle de la feuille de calcul nommée NoConditionalFormatting.

 Une fois, il charge le[fichier excel source](5115255.xlsx) avec un filtre personnalisé, il prend les images de toutes les feuilles de calcul une par une. Voici les images de sortie pour votre référence. Comme vous pouvez le voir, la première image n'a pas de graphiques, la deuxième image n'a pas de formes et la troisième image n'a pas de mise en forme conditionnelle.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Voici comment utiliser la classe CustomLoadFilter selon les noms de feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
