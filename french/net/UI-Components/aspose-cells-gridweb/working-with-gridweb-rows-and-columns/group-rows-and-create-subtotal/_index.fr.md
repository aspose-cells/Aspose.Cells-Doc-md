---
title: Regrouper les lignes et créer un sous total
type: docs
weight: 70
url: /fr/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: Cet article présente comment regrouper/dégrouper des lignes/colonnes et comment travailler avec un sous total dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb peut créer un sommaire pour vos données. Cela vous permet de montrer ou de masquer les niveaux de détail en cliquant sur les symboles de sommaire "+" et "-" pour n'afficher que les lignes qui fournissent des résumés ou des en-têtes pour les sections dans une feuille de calcul. Vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuel.

Lors du regroupement des lignes, il est important de sélectionner uniquement les lignes de détail qui composent le groupe. N'incluez pas la ligne de résumé associée. Par exemple, si la ligne 6 contient les totaux des données des lignes 3 à 5, sélectionnez uniquement les lignes 3 à 5 pour définir le groupe. Le contrôle Aspose.Cells.GridWeb affiche les symboles **afficher le détail** (+) et **masquer le détail** (-) à côté des en-têtes de ligne spécifiant les groupes dans la feuille de calcul.

Aspose.Cells.GridWeb permet également de créer des sous-totaux basés sur n'importe quel champ de données. Un sous-total n'est pas nécessairement une somme : il peut s'agir d'une moyenne, d'un nombre, d'un minimum, d'un maximum ou d'un autre calcul statistique.

Ce sujet traite du regroupement des lignes et de la création de sous-totaux à l'aide de l'API Aspose.Cells.GridWeb. Les développeurs peuvent regrouper des lignes avec n'importe quel niveau d'imbriquation et créer facilement des sous-totaux.

{{% /alert %}} 
## **Regroupement des lignes**
Pour regrouper un nombre spécifique de lignes :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Sélectionnez le nombre souhaité de cellules dans les lignes.
1. Regrouper les lignes.

Lorsque les lignes sont regroupées, un bouton d'extension/réduction est affiché en haut de la ligne de résumé des lignes. Vous pouvez modifier le paramétrage de la direction. La propriété WebWorksheet.IsSummaryRowBelow est une propriété booléenne. Définissez-la sur false (par défaut) et la ligne de résumé sera au-dessus des lignes de détail. Définissez-la sur true et la ligne de résumé sera en dessous des lignes de détail. Cliquez sur le bouton d'extension/réduction pour développer ou réduire les lignes regroupées.

L'exemple suivant regroupe les lignes de la 2e ligne à la 10e ligne.

**Regroupement de lignes** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Imbrication des lignes regroupées**
Vous pouvez créer des niveaux d'organisation tout en regroupant un ensemble de lignes. Vous pouvez regrouper des lignes parmi les lignes regroupées. L'exemple suivant montre l'imbrication des lignes regroupées.

**Regroupement de lignes** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Processus interne : Comment fonctionne le contrôle ?**
Chaque ligne de la feuille a un numéro de plan. La valeur par défaut du numéro de plan est zéro. Chaque fois que vous regroupez les lignes, le numéro de plan est augmenté de 1. Vous pouvez obtenir le numéro de plan en appelant la méthode GridWorksheet.Cells.GetRowOutlineLevel().
## **Dégrouper les lignes**
Aspose.Cells.GridWeb vous permet de dégrouper des lignes groupées.

Pour dégrouper un nombre spécifique de lignes :

1. Sélectionnez un certain nombre de cellules dans les lignes de la feuille de calcul à dégrouper.
1. Dégrouper les lignes.

L'exemple suivant dégroupe les lignes de la 2e à la 10e ligne.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Lorsque vous appelez la méthode GridWorksheet.Cells.UngroupRows(), le numéro de plan des lignes groupées est défini à zéro.

{{% /alert %}} 
## **Création d'un sous-total**
La fonction de sous-total du contrôle permet de regrouper les lignes dans la feuille avec une colonne spécifiée, et de calculer le résumé des colonnes. Aspose.Cells.GridWeb peut calculer automatiquement les valeurs de sous-total pour une liste. Lorsque vous implémentez des sous-totaux, le contrôle met en exergue la liste de sorte que vous puissiez afficher et masquer les lignes de détail pour chaque sous-total. Avant d'ajouter des sous-totaux, triez sur le champ sur lequel vous souhaitez faire un sous-total. Pour créer des sous-totaux, utilisez n'importe quelle version de la méthode WebWorksheet.CreateSubtotal surchargée.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **Liste des paramètres**

|**No.**|**Nom du paramètre**|**Description**|
| :- | :- | :- |
|1|columnNameRowIndex|L'indice de ligne de la ligne de nom de colonne.|
|2|dataRows|Le nombre de lignes de données.|
|3|groupByColumnIndex|L'indice de colonne de la colonne à regrouper.|
|4|subtotalFunction|Le type d'énumération de la fonction de sous-total.|
|5|subtotalColumnIndexList|Les index de colonnes à soustotaliser.|
### **Liste des Fonctions de Résumé**
Il existe plusieurs types de fonctions de résumé pris en charge par l'énumération {[SubtotalFunction}}:

|**No.**|**Nom de la Fonction**|**Description**|
| :- | :- | :- |
|1|AVERAGE|Calcule la moyenne des valeurs.|
|2|COUNT|Compte les valeurs numériques dans les cellules.|
|3|COUNTA|Compte les données non numériques dans les cellules.|
|4|MAX|Calcule la plus grande valeur.|
|5|MIN|Calcule la plus petite valeur.|
|6|PRODUCT|Calcule le produit des valeurs.|
|7|SUM|Calcule la somme des valeurs.|
L'exemple suivant génère les totaux partiels qui calculent les valeurs non numériques regroupées par la deuxième colonne dans la feuille de calcul.

**Totaux Partiels** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Suppression du Sous-total**
Pour supprimer un sous-total, utilisez la méthode WebWorksheet.RemoveSubtotal. L'exemple suivant supprime les sous-totaux.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **A propos de la fonction SOUSTOTAL**
Le contrôle GridWeb utilise la fonction de formule SOUSTOTAL pour calculer la valeur du sous-total.

Syntaxe : SOUSTOTAL(num_function, ref1, ref2, ...)

num_function est un nombre spécifiant le type de fonction utilisé dans le calcul du sous-total.

|**1**|**MOYENNE**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1, ref2, sont les zones à totaliser. Si ref1, ref2, ... contiennent d'autres fonctions de total partiel, les cellules référencées sont ignorées pour éviter des calculs en double.
