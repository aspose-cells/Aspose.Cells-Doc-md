---
title: Importation intelligente et placement de données avec des marqueurs intelligents
linktitle: Marqueurs intelligents
type: docs
weight: 190
url: /fr/net/using-smart-markers/
description: Importation intelligente et placement de données conforme aux fichiers Excel modèle avec la bibliothèque Aspose.Cells.
---

## **Pourquoi importer des données dans Excel avec des marqueurs intelligents**
Utiliser des marqueurs intelligents pour importer des données dans Excel simplifie l’intégration de données en combinant une conception basée sur un modèle avec une liaison de données dynamique. Cette approche est particulièrement précieuse dans des outils comme Aspose.Cells, où les marqueurs servent de placeholders dans des modèles pour remplir automatiquement les données provenant de diverses sources. Voici les principales raisons d'adopter cette méthode :

1. Efficacité dans la génération de rapports répétitifs : Réutilisation des modèles, modèles Excel préconçus avec des marqueurs intégrés (par exemple, &=VariableName, &=DataSource.Field) pouvant être réutilisés pour plusieurs ensembles de données, éliminant le besoin de reformater manuellement. Par exemple, les rapports financiers ou les fiches d'inventaire nécessitent uniquement la mise à jour de la source de données, sans reconstruction du layout. Liaison de données automatisée, les marqueurs intelligents se lient directement aux sources de données (bases de données, JavaBeans, tableaux). Les changements dans les données sources se reflètent automatiquement dans le fichier Excel après traitement, réduisant les erreurs de copier-coller.

2. Support des structures de données complexes : Intégration multi-sources, un seul modèle peut fusionner des données provenant de diverses sources (variables, tableaux, ResultSets). Gestion de données hiérarchiques, les données imbriquées (ex : enregistrements groupés) peuvent être traitées avec des marqueurs comme &=subtotal9:Person.id pour générer des résumés (somme, moyennes) par groupe directement dans Excel.

3. Préservation des fonctionnalités Excel : Les marqueurs intelligents coexistent avec les fonctionnalités Excel telles que les formules, la mise en forme conditionnelle et les graphiques. Par exemple : les calculs dynamiques utilisant &==C{r}*D{r} appliquent des formules spécifiques à chaque ligne lors de l’injection des données. Les modèles conservent les styles prédéfinis (ex : en-têtes, couleurs de cellules), assurant la cohérence sans ajustements après importation.

4. Capacités avancées d'automatisation : Intégration de sources de données personnalisées, les développeurs peuvent implémenter des interfaces comme ICellsDataTable (en .NET) pour mapper des structures de données propriétaires aux marqueurs. Cette flexibilité permet d’intégrer des données en temps réel issues d’API ou capteurs. Traitement par lots, des outils comme WorkbookDesigner d’Aspose.Cells permettent des opérations en masse (ex : générer plus de 1000 factures en un seul passage) en parcourant des jeux de données.

5. Réduction des efforts de développement et de maintenance : Séparation de la logique et du design, les designers gèrent des modèles dans Excel (sans codage), tandis que les développeurs gèrent la logique de données. Cette division accélère les itérations. Réduction des erreurs, la cartographie automatique des données minimise les risques d’erreurs manuelles. Par exemple, les données de capteurs analysées en VC++ peuvent être automatiquement insérées dans des modèles Excel via des interfaces d’objets, évitant ainsi les erreurs de transcription.

## **Code exemple pour l'importation de DataTable avec des marqueurs intelligents**
Le code exemple suivant a une source de données contenant 6 enregistrements. Nous voulons n’en afficher que 3 dans une feuille de calcul, puis le reste sera automatiquement déplacé vers la seconde feuille. Notez que la seconde feuille doit également avoir la même balise de marqueur intelligent et vous devez appeler la méthode [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) pour les deux feuilles. Veuillez consulter le fichier Excel généré [SmartMarkerDataTableToExcel.xlsx](SmartMarkerDataTableToExcel.xlsx) pour référence.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **Exemple de code pour importer des données JSON avec des marqueurs intelligents**
Aspose.Cells for .NET prend en charge les données JSON dans les marqueurs intelligents. Le code exemple charge un modèle de tableau, importe intelligemment les données JSON pour le remplir, puis calcule les données du tableau. Veuillez vérifier [le fichier modèle](table.xlsx), [le fichier JSON](table.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier table.xlsx montrant les marqueurs intelligents.**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](tableresult.png)|

Données JSON comme suit :
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **Exemple de code pour importer des objets imbriqués avec des marqueurs intelligents**
Aspose.Cells prend en charge les objets imbriqués dans les marqueurs intelligents, les objets imbriqués doivent être simples. Nous utilisons un fichier de modèle simple. Consultez la feuille de calcul de conception qui contient quelques marqueurs intelligents imbriqués.

|**La première feuille de calcul du fichier SM_NestedObjects.xlsx montrant des marqueurs intelligents imbriqués.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
L'exemple suivant montre comment cela fonctionne.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Sujets avancés**
- [Paramètres du marqueur intelligent](/cells/fr/net/smart-marker-parameters/)
- [Ajouter un objet anonyme ou personnalisé dans les SmartMarkers](/cells/fr/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Remplir automatiquement les données de Smart Marker dans d'autres feuilles de calcul si les données sont trop nombreuses](/cells/fr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatage des Smart Markers](/cells/fr/net/formatting-smart-markers/)
- [Recevoir des notifications lors de la fusion de données avec des marqueurs intelligents](/cells/fr/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Définir une source de données personnalisée pour WorkbookDesigner](/cells/fr/net/set-custom-datasource-for-workbookdesigner/)
- [Afficher une apostrophe de tête dans les cellules](/cells/fr/net/show-leading-apostrophe-in-cells/)
- [Utilisation du paramètre de formule dans le champ Smart Marker](/cells/fr/net/using-formula-parameter-in-smart-marker-field/)
- [Importer intelligemment un élément de tableau par index dans Excel avec des marqueurs intelligents](/cells/fr/net/how-to-import-array-element-by-index-with-smart-markers/)
- [Importer intelligemment un élément de tableau par trancheur dans Excel avec des marqueurs intelligents](/cells/fr/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [Importer intelligemment un JSON dans Excel avec des marqueurs intelligents](/cells/fr/net/how-to-import-json-into-excel-with-smart-markers/)
- [Importer intelligemment des objets imbriqués dans Excel avec des marqueurs intelligents](/cells/fr/net/how-to-import-nested-objects-with-smart-markers/)
- [Importer intelligemment des tableaux variables dans Excel avec des marqueurs intelligents](/cells/fr/net/how-to-import-variable-arrays-with-smart-markers/)
- [Comment utiliser les marqueurs d’image dans les marqueurs intelligents](/cells/fr/net/how-to-use-image-markers-in-smart-markers/)
- [Comment regrouper des données dans les marqueurs intelligents](/cells/fr/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
