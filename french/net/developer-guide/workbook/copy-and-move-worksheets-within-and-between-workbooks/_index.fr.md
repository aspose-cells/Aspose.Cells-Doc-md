---
title: Copier et déplacer des feuilles de calcul dans et entre des classeurs
type: docs
weight: 80
url: /fr/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec un formatage et une saisie de données communs. Par exemple, si vous travaillez avec des budgets trimestriels, vous souhaiterez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il existe un moyen de le faire : en créant une feuille, puis en la copiant trois fois.

Aspose.Cells prend en charge la copie ou le déplacement de feuilles de calcul dans ou entre des classeurs. Les feuilles de calcul, y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et d'autres objets sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Copier et déplacer des feuilles de calcul**

### **Copier une feuille de calcul dans un classeur**

Les étapes initiales sont les mêmes pour tous les exemples.

1. Créez deux classeurs avec des données dans Microsoft Excel. Pour les besoins de cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi des données dans les feuilles de calcul.

- FirstWorkbook.xlsx (3 feuilles de calcul).
- SecondWorkbook.xlsx (1 feuille de calcul).

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Installez-le sur votre ordinateur de développement.
 Tout[Aspose](http://www.aspose.com/) les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.
1. Créer un projet :
 1. Démarrez Visual Studio.Net.
 1. Créez une nouvelle application console.
1. Ajoutez des références :
 1. Ajoutez une référence à Aspose.Cells au projet.
 Par exemple, ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Copier la feuille de calcul dans un classeur
 Le premier exemple copie la première feuille de calcul (Copy) dans FirstWorkbook.xlsx.

Lors de l'exécution du code, la feuille de calcul nommée Copy est copiée dans FirstWorkbook.xlsx avec le nom Last Sheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Déplacer une feuille de calcul dans un classeur**

Le code ci-dessous montre comment déplacer une feuille de calcul d'une position dans un classeur à une autre. L'exécution du code déplace la feuille de calcul appelée Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Copier une feuille de calcul entre des classeurs**

L'exécution du code copie la feuille de calcul nommée Copier dans SecondWorkbook.xlsx avec le nom Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Déplacement d'une feuille de calcul entre des classeurs**

L'exécution du code déplace la feuille de calcul nommée Move from FirstWorkbook.xlsx to SecondWorkbook.xlsx avec le nom Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
