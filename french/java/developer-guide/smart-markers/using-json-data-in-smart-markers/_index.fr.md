---
title: Utilisation des données JSON dans les marqueurs intelligents
type: docs
weight: 30
url: /fr/java/using-json-data-in-smart-markers/
---

## **Pourquoi utiliser les données JSON dans les marqueurs intelligents**
Pourquoi utiliser les données JSON comme données d'origine pour les marqueurs intelligents ?
JSON (JavaScript Object Notation) est un format léger d'échange de données lisible par l'humain, idéal pour structurer des données hiérarchiques. Voici pourquoi il est bien adapté comme données d'origine pour les marqueurs intelligents (espaces réservés dynamiques qui se remplissent automatiquement dans les tableurs, documents ou tableaux de bord) :

1. Support des données structurées et hiérarchiques
JSON supporte nativement des objets imbriqués et des tableaux (par exemple, { "utilisateur": { "nom": "Alice", "commandes": [ ... ] } }). Les marqueurs intelligents peuvent parcourir cette hiérarchie (par exemple, {{utilisateur.commandes[0].prix}}), facilitant la cartographie de données complexes vers des modèles.

2. Indépendant du langage et de la plateforme
Des analyseurs JSON existent dans presque tous les langages de programmation (Python, JavaScript, Java, etc.). Des outils comme Power Query d’Excel, Google Apps Script ou des plateformes sans code (par exemple Airtable) ingèrent pleinement le JSON.

3. Compatible avec les API
La plupart des API modernes (par exemple REST, GraphQL) renvoient des données au format JSON. Les marqueurs intelligents peuvent consommer directement des JSON en direct provenant de services web, permettant des mises à jour en temps réel (par exemple, prix boursiers, météo).

4. Lisible par l’humain et facile à déboguer
La structure en texte brut du JSON est facile à : Valider (par exemple, avec JSONLint). Modifier manuellement ou via des scripts. Déboguer lors de la cartographie des données vers des marqueurs.

5. Extensibilité et flexibilité
Ajouter/supprimer des champs dans le JSON sans casser les marqueurs intelligents existants (si les champs optionnels sont gérés avec souplesse). Supporte divers types de données : chaînes, nombres, booléens, tableaux et objets.

6. Compatibilité avec l'écosystème
Fonctionne avec des outils de données modernes : Bases de données : MongoDB, PostgreSQL (JSONB), etc. Outils d'automatisation : Zapier, Integromat. Pipelines de données : Apache NiFi, Talend.

## **Utilisation du modèle imbriqué Excel avec des données JSON**
Aspose.Cells for Java supporte les données JSON dans les marqueurs intelligents, les données JSON peuvent être hiérarchiquement imbriquées. Veuillez consulter le [fichier modèle](smartmarker.xlsx), le [fichier JSON](smartmarker.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier smartmarker.xlsx montrant les marqueurs intelligents.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Données JSON comme suit :
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **Utilisation du modèle de sous-totaux Excel avec des données JSON**
Aspose.Cells for Java supporte les données JSON dans les marqueurs intelligents, les données JSON peuvent être hiérarchiquement imbriquées. Des sous-totaux ont été utilisés pour la statistique des données dans le modèle Excel. Veuillez consulter le [fichier modèle](jsonExcelTemplate.xlsx), le [fichier JSON](jsonData.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille de calcul du fichier jsonExcelTemplate.xlsx affichant des marqueurs intelligents.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Données JSON comme suit :
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
