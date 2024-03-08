---
title: Comment ajouter un graphique croisé dynamique en utilisant Aspose.Cells
linktitle: Graphique croisé dynamique
type: docs
weight: 100
url: /fr/net/how-to-add-pivot-chart/
description: Comment ajouter un graphique croisé dynamique en utilisant Aspose.Cells.
keywords: PivotChart
---
##  Qu'est-ce qu'un graphique croisé dynamique

Un graphique croisé dynamique dans Excel est une représentation graphique de données créées à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les graphiques croisés dynamiques sont interactifs et peuvent être facilement modifiés pour afficher différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation des données dans Excel.

##  Comment ajouter un graphique croisé dynamique en utilisant Aspose.Cells

###  **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez des données aux cellules d’une feuille de calcul à l’aide de la méthode PutValue/setValue d’un objet Cell. Vous utilisez également un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Worksheet).
1. Accédez au nouvel objet PivotTable de la collection PivotTables en passant son index. # Utilisez l'un des objets de tableau croisé dynamique encapsulés dans l'objet PivotTable pour gérer le tableau.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Ajouter un graphique croisé dynamique**

Pour créer un graphique croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez le PivotSource du graphique pour faire référence à un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

