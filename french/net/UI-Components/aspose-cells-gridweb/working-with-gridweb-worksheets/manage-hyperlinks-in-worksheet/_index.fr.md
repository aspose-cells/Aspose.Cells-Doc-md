---
title: Gérer les liens hypertexte dans la feuille de calcul
type: docs
weight: 100
url: /fr/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

Cette rubrique explique quels types de liens hypertexte sont pris en charge dans Aspose.Cells.GridWeb et comment les gérer par programme. Les hyperliens peuvent être utilisés pour créer des liens vers des URL Web ou pour effectuer une publication sur un serveur.

{{% /alert %}} 
## **Travailler avec des hyperliens**
### **Types d'hyperliens**
Généralement, les hyperliens suivants sont pris en charge par Aspose.Cells.GridWeb :

- [Liens hypertexte URL](/cells/fr/net/manage-hyperlinks-in-worksheet/), des hyperliens qui peuvent être liés à des URL Web.
- [Liens hypertexte de texte](/cells/fr/net/manage-hyperlinks-in-worksheet/), Liens hypertexte URL appliqués au texte.
- [Liens hypertexte des images](/cells/fr/net/manage-hyperlinks-in-worksheet/), liens hypertexte URL appliqués aux images.
- [Cell hyperliens de commande](/cells/fr/net/manage-hyperlinks-in-worksheet/), liens hypertexte qui envoient des données à un serveur. Ces hyperliens agissent davantage comme un bouton qui déclenche un événement côté serveur lorsqu'il est cliqué.

Les sections ci-dessous décrivent en détail l'utilisation de tous les types d'hyperliens. Il explique également comment accéder ou supprimer des liens.
### **Ajout d'hyperliens**

#### **Liens hypertexte URL**
Les hyperliens URL ressemblent davantage à de simples hyperliens que vous voyez normalement sur les sites Web. Un lien hypertexte URL fonctionne comme une ancre dans une cellule. Chaque fois qu'il est cliqué, il navigue vers une page Web ou ouvre une nouvelle fenêtre de navigateur.

Il existe différents types d'hyperliens URL :

- Liens hypertexte de texte.
- Liens hypertexte des images.

Les développeurs peuvent spécifier une image pour le lien hypertexte. Si une image n'est pas spécifiée, un lien hypertexte texte est créé ; sinon, un lien hypertexte vers l'image est créé.


##### **Liens hypertexte de texte**
Pour ajouter un lien hypertexte vers une feuille de calcul :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accéder à une feuille de calcul.
1. Ajoutez un lien hypertexte vers une cellule de la feuille de calcul.
1. Définissez le texte qui sera affiché dans la cellule.
1. Définissez l'URL du lien hypertexte.
1. Définissez la cible du lien hypertexte, si vous le souhaitez.
1. Définissez une info-bulle, si vous le souhaitez.

{{% alert color="primary" %}} 

 REMARQUE : La cible du lien hypertexte peut être définie sur_ soi,_top ou _parent pour ouvrir les URL Web respectivement dans une nouvelle fenêtre, la fenêtre actuelle ou la fenêtre supérieure.

{{% /alert %}} 

L'exemple ci-dessous ajoute deux liens hypertexte à une feuille de calcul. L'un n'a pas de cible tandis que l'autre est défini sur _parent.

**Sortie : liens hypertexte ajoutés à la feuille de calcul** 

![tâche : image_autre_texte](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Hyperliens d'images**
Pour ajouter un lien hypertexte vers une image :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accéder à une feuille de calcul.
1. Ajouter un lien hypertexte à une cellule.
1. Définissez l'URL de l'image qui sera affichée sous forme de lien hypertexte.
1. Définissez l'URL du lien hypertexte.
1. Définissez une info-bulle, si vous le souhaitez.
1. Définissez le texte du lien hypertexte, si vous le souhaitez.

**Sortie : liens hypertexte d'image ajoutés à la feuille de calcul** 

![tâche : image_autre_texte](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 La définition de l'AltText du lien hypertexte de l'image remplit une fonction similaire à la définition d'un<ALT> balise dans HTML. Le texte s'affiche uniquement si l'image hyperliée n'est pas affichée. (Par exemple, si l'image ne se trouve pas à l'emplacement spécifié.) Si l'image du deuxième lien hypertexte est introuvable, la sortie de l'extrait de code ci-dessous se présentera comme suit.

**L'image pour l'URL de l'image est introuvable** 

![tâche : image_autre_texte](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell Hyperliens de commande**
Un lien hypertexte de commande de cellule est un type spécial de lien hypertexte qui déclenche un événement côté serveur au lieu d'ouvrir une page Web. Les développeurs peuvent ajouter du code à l'événement côté serveur et effectuer n'importe quelle tâche lorsque le lien hypertexte est cliqué. Cette fonctionnalité permet aux développeurs de créer des applications plus interactives.

Pour ajouter un hyperlien de commande de cellule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accéder à une feuille de calcul.
1. Ajouter un lien hypertexte à une cellule.
1. Définissez la commande du lien hypertexte sur la valeur souhaitée.
 La valeur est utilisée par le gestionnaire d'événements du lien hypertexte pour le reconnaître.
1. Définissez une info-bulle, si vous le souhaitez.
1. Définissez l'URL de l'image qui sera affichée sous forme de lien hypertexte.

**Un lien hypertexte de commande de cellule a été ajouté à la feuille de calcul** 

![tâche : image_autre_texte](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Gestion des événements des hyperliens de commande Cell**
Les développeurs doivent créer un gestionnaire d'événements pour l'événement CellCommand du contrôle GridWeb afin d'effectuer des tâches spécifiques lorsqu'un lien hypertexte de commande de cellule spécifique est cliqué. Le gestionnaire d'événements de l'événement CellCommand fournit un objet de type CellEventArgs qui offre la propriété Argument. Utilisez la propriété Argument pour identifier un lien hypertexte spécifique en comparant sa valeur CellCommand.

L'exemple ci-dessous crée un gestionnaire d'événements pour le lien hypertexte de commande de cellule créé dans le code ci-dessus. Le CellCommand du lien hypertexte a été défini sur Click. Donc, dans le gestionnaire d'événements, vérifiez-le d'abord, puis ajoutez du code qui affiche un message dans la cellule A6.

Le gestionnaire d'événements est appelé lorsque le lien hypertexte est cliqué.

**Sortie : texte ajouté à la cellule A6 lorsque le lien hypertexte est cliqué** 

![tâche : image_autre_texte](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Accéder aux hyperliens**
Pour accéder à un lien hypertexte existant :

1. Accédez à la cellule qui le contient.
1. Obtenez la référence de la cellule.
1. Transmettez la référence à la méthode GetHyperlink de la collection Hyperlinks pour accéder au lien hypertexte.
1. Modifiez les propriétés du lien hypertexte.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Suppression des hyperliens**
Pour supprimer un lien hypertexte :

1. Accéder à la feuille de calcul active.
1. Supprimez un lien hypertexte à l'aide de la méthode Remove de la collection Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
