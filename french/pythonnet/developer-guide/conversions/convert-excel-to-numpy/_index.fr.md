---
title: Convertir Excel en NumPy
type: docs
weight: 30
url: /fr/python-net/convert-excel-to-numpy/
description: Convertir Excel en NumPy en utilisant l API Aspose.Cells for Python via .NET.
keywords: Python Convertir Excel en tableau NumPy, Exporter le classeur en tableau NumPy en Python via NET, Python Convertir Ligne en tableau NumPy, Python Convertir Tableau en tableau NumPy, Exporter ListObject en tableau NumPy en Python via NET, Python Convertir Plage en tableau NumPy, Colonne en tableau NumPy en utilisant Python.
---

## **Introduction à NumPy**
NumPy (Numerical Python) est une extension de calcul numérique open-source de Python. Cet outil peut être utilisé pour stocker et traiter de grandes matrices, ce qui est beaucoup plus efficace que la structure de listes imbriquées de Python (qui peut également être utilisée pour représenter des matrices). Il prend en charge un grand nombre de tableaux dimensionnels et d'opérations matricielles, et fournit également un grand nombre de bibliothèques de fonctions mathématiques pour les opérations sur les tableaux. 

Les principales fonctions de NumPy :
1. Ndarray, un objet de tableau multidimensionnel, est une structure de données rapide, flexible et économique en espace.
1. Opérations d'algèbre linéaire, y compris la multiplication de matrices, la transposition, l'inversion, etc.
1. Transformation de Fourier, effectuant une transformation de Fourier rapide sur un tableau.
1. Opération rapide des tableaux à virgule flottante.
1. Intégrer du code en langage C dans Python pour le faire fonctionner plus rapidement.

En utilisant l'API Aspose.Cells pour Python via .NET, vous pouvez convertir des fichiers Excel, TSV, CSV, Json et de nombreux autres formats en tableau Numpy.

## **Comment convertir un classeur Excel en tableau Numpy**
Voici un exemple de code pour montrer comment exporter des données Excel vers un tableau NumPy en utilisant Aspose.Cells pour Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Parcourir les données Excel et exporter les données en tableau Numpy en utilisant Aspose.Cells pour Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

Le résultat en sortie :
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Comment convertir une feuille de calcul en tableau Numpy**
Voici un exemple de code pour montrer comment exporter des données de feuille de calcul en tableau Numpy en utilisant Aspose.Cells pour Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Convertir les données de la feuille de calcul en tableau Numpy en utilisant la bibliothèque Excel Aspose.Cells pour Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

Le résultat en sortie :
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Comment convertir une plage d'Excel en tableau Numpy**
Voici un exemple de code pour montrer comment exporter des données de plage en tableau Numpy en utilisant Aspose.Cells pour Python via .NET:
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Créer la plage.
1. Convertir les données de la plage en tableau Numpy en utilisant la bibliothèque Excel Aspose.Cells pour Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

Le résultat en sortie :
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Comment convertir un ListObject d'Excel en NumPy ndarray**
Voici un exemple de code pour démontrer comment exporter les données ListObject vers un NumPy ndarray en utilisant Aspose.Cells pour Python via .NET :
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Créer un objet ListObject.
1. Convertir les données ListObject en NumPy ndarray en utilisant la bibliothèque Aspose.Cells pour Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

Le résultat en sortie :
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Comment convertir une ligne d'Excel en NumPy ndarray**
Voici un exemple de code pour démontrer comment exporter les données de ligne vers un NumPy ndarray en utilisant Aspose.Cells pour Python via .NET :
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Obtenir un objet Row par indice de ligne.
1. Convertir les données de la ligne en NumPy ndarray en utilisant la bibliothèque Aspose.Cells pour Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

Le résultat en sortie :
```
['Detroit' 'Central' '3074']
```

## **Comment convertir une colonne d'Excel en NumPy ndarray**
Voici un exemple de code pour démontrer comment exporter les données de colonne vers un NumPy ndarray en utilisant Aspose.Cells pour Python via .NET :
1. Charger le [fichier d'exemple](sample_data.xlsx).
1. Obtenir la première feuille de calcul.
1. Obtenir un objet Column par indice de colonne.
1. Convertir les données de la colonne en NumPy ndarray en utilisant la bibliothèque Aspose.Cells pour Python Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

Le résultat en sortie :
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
