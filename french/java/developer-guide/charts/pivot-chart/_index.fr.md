---
title: Comment ajouter un tableau croisé dynamique à l aide d Aspose.Cells
linktitle: Tableau croisé dynamique
type: docs
weight: 100
url: /fr/java/how-to-add-pivot-chart/
description: Comment ajouter un tableau croisé dynamique à l aide d Aspose.Cells.
keywords: Tableau croisé dynamique
---
## Qu'est-ce qu'un tableau croisé dynamique

Un tableau croisé dynamique dans Excel est une représentation graphique des données créée à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les tableaux croisés dynamiques sont interactifs et peuvent être facilement modifiés pour montrer différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation de données dans Excel.

## Comment ajouter un tableau croisé dynamique à l'aide d'Aspose.Cells
### **Création d'un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données à une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable dans la collection PivotTables en passant son index.
1. Utilisez l'un des objets de tableau croisé dynamique encapsulés dans l'objet PivotTable pour gérer le tableau.

Un exemple de code est donné ci-dessous. L'exécution du code génère un nouveau fichier : pivotTable_test.xls.

**Données d'entrée** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Le tableau croisé dynamique de sortie**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Création d'un graphique dynamique en fonction du tableau croisé dynamique**

Pour créer un graphique dynamique à l'aide d'Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

Ci-dessous est le code utilisé par le composant pour accomplir la tâche. L'exécution du code génère un nouveau fichier : pivotChart_test.xls.

**La feuille de graphique croisé dynamique**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Cet article montre comment créer des tableaux croisés dynamiques et des graphiques croisés dynamiques à l'aide d'Aspose.Cells. Espérons que cela vous aidera à utiliser ces fonctionnalités dans vos propres scénarios.

Aspose.Cells a bénéficié de années de recherche, de conception et d'ajustements minutieux.

Nous sommes à votre disposition pour toute question, commentaire ou suggestion sur le [forum Aspose.Cells](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
