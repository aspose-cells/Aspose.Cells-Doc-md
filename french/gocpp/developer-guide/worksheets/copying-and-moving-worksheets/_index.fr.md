---
title: Copier et Déplacer des Feuilles de calcul
type: docs
weight: 10
url: /fr/go-cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il y a un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells prend en charge la copie et le déplacement de feuilles de calcul au sein d'un classeur ou entre classeurs. Une feuille de calcul, accompagnée de données, de mise en forme, de tableaux, de matrices, de graphiques, d'images et d'autres objets, est copiée avec le plus haut degré de précision.

{{% /alert %}}

## **Déplacement ou Copie de feuilles à l'aide de Microsoft Excel**

Les étapes suivantes sont impliquées dans la copie et le déplacement de feuilles de calcul au sein d'un classeur ou entre classeurs dans Microsoft Excel.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou copier la feuille**.
1. Dans la boîte de dialogue **Vers le classeur**, cliquez sur le classeur qui recevra les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées vers un nouveau classeur, cliquez sur **Nouveau Classeur**.
1. Dans la zone **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.

### **Copier des Feuilles au sein d'un Classeur avec Aspose.Cells**

Aspose.Cells propose une méthode surchargeée [AddCopy()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/addcopy_string/) pour ajouter une feuille de calcul à la collection et copier les données d’une feuille existante. Une version de la méthode prend l’indice de la feuille source comme paramètre. L’autre version prend le nom de la feuille source. L’exemple suivant montre comment copier une feuille de calcul existante au sein d’un classeur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyWorksheetsWithinWorkbook.go" >}}

### **Déplacer des feuilles de calcul dans un classeur**

Aspose.Cells fournit une méthode [MoveTo()](https://reference.aspose.com/cells/go-cpp/worksheet/moveto/) pour déplacer une feuille de calcul à un autre emplacement dans le même classeur. La méthode prend en paramètre l’indice de la feuille cible. L’exemple suivant montre comment déplacer une feuille à un autre emplacement au sein du classeur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MoveWorksheetsWithinWorkbook.go" >}}
