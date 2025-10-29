---
title: Importation intelligente de tableaux variables dans Excel avec des marqueurs intelligents
type: docs
weight: 30
url: /fr/net/how-to-import-variable-arrays-with-smart-markers/
---

## **Pourquoi utiliser des tableaux variables pour les marqueurs intelligents**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. Répétition dynamique sans codage fixe : les marqueurs statiques échouent pour les données de longueur variable (par exemple, items de commande, permissions utilisateur). Les tableaux s'itèrent dynamiquement. 
2. Agrégation simplifiée : calculez les sommes, moyennes ou filtres directement. Évitez la logique manuelle en JavaScript/C# dans les modèles.
3. Représentation des données sous forme de tableau/liste : adaptée : tables, grilles et listes se cartographient naturellement vers des tableaux.
4. Efficacité mémoire : les tableaux réduisent la complexité des modèles et la surcharge de liaison de données.
5. Intégration avec API/sources de données : s'aligne avec des données centrées sur JSON/array (par exemple, API REST).

## **Comment importer des tableaux variables avec des marqueurs intelligents**
L'exemple de code suivant montre comment utiliser des tableaux de variables dans les marqueurs intelligents. Nous plaçons un marqueur de tableau de variables dans la cellule A1 de la première feuille de travail du classeur de manière dynamique, qui contient une chaîne de valeurs que nous définissons pour le marqueur, traitons les marqueurs pour remplir les données dans les cellules par rapport au marqueur. Enfin, nous enregistrons le fichier Excel.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **Comment importer une propriété HTML avec des marqueurs intelligents**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
