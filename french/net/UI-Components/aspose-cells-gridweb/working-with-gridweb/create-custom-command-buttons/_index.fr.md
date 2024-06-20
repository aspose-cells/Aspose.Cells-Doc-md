---
title: Créer des boutons de commande personnalisés
type: docs
weight: 100
url: /fr/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, commande, boutons de commande, personnalisation
description: Cet article explique comment créer des boutons de commande personnalisés dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contient des boutons spéciaux tels que **Soumettre**, **Enregistrer** et **Annuler**. Tous ces boutons effectuent des tâches spécifiques pour Aspose.Cells.GridWeb.
Il est également possible d'ajouter des boutons personnalisés qui effectuent des tâches personnalisées. Ce sujet explique comment utiliser cette fonctionnalité.

{{% /alert %}} 
## **Création de boutons de commande personnalisés**
Pour créer un bouton de commande personnalisé dans Aspose.Cells.GridWeb :

1. Ajouter le contrôle Aspose.Cells.GridWeb au formulaire Web.
1. Accéder à une feuille de calcul.
1. Créez une instance de la classe CustomCommandButton.
1. Définissez la commande du bouton sur une valeur. Cette valeur est utilisée dans le gestionnaire d'événements du bouton.
1. Définissez le texte du bouton.
1. Définissez l'URL de l'image du bouton.
1. Enfin, ajoutez l'objet CustomCommandButton à la collection CustomCommandButtons du contrôle GridWeb.

{{% alert color="primary" %}} 

Les boutons de commande personnalisés peuvent également être ajoutés en mode WYSIWYG à l'aide de la boîte de dialogue Propriétés de Visual Studio.

{{% /alert %}} 

La sortie de l'exemple de code est affichée ci-dessous :

**Un bouton de commande personnalisé ajouté au contrôle GridWeb** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Gestion d'événements du bouton de commande personnalisé**
L'aspect le plus important des boutons de commande personnalisés est l'action qu'ils effectuent lorsque vous cliquez dessus. Pour définir l'action, créez un gestionnaire d'événements pour l'événement CustomCommand du contrôle GridWeb.

L'événement CustomCommand est toujours déclenché lorsque vous cliquez sur un bouton de commande personnalisé. Le gestionnaire d'événements doit donc identifier le bouton de commande personnalisé spécifique auquel il s'applique en fonction de la commande définie lors de l'ajout du bouton au contrôle GridWeb. Enfin, ajoutez un code personnalisé qui est exécuté lorsque le bouton est cliqué.

Dans l'exemple de code ci-dessous, un message texte est ajouté à la cellule A1 lorsque le bouton est cliqué.

**Texte ajouté à la cellule A1 lors du clic sur le bouton de commande personnalisé** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
