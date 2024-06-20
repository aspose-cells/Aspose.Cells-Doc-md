---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 10
url: /fr/java/create-pivot-tables-and-pivot-charts/
description: Créer des tables pivot et des graphiques pivot avec l API Aspose.Cells for Java.
keywords: créer une table pivot excel java, créer un graphique pivot excel java, créer une table pivot excel et un graphique pivot java, créer une table pivot excel java, créer un graphique pivot excel java, créer une table pivot excel et un graphique pivot java, java créer une table pivot excel et un graphique pivot, comment créer une table pivot excel et un graphique pivot java
---

{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste dans une feuille de calcul. Un tableau croisé dynamique peut totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réarranger rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un graphique croisé dynamique est une représentation graphique interactive des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique rend encore plus facile la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

Aspose.Cells prend en charge les [tables pivot](/cells/fr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) et les [graphiques pivot](/cells/fr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Ajout de tables pivot et de graphiques**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer des tables pivot. Ces classes sont utilisées pour créer et définir les objets PivotTable, qui agissent comme des blocs de construction de base d'un objet PivotTable :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- PivotTable, un rapport de tableau croisé dynamique sur une feuille de calcul.
- PivotTables, une collection de tous les objets PivotTable sur la feuille de calcul.

### **Préparation à l'utilisation d'Aspose.Cells**

1. Téléchargez et installez Aspose.Cells.Zip :
   1. [Télécharger Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Décompressez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.
1. Créez un projet
   1. Vous pouvez soit créer un projet à l'aide d'un éditeur Java comme Eclipse, soit créer un simple programme à l'aide d'un Bloc-notes.
1. Ajoutez un chemin de classe :
   Pour définir un chemin de classe à l'aide d'Eclipse :
   1. Extrayez le fichier Aspose.Cells.jar et dom4j_1.6.1.jar du fichier Aspose.Cells.zip.
   1. Définissez le chemin de classe du projet dans Eclipse :
   1. Sélectionnez votre projet dans Eclipse, puis cliquez sur le menu Projet-Propriétés.
   1. Sélectionnez "Chemin de construction Java" dans le côté gauche de la fenêtre contextuelle, puis sélectionnez l'onglet "Bibliothèques", cliquez sur "Ajouter JARs" ou "Ajouter des JARs externes" pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et ajoutez-les dans les chemins de construction.
   1. Écrivez une application pour appeler les API des composants d'Aspose.
      Ou vous pouvez le définir au moment de l'exécution à l'invite de commande dans Windows.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

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

## Articles Connexes

- [Tri personnalisé dans le tableau croisé dynamique](/cells/fr/java/custom-sorting-in-pivot-table/)
- [Formatage du tableau croisé dynamique](/cells/fr/java/formatting-pivot-table/)
- [Actualiser et calculer un tableau croisé dynamique avec des éléments calculés](/cells/fr/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Désactiver les rubans du tableau croisé dynamique](/cells/fr/java/disable-pivot-table-ribbons/)

