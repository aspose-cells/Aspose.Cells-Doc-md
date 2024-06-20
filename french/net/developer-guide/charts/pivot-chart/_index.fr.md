---
title: Comment ajouter un tableau croisé dynamique à l aide d Aspose.Cells
linktitle: Tableau croisé dynamique
type: docs
weight: 100
url: /fr/net/how-to-add-pivot-chart/
description: Comment ajouter un tableau croisé dynamique à l aide d Aspose.Cells.
keywords: Tableau croisé dynamique
---
## Qu'est-ce qu'un tableau croisé dynamique

Un tableau croisé dynamique dans Excel est une représentation graphique des données créée à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les tableaux croisés dynamiques sont interactifs et peuvent être facilement modifiés pour montrer différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation de données dans Excel.

## Comment ajouter un tableau croisé dynamique à l'aide d'Aspose.Cells

### **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données à une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable depuis la collection PivotTables en passant son index. # Utilisez l'un des objets table pivotante encapsulés dans l'objet PivotTable pour gérer la table.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Ajout d'un graphique croisé dynamique**

Pour créer un graphique croisé dynamique en utilisant Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

