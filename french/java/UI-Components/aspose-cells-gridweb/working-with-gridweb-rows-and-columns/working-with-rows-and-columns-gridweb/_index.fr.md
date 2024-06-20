---
title: Travailler avec les lignes et colonnes de GridWeb
type: docs
weight: 20
url: /fr/java/working-with-rows-and-columns-gridweb/
---

## **Insertion de lignes et colonnes**
Ce sujet explique comment insérer de nouvelles lignes et colonnes dans une feuille de calcul en utilisant l'API Aspose.Cells.GridWeb. Les lignes ou les colonnes peuvent être insérées à n'importe quelle position dans la feuille de calcul.
### **Insertion de lignes**
Pour insérer une ligne à n'importe quelle position dans une feuille de calcul :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web ou à la page.
1. Accédez à la feuille de calcul à laquelle vous ajoutez des lignes.
1. Insérez une ligne en spécifiant un index de ligne où la ligne doit être insérée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Insertion de colonnes**
Pour insérer une colonne à n'importe quelle position dans une feuille de calcul:

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web ou une page.
1. Accédez à la feuille de calcul à laquelle vous souhaitez ajouter des colonnes.
1. Insérez une colonne en spécifiant l'index de la colonne où la colonne doit être insérée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Vous pouvez également utiliser les méthodes insertRows()/insertColumns() pour insérer plusieurs lignes/colonnes dans les feuilles de calcul respectivement.

{{% /alert %}} 
## **Suppression de lignes et de colonnes**
Ce sujet montre comment supprimer des lignes et des colonnes d'une feuille de calcul en utilisant l'API Aspose.Cells.GridWeb. Grâce à cette fonctionnalité, les développeurs peuvent supprimer des lignes ou des colonnes à l'exécution.
### **Suppression de lignes**
Pour supprimer une ligne de votre feuille de calcul:

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web ou une page.
1. Accédez à la feuille de calcul à partir de laquelle vous souhaitez supprimer des lignes.
1. Supprimez une ligne de la feuille de calcul en spécifiant son index de ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Suppression de colonnes**
Pour supprimer une colonne de votre feuille de calcul:

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web ou une page.
1. Accédez à la feuille de calcul à partir de laquelle vous souhaitez supprimer des colonnes.
1. Supprimez une colonne de la feuille de calcul en spécifiant son index de colonne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Définition de la hauteur de ligne et de la largeur de colonne**
Parfois, les valeurs des cellules sont plus larges que la cellule dans laquelle elles se trouvent ou sont sur plusieurs lignes. De telles valeurs ne sont pas entièrement visibles pour les utilisateurs à moins qu'ils ne modifient la hauteur et la largeur des lignes et des colonnes. Aspose.Cells.GridWeb prend en charge pleinement le réglage de la hauteur des lignes et de la largeur des colonnes. Ce sujet traite de ces fonctionnalités en détail à l'aide d'exemples.
### **Travailler avec la hauteur des lignes et la largeur des colonnes**
#### **Réglage de la hauteur des lignes**
Pour définir la hauteur d'une ligne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire/page Web.
1. Accédez à la collection de cellules de la feuille de calcul.
1. Définissez la hauteur de toutes les cellules dans une ligne spécifiée.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb accepte les mesures de hauteur de ligne et de largeur de colonne en points, pouces, pixels, etc.

{{% /alert %}} 

**Résultat : la hauteur de la 1ère ligne a été définie à 50 points** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Réglage de la largeur de la colonne**
Pour définir la largeur d'une colonne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire/page Web.
1. Accédez à la collection de cellules de la feuille de calcul.
1. Définissez la largeur de toutes les cellules dans une colonne spécifiée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Personnalisation des en-têtes de ligne et de colonne**
Comme Microsoft Excel, Aspose.Cells.GridWeb utilise également des en-têtes ou des libellés standard pour les lignes (nombres comme 1, 2, 3, etc.) et les colonnes (alphabétiques comme A, B, C, etc.). Aspose.Cells.GridWeb permet également de personnaliser les libellés. Ce sujet traite de la personnalisation des en-têtes de ligne et de colonne à l'exécution en utilisant l'API Aspose.Cells.GridWeb.
### **Personnalisation de l'en-tête de ligne**
Pour personnaliser l'en-tête ou le libellé d'une ligne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire/page Web.
1. Accédez à la feuille de calcul dans GridWorksheetCollection.
1. Définir la légende de n'importe quelle ligne spécifiée.

**Les en-têtes des lignes 1 et 2 ont été personnalisés** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Personnalisation de l'en-tête de colonne**
Pour personnaliser l'en-tête ou la légende d'une colonne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire/page Web.
1. Accédez à la feuille de calcul dans GridWorksheetCollection.
1. Définissez la légende de n'importe quelle colonne spécifiée.

**Les en-têtes des colonnes 1 et 2 ont été personnalisés** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Geler et dégeler les lignes et les colonnes**
Ce sujet explique comment geler et dégeler les lignes et les colonnes. Geler des colonnes ou des lignes permet aux utilisateurs de conserver les en-têtes de colonnes ou les titres de lignes visibles lorsqu'ils font défiler d'autres parties de la feuille de calcul. Cette fonctionnalité est très utile lors de travaux avec des feuilles de calcul contenant de grands volumes de données. Lorsque les utilisateurs font défiler, seules les données sont déplacées vers le bas et les en-têtes restent en place, facilitant la lecture des données. La fonction de figer les volets est uniquement prise en charge dans Internet Explorer 6.0 ou version ultérieure.
### **Geler les lignes et les colonnes**
Pour geler un nombre spécifique de lignes et de colonnes :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire/page Web.
1. Accéder à une feuille de calcul.
1. Geler un nombre de lignes et de colonnes.

{{% alert color="primary" %}} 

Il est également possible de geler un nombre spécifique de lignes et de colonnes à l'aide de l'interface. Cliquez avec le bouton droit sur une cellule où vous voulez geler des lignes et des colonnes et sélectionnez **Geler** dans la liste.

{{% /alert %}} 

**Lignes et colonnes dans un état figé** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Dégeler les lignes et les colonnes**
Pour dégeler des lignes et des colonnes :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire/page Web.
1. Accéder à une feuille de calcul.
1. Dégeler les lignes et les colonnes.

**Feuille de calcul après avoir été dégelée** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Protéger les lignes et les colonnes**
Ce sujet aborde quelques techniques pour protéger les cellules des lignes et des colonnes contre toute action des utilisateurs finaux. Les développeurs peuvent implémenter cette protection en utilisant deux techniques : en rendant les cellules des lignes et des colonnes en lecture seule, ou en restreignant les options du menu contextuel de GridWeb.
### **Restreindre les options du menu contextuel**
GridWeb fournit un menu contextuel que les utilisateurs finaux peuvent utiliser pour effectuer des opérations sur le contrôle. Le menu offre de nombreuses options pour manipuler les cellules, les lignes et les colonnes.

**Options contextuelles complètes** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Il est possible de restreindre tout type d'opérations côté client sur les lignes et les colonnes en restreignant les options disponibles dans le menu contextuel. Cela peut être fait en définissant les attributs EnableClientColumnOperations et EnableClientRowOperations du contrôle GridWeb sur false. Il est également possible de restreindre les utilisateurs à geler les lignes et les colonnes en définissant l'attribut EnableClientFreeze du contrôle GridWeb sur false.

**Menu contextuel après avoir restreint les options de ligne et de colonne** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
