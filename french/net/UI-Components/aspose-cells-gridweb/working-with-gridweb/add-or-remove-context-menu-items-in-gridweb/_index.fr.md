---
title: Ajouter ou supprimer des éléments de menu contextuel dans GridWeb
type: docs
weight: 130
url: /fr/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

Vous pouvez ajouter des éléments de menu contextuel à l'aide du balisage ASP.NET ou du code .NET. Vous pouvez également supprimer des éléments de menu contextuel à l'aide du code .NET. Veuillez utiliser les méthodes GridWeb.CustomCommandButtons.Add() et GridWeb.CustomCommandButtons.Remove() ou RemoveAt() à ces fins.

{{% /alert %}} 
## **Ajouter un élément de menu contextuel à l'aide du balisage ASP.NET**
Le balisage ASP.NET suivant ajoute un élément de menu contextuel dans GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Voici le balisage ASP.NET complet qui crée un GridWeb avec l'élément de menu contextuel ci-dessus. Veuillez noter l'attribut OnCustomCommand="GridWeb1_CustomCommand". C'est le nom du gestionnaire d'événements qui sera appelé lorsque votre élément de menu contextuel sera cliqué.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Voici à quoi ressemble l'élément de menu contextuel après avoir été ajouté à l'aide du balisage ASP.NET ci-dessus.

![tâche : image_autre_texte](add-or-remove-context-menu-items-in-gridweb_1.png)

Il s'agit du code du gestionnaire d'événements qui est exécuté lorsque l'élément du menu contextuel est cliqué. Le code vérifie d'abord le nom de la commande, s'il correspond à notre commande, il ajoute un texte dans la cellule A1 de la feuille de calcul GridWeb active et définit la largeur de la première colonne sur 40 unités pour rendre le texte visible.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Voici à quoi ressemble le GridWeb lorsque vous cliquez sur l'élément de menu contextuel.

![tâche : image_autre_texte](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Ajouter des éléments de menu contextuel dans Aspose.Cells.GridWeb à l'aide de code**
Ce code montre comment ajouter un élément de menu contextuel dans un GridWeb à l'aide de code.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Supprimer les éléments du menu contextuel dans Aspose.Cells.GridWeb à l'aide de code**
Ce code montre comment supprimer un élément de menu contextuel à l'aide des méthodes CustomCommandButtons.Remove() et CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
