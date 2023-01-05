---
title: Travailler avec des feuilles de calcul GridWeb
type: docs
weight: 30
url: /fr/java/working-with-worksheets-gridweb/
---
## **Accéder aux feuilles de travail**

Cette rubrique décrit l'accès aux feuilles de calcul du contrôle GridWeb. Nous pouvons également appeler ces feuilles de calcul des feuilles de calcul Web car elles appartiennent à GridWeb et sont utilisées dans des applications Web.

Toutes les feuilles de calcul contenues dans le contrôle GridWeb sont stockées dans un GridWorksheetCollection du contrôle GridWeb. Il est simple d'accéder à une feuille de calcul particulière par son index de feuille.

Les développeurs peuvent accéder à une feuille de calcul spécifique en spécifiant son index de feuille, comme illustré ci-dessous dans l'exemple d'extrait de code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Suppression d'une feuille de calcul**

Cette rubrique fournit de brèves informations sur la suppression des feuilles de calcul des fichiers Excel Microsoft à l'aide de GridWeb API. Supprimez une feuille de calcul en spécifiant son index de feuille.

Les développeurs peuvent supprimer une feuille de calcul spécifique en spécifiant son index de feuille à l'aide de la méthode removeAt de la collection GridWorksheetCollection, comme illustré ci-dessous dans l'exemple d'extrait de code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Ajout de feuilles de calcul**

Les feuilles de travail font partie intégrante de GridWeb. Toutes les données sont gérées et stockées sous forme de feuilles de calcul. GridWeb permet aux développeurs d'ajouter une ou plusieurs feuilles de calcul au contrôle Aspose.Cells.GridWeb. Cette rubrique présente des approches simples pour ajouter des feuilles de calcul à GridWeb.

### **Sans spécifier le nom de la feuille**

