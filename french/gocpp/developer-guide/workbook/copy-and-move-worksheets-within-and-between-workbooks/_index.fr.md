---
title: Copier et déplacer des feuilles entre et dans les classeurs avec Golang via C++
linktitle: Copier et déplacer des feuilles de calcul
type: docs
weight: 80
url: /fr/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Apprenez à copier et déplacer des feuilles de calcul à l intérieur et entre des classeurs Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de plusieurs feuilles de calcul avec une mise en forme commune et des saisies de données. Par exemple, si vous travaillez avec des budgets trimestriels, vous pouvez vouloir créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il existe une façon de faire cela : en créant une feuille, puis en la copiant plusieurs fois.

Aspose.Cells prend en charge la copie ou le déplacement de feuilles de calcul à l'intérieur ou entre des classeurs. Les feuilles de calcul, y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et d'autres objets, sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Copier et Déplacer des Feuilles de calcul**

### **Copier une Feuille de Calcul à l'Intérieur d'un Classeur**

Les étapes initiales sont les mêmes pour tous les exemples :

1. Créez deux classeurs Excel avec quelques données. Pour cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi quelques données dans les feuilles :
   - FirstWorkbook.xlsx (3 feuilles)
   - SecondWorkbook.xlsx (1 feuille)

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Installez-le sur votre ordinateur de développement

1. Créer un projet :
   1. Créez un nouveau projet C++ dans votre IDE préféré

1. Ajouter des références:
   1. Ajoutez la bibliothèque Aspose.Cells for C++ à votre projet

1. Copiez la feuille de calcul dans un classeur
   Le premier exemple copie la première feuille de calcul (Copie) dans FirstWorkbook.xlsx.

Lors de l'exécution du code, la feuille de calcul nommée Copie est copiée dans FirstWorkbook.xlsx avec le nom Dernière Feuille.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Déplacer une feuille de calcul dans un classeur**

Le code ci-dessous montre comment déplacer une feuille de calcul d'une position à une autre dans un classeur. En exécutant le code, la feuille de calcul appelée Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Copier une feuille de calcul entre des classeurs**

Exécuter le code copie la feuille de calcul nommée Copy dans SecondWorkbook.xlsx avec le nom Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Déplacer une feuille de calcul entre des classeurs**

En exécutant le code, la feuille de calcul nommée Déplacer de FirstWorkbook.xlsx est déplacée vers SecondWorkbook.xlsx avec le nom Feuille3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
