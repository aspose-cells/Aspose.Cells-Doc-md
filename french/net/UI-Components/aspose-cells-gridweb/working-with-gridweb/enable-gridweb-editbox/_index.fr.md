---
title: Activer la boîte de modification de GridWeb
type: docs
weight: 110
url: /fr/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, éditeur, barre de formules
description: Cet article présente comment travailler avec la barre de formules ou l éditeur dans GridWeb.
---

{{% alert color="primary" %}} 

La boîte de modification de GridWeb (appelée barre de formules dans Excel) est une barre d'outils qui est rendue en haut du contrôle et que vous pouvez utiliser pour afficher ou saisir une valeur ou copier des données/formules pour la cellule sélectionnée. Elle affiche également le nom de la cellule que vous modifiez. Après avoir cliqué sur le cadre ou lorsque vous commencez à écrire des données ou à taper un symbole égal (=), la boîte de modification sera activée.

{{% /alert %}} 
## **Définition de la boîte de modification de Aspose.Cells.GridWeb**
Le contrôle GridWeb fournit la propriété ShowCellEditBox à laquelle les développeurs peuvent l'assigner à "True" pour l'activer. La valeur par défaut de l'attribut est False. Lorsque vous définissez sa valeur sur "True", la boîte de modification apparaîtra en haut du contrôle GridWeb.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Contrôle GridWeb avec zone de saisie** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Exemple**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
