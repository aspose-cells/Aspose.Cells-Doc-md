---
title: Ajuster les lignes pour les cellules fusionnées
type: docs
weight: 120
url: /fr/python-net/autofit-rows-for-merged-cells/
description: Cet article montre comment ajuster automatiquement les lignes pour les cellules fusionnées via l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Comment utiliser AutoFitMergedCellsType pour ajuster automatiquement les lignes, Ajuster automatiquement les lignes pour les cellules fusionnées en Python.
---

{{% alert color="primary" %}}

Microsoft Excel fournit une fonctionnalité qui vous permet de redimensionner automatiquement la hauteur d'une cellule en fonction de son contenu. La fonctionnalité s'appelle ajustement automatique des lignes. Microsoft Excel ne définit pas automatiquement l'opération d'ajustement automatique sur les cellules fusionnées nativement. Parfois, la fonctionnalité devient vitale pour un utilisateur qui doit vraiment implémenter l'ajustement automatique des lignes sur les cellules fusionnées également.

{{% /alert %}}

## **Comment utiliser AutoFitMergedCellsType pour ajuster automatiquement les lignes**
Aspose.Cells pour Python via .NET prend en charge cette fonctionnalité via l'API [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/). En utilisant cette API, il est possible d'ajuster automatiquement les lignes dans une feuille de calcul, y compris pour les cellules fusionnées. Voici une liste de tous les types possibles d'ajustement automatique des cellules fusionnées :

- NONE
- PREMIÈRE_LIGNE
- DERNIÈRE_LIGNE
- CHAQUE_LIGNE

## **Ajustement automatique des lignes pour les cellules fusionnées**

Veuillez consulter le code suivant, il crée un objet classeur et ajoute plusieurs feuilles de calcul. Utilisez différentes méthodes pour les opérations d'ajustement automatique dans chaque feuille de calcul. La capture d'écran montre les résultats après l'exécution du code d'exemple.

<br>
<img src="result.png" width=80% />

## **Code d'exemple C#**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
