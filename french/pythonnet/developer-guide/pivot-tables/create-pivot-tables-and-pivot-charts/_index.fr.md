---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 20
url: /fr/python-net/create-pivot-tables-and-pivot-charts/
description: Comment ajouter des tableaux croisés dynamiques et des graphiques croisés dynamiques avec Aspose.Cells for Python via .NET.
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste dans une feuille de calcul. Un tableau croisé dynamique permet de totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réorganiser rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un tableau croisé dynamique est une représentation graphique interactive des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique facilite encore plus la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

 Aspose.Cells for Python via .NET prend en charge[tableaux croisés dynamiques](/cells/fr/python-net/create-pivot-tables-and-pivot-charts/) et[tableaux croisés dynamiques](/cells/fr/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **Ajout de tableaux croisés dynamiques et de graphiques**

Aspose.Cells for Python via .NET fournit un ensemble spécial de classes utilisées pour créer des tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir des objets PivotTable, qui agissent comme les éléments de base d'un objet PivotTable :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- PivotTable, un rapport de tableau croisé dynamique sur une feuille de calcul.
- PivotTables, une collection de tous les objets PivotTable de la feuille de calcul.

###  **Préparation à l'utilisation Aspose.Cells for Python via .NET**
1.  Installez Aspose.Cells for Python via .NET à partir de[Pypi](https://pypi.org/project/aspose-cells-python/)utilisez la commande comme : $ pip install aspose-cells-python.
1. Vous pouvez également suivre les instructions étape par étape pour installer « Aspose.Cells for Python via .NET » dans votre environnement de développeur.


###  **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells for Python via .NET :

1. Ajoutez des données aux cellules d'une feuille de calcul à l'aide de la méthode put_value d'un objet Cell. Vous utilisez également un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Worksheet).
1. Accédez au nouvel objet PivotTable de la collection PivotTables en passant son index. # Utilisez l'un des objets de tableau croisé dynamique encapsulés dans l'objet PivotTable pour gérer le tableau.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **Ajouter un graphique croisé dynamique**

Pour créer un graphique croisé dynamique en utilisant Aspose.Cells for Python via .NET :

1. Ajoutez un graphique.
1. Définissez le PivotSource du graphique pour faire référence à un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

