---
title: Copier et déplacer des feuilles de calcul dans et entre des classeurs
type: docs
weight: 20
url: /fr/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec un formatage et une saisie de données communs. Par exemple, si vous travaillez avec des budgets trimestriels, vous souhaiterez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il existe un moyen de le faire : en créant une feuille, puis en la copiant trois fois.

Aspose.Cells prend en charge la copie ou le déplacement de feuilles de calcul dans ou entre des classeurs. Les feuilles de calcul, y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et d'autres objets sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Copier et déplacer des feuilles de calcul**

Cet article explique comment utiliser Aspose.Cells pour :

- [Copier une feuille de calcul dans un classeur](/cells/fr/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Déplacer une feuille de calcul dans un classeur](/cells/fr/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Copier une feuille de calcul entre des classeurs](/cells/fr/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Déplacer une feuille de calcul entre des classeurs](/cells/fr/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Copier une feuille de calcul dans un classeur**

Les étapes initiales sont les mêmes pour tous les exemples.

1. Créez deux classeurs avec des données dans Microsoft Excel. Pour les besoins de cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi des données dans les feuilles de calcul.

- FirstWorkbook.xls (3 feuilles de calcul)
- SecondWorkbook.xls (1 feuille de calcul).

  **FirstWorkbook.xls**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Décompressez-le sur votre ordinateur de développement.
 Tout[Aspose](http://www.aspose.com/) les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.
1. Créer un projet :
 1. Créez un projet à l'aide d'un éditeur Java tel qu'Eclipse ou créez un programme simple à l'aide d'un éditeur de texte.
1. Ajoutez un chemin de classe :
1. Extrayez les fichiers Aspose.Cells.jar et dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Définissez le chemin de classe du projet dans Eclipse :
 1. Sélectionnez votre projet dans Eclipse et cliquez sur les menus**Projet** , alors**Propriétés**.
 1. Sélectionnez**Java Chemin de construction** dans la partie gauche de la boîte de dialogue, puis sélectionnez l'onglet Bibliothèques,
 1. Cliquez sur**Ajouter des JAR** ou**Ajouter des fichiers JAR externes** pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et les ajouter dans les chemins de génération.

{{% alert color="primary" %}}

Ou vous pouvez définir le chemin de classe au moment de l'exécution dans une invite DOS sur Windows.
Par exemple:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Copier une feuille de calcul dans un classeur :
 Vous trouverez ci-dessous le code utilisé par pour accomplir la tâche. Il copie la feuille de calcul Copy dans FirstWorkbook.xls.

L'exécution du code déplace la feuille de calcul nommée Copy dans FirstWorkbook.xls avec le nouveau nom Last Sheet.

**Fichier de sortie**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Déplacer une feuille de calcul avec dans un classeur**

Vous trouverez ci-dessous le code utilisé pour accomplir la tâche.

L'exécution du code déplace la feuille de calcul Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xls.

**Fichier de sortie**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Copier une feuille de calcul entre des classeurs**

L'exécution du code copie la feuille de calcul Copy to SecondWorkbook.xls avec le nouveau nom Sheet2.

**Fichier de sortie**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Déplacement d'une feuille de calcul entre des classeurs**

L'exécution du code déplace la feuille de calcul de déplacement de FirstWorkbook.xls vers SecondWorkbook.xls avec le nouveau nom Sheet3.

**Sortie FirstWorkbook.xls**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Sortie SecondWorkbook.xls**

![tâche : image_autre_texte](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Conclusion**

{{% alert color="primary" %}}

Cet article explique comment copier et déplacer des feuilles de calcul dans et entre des classeurs à l'aide de Aspose.Cells.

 Aspose.Cells a bénéficié d'années de recherche, de conception et de réglage minutieux. Nous accueillons vos questions, commentaires et suggestions à[Aspose.CellsForum](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
