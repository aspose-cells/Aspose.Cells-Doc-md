---
title: Gérer les hyperliens dans la feuille de calcul
type: docs
weight: 100
url: /fr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb, hyperlien
description: Cet article présente comment travailler avec les hyperliens dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet traite des types de hyperliens pris en charge dans Aspose.Cells.GridWeb et de comment les gérer de manière programmable. Les hyperliens peuvent être utilisés soit pour créer des liens vers des URL Web, soit pour effectuer un retour au serveur.

{{% /alert %}} 
## **Travailler avec les hyperliens**
### **Types de hyperliens**
Généralement, les types d'hyperliens suivants sont pris en charge par Aspose.Cells.GridWeb :

- [Hyperliens URL](/cells/fr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), des hyperliens pouvant être liés à des URL Web.
- [Hyperliens textuels](/cells/fr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hyperliens URL appliqués au texte.
- [Hyperliens d'images](/cells/fr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), hyperliens URL appliqués aux images.
- [Hyperliens de commande de cellule](/cells/fr/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), des hyperliens qui transmettent des données à un serveur. De tels hyperliens agissent davantage comme un bouton qui déclenche un événement côté serveur lorsqu'il est cliqué.

Les sections ci-dessous décrivent en détail l'utilisation de tous les types d'hyperliens. Il discute également de l'accès ou de la suppression des liens.
### **Ajout de liens hypertexte**

#### **Hyperliens URL**
Les hyperliens URL ressemblent davantage à des hyperliens simples que vous voyez normalement sur les sites Web. Un hyperlien URL fonctionne comme une ancre dans une cellule. Chaque fois qu'il est cliqué, il navigue vers une page Web ou ouvre une nouvelle fenêtre de navigateur.

Il existe différents types d'hyperliens URL :

- Hyperliens textuels.
- Hyperliens d'images.

Les développeurs peuvent spécifier une image pour l'hyperlien. Si aucune image n'est spécifiée, un hyperlien textuel est créé ; sinon, un hyperlien d'image est créé.


##### **Liens hypertextes de texte**
Pour ajouter un lien hypertexte à un classeur :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accéder à une feuille de calcul.
1. Ajoutez un lien hypertexte à une cellule de la feuille de calcul.
1. Définissez le texte qui sera affiché dans la cellule.
1. Définissez l'URL du lien hypertexte.
1. Définissez la cible du lien hypertexte, si désiré.
1. Définissez une info-bulle, si désiré.

{{% alert color="primary" %}} 

REMARQUE : La cible du lien hypertexte peut être définie sur _self, _top ou _parent pour ouvrir les URL web dans une nouvelle, la fenêtre actuelle ou la fenêtre principale respectivement.

{{% /alert %}} 

L'exemple ci-dessous ajoute deux liens hypertextes à une feuille de calcul. L'un n'a pas de cible, tandis que l'autre est défini sur _parent.

**Sortie : hyperliens de texte ajoutés à la feuille de calcul** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Liens hypertextes d'image**
Pour ajouter un lien hypertexte d'image :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accéder à une feuille de calcul.
1. Ajoutez un lien hypertexte à une cellule.
1. Définissez l'URL de l'image qui sera affichée en tant que lien hypertexte.
1. Définissez l'URL du lien hypertexte.
1. Définissez une info-bulle, si désiré.
1. Définissez le texte du lien hypertexte, si désiré.

**Résultat: des liens hypertexte d'image ajoutés à la feuille de calcul** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**L'image pour l'URL de l'image n'a pas pu être trouvée.** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Liens hypertexte de commandes de cellules**
Un lien hypertexte de commande de cellule est un type spécial de lien hypertexte qui déclenche un événement côté serveur au lieu d'ouvrir une page web. Les développeurs peuvent ajouter du code à l'événement côté serveur et effectuer n'importe quelle tâche lorsque le lien hypertexte est cliqué. Cette fonctionnalité permet aux développeurs de créer des applications plus interactives.

Pour ajouter un lien hypertexte de commande de cellule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accéder à une feuille de calcul.
1. Ajoutez un lien hypertexte à une cellule.
1. Définissez la commande du lien hypertexte à n'importe quelle valeur désirée.
   La valeur est utilisée par le gestionnaire d'événements du lien hypertexte pour le reconnaître.
1. Définissez une info-bulle, si désiré.
1. Définissez l'URL de l'image qui sera affichée sous forme de lien hypertexte.

**Un lien hypertexte de commande de cellule a été ajouté à la feuille de calcul** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Gestion des événements des liens hypertexte de commandes de cellules**
Les développeurs doivent créer un gestionnaire d'événements pour l'événement CellCommand du contrôle GridWeb afin d'effectuer des tâches spécifiques lorsqu'un lien hypertexte de commande de cellule spécifique est cliqué. Le gestionnaire d'événements de l'événement CellCommand fournit un objet de type CellEventArgs qui offre la propriété Argument. Utilisez la propriété Argument pour identifier un lien hypertexte spécifique en comparant sa valeur de commande de cellule.

L'exemple ci-dessous crée un gestionnaire d'événements pour le lien hypertexte de commande de cellule créé dans le code ci-dessus. La commande de cellule du lien hypertexte a été définie sur Clic. Donc, dans le gestionnaire d'événements, vérifiez d'abord cela et ajoutez ensuite du code qui affiche un message dans la cellule A6.

Le gestionnaire d'événements est invoqué lorsque le lien hypertexte est cliqué.

**Résultat: texte ajouté à la cellule A6 lorsque le lien hypertexte est cliqué** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Accès aux liens hypertexte**
Pour accéder à un hyperlien existant :

1. Accédez à la cellule qui le contient.
1. Obtenez la référence de la cellule.
1. Transmettez la référence à la méthode GetHyperlink de la collection Hyperlinks pour accéder à l'hyperlien.
1. Modifiez les propriétés de l'hyperlien.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Suppression des hyperliens**
Pour supprimer un hyperlien :

1. Accédez à la feuille de calcul active.
1. Supprimez un hyperlien à l'aide de la méthode Remove de la collection Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
