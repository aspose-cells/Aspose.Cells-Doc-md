---
title: Ajouter ou supprimer des éléments de menu contextuel dans GridWeb
type: docs
weight: 130
url: /fr/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb,menu du contexte,menu
description: Cet article présente comment ajouter ou supprimer des éléments de menu contextuel dans GridWeb.
---

{{% alert color="primary" %}} 

Vous pouvez ajouter des éléments de menu contextuel en utilisant le balisage ASP.NET ou en utilisant le code .NET. Vous pouvez également supprimer des éléments de menu contextuel en utilisant le code .NET. Veuillez utiliser les méthodes GridWeb.CustomCommandButtons.Add() et GridWeb.CustomCommandButtons.Remove() ou RemoveAt() à cet effet.

{{% /alert %}} 
## **Ajouter un élément de menu contextuel en utilisant le balisage ASP.NET**
Le balisage ASP.NET suivant ajoute un élément de menu contextuel dans GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Voici le balisage ASP.NET complet qui crée un GridWeb avec l'élément de menu contextuel ci-dessus. Veuillez noter l'attribut OnCustomCommand="GridWeb1_CustomCommand". C'est le nom du gestionnaire d'événements qui sera appelé lorsque votre élément de menu contextuel sera cliqué.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Voici à quoi ressemble l'élément de menu contextuel après avoir été ajouté en utilisant le balisage ASP.NET ci-dessus.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Ceci est le code du gestionnaire d'événements qui est exécuté lorsque l'élément de menu contextuel est cliqué. Le code vérifie d'abord le nom de la commande, s'il correspond à notre commande, il ajoute un texte dans la cellule A1 de la feuille de calcul GridWeb active et règle la largeur de la première colonne à 40 unités pour rendre le texte visible.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Voici à quoi ressemble le GridWeb lorsque vous cliquez sur l'élément de menu contextuel.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Ajouter des éléments de menu contextuel dans Aspose.Cells.GridWeb en utilisant du code**
Ce code montre comment ajouter un élément de menu contextuel à l'intérieur d'un GridWeb en utilisant du code.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Supprimer des éléments de menu contextuel dans Aspose.Cells.GridWeb en utilisant du code**
Ce code montre comment supprimer un élément de menu contextuel en utilisant les méthodes CustomCommandButtons.Remove() et CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
