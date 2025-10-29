---
title: Importation intelligente des données maître et détail dans Excel avec des marqueurs intelligents
type: docs
weight: 30
url: /fr/net/how-to-use-master-and-details-with-smart-markers/
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez générer des rapports Excel dynamiques, comprenant un tableau de bord principal complet et plusieurs feuilles détaillées à grains fins. Parmi eux, une table principale présente un aperçu, qui peut montrer différentes variantes de produits, et chaque feuille détaillée correspondante fournit des données spécifiques et approfondies pour une seule variante. Aspose.Cells peut parfaitement répondre à vos besoins via maître et détails avec des marqueurs intelligents.


## **Paramètres du marqueur intelligent pour maître et détails**
Pour importer des données maître et détail dans Excel, vous devez utiliser les paramètres du marqueur intelligent suivants :

| Paramètre | Description | Valeurs Acceptables (Syntaxe) | Restrictions | Optionnalité | Comportement Par Défaut | Contraintes Excel |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | Spécifier le nom de la feuille de détail stockée dans le fichier modèle. | Valeur de chaîne | La valeur doit être nulle ou le nom de la feuille. Si null, c'est une feuille de détails. Cela doit être une valeur de chaîne simple. La variable n'est pas prise en charge. | Si omis, pas une feuille maître ou de détail. | Feuille de calcul normale, ni feuille maître ni feuille de détail. | |
| `DetailTable` | Spécifier le nom de la table de la feuille de détail dans le fichier modèle. | Valeur de chaîne | | Si omis, le marqueur intelligent dans la feuille de détail doit être similaire à la feuille maître, sinon nous ne pouvons pas trouver la source de données. | Si omis, le marqueur intelligent de la feuille de détail doit être similaire à celui de la feuille maître, sinon nous ne pouvons pas trouver la source de données. | |
| `DetailSheetNewName` | Spécifier le nom de la nouvelle feuille de détail créée. | Expression de type formule Excel | Cela doit être une formule valide pour Excel si nous remplaçons la variable ({a.bc}) par une valeur simple. | Si omis, de nouvelles feuilles seront Sheet1, Sheet2... | Si omis, de nouvelles feuilles seront Sheet1, Sheet2... | Le nom doit être un nom valide de feuille de calcul. |
| `DetailLink` | Indiquer si ajouter des hyperliens vers l'emplacement des données importées. | | | Si omis, ne pas ajouter d'hyperliens vers l'emplacement des données importées. | Si omis, ne pas ajouter d'hyperliens vers l'emplacement des données importées. | |

## **Comment utiliser maître et détails lorsque maître et détails dans une seule feuille de calcul**
Parfois, vous avez besoin d'importer des données maître et détail dans Excel dans SmartMarkers. Aspose.Cells permet d'utiliser les paramètres maître et détails dans SmartMarkers. Veuillez vérifier [fichier modèle](MasterDetailInOneSheet.xlsx), [fichier JSON](MasterDetailData.json) et la capture d'écran du fichier Excel de sortie généré avec le code suivant.

|**La première feuille du fichier modèle.xlsx.**|
| :- |
|![todo:image_alt_text](1.png)|

|**La première feuille du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](2.png)|

|**La deuxième feuille du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](3.png)|

Données JSON comme suit :
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **Comment utiliser maître et détails lorsque maître et détails dans des feuilles différentes**
Parfois, vous avez besoin d'importer des données maître et détail dans Excel dans SmartMarkers. Aspose.Cells permet d'utiliser les paramètres maître et détails dans SmartMarkers. Veuillez vérifier [fichier modèle](MasterDetailInTwoSheets.xlsx), [fichier JSON](MasterDetailData.json) et la capture d'écran du fichier Excel de sortie généré avec le code suivant.

|**La première feuille maître du fichier template.xlsx.**|
| :- |
|![todo:image_alt_text](4.png)|

|**La deuxième feuille maître du fichier template.xlsx.**|
| :- |
|![todo:image_alt_text](5.png)|

|**La feuille de détails du fichier template.xlsx.**|
| :- |
|![todo:image_alt_text](6.png)|

|**La première feuille maître du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](7.png)|

|**La deuxième feuille maître du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](8.png)|

|**La feuille de détails de la première feuille maître dans le fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](9.png)|

|**La première feuille de détails de la deuxième feuille maître dans le fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](10.png)|

|**La deuxième feuille de détails de la deuxième feuille maître dans le fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](11.png)|

Données JSON comme suit :
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
