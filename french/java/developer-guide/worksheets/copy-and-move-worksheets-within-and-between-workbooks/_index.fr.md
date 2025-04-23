---
title: Copier et Déplacer des Feuilles de Calcul Dans et Entre des Classeurs
type: docs
weight: 20
url: /fr/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme commune et une saisie de données. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il y a une façon de faire cela : en créant une feuille, puis en la copiant trois fois.

Aspose.Cells prend en charge la copie ou le déplacement de feuilles de calcul à l'intérieur ou entre des classeurs. Les feuilles de calcul, y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et d'autres objets, sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Copier et Déplacer des Feuilles de calcul**

Cet article explique comment utiliser Aspose.Cells pour :

- [Copier une feuille de calcul à l'intérieur d'un classeur](/cells/fr/java/copier-et-déplacer-des-feuilles-de-calcul-dans-et-entre-des-classeurs/#copier-une-feuille-de-calcul-à-l'intérieur-d'un-classeur).
- [Déplacer une feuille de calcul à l'intérieur d'un classeur](/cells/fr/java/copier-et-déplacer-des-feuilles-de-calcul-dans-et-entre-des-classeurs/#déplacer-une-feuille-de-calcul-à-l'intérieur-d'un-classeur).
- [Copier une feuille de calcul entre des classeurs](/cells/fr/java/copier-et-déplacer-des-feuilles-de-calcul-dans-et-entre-des-classeurs/#copier-une-feuille-de-calcul-entre-des-classeurs).
- [Déplacer une feuille de calcul entre des classeurs](/cells/fr/java/copier-et-déplacer-des-feuilles-de-calcul-dans-et-entre-des-classeurs/#déplacer-une-feuille-de-calcul-entre-des-classeurs).

### **Copier une Feuille de Calcul à l'Intérieur d'un Classeur**

Les étapes initiales sont les mêmes pour tous les exemples.

1. Créez deux classeurs avec des données dans Microsoft Excel. Dans le cadre de cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi certaines données dans les feuilles de calcul.

- PremierClasseur.xls (3 feuilles de calcul)
- DeuxièmeClasseur.xls (1 feuille de calcul)

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Décompressez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.
1. Créer un projet :
   1. Créez un projet à l'aide d'un éditeur Java tel qu'Eclipse ou créez un programme simple à l'aide d'un éditeur de texte.
1. Ajoutez un chemin de classe :
   1. Extrayez le fichier Aspose.Cells.jar et dom4j_1.6.1.jar du fichier Aspose.Cells.zip.
   1. Définissez le chemin de classe du projet dans Eclipse :
      1. Sélectionnez votre projet dans Eclipse et cliquez sur les menus **Projet**, puis **Propriétés**.
      1. Sélectionnez **Chemin de construction Java** dans le côté gauche de la boîte de dialogue, puis sélectionnez l'onglet Bibliothèques.
      1. Cliquez sur **Ajouter des JAR** ou **Ajouter des JAR externes** pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et les ajouter aux chemins de construction.

{{% alert color="primary" %}}

Ou vous pouvez définir le chemin de classe à l'exécution dans une invite DOS sur Windows.
Par exemple:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Copier la feuille de calcul dans un classeur :
   Ci-dessous est le code utilisé pour accomplir la tâche. Il copie la feuille de calcul Copie dans PremierClasseur.xls.

L'exécution du code déplace la feuille de calcul nommée Copie dans le classeur FirstWorkbook.xls avec le nouveau nom Dernière Feuille.

**Fichier de sortie**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Déplacer une feuille de calcul dans un classeur**

Ci-dessous se trouve le code utilisé pour accomplir la tâche.

L'exécution du code déplace la feuille de calcul Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xls.

**Fichier de sortie**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Copier une feuille de calcul entre des classeurs**

L'exécution du code copie la feuille de calcul Copie dans SecondWorkbook.xls avec le nouveau nom Feuille2.

**Fichier de sortie**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Déplacer une feuille de calcul entre des classeurs**

L'exécution du code déplace la feuille de calcul déplacer de FirstWorkbook.xls à SecondWorkbook.xls avec le nouveau nom Feuille3.

**Sortie FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Sortie SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Conclusion**

{{% alert color="primary" %}}

Cet article explique comment copier et déplacer des feuilles de calcul à l'intérieur et entre des classeurs à l'aide d'Aspose.Cells.

Aspose.Cells a bénéficié d'années de recherche, de conception et d'ajustement minutieux. Nous vous invitons à poser vos questions, à formuler vos commentaires et à faire part de vos suggestions sur le [forum Aspose.Cells](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
