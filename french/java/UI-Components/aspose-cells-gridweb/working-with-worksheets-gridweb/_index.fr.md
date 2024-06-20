---
title: Travailler avec les feuilles de calcul GridWeb
type: docs
weight: 30
url: /fr/java/working-with-worksheets-gridweb/
---

## **Accéder aux feuilles de calcul**

Ce sujet traite de l'accès aux feuilles de calcul du contrôle GridWeb. Nous pouvons aussi appeler ces feuilles de calcul des feuilles de calcul web car elles appartiennent à GridWeb et sont utilisées dans les applications web.

Toutes les feuilles de calcul contenues dans le contrôle GridWeb sont stockées dans une GridWorksheetCollection du contrôle GridWeb. Il est simple d'accéder à une feuille de calcul particulière par son index de feuille.

Les développeurs peuvent accéder à une feuille de calcul spécifique en spécifiant son index de feuille comme démontré ci-dessous dans un exemple de code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Suppression d'une feuille de calcul**

Ce sujet fournit des informations succinctes sur la suppression de feuilles de calcul à partir de fichiers Microsoft Excel en utilisant l'API GridWeb. Supprimez une feuille de calcul en spécifiant son index de feuille.

Les développeurs peuvent supprimer une feuille de calcul spécifique en spécifiant son index de feuille à l'aide de la méthode removeAt de la collection GridWorksheetCollection, comme le montre l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Ajout de feuilles de calcul**

Les feuilles de calcul sont une partie intégrante de GridWeb. Toutes les données sont gérées et stockées sous forme de feuilles de calcul. GridWeb permet aux développeurs d'ajouter une ou plusieurs feuilles de calcul au contrôle Aspose.Cells.GridWeb. Ce sujet montre des approches simples pour ajouter des feuilles de calcul à GridWeb.

### **Sans spécifier le nom de la feuille**

