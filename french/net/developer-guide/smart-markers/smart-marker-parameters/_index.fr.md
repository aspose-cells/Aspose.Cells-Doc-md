---
title: Paramètres du Smart Marker
type: docs
weight: 30
url: /fr/net/smart-marker-parameters/
---

## **Feuille de calcul du Concepteur & Marqueurs intelligents**
Les feuilles de calcul du concepteur sont des fichiers Excel standard contenant un formatage visuel, des formules et des marqueurs intelligents. Elles peuvent contenir des marqueurs intelligents qui font référence à une ou plusieurs sources de données, telles que des informations d'un projet et des informations pour des contacts associés. Les marqueurs intelligents sont écrits dans les cellules où vous souhaitez afficher les informations.

Tous les marqueurs intelligents commencent par &=. Un exemple de marqueur de données est &=Party.FullName. Si le marqueur de données donne lieu à plusieurs éléments, par exemple une ligne complète, alors les lignes suivantes sont automatiquement déplacées vers le bas pour faire de la place pour les nouvelles informations. Ainsi, les sous-totaux et les totaux peuvent être placés sur la ligne immédiatement après le marqueur de données pour effectuer des calculs basés sur les données insérées. Pour effectuer des calculs sur les lignes insérées, utilisez des **formules dynamiques**.

Les marqueurs intelligents se composent des parties **source de données** et **nom de champ** pour la plupart des informations. Des informations spéciales peuvent également être transmises avec des variables et des tableaux de variables. Les variables remplissent toujours une seule cellule tandis que les tableaux de variables peuvent en remplir plusieurs. Utilisez un seul marqueur de données par cellule. Les marqueurs intelligents inutilisés sont supprimés.

Le marqueur intelligent peut également contenir des paramètres. Les paramètres vous permettent de modifier comment les informations sont disposées. Ils sont ajoutés à la fin du marqueur intelligent entre parenthèses sous forme d'une liste séparée par des virgules.

## **Options de marqueur intelligent**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Paramètres du Smart Marker**
Les paramètres suivants sont autorisés :

- **noadd** - Ne pas ajouter de lignes supplémentaires pour s'adapter aux données.
- **skip:n** - Ignorer n lignes pour chaque ligne de données.
- **ascending:n** ou **descending:n** - Trier les données dans les marqueurs intelligents. Si n est 1, alors la colonne est la première clé du trieur. Les données sont triées après le traitement de la source de données. Par exemple : &=Table1.Field3(ascending:1).
- **horizontal** - Écrire les données de gauche à droite, au lieu du haut en bas.
- **numérique** - Convertir le texte en nombre si possible.
- **décaler** - Décaler vers le bas ou vers la droite, en créant des lignes ou des colonnes supplémentaires pour s'adapter aux données. Le paramètre de décalage fonctionne de la même manière que dans Microsoft Excel. Par exemple, dans Microsoft Excel, lorsque vous sélectionnez une plage de cellules, faites un clic droit et sélectionnez **Insérer** et spécifiez **décaler les cellules vers le bas**, **décaler les cellules vers la droite** et d'autres options. En bref, le paramètre **décaler** remplit la même fonction pour les marqueurs intelligents verticaux/normaux (haut en bas) ou horizontaux (gauche à droite).
- **copierstyle** - Copier le style de la cellule de base dans toutes les cellules de cette colonne.

Les paramètres noadd et skip peuvent être combinés pour insérer des données sur des lignes alternées. Étant donné que le modèle est traité de bas en haut, vous devriez ajouter noadd sur la première ligne pour éviter que des lignes supplémentaires ne soient insérées avant la ligne alternative.

Si vous avez plusieurs paramètres, séparez-les par des virgules, mais sans espace : paramètreA, paramètreB, paramètreC

Les captures d'écran suivantes montrent comment insérer des données sur chaque autre ligne.

|**Fichier modèle**|**Fichier de sortie**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **Formules dynamiques**
Les formules dynamiques vous permettent d'insérer des formules Excel dans des cellules même lorsque la formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Les formules dynamiques peuvent se répéter pour chaque ligne insérée ou utiliser uniquement la cellule où le marqueur de données est placé.

Les formules dynamiques permettent les options supplémentaires suivantes :

- r - Numéro de ligne actuelle.
- 2, -1 - Décalage par rapport au numéro de ligne actuelle.

Par exemple:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Dans le marqueur de formule dynamique, "-1" désigne le décalage par rapport à la ligne actuelle dans les colonnes B et C respectivement, qui sera défini pour l'opération de division, le paramètre de saut est d'une ligne. De plus, nous devons spécifier le caractère suivant:

{{< highlight java >}}

 "~"

{{< /highlight >}}

comme caractère de séparateur pour appliquer d'autres paramètres dans les formules dynamiques.

Les captures d'écran suivantes illustrent une formule dynamique répétitive et la feuille de calcul Excel résultante.

|**Fichier Modèle**|**Fichier de Sortie**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
La cellule "C1" contient la formule **= A1*B1**, la cellule "C2" contient **= A2*B2** et la cellule "C3" contient **= A3*B3**.

Il est très facile de traiter les marqueurs intelligents. L'exemple de code suivant montre comment utiliser des formules dynamiques dans les marqueurs intelligents. Nous chargeons le [fichier modèle](templateDynamicFormulas.xlsx) et créons des données de test, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Comment utiliser les formules dynamiques et les variables dans SmartMarkers**
Parfois, vous devez utiliser des formules dynamiques et des variables dans SmartMarkers. Pour les formules dynamiques, ajoutez le caractère spécial (~) comme séparateur. Aspose.Cells permet d'utiliser des formules dynamiques et des variables dans SmartMarkers. Veuillez consulter le [fichier de modèle](template.xlsx), le [fichier JSON](employees-data.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier template.xlsx montrant les variables.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**La deuxième feuille du fichier template.xlsx montrant les smart markers.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](template_result.png)|

Données JSON comme suit :
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