Le moyen le plus simple d'ajouter une feuille de calcul à Aspose.Cells.GridWeb consiste à appeler la méthode d'ajout de la classe GridWorksheetCollection dans le contrôle GridWeb. Cela crée des feuilles de calcul qui utilisent des noms par défaut (c'est-à-dire Feuil1, Feuil2, Feuil3, etc.) et les ajoute au contrôle GridWeb.

**Sortie : une feuille de calcul avec un nom par défaut a été ajoutée à GridWeb** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Avec le nom de feuille spécifié**

Pour ajouter une feuille de calcul avec un nom spécifique au contrôle GridWeb au lieu d'utiliser le schéma de dénomination par défaut, appelez une version surchargée de la méthode add qui prend la chaîne spécifiée SheetName. Par exemple, l'exemple ci-dessous ajoute une feuille de calcul nommée Facture.

**Sortie : une feuille de calcul avec un nom spécifié a été ajoutée à GridWeb** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 La méthode add() renvoie l'index de la nouvelle feuille de calcul qui peut être utilisé pour accéder à l'instance de cette feuille de calcul. Pour plus de détails sur la façon d'accéder aux feuilles de calcul, lisez[Accéder aux feuilles de travail](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Renommer une feuille de calcul**

Renommer une feuille de calcul peut être très utile lorsque vous travaillez avec de nombreuses feuilles de calcul dans GridWeb et décidez de changer leurs noms pour les rendre plus significatifs. Par exemple, une feuille de calcul contenant une facture peut être renommée Facture au lieu de Feuille1. Cette rubrique décrit cette fonctionnalité simple mais utile.

### **Renommer une feuille de calcul**

Toutes les feuilles de calcul contiennent une propriété Name qui permet aux développeurs d'accéder ou de modifier les noms des feuilles de calcul. Pour renommer une feuille de calcul :

1. Accédez à une feuille de calcul à partir de GridWorksheetCollection.
1. Renommer la feuille de calcul sélectionnée.

{{% alert color="primary" %}}

 Pour plus de détails sur la façon d'accéder aux feuilles de calcul dans Aspose.Cells.GridWeb, veuillez vous référer à[Accéder aux feuilles de travail](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Avant d'exécuter le code, la feuille de calcul a un nom par défaut, tel que Sheet1.

**Fichier d'entrée : une feuille de calcul avec un nom par défaut Sheet1** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_3.png)

Après avoir exécuté le code, la feuille de calcul est renommée Facture.

**Sortie : la feuille de calcul est renommée Facture** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Copier une feuille de calcul**

[Ajout de feuilles de calcul](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)décrit comment ajouter de nouvelles feuilles de calcul à GridWeb. Il est également possible d'ajouter une copie (ou réplique) d'une autre feuille de calcul au contrôle Aspose.Cells.GridWeb. Cette fonctionnalité peut être utile lorsque des données identiques ou similaires dans une feuille de calcul sont également requises dans une autre feuille de calcul. Lorsque c'est le cas, il est plus facile de copier une feuille de calcul existante et de l'ajouter à Aspose.Cells.GridWeb en tant que nouvelle feuille de calcul au lieu de la créer à partir de zéro.

### **Utilisation de l'index de feuille**

L'exemple de code ci-dessous montre comment ajouter une copie d'une feuille de calcul au contrôle GridWeb en spécifiant l'index de la feuille de calcul dans la méthode addCopy de GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Utilisation du nom de la feuille**
L'exemple de code ci-dessous montre comment ajouter une copie d'une feuille de calcul au contrôle GridWeb en spécifiant le nom de la feuille de calcul dans la méthode addCopy de GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 La méthode addCopy renvoie l'index de la feuille de calcul nouvellement ajoutée qui peut être utilisée pour accéder à l'instance de la feuille de calcul. Pour plus de détails sur la façon d'accéder aux feuilles de calcul, lisez[Accéder aux feuilles de travail](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Travailler avec des plages nommées**

Normalement, les étiquettes de colonne et de ligne sont utilisées pour faire référence de manière unique aux cellules. Mais vous pouvez créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes.

 Le mot**Nom** peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Par exemple, utilisez des noms faciles à comprendre, tels que Products, pour faire référence à des plages difficiles à comprendre, telles que Sales!C20:C30.

 Les étiquettes peuvent être utilisées dans des formules faisant référence à des données sur la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom.**Plages nommées** est l'une des fonctionnalités les plus puissantes de Microsoft Excel.

Les utilisateurs peuvent attribuer un nom à une plage et utiliser ce nom dans des formules. Aspose.Cells.GridWeb prend en charge cette fonctionnalité.

### **Ajout/référencement de plages nommées dans les formules**

Le contrôle GridWeb fournit deux classes (GridName et GridNameCollection) pour travailler avec des plages nommées.

L'extrait de code suivant vous aidera à comprendre comment les utiliser.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Gestion des commentaires dans la feuille de calcul**

Cette rubrique traite de l'ajout, de l'accès et de la suppression de commentaires dans les feuilles de calcul. Les commentaires sont utiles pour ajouter des notes ou des informations utiles aux utilisateurs qui travailleront avec la feuille. Les développeurs ont la possibilité d'ajouter des commentaires à n'importe quelle cellule de la feuille de calcul.

### **Travailler avec des commentaires**

#### **Ajouter des commentaires**

Pour ajouter un commentaire à la feuille de calcul, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web.
1. Accédez à la feuille de calcul à laquelle vous ajoutez des commentaires.
1. Ajouter un commentaire à une cellule.
1. Définissez une note pour le nouveau commentaire.

**Un commentaire a été ajouté à la feuille de calcul** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Accéder aux commentaires**

Pour accéder à un commentaire :

1. Accédez à la cellule qui contient le commentaire.
1. Obtenez la référence de la cellule.
1. Transmettez la référence à la collection Comment pour accéder au commentaire.
1. Il est maintenant possible de modifier les propriétés du commentaire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Suppression de commentaires**

Pour supprimer un commentaire :

1. Accédez à la cellule comme expliqué ci-dessus.
1. Utilisez la méthode removeAt de la collection Comment pour supprimer le commentaire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Gestion des hyperliens dans la feuille de calcul**

Cette rubrique explique quels types de liens hypertexte sont pris en charge dans Aspose.Cells.GridWeb et comment les gérer par programme. Les hyperliens peuvent être utilisés pour créer des liens vers des URL Web ou pour effectuer une publication sur un serveur.

### **Types d'hyperliens**

Les hyperliens suivants sont pris en charge par Aspose.Cells.GridWeb :

- Liens hypertexte URL du texte, liens hypertexte URL appliqués au texte.
- Liens hypertexte URL d'image, liens hypertexte URL appliqués aux images.

#### **Liens hypertexte d'URL de texte**

 L'exemple ci-dessous ajoute deux liens hypertexte à une feuille de calcul. L'un a un_ cible vide tandis que l'autre est réglé sur_parent.

![tâche : image_autre_texte](working-with-worksheets-gridweb_6.png)

**Sortie : liens hypertexte ajoutés à la feuille de calcul**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Liens hypertexte d'URL d'image**

L'exemple ci-dessous ajoute un lien hypertexte URL d'image à une feuille de calcul.

![tâche : image_autre_texte](working-with-worksheets-gridweb_7.png)

**Sortie : lien hypertexte vers l'image ajouté à la feuille de calcul**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Tri des données**

Le tri est une fonctionnalité très précieuse lorsqu'il s'agit de traitement de données. Les données non triées sont pénibles pour les utilisateurs lorsqu'ils recherchent des informations spécifiques. Aspose.Cells.GridWeb prend en charge de puissantes fonctionnalités de tri. Cette rubrique traite du tri des données à l'aide de Aspose.Cells.GridWeb API.

Aspose.Cells.GridWeb permet aux développeurs de trier les données horizontalement et verticalement afin que les développeurs puissent trier les données de haut en bas ou de gauche à droite.

### **Du haut jusqu'en bas**

Pour trier les données de haut en bas :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la feuille de calcul que vous souhaitez trier.
1. Triez la plage de données dans n'importe quel ordre (croissant ou décroissant). Assurez-vous de sélectionner l'orientation de haut en bas.

L'exemple ci-dessous trie les données dans deux colonnes (ID étudiant et Nom de l'étudiant) d'une feuille de calcul par ordre croissant. Seules douze lignes de deux colonnes sont triées de haut en bas.

