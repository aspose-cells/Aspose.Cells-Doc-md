---
title: Regrouper les lignes et créer un sous-total
type: docs
weight: 70
url: /fr/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb peut créer un plan pour vos données. Cela vous permet d'afficher et de masquer les niveaux de détail en cliquant sur les symboles de plan "+" et "-" pour afficher uniquement les lignes qui fournissent des résumés ou des en-têtes pour les sections d'une feuille de calcul. Vous pouvez utiliser les symboles pour voir les détails sous un résumé ou un titre individuel.

Lors du regroupement de lignes, il est important de sélectionner uniquement les lignes de détail qui composent le groupe. N'incluez pas la ligne récapitulative associée. Par exemple, si la ligne 6 contient les totaux des données des lignes 3 à 5, sélectionnez uniquement les lignes 3 à 5 pour définir le groupe. Le contrôle Aspose.Cells.GridWeb affiche le**Montrer les détails** (+) et**masquer les détails** (-) symboles à côté des en-têtes de ligne spécifiant les groupes dans la feuille de calcul.

Aspose.Cells.GridWeb vous permet également de créer des sous-totaux basés sur n'importe quel champ de données. Un sous-total n'est pas nécessairement une somme : il peut s'agir d'une moyenne, d'un comptage, d'un minimum, d'un maximum ou d'un autre calcul statistique.

Cette rubrique traite du regroupement de lignes et de la création de sous-totaux à l'aide de Aspose.Cells.GridWeb API. Les développeurs peuvent regrouper des lignes avec n'importe quel niveau d'imbrication et créer facilement des sous-totaux.

{{% /alert %}} 
## **Groupement de lignes**
Pour regrouper un nombre spécifique de lignes :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Sélectionnez le nombre souhaité de cellules dans les rangées.
1. Groupez les rangées.

Lorsque les lignes sont regroupées, un bouton développer/réduire s'affiche en haut de la ligne récapitulative des lignes. Vous pouvez modifier le réglage de la direction. La propriété WebWorksheet.IsSummaryRowBelow est une propriété booléenne. Définissez-le sur false (par défaut) et la ligne de résumé sera au-dessus des lignes de détail. Définissez-le sur true et la ligne de résumé sera sous les lignes de détail. Cliquez sur le bouton développer/réduire pour développer ou réduire les lignes groupées.

L'exemple suivant regroupe les lignes de la 2e à la 10e ligne.

**Groupement de lignes** 

![tâche : image_autre_texte](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Imbrication de lignes groupées**
Vous pouvez créer des niveaux d'organisation tout en regroupant un ensemble de lignes. Vous pouvez grouper des rangées parmi les rangées groupées. L'exemple suivant montre l'imbrication de lignes groupées.

**Groupement de lignes** 

![tâche : image_autre_texte](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Processus interne : comment fonctionne le contrôle ?**
Chaque ligne de la feuille a un numéro de plan. La valeur par défaut du numéro de contour est zéro. Chaque fois que vous regroupez les lignes, le numéro de plan est augmenté de 1. Vous pouvez obtenir le numéro de plan en appelant la méthode GridWorksheet.Cells.GetRowOutlineLevel().
## **Dissocier les lignes**
Aspose.Cells.GridWeb vous permet de dissocier des lignes groupées.

Pour dissocier un nombre spécifique de lignes :

1. Sélectionnez un certain nombre de cellules dans les lignes de la feuille de calcul à dissocier.
1. Dégroupez les lignes.

L'exemple suivant dissocie les lignes de la 2e à la 10e ligne.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Lorsque vous appelez la méthode GridWorksheet.Cells.UngroupRows(), le numéro de plan des lignes groupées est défini sur zéro.

{{% /alert %}} 
## **Créer un sous-total**
La fonctionnalité de sous-total du contrôle peut regrouper les lignes de la feuille avec une colonne spécifiée et calculer le résumé des colonnes. Aspose.Cells.GridWeb peut calculer automatiquement les valeurs de sous-total pour une liste. Lorsque vous implémentez des sous-totaux, le contrôle présente la liste afin que vous puissiez afficher et masquer les lignes de détail pour chaque sous-total. Avant d'ajouter des sous-totaux, triez sur le champ sur lequel vous souhaitez effectuer un sous-total. Pour créer des sous-totaux, utilisez n'importe quelle version de la méthode WebWorksheet.CreateSubtotal surchargée.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **Liste des paramètres**

|**Non.**|**Le nom du paramètre**|**Description**|
|:- |:- |:- |
|1|nom_colonneRowIndex|Index de ligne de la ligne du nom de colonne.|
|2|dataRows|Le nombre de lignes de données.|
|3|groupByColumnIndexgroupByColumnIndex|Index de colonne de la colonne à regrouper.|
|4|fonction de sous-total|Énumération du type de fonction de sous-total.|
|5|subtotalColumnIndexList|Les index de colonne à sous-totaliser.|
### **Liste des fonctions récapitulatives**
Il existe plusieurs types de fonctions récapitulatives prises en charge par l'énumération {[SubtotalFunction}} :

|**Non.**|**Nom de la fonction**|**Description**|
|:- |:- |:- |
|1|MOYENNE|Calcule la moyenne des valeurs.|
|2|COMPTER|Compte les valeurs numériques dans les cellules.|
|3|COUNTA|Compte les données non numériques dans les cellules.|
|4|MAX|Calcule la plus grande valeur.|
|5|MIN|Calcule la plus petite valeur.|
|6|PRODUIT|Calcule le produit des valeurs.|
|7|SOMME|Calcule la somme des valeurs.|
L'exemple suivant génère les sous-totaux qui calculent les valeurs non numériques regroupées par la deuxième colonne de la feuille de calcul.

**Sous-totaux** 

![tâche : image_autre_texte](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Suppression du sous-total**
Pour supprimer un sous-total, utilisez la méthode WebWorksheet.RemoveSubtotal. L'exemple suivant supprime les sous-totaux.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **À propos de la fonction SOUS-TOTAL**
Le contrôle GridWeb utilise la fonction de formule SOUS-TOTAL pour calculer la valeur du sous-total.

Syntaxe : SOUS-TOTAL(num_fonction, réf1, réf2, ...)

function_num est un nombre spécifiant le type de la fonction utilisée dans le calcul du sous-total.

|**1**|**MOYENNE**|
|:- |:- |
|2|COMPTER|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUIT|
|7|SOMME|
ref1, ref2, sont les zones à sous-totaliser. Si ref1, ref2, ... contiennent d'autres fonctions de sous-total, les cellules référencées sont ignorées pour éviter un calcul en double.
