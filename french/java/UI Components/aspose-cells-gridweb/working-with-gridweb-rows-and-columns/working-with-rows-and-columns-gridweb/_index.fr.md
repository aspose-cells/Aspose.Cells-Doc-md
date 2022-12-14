---
title: Travailler avec des lignes et des colonnes GridWeb
type: docs
weight: 20
url: /fr/java/working-with-rows-and-columns-gridweb/
---
## **Insertion de lignes et de colonnes**
Cette rubrique explique comment insérer de nouvelles lignes et colonnes dans une feuille de calcul à l'aide de Aspose.Cells.GridWeb API. Des lignes ou des colonnes peuvent être insérées à n'importe quelle position dans la feuille de calcul.
### **Insertion de lignes**
Pour insérer une ligne à n'importe quel endroit d'une feuille de calcul :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web ou à la page.
1. Accédez à la feuille de calcul à laquelle vous ajoutez des lignes.
1. Insérez une ligne en spécifiant un index de ligne où la ligne serait insérée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Insertion de colonnes**
Pour insérer une colonne à n'importe quel endroit d'une feuille de calcul :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web ou à une page.
1. Accédez à la feuille de calcul à laquelle vous ajoutez des colonnes.
1. Insérez une colonne en spécifiant l'index de colonne où la colonne serait insérée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Vous pouvez également utiliser les méthodes insertRows()/insertColumns() pour insérer plusieurs lignes/colonnes dans les feuilles de calcul en conséquence.

{{% /alert %}} 
## **Suppression de lignes et de colonnes**
Cette rubrique montre comment supprimer des lignes et des colonnes d'une feuille de calcul à l'aide de Aspose.Cells.GridWeb API. Avec l'aide de cette fonctionnalité, les développeurs peuvent supprimer des lignes ou des colonnes lors de l'exécution.
### **Suppression de lignes**
Pour supprimer une ligne de votre feuille de calcul :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web ou à une page.
1. Accédez à la feuille de calcul dont vous souhaitez supprimer des lignes.
1. Supprimez une ligne de la feuille de calcul en spécifiant son index de ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Suppression de colonnes**
Pour supprimer une colonne de votre feuille de calcul :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web ou à une page.
1. Accédez à la feuille de calcul dont vous souhaitez supprimer les colonnes.
1. Supprimez une colonne de la feuille de calcul en spécifiant son index de colonne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Définition de la hauteur de ligne et de la largeur de colonne**
Parfois, les valeurs des cellules sont plus larges que la cellule dans laquelle elles se trouvent ou se trouvent sur plusieurs lignes. Ces valeurs ne sont pas entièrement visibles pour les utilisateurs, sauf si elles modifient la hauteur et la largeur des lignes et des colonnes. Aspose.Cells.GridWeb prend entièrement en charge la définition des hauteurs de ligne et de la largeur de colonne. Cette rubrique décrit ces fonctionnalités en détail à l'aide d'exemples.
### **Travailler avec les hauteurs de ligne et la largeur de colonne**
#### **Définition de la hauteur de ligne**
Pour définir la hauteur d'une ligne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire/page Web.
1. Accédez à la collection GridCells de la feuille de calcul.
1. Définissez la hauteur de toutes les cellules dans n'importe quelle ligne spécifiée.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb accepte les mesures de hauteur de ligne et de largeur de colonne en points, pouces, pixels, etc.

{{% /alert %}} 

**Sortie : la hauteur de la 1ère ligne a été définie sur 50 points** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Définition de la largeur de colonne**
Pour définir la largeur d'une colonne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire/page Web.
1. Accédez à la collection GridCells de la feuille de calcul.
1. Définissez la largeur de toutes les cellules dans une colonne spécifiée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Personnalisation des en-têtes de ligne et de colonne**
Comme Microsoft Excel, Aspose.Cells.GridWeb utilise également des en-têtes ou des légendes standard pour les lignes (numéros comme 1, 2, 3, etc.) et les colonnes (alphabétiques comme A, B, C, etc.). Aspose.Cells.GridWeb permet également de personnaliser les légendes. Cette rubrique traite de la personnalisation des en-têtes de ligne et de colonne lors de l'exécution à l'aide de Aspose.Cells.GridWeb API.
### **Personnalisation de l'en-tête de ligne**
Pour personnaliser l'en-tête ou la légende d'une ligne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à une page Web Form/.
1. Accédez à la feuille de calcul dans GridWorksheetCollection.
1. Définissez la légende de toute ligne spécifiée.

**Les en-têtes des lignes 1 et 2 ont été personnalisés** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Personnalisation de l'en-tête de colonne**
Pour personnaliser l'en-tête ou la légende d'une colonne :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à une page Web Form/.
1. Accédez à la feuille de calcul dans GridWorksheetCollection.
1. Définissez la légende de toute colonne spécifiée.

**Les en-têtes des colonnes 1 et 2 ont été personnalisés** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Geler et dégeler des lignes et des colonnes**
Cette rubrique explique comment figer et libérer des lignes et des colonnes. Le gel des colonnes ou des lignes permet aux utilisateurs de garder les en-têtes de colonne ou les titres de ligne visibles pendant qu'ils font défiler vers d'autres parties de la feuille de calcul. Cette fonctionnalité est très utile lorsque vous travaillez avec des feuilles de calcul contenant de gros volumes de données. Lorsque les utilisateurs font défiler, seules les données défilent vers le bas et les en-têtes restent en place, ce qui facilite la lecture de la date. La fonctionnalité de volets figés n'est prise en charge que dans Internet Explorer 6.0 ou supérieur.
### **Figer les lignes et les colonnes**
Pour figer un nombre spécifique de lignes et de colonnes :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à une page Web Form/.
1. Accéder à une feuille de calcul.
1. Geler un certain nombre de lignes et de colonnes.

{{% alert color="primary" %}} 

 Il est également possible de figer un nombre spécifique de lignes et de colonnes à l'aide de l'interface. Cliquez avec le bouton droit sur une cellule où vous souhaitez figer les lignes et les colonnes et sélectionnez**Gel** de la liste.

{{% /alert %}} 

**Lignes et colonnes à l'état figé** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Dégeler les lignes et les colonnes**
Pour dégeler des lignes et des colonnes :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à une page Web Form/.
1. Accéder à une feuille de calcul.
1. Libérez les lignes et les colonnes.

**Feuille de travail après avoir été dégelée** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Protection des lignes et des colonnes**
Cette rubrique présente quelques techniques de protection des cellules dans les lignes et les colonnes contre tout type d'action effectuée par les utilisateurs finaux. Les développeurs peuvent implémenter cette protection en utilisant deux techniques : en rendant les cellules des lignes et des colonnes en lecture seule, ou en limitant les options du menu contextuel de GridWeb.
### **Restreindre les options du menu contextuel**
GridWeb fournit un menu contextuel que les utilisateurs finaux peuvent utiliser pour effectuer des opérations sur le contrôle. Le menu propose de nombreuses options pour manipuler les cellules, les lignes et les colonnes.

**Options contextuelles complètes** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_6.png)

Il est possible de restreindre tout type d'opérations côté client sur les lignes et les colonnes en limitant les options disponibles dans le menu contextuel. Cela peut être fait en définissant les attributs EnableClientColumnOperations et EnableClientRowOperations du contrôle GridWeb sur false. Il est également possible d'empêcher les utilisateurs de geler des lignes et des colonnes en définissant l'attribut EnableClientFreeze du contrôle GridWeb sur false.

**Menu contextuel après avoir restreint les options de ligne et de colonne** 

![tâche : image_autre_texte](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
