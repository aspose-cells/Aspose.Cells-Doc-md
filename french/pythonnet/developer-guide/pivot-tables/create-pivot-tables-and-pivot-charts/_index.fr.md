---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 20
url: /fr/python-net/create-pivot-tables-and-pivot-charts/
description: Comment ajouter des tableaux croisés dynamiques et des graphiques croisés dynamiques avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells pour Python Excel, bibliothèque Excel Python, Ajouter des tableaux croisés dynamiques et des graphiques croisés dynamiques à l aide de la bibliothèque Excel Aspose.Cells pour Python.
---

{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste dans une feuille de calcul. Un tableau croisé dynamique peut totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réarranger rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un graphique croisé dynamique est une représentation graphique interactive des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique rend encore plus facile la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

Aspose.Cells pour Python via .NET prend en charge les [tableaux croisés dynamiques](/cells/fr/python-net/create-pivot-tables-and-pivot-charts/) et les [graphiques croisés dynamiques](/cells/fr/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Ajouter des tableaux croisés dynamiques et des graphiques à l'aide de la bibliothèque Excel Aspose.Cells pour Python**

Aspose.Cells pour Python via .NET fournit un ensemble spécial de classes utilisées pour créer des tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir des objets PivotTable, qui agissent comme éléments de base des objets PivotTable :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- PivotTable, un rapport de tableau croisé dynamique sur une feuille de calcul.
- PivotTables, une collection de tous les objets PivotTable sur la feuille de calcul.

### **Préparez-vous à utiliser Aspose.Cells pour Python via .NET**
1. Installez Aspose.Cells for Python via .NET depuis [pypi](https://pypi.org/project/aspose-cells-python/), utilisez la commande suivante : $ pip install aspose-cells-python.
1. Vous pouvez également suivre les instructions étape par étape sur la façon d'installer "Aspose.Cells for Python via .NET" dans votre environnement de développement.


### **Comment ajouter une table pivotante à l'aide de la bibliothèque Excel Aspose.Cells for Python**

Pour créer une table pivotante à l'aide de Aspose.Cells for Python via .NET :

1. Ajoutez des données à des cellules de feuille de calcul en utilisant la méthode put_value d'un objet Cell. Vous pouvez également utiliser un fichier de modèle déjà rempli de données. Les données seront utilisées comme source de données de la table pivotante.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable depuis la collection PivotTables en passant son index. # Utilisez l'un des objets table pivotante encapsulés dans l'objet PivotTable pour gérer la table.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Comment ajouter un graphique pivotant à l'aide de la bibliothèque Excel Aspose.Cells for Python**

Pour créer un graphique pivotant à l'aide de Aspose.Cells for Python via .NET :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