La manière la plus simple d'ajouter une feuille de calcul à Aspose.Cells.GridWeb est d'appeler la méthode add de la classe GridWorksheetCollection dans le contrôle GridWeb. Cela crée des feuilles de calcul qui utilisent des noms par défaut (c'est-à-dire Feuille1, Feuille2, Feuille3, etc.) et les ajoute au contrôle GridWeb.

**Sortie : une feuille de calcul avec un nom par défaut a été ajoutée à GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Avec un nom de feuille spécifié**

Pour ajouter une feuille de calcul avec un nom spécifique au contrôle GridWeb au lieu d'utiliser le schéma de nommage par défaut, appelez une version surchargée de la méthode add qui prend la chaîne spécifiée NomFeuille. Par exemple, l'exemple ci-dessous ajoute une feuille de calcul nommée Facture.

**Sortie : une feuille de calcul avec un nom spécifié a été ajoutée à GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

La méthode add() renvoie l'index de la nouvelle feuille de calcul qui peut être utilisé pour accéder à l'instance de cette feuille de calcul. Pour plus de détails sur l'accès aux feuilles de calcul, consultez [Accéder aux feuilles de calcul](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Renommer une feuille de calcul**

Renommer une feuille de calcul peut être très utile lorsqu'on travaille avec de nombreuses feuilles de calcul dans GridWeb et qu'on décide de changer leurs noms pour les rendre plus significatifs. Par exemple, une feuille de calcul contenant une facture peut être renommée Facture au lieu de Feuille1. Ce sujet décrit cette fonction simple mais utile.

### **Renommer une feuille de calcul**

Toutes les feuilles de calcul contiennent une propriété Nom qui permet aux développeurs d'accéder ou de modifier les noms des feuilles de calcul. Pour renommer une feuille de calcul :

1. Accédez à une feuille de calcul à partir de la collection GridWorksheet.
1. Renommez la feuille de calcul sélectionnée.

{{% alert color="primary" %}}

Pour plus de détails sur l'accès aux feuilles de calcul dans Aspose.Cells.GridWeb, veuillez vous référer à [Accéder aux feuilles de calcul](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Avant d'exécuter le code, la feuille de calcul a un nom par défaut, tel que Feuille1.

**Fichier d'entrée : une feuille de calcul avec un nom par défaut Feuille1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Après l'exécution du code, la feuille de calcul est renommée Facture.

**Sortie: la feuille de calcul est renommée Facture** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Copier une feuille de calcul**

[Ajout de feuilles de calcul](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets) décrit comment ajouter de nouvelles feuilles de calcul à GridWeb. Il est également possible d'ajouter une copie (ou réplique) d'une autre feuille de calcul au contrôle Aspose.Cells.GridWeb. Cette fonctionnalité peut être utile lorsque des données identiques ou similaires dans une feuille de calcul sont également requises dans une autre feuille de calcul. Dans ce cas, il est plus facile de copier une feuille de calcul existante et de l'ajouter à Aspose.Cells.GridWeb en tant que nouvelle feuille de calcul au lieu de la créer à partir de zéro.

### **Utilisation de l'index de feuille**

Le code d'exemple ci-dessous montre comment ajouter une copie d'une feuille de calcul au contrôle GridWeb en spécifiant l'index de la feuille de calcul dans la méthode addCopy de la collection GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Utilisation du nom de la feuille**
Le code d'exemple ci-dessous montre comment ajouter une copie d'une feuille de calcul au contrôle GridWeb en spécifiant le nom de la feuille de calcul dans la méthode addCopy de la collection GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

La méthode addCopy renvoie l'index de la feuille de calcul nouvellement ajoutée qui peut être utilisé pour accéder à l'instance de la feuille de calcul. Pour plus de détails sur la façon d'accéder aux feuilles de calcul, consultez [Accéder aux feuilles de calcul](/cells/fr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Travailler avec des plages nommées**

Normalement, les étiquettes de colonnes et de lignes sont utilisées pour faire référence de manière unique aux cellules. Mais vous pouvez créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes.

Le mot **nom** peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Par exemple, utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des plages difficiles à comprendre, telles que Ventes!C20:C30.

Les étiquettes peuvent être utilisées dans des formules qui font référence à des données dans la même feuille de calcul; si vous voulez représenter une plage dans une autre feuille de calcul, vous pouvez utiliser un nom. Les **plages nommées** sont l'une des fonctionnalités les plus puissantes de Microsoft Excel.

Les utilisateurs peuvent attribuer un nom à une plage et utiliser ce nom dans des formules. Aspose.Cells.GridWeb prend en charge cette fonctionnalité.

### **Ajout/Référence de plages nommées dans des formules**

Le contrôle GridWeb fournit deux classes (GridName et GridNameCollection) pour travailler avec les plages nommées.

Le snippet de code suivant vous aidera à comprendre comment les utiliser.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Gestion des commentaires dans la feuille de calcul**

Ce sujet traite de l'ajout, de l'accès et de la suppression de commentaires dans les feuilles de calcul. Les commentaires sont utiles pour ajouter des notes ou des informations utiles aux utilisateurs qui travailleront avec la feuille. Les développeurs ont la flexibilité d'ajouter des commentaires à n'importe quelle cellule de la feuille de calcul.

### **Travailler avec des commentaires**

#### **Ajout de commentaires**

Pour ajouter un commentaire à la feuille de calcul, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web.
1. Accédez à la feuille de calcul à laquelle vous souhaitez ajouter des commentaires.
1. Ajoutez un commentaire à une cellule.
1. Définissez une note pour le nouveau commentaire.

**Un commentaire a été ajouté à la feuille de calcul** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Accéder aux commentaires**

Pour accéder à un commentaire :

1. Accédez à la cellule qui contient le commentaire.
1. Obtenez la référence de la cellule.
1. Passez la référence à la collection de commentaires pour accéder au commentaire.
1. Il est désormais possible de modifier les propriétés du commentaire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Supprimer les Commentaires**

Pour supprimer un commentaire :

1. Accédez à la cellule comme expliqué ci-dessus.
1. Utilisez la méthode removeAt de la collection de commentaires pour supprimer le commentaire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Gestion des hyperliens dans la feuille de calcul**

Ce sujet traite des types de hyperliens pris en charge dans Aspose.Cells.GridWeb et de comment les gérer de manière programmable. Les hyperliens peuvent être utilisés soit pour créer des liens vers des URL Web, soit pour effectuer un retour au serveur.

### **Types de hyperliens**

Les hyperliens suivants sont pris en charge par Aspose.Cells.GridWeb :

- Hyperliens URL de texte, hyperliens URL appliqués au texte.
- Hyperliens URL d'image, hyperliens URL appliqués aux images.

#### **Hyperliens URL de texte**

L'exemple ci-dessous ajoute deux hyperliens à une feuille de calcul. L'un a une cible _blank tandis que l'autre est réglé sur _parent.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Sortie : hyperliens de texte ajoutés à la feuille de calcul**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Hyperliens d'image URL**

L'exemple ci-dessous ajoute un hyperlien d'image URL à une feuille de calcul.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Sortie : lien d'image ajouté à la feuille de calcul**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Tri de données**

Le tri est une fonctionnalité très précieuse en matière de traitement des données. Les données non triées sont une douleur pour les utilisateurs lorsqu'ils recherchent des informations spécifiques. Aspose.Cells.GridWeb prend en charge de puissantes fonctionnalités de tri. Ce sujet traite du tri des données en utilisant l'API Aspose.Cells.GridWeb.

Aspose.Cells.GridWeb permet aux développeurs de trier des données horizontalement et verticalement afin que les développeurs puissent trier des données de haut en bas ou de gauche à droite.

### **De haut en bas**

Pour trier les données de haut en bas :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la feuille de calcul que vous souhaitez trier.
1. Triez la plage de données dans n'importe quel ordre (croissant ou décroissant). Assurez-vous de sélectionner l'orientation de haut en bas.

L'exemple ci-dessous trie les données de deux colonnes (ID de l'élève et nom de l'élève) d'une feuille de calcul par ordre croissant. Seules douze lignes de deux colonnes sont triées dans l'orientation de haut en bas.

Avant d'appliquer le code, la feuille de calcul contient des données non triées.

**Entrée : données non triées** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Après l'exécution du code, les données sont triées par ordre croissant.

**Sortie : données triées de haut en bas par ordre croissant** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **De gauche à droite**

Pour trier les données de gauche à droite :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la feuille de calcul que vous souhaitez trier.
1. Triez la plage de données dans n'importe quel ordre (croissant ou décroissant). Assurez-vous de sélectionner de gauche à droite.

L'exemple ci-dessous trie les données en deux lignes (ID de l'étudiant et Nom de l'étudiant) par ordre croissant. Seules deux lignes sur quatre colonnes sont triées de gauche à droite.

Avant d'appliquer le code, la feuille de calcul contient des données non triées.

**Entrée : données non triées avant l'exécution de l'extrait de code** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Après l'exécution du code, les données sont triées par ordre croissant.

**Sortie : données triées de gauche à droite par ordre croissant** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Recherche et Remplacement**

Un des moyens les plus rapides pour apporter des modifications répétitives dans une grande feuille de calcul est d'utiliser la fonction de recherche et de remplacement. La fonction de recherche vous aide à localiser une chaîne de texte ou des données et le remplacement la substitue par une nouvelle valeur. Aspose.Cells.GridWeb fournit cette fonctionnalité. Elle vous permet de rechercher et de remplacer une chaîne de texte spécifique ou une valeur dans le client de feuille de calcul via une boîte de dialogue simple. Elle vous permet même de rechercher une donnée partielle.

### **La boîte de dialogue Rechercher/Remplacer**

Il y a deux façons d'ouvrir la boîte de dialogue Rechercher/Remplacer :

1. Lorsque le contrôle est actif, appuyez sur **CTRL+F** pour ouvrir la boîte de dialogue, ou appuyez sur la touche **CTRL+R** pour ouvrir la boîte de dialogue avec le bouton **Remplacer** activé.
1. Déplacez le curseur vers la zone de cellule dans la feuille de calcul, puis faites un clic droit. Sélectionnez **Rechercher** ou **Remplacer** dans le menu.

**Sélection de Rechercher**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

Une boîte de dialogue de recherche et de remplacement s'affiche.

**La boîte de dialogue Rechercher/Remplacer**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Utiliser la fonction Rechercher**

Pour rechercher:

1. Ouvrez la boîte de dialogue Rechercher/Remplacer.
1. Tapez la chaîne que vous souhaitez rechercher dans le champ Rechercher.
1. Cliquez sur Suivant pour rechercher.

La prochaine cellule correspondant à votre critère de recherche est mise en surbrillance.

{{% alert color="primary" %}}

Si votre critère de recherche n'est pas trouvé, une boîte de dialogue s'affiche pour vous informer.

{{% /alert %}}

### **Options de Recherche**

Il existe des options de recherche que vous pouvez personnaliser dans la boîte de dialogue. Le tableau ci-dessous les répertorie.

|**No.**|**Nom de l'Option**|**Description**|
| :- | :- | :- |
|1|Respecter la casse|Indique s'il faut respecter la casse lors de la recherche.|
|2|Correspondance mot entier|Indique s'il faut rechercher le mot entier lors de la recherche.|
|3|Recherche ascendante|Indique si la recherche se fera du bas vers le haut.|
|4|Expression régulière|Lorsque cochée, le contrôle traitera la chaîne dans le champ Rechercher comme une expression régulière lors du processus de recherche.|
|5|Rechercher dans Formules/Valeurs|Quand Formules est sélectionné, le contrôle fera correspondre la formule ou la valeur non formatée des cellules si la formule ou la valeur non formatée est présente. Quand Valeurs est sélectionné, le contrôle fera correspondre uniquement la valeur affichée des cellules.|

### **Utilisation de Remplacer**

Pour remplacer du texte ou des valeurs:

1. Ouvrez la boîte de dialogue Rechercher/Remplacer en appuyant sur **CTRL+F**, ou sélectionnez un clic droit sur une cellule et sélectionnez **Rechercher** avant de cliquer sur **Remplacer**.
1. Tapez la chaîne de remplacement dans le champ **Remplacer par**.
1. Cliquez sur **Remplacer**.

Pour remplacer le texte :

1. Ouvrez la boîte de dialogue.
1. Entrez le texte que vous souhaitez trouver dans le champ **Rechercher** et le texte que vous souhaitez remplacer dans le champ **Remplacer par**.
1. Remplacez une occurrence à la fois en cliquant sur **Suivant** suivi de **Remplacer**.
1. Si vous êtes très sûr de ce que contient la feuille de calcul, cliquez sur **Remplacer tout**.

{{% alert color="primary" %}}

Si la feuille de calcul n'est pas en mode édition, le bouton **Remplacer** n'est pas affiché.

{{% /alert %}}

## Ajouter/Supprimer des hyperliens côté client

Aspose.Cells GridWeb prend désormais en charge l'ajout et la suppression d'hyperliens côté client. Pour cela, l'API fournit les fonctions "addCelllink" et "delCelllink". Les extraits de code suivants démontrent comment ajouter et supprimer des hyperliens côté client dans GridWeb.

### Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Vous pouvez également lier une feuille en utilisant l'extrait de code suivant.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Mettre à jour les paramètres de police depuis le côté client

Aspose.Cells GridWeb prend désormais en charge la modification des paramètres de police depuis le côté client. Pour cela, l'API fournit les fonctions suivantes

- **updateCellFontStyle**: Params - r/i/b/ib pour régulier/italique/gras/italique&&gras
- **updateCellFontSize**: Params - nom de la police, etc. 'Système'
- **updateCellFontName**: Params - taille de police, etc. '12pt'
- **updateCellFontColor**: Params - none/u/l/ul/ pour aucun/souligner/barré/souligner&&barré
- **updateCellFontLine**: Params - couleur HTML comme #aa22ee ou nom de couleur bien connu comme vert, rouge, ...
- **updateCellBackGroundColor**: Params - couleur HTML comme #aa22ee ou nom de couleur bien connu comme vert, rouge, ...

Les extraits de code suivants démontrent la modification des paramètres de police depuis le côté client dans GridWeb.

### Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Ajouter/Supprimer des commentaires côté client

Aspose.Cells GridWeb prend maintenant en charge l'ajout et la suppression de commentaires côté client. Pour cela, l'API fournit les fonctions "addcomments" et "delcomments". L'extrait de code suivant illustre l'ajout et la suppression de commentaires côté client dans GridWeb.

### Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Afficher les boutons pour ajouter/supprimer des feuilles de calcul

Aspose.Cells GridWeb prend désormais en charge l'ajout et la suppression de feuilles en utilisant des boutons dans la barre d'outils. Pour que les boutons soient visibles côté frontal, vous devez définir **GridWeb1.ShowAddButton** sur **true**. L'extrait de code suivant illustre l'ajout de boutons Ajouter/Supprimer à la barre d'outils de GridWeb.

### Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
