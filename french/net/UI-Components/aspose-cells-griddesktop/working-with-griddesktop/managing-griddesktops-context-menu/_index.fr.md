---
title: Gestion du menu contextuel de GridDesktops
type: docs
weight: 40
url: /fr/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop a un menu contextuel qui contient toutes les commandes couramment utilisées. Le contrôle vous permet de masquer/afficher les éléments de menu. De plus, il est possible d'ajouter de nouveaux éléments de menu avec des gestionnaires d'événements au menu.

{{% /alert %}} 
## **Introduction**
La classe ContextMenuManager est utilisée pour gérer les éléments du menu contextuel. L'attribut GridDesktop.ContextMenuManager obtient l'instance de l'objet ContextMenuManager. Par exemple, l'attribut ContextMenuManager.MenuItemAvailable_Copy obtient ou définit une valeur indiquant si l'élément de menu contextuel **Copy** est disponible ou non. De même, nous avons tous les attributs correspondants pour différents éléments de menu contextuel.

**IMPORTANT:** Par défaut, tous les éléments du menu contextuel sont visibles dans la liste.
## **Gestion du menu contextuel**
### **Masquer les éléments du menu contextuel**
Pour effectuer cette tâche, nous examinons d'abord le menu contextuel par défaut de GridDesktop.

**Menu par défaut de GridDeskop** 

![tâche : image_autre_texte](managing-griddesktops-context-menu_1.png)

Maintenant, masquez certains éléments de menu en utilisant le code ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Après avoir exécuté le code ci-dessus, certains éléments de menu ne seront pas visibles pour les utilisateurs :

**Certains éléments de menu sont masqués** 

![tâche : image_autre_texte](managing-griddesktops-context-menu_2.png)
### **Ajout de nouveaux éléments de menu**
Ajoutez un nouvel élément de menu contextuel à la liste à l'aide de l'extrait de code suivant.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Nous spécifions également un gestionnaire d'événements pour la nouvelle commande/option.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Après avoir exécuté le code ci-dessus, un nouvel élément de menu peut être vu dans le menu contextuel. Un message apparaîtra également lorsque la cellule est cliqué.

**Un nouvel élément de menu est ajouté à la liste** 

![tâche : image_autre_texte](managing-griddesktops-context-menu_3.png)
