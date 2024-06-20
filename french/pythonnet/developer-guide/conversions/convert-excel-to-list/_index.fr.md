---
title: Convertir Excel en données Python
type: docs
weight: 30
url: /fr/python-net/convert-excel-to-list/
description: Convertir Excel en liste en utilisant Aspose.Cells pour l API Python via .NET.
keywords: Convertir Excel en dictionnaire en utilisant la bibliothèque Excel Python, Convertir le classeur en dictionnaire en utilisant la bibliothèque Excel Python, Convertir un objet de ligne en liste à l aide de la bibliothèque Excel Python, Comment convertir un objet ListObject en liste, Convertir un objet de colonne en liste en utilisant la bibliothèque Excel Python, Convertir une plage en liste en utilisant la bibliothèque Excel Python, Convertir une feuille de calcul en liste en utilisant la bibliothèque Excel Python.
---

{{% alert color="primary" %}}

En utilisant Aspose.Cells pour l'API Python via .NET, vous pouvez convertir un classeur, une feuille de calcul, une plage, une ligne, une colonne et d'autres données Excel en liste Python.

{{% /alert %}}

## **Comment convertir un classeur Excel en dictionnaire**
Voici un extrait de code d'exemple pour démontrer comment exporter des données Excel en dictionnaire en utilisant Aspose.Cells pour Python via .NET :
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Parcourir toutes les feuilles de calcul et convertir le classeur en dictionnaire en utilisant la bibliothèque Excel Python d'Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

Le résultat en sortie :
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Comment convertir un classeur Excel en liste**
Voici un extrait de code d'exemple pour démontrer comment exporter des données Excel en liste en utilisant Aspose.Cells pour Python via .NET :
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Parcourir toutes les feuilles de calcul et convertir le classeur en liste en utilisant la bibliothèque Excel Python d'Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

Le résultat en sortie :
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Comment convertir une feuille de calcul en liste**
Voici un extrait de code d'exemple pour démontrer comment exporter des données de feuille de calcul en liste en utilisant Aspose.Cells pour Python via .NET :
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Convertir les données de la feuille de calcul en liste en utilisant la bibliothèque Excel Aspose.Cells pour Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

Le résultat en sortie :
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Comment convertir un objet ListObject d'Excel en liste**
Voici un exemple de code pour démontrer comment exporter les données ListObject en liste en utilisant Aspose.Cells pour la bibliothèque Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Créer un objet ListObject.
1. Convertir les données de l'objet ListObject en liste en utilisant la bibliothèque Excel Aspose.Cells pour Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

Le résultat en sortie :
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Comment convertir une ligne d'Excel en liste**
Voici un exemple de code pour démontrer comment exporter les données de ligne en liste en utilisant Aspose.Cells pour la bibliothèque Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Obtenir un objet Row par indice de ligne.
1. Convertir les données de la ligne en liste en utilisant la bibliothèque Excel Aspose.Cells pour Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

Le résultat en sortie :
```
['Detroit', 'Central', 3074]
```

## **Comment convertir une colonne d'Excel en liste**
Voici un exemple de code pour démontrer comment exporter les données de colonne en liste en utilisant Aspose.Cells pour la bibliothèque Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Obtenir un objet Column par indice de colonne.
1. Convertissez les données de colonne en liste en utilisant la bibliothèque Excel Aspose.Cells for Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

Le résultat en sortie :
```
['Store', 3055, 3036, 3074]
```

## **Comment convertir une plage d'Excel en liste**
Voici un extrait de code d'exemple pour démontrer comment exporter des données de plage en liste en utilisant Aspose.Cells pour Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Créer la plage.
1. Convertissez les données de plage en liste en utilisant la bibliothèque Excel Aspose.Cells pour Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

Le résultat en sortie :
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
