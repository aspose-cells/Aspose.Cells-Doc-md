---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 10
url: /fr/java/create-pivot-tables-and-pivot-charts/
description: Créez des tableaux croisés dynamiques et des graphiques croisés dynamiques avec Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste d'une feuille de calcul. Un tableau croisé dynamique permet de totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réorganiser rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un tableau croisé dynamique est une représentation graphique interactive des données d'un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique facilite encore la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

 Aspose.Cells prend en charge[tableaux croisés dynamiques](/cells/fr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) et[tableaux croisés dynamiques](/cells/fr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Ajout de tableaux croisés dynamiques et de graphiques**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer des tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir des objets PivotTable, qui agissent comme les blocs de construction de base d'un objet PivotTable :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- Tableau croisé dynamique, un rapport de tableau croisé dynamique sur une feuille de calcul.
- Tableaux croisés dynamiques, une collection de tous les objets de tableau croisé dynamique de la feuille de calcul.

### **Préparation à l'utilisation Aspose.Cells**

1. Téléchargez et installez Aspose.Cells.Zip :
   1. [Télécharger Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Décompressez-le sur votre ordinateur de développement.
 Tout[Aspose](http://www.aspose.com/) les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.
1. Créer un projet
 1. Vous pouvez soit créer un projet à l'aide d'un éditeur Java, par exemple Eclipse, soit créer un programme simple à l'aide d'un bloc-notes.
1. Ajouter un chemin de classe :
 Pour définir un chemin de classe à l'aide d'Eclipse :
1. Extrayez les fichiers Aspose.Cells.jar et dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Définissez le chemin de classe du projet dans Eclipse :
1. Sélectionnez votre projet dans Eclipse puis cliquez sur les menus Projet-Propriétés.
 1. Sélectionnez "Java Build Path" dans la partie gauche de la fenêtre contextuelle, puis sélectionnez l'onglet "Libraries", cliquez sur "Add JARs" ou "Add External JARs" pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et ajoutez-les dans les chemins de construction.
 1. Écrivez une application pour invoquer les API des composants de Aspose.
 Ou vous pouvez le définir lors de l'exécution à l'invite dos dans Windows.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Création d'un tableau croisé dynamique**

Pour créer un tableau croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez des données aux cellules d'une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous utilisez également un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Worksheet).
1. Accédez au nouvel objet PivotTable à partir de la collection PivotTables en transmettant son index.
1. Utilisez n'importe lequel des objets de tableau croisé dynamique encapsulés dans l'objet PivotTable pour gérer le tableau.

Un exemple de code est donné ci-dessous. L'exécution du code génère un nouveau fichier : pivotTable_test.xls.

**Des données d'entrée** 

![tâche : image_autre_texte](create-pivot-tables-and-pivot-charts_1.png)

**Le tableau croisé dynamique de sortie**

![tâche : image_autre_texte](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Création d'un graphique croisé dynamique basé sur le tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez le PivotSource du graphique pour faire référence à un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

Vous trouverez ci-dessous le code utilisé par le composant pour accomplir la tâche. L'exécution du code génère un nouveau fichier : pivotChart_test.xls.

**La feuille de tableau croisé dynamique**

![tâche : image_autre_texte](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Cet article explique comment créer des tableaux croisés dynamiques et des graphiques croisés dynamiques à l'aide de Aspose.Cells. J'espère qu'il vous aidera à utiliser ces fonctionnalités dans vos propres scénarios.

Aspose.Cells a bénéficié d'années de recherche, de conception et de réglage minutieux.

 Nous accueillons vos questions, commentaires et suggestions à[Aspose.CellsForum](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}

## Articles Liés

- [Tri personnalisé dans le tableau croisé dynamique](/cells/fr/java/custom-sorting-in-pivot-table/)
- [Formatage du tableau croisé dynamique](/cells/fr/java/formatting-pivot-table/)
- [Actualiser et calculer le tableau croisé dynamique ayant des éléments calculés](/cells/fr/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Désactiver les rubans du tableau croisé dynamique](/cells/fr/java/disable-pivot-table-ribbons/)

