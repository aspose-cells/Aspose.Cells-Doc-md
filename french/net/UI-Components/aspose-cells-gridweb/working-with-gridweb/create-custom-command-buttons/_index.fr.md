---
title: Créer des boutons de commande personnalisés
type: docs
weight: 100
url: /fr/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb contient des boutons spéciaux comme**Nous faire parvenir**, **Sauver** et**annuler**. Tous ces boutons effectuent des tâches spécifiques pour Aspose.Cells.GridWeb.
Il est également possible d'ajouter des boutons personnalisés qui effectuent des tâches personnalisées. Cette rubrique explique comment utiliser cette fonctionnalité.

{{% /alert %}} 
## **Création de boutons de commande personnalisés**
Pour créer un bouton de commande personnalisé dans Aspose.Cells.GridWeb :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web.
1. Accéder à une feuille de calcul.
1. Créez une instance de la classe CustomCommandButton.
1. Définissez la commande du bouton sur une certaine valeur. Cette valeur est utilisée dans le gestionnaire d'événements du bouton.
1. Définissez le texte du bouton.
1. Définissez l'URL de l'image du bouton.
1. Enfin, ajoutez l'objet CustomCommandButton à la collection CustomCommandButtons du contrôle GridWeb.

{{% alert color="primary" %}} 

Des boutons de commande personnalisés peuvent également être ajoutés en mode WYSIWYG à l'aide de la boîte de dialogue Propriétés de Visual Studio.

{{% /alert %}} 

La sortie de l'extrait de code est illustrée ci-dessous :

**Un bouton de commande personnalisé ajouté au contrôle GridWeb** 

![tâche : image_autre_texte](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Gestion des événements du bouton de commande personnalisé**
L'aspect le plus important des boutons de commande personnalisés est l'action qu'ils effectuent lorsqu'ils sont cliqués. Pour définir l'action, créez un gestionnaire d'événements pour l'événement CustomCommand du contrôle GridWeb.

L'événement CustomCommand est toujours déclenché lorsqu'un bouton de commande personnalisé est cliqué. Ainsi, le gestionnaire d'événements doit identifier le bouton de commande personnalisé spécifique auquel il s'applique par le jeu de commandes lors de l'ajout du bouton au contrôle GridWeb. Enfin, ajoutez un code personnalisé qui est exécuté lorsque le bouton est cliqué.

Dans l'exemple de code ci-dessous, un message texte est ajouté à la cellule A1 lorsque le bouton est cliqué.

**Texte ajouté à la cellule A1 lorsque le bouton de commande personnalisé est cliqué** 

![tâche : image_autre_texte](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