Avant d'appliquer le code, la feuille de calcul contient des données non ordonnées.

**Entrée : données non triées** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_8.png)

Après l'exécution du code, les données sont triées par ordre croissant.

**Sortie : données triées de haut en bas par ordre croissant** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **De gauche à droite**

Pour trier les données de gauche à droite :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la feuille de calcul que vous souhaitez trier.
1. Triez la plage de données dans n'importe quel ordre (croissant ou décroissant). Assurez-vous de sélectionner de gauche à droite.

L'exemple ci-dessous trie les données sur deux lignes (ID étudiant et Nom de l'étudiant) par ordre croissant. Seules deux lignes de quatre colonnes sont triées de gauche à droite.

Avant d'appliquer le code, la feuille de calcul contient des données non ordonnées.

**Entrée : données non triées avant l'exécution de l'extrait de code** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_10.png)

Après l'exécution du code, les données sont triées par ordre croissant.

**Sortie : données triées de gauche à droite par ordre croissant** 

![tâche : image_autre_texte](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Recherche et remplacement**

L'un des moyens les plus rapides d'apporter des modifications répétitives dans une grande feuille de calcul consiste à utiliser la fonction Rechercher et remplacer. Find vous aide à localiser une chaîne de texte ou des données et replace les remplace par une nouvelle valeur. Aspose.Cells.GridWeb fournit cette fonctionnalité. Il vous permet de rechercher et de remplacer par une chaîne de texte ou une valeur spécifique dans la feuille de calcul côté client via une simple boîte de dialogue. Il vous permet même de rechercher des données partielles.

### **La boîte de dialogue Rechercher/Remplacer**

Il existe deux manières d'ouvrir la boîte de dialogue Rechercher/Remplacer :

1.  Lorsque la commande est active, appuyez sur**CTRL+F** pour ouvrir la boîte de dialogue, ou appuyez sur**CTRL+R** touche pour ouvrir la boîte de dialogue avec la**Remplacer** bouton activé.
1.  Déplacez le curseur vers la zone de cellule dans la feuille de calcul, puis cliquez avec le bouton droit. Sélectionner**Trouver** ou alors**Remplacer** du menu.

**Sélection de Rechercher**

![tâche : image_autre_texte](working-with-worksheets-gridweb_12.png)

Une boîte de dialogue Rechercher et remplacer s'affiche.

**La boîte de dialogue Rechercher/Remplacer**

![tâche : image_autre_texte](working-with-worksheets-gridweb_13.png)

**Utilisation de la recherche**

Chercher:

1. Ouvrez la boîte de dialogue Rechercher/Remplacer.
1. Tapez la chaîne que vous souhaitez rechercher dans le champ Rechercher.
1. Cliquez sur Rechercher suivant pour rechercher.

La cellule suivante qui correspond à votre condition de recherche est mise en surbrillance.

{{% alert color="primary" %}}

Si votre critère de recherche n'est pas trouvé, une boîte de dialogue s'affiche pour vous le signaler.

{{% /alert %}}

### **Options de recherche**

Vous pouvez personnaliser certaines options de recherche dans la boîte de dialogue. Le tableau ci-dessous les répertorie.

|**Non.**|**Nom de l'option**|**Description**|
|:- |:- |:- |
|1|Cas de correspondance|Indique s'il faut utiliser la sensibilité à la casse dans la recherche.|
|2|Correspond à un mot entier|Indique s'il faut faire correspondre le mot entier dans la recherche.|
|3|Rechercher|Indique si la recherche se fera de bas en haut.|
|4|Expression régulière|Lorsque cette case est cochée, le contrôle traite la chaîne dans la zone de texte Rechercher comme une expression régulière dans le processus de recherche.|
|5|Rechercher dans les formules/valeurs|Lorsque les formules sont sélectionnées, le contrôle correspondra à la formule ou à la valeur non formatée des cellules si la formule ou la valeur non formatée est présente. Lorsque les valeurs sont sélectionnées, le contrôle ne correspondra qu'à la valeur affichée des cellules.|

### **Utiliser Remplacer**

Pour remplacer du texte ou des valeurs :

1.  Ouvrez la boîte de dialogue Rechercher/Remplacer en appuyant sur**CTRL+F** , ou cliquez avec le bouton droit sur une cellule et sélectionnez**Trouver** avant de cliquer**Remplacer**.
1.  Tapez la chaîne de remplacement dans le champ**Remplacer par**domaine.
1.  Cliquez sur**Remplacer**.

Pour remplacer du texte :

1. Ouvrez la boîte de dialogue.
1.  Entrez le texte que vous souhaitez rechercher dans le**Trouver quoi** champ, et le texte que vous souhaitez remplacer dans le**Remplacer par** domaine.
1.  Remplacez une occurrence à la fois en cliquant sur**Rechercher suivant** suivie par**Remplacer**.
1.  Si vous êtes sûr du contenu de la feuille de calcul, cliquez sur**Remplace tout**.

{{% alert color="primary" %}}

 Si la feuille de calcul n'est pas en mode édition, le**Remplacer** le bouton ne s'affiche pas.

{{% /alert %}}

## Ajouter/supprimer des hyperliens côté client

Aspose.Cells GridWeb prend désormais en charge l'ajout et la suppression d'hyperliens côté client. Pour cela, le API met à disposition les fonctions "addCelllink" et "delCelllink". Les extraits de code suivants illustrent l'ajout et la suppression d'hyperliens côté client dans GridWeb.

### Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Vous pouvez également créer un lien vers la feuille à l'aide de l'extrait de code suivant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Mettre à jour les paramètres de police du côté client

Aspose.Cells GridWeb prend désormais en charge la modification des paramètres de police du côté client. Pour cela, le API propose les fonctions suivantes

- **mettre à jourCellFontStyle**: Params - r/i/b/ib pour regular/italic/bold/italic&&bold
- **mettre à jourCellFontSize**: Params - nom de la police, etc. 'Système'
- **updateCellFontName**: Paramètres - taille de la police, etc. '12pt'
- **updateCellFontColor**: Params - none/u/l/ul/ for none/underline/barré/underline&&barré
- **updateCellFontLine**: Params - couleur html comme #aa22ee ou nom de couleur bien connu comme vert, rouge,...
- **updateCellBackGroundColor**: Params - couleur html comme #aa22ee ou nom de couleur bien connu comme vert, rouge,...

L'extrait de code suivant illustre la modification des paramètres de police du côté client dans GridWeb.

### Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Ajouter/supprimer des commentaires du côté client

Aspose.Cells GridWeb prend désormais en charge l'ajout et la suppression de commentaires côté client. Pour cela, le API met à disposition les fonctions "addcomments" et "delcomments". L'extrait de code suivant illustre l'ajout et la suppression de commentaires côté client dans GridWeb.

### Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Afficher les boutons pour ajouter/supprimer des feuilles de calcul

 Aspose.Cells GridWeb prend désormais en charge l'ajout et la suppression de feuilles à l'aide des boutons de la barre d'outils. Pour que les boutons soient visibles sur le frontend, vous devez définir**GridWeb1.ShowAddButton** à**vrai**. L'extrait de code suivant illustre l'ajout de boutons Ajouter/Supprimer à la barre d'outils GridWeb.

### Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
