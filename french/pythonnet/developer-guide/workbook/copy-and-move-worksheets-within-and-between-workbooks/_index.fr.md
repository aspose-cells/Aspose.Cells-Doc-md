---
title: Copier et Déplacer des Feuilles de Calcul Dans et Entre des Classeurs
type: docs
weight: 80
url: /fr/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme commune et une saisie de données. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il y a une façon de faire cela : en créant une feuille, puis en la copiant trois fois.

Aspose.Cells pour Python via .NET prend en charge la copie ou le déplacement de feuilles de calcul dans un classeur ou entre plusieurs classeurs. Les feuilles de calcul, y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et autres objets, sont copiées avec la plus haute précision.

{{% /alert %}}

## **Copier et Déplacer des Feuilles de calcul**

### **Copier une Feuille de Calcul à l'Intérieur d'un Classeur**

Les étapes initiales sont les mêmes pour tous les exemples.

1. Créez deux classeurs avec des données dans Microsoft Excel. Dans le cadre de cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi certaines données dans les feuilles de calcul.

- FirstWorkbook.xlsx (3 feuilles de calcul).
- SecondWorkbook.xlsx (1 feuille de calcul).

1. Téléchargez et installez Aspose.Cells pour Python via .NET :
   1. [Télécharger Aspose.Cells pour Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.
1. Créez un projet et ajoutez des références:   
1. Copiez la feuille de calcul dans un classeur
   Le premier exemple copie la première feuille de calcul (Copie) dans FirstWorkbook.xlsx.

Lors de l'exécution du code, la feuille de calcul nommée Copie est copiée dans FirstWorkbook.xlsx avec le nom Dernière Feuille.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Déplacer une feuille de calcul dans un classeur**

Le code ci-dessous montre comment déplacer une feuille de calcul d'une position à une autre dans un classeur. En exécutant le code, la feuille de calcul appelée Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Copier une feuille de calcul entre des classeurs**

En exécutant le code, la feuille de calcul nommée Copie est copiée dans SecondWorkbook.xlsx avec le nom Feuille2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Déplacer une feuille de calcul entre des classeurs**

En exécutant le code, la feuille de calcul nommée Déplacer de FirstWorkbook.xlsx est déplacée vers SecondWorkbook.xlsx avec le nom Feuille3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
{{< app/cells/assistant language="python-net" >}}
