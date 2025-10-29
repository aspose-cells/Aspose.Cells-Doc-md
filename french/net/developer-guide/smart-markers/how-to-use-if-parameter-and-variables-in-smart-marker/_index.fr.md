---
title: Comment utiliser le paramètre if et les variables dans SmartMarkers
type: docs
weight: 10
url: /fr/net/how-to-use-if-parameter-and-Variables-in-smart-markers/
---

## **Pourquoi utiliser le paramètre if et les variables dans Smart Markers**
Les Smart Markers sont des outils puissants utilisés dans divers contextes. L'utilisation de paramètres et de variables au sein des Smart Markers améliore considérablement leur flexibilité, leur efficacité et leur fonctionnalité.

1. Manipulation dynamique des données et flexibilité : Les paramètres et variables permettent aux Smart Markers de gérer les données de manière dynamique, en s'adaptant aux entrées changeantes sans nécessiter d'ajustements manuels du modèle ou du code.
2. Contrôle du comportement et des opérations : Les paramètres affinent le comportement des Smart Markers, permettant des opérations telles que le regroupement, le tri, le sous-total et la mise en forme conditionnelle.
3. Support pour les structures de données complexes : Les variables permettent aux Smart Markers de travailler avec des sources de données complexes, y compris des tableaux, des objets et des données multidimensionnelles.
4. Efficacité et automatisation : Les paramètres et variables automatisent les tâches répétitives, réduisant l'effort manuel et les erreurs potentielles.
5. Logique conditionnelle et filtrage : Bien que limitées dans certains contextes, les paramètres et variables peuvent implémenter une logique conditionnelle.
6. Personnalisation et interaction utilisateur : Les variables permettent aux utilisateurs de personnaliser dynamiquement le comportement du Smart Marker.
7. Optimisation des performances : Les paramètres aident à optimiser les performances en contrôlant la façon dont les données sont traitées.


## **Comment utiliser le paramètre if et les variables dans SmartMarkers**
Parfois, vous devez ajouter une condition if dans les paramètres de variable dans SmartMarkers. Aspose.Cells permet d'utiliser le paramètre if et les variables dans SmartMarkers. Veuillez consulter [le fichier modèle](template.xlsx), [le fichier JSON](data.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier template.xlsx montrant les variables.**|
| :- |
|![todo:image_alt_text](variables.png)|

|**La deuxième feuille du fichier template.xlsx montrant les smart markers.**|
| :- |
|![todo:image_alt_text](template.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](result.png)|

Données JSON comme suit :
```json data
{
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
    "DOB": "2025-02-08",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111"
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-If-Parameter-And-Variables.cs" >}}

{{< app/cells/assistant language="csharp" >}}
