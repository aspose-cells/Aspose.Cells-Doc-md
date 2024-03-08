---
title: Comment ajouter un graphique croisé dynamique en utilisant Aspose.Cells
linktitle: Graphique croisé dynamique
type: docs
weight: 100
url: /fr/java/how-to-add-pivot-chart/
description: Comment ajouter un graphique croisé dynamique en utilisant Aspose.Cells.
keywords: PivotChart
---
##  Qu'est-ce qu'un graphique croisé dynamique

Un graphique croisé dynamique dans Excel est une représentation graphique de données créées à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les graphiques croisés dynamiques sont interactifs et peuvent être facilement modifiés pour afficher différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation des données dans Excel.

##  Comment ajouter un graphique croisé dynamique en utilisant Aspose.Cells
###  **Créer un tableau croisé dynamique**

Pour créer un tableau croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez des données aux cellules d’une feuille de calcul à l’aide de la méthode PutValue/setValue d’un objet Cell. Vous utilisez également un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Worksheet).
1. Accédez au nouvel objet PivotTable de la collection PivotTables en passant son index.
1. Utilisez l’un des objets de tableau croisé dynamique encapsulés dans l’objet PivotTable pour gérer le tableau.

Un exemple de code est donné ci-dessous. L'exécution du code génère un nouveau fichier : pivotTable_test.xls.

**Des données d'entrée** 

![tâche : image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Le tableau croisé dynamique de sortie**

![tâche : image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **Création d'un graphique croisé dynamique basé sur le tableau croisé dynamique**

Pour créer un tableau croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez le PivotSource du graphique pour faire référence à un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

Vous trouverez ci-dessous le code utilisé par le composant pour accomplir la tâche. L'exécution du code génère un nouveau fichier : pivotChart_test.xls.

**La feuille du tableau croisé dynamique**

![tâche : image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Cet article montre comment créer des tableaux croisés dynamiques et des graphiques croisés dynamiques à l'aide de Aspose.Cells. Espérons qu'il vous aidera à utiliser ces fonctionnalités dans vos propres scénarios.

Aspose.Cells a bénéficié d'années de recherche, de conception et de réglages minutieux.

 Nous apprécions vos questions, commentaires et suggestions à[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
