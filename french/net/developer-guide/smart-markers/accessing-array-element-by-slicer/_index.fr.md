---
title: Importation intelligente d un élément de tableau par slicer dans Excel avec des marqueurs intelligents
type: docs
weight: 30
url: /fr/net/how-to-import-array-element-by-slicer-with-smart-markers/
---

## **Pourquoi accéder à un élément de tableau par slicer**
Dans les marqueurs intelligents de FastReport, accéder aux éléments du tableau en utilisant un slicer (par exemple, [array[1..3]]) fournit un moyen concis et efficace de travailler avec des sous-ensembles de données.

1. Extraction de données simplifiée : Parcourir manuellement de grands tableaux nécessite des boucles et une syntaxe complexe. Les slicers vous permettent d'extraire des plages (sous-tableaux) en une ligne. Exemple : [Produits[1..5].Nom] récupère les noms des 5 premiers produits.
2. Rapport dynamique : Générer des rapports pour des portions de données variables (par exemple, "Top N éléments", vues paginées). Exemple : [Ventes[0..{PageNo*10}]] charge dynamiquement des morceaux de données pour des rapports multipages.
3. Optimisation des performances : Éviter de charger l'ensemble des tableaux en mémoire. Récupérer uniquement les éléments nécessaires. Exemple : [Logs[^10..^1]] récupère efficacement les 10 dernières entrées.
4. Syntaxe déclarative : Exprimer l'intention directement dans les marqueurs de template. Exemple : [Employés[3..7].Département] sélectionne clairement les départements des entrées 3 à 7.
5. Intégration avec les sources de données : Fonctionne avec des tableaux provenant de bases de données, JSON ou code. Exemple : Lier Invoice.Items[0..2] pour afficher les 3 premières lignes.
6. Les trancheurs dans Smart Markers réduisent la complexité du code, améliorent la lisibilité et optimisent la gestion des données pour les sous-ensembles de tableaux. Utilisez-les lorsque vous avez besoin d'un accès rapide basé sur une plage — idéal pour la pagination, les listes top-N ou les vues de données en fenêtre. 

## **Comment importer un élément du tableau par trancheur dans Excel avec Smart Markers**
Aspose.Cells supporte l'accès à un élément du tableau par trancheur dans les smart markers. Veuillez consulter [le fichier modèle](ElementBySlicer.xlsx), [le fichier JSON](ElementBySlicer.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier smartmarker.xlsx montrant les marqueurs intelligents.**|
| :- |
|![todo:image_alt_text](ElementBySlicer1.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](ElementBySlicer2.png)|

Données JSON comme suit :
```json data
{
  "EntityCin": "EntityCin Test",
  "EntityName": "EntityName Test",
  "FirstName": "FirstName Test",
  "MiddleName": "MiddleName Test",
  "LastName": "LastName Test",
  "DOB": "2025-02-08",
  "SSN": "11111111",
  "Directors": [
    {
      "id": "director id 1",
      "FirstName": "director first 1",
      "MiddleName": "director middle 1",
      "LastName": "director last 1",
      "Reportees": [
        {
          "id": "aaa",
          "FirstName": "first aaa",
          "MiddleName": "middle aaa",
          "LastName": "last aaa",
          "Department": "aaa department",
          "City": "aaa city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "bbb",
          "FirstName": "first bbb",
          "MiddleName": "middle bbb",
          "LastName": "last bbb",
          "Department": "bbb department",
          "City": "bbb city",
          "GST": "Yes",
          "ITR": "Yes"
        },
        {
          "id": "ccc",
          "FirstName": "first ccc",
          "MiddleName": "middle ccc",
          "LastName": "last ccc",
          "Department": "ccc department",
          "City": "ccc city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 2",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee",
          "FirstName": "first eee",
          "MiddleName": "middle eee",
          "LastName": "last eee",
          "Department": "eee department",
          "City": "eee city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff",
          "FirstName": "first fff",
          "MiddleName": "middle fff",
          "LastName": "last fff",
          "Department": "fff department",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 3",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee3",
          "FirstName": "first eee3",
          "MiddleName": "middle eee3",
          "LastName": "last eee3",
          "Department": "eee department3",
          "City": "eee city3",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff3",
          "FirstName": "first fff3",
          "MiddleName": "middle fff3",
          "LastName": "last fff3",
          "Department": "fff department3",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 4",
      "FirstName": "director first 4",
      "MiddleName": "director middle 4",
      "LastName": "director last 4",
      "Reportees": [
        {
          "id": "eee4",
          "FirstName": "first eee4",
          "MiddleName": "middle eee4",
          "LastName": "last eee4",
          "Department": "eee department4",
          "City": "eee city4",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff4",
          "FirstName": "first fff4",
          "MiddleName": "middle fff4",
          "LastName": "last fff4",
          "Department": "fff department4",
          "City": "fff city4",
          "GST": "No",
          "ITR": "No"
        }
      ]
    }
  ]
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-AccessElementBySlicer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
