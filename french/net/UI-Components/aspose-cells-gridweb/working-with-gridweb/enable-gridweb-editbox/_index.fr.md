---
title: Activer GridWeb EditBox
type: docs
weight: 110
url: /fr/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

La zone d'édition de GridWeb est une barre d'outils affichée en haut du contrôle que vous pouvez utiliser pour voir/saisir ou copier des données/formules dans des cellules. Il affiche également le nom de la cellule que vous modifiez. Après avoir cliqué sur le cadre ou lorsque vous commencez à écrire des données ou tapez un symbole égal (=), la zone d'édition sera activée.

{{% /alert %}} 
## **Définition de la zone d'édition de Aspose.Cells.GridWeb**
Le contrôle GridWeb fournit la propriété ShowCellEditBox à laquelle les développeurs peuvent l'affecter à "True" pour activer la barre d'outils. La valeur par défaut de l'attribut est False. Lorsque vous définissez sa valeur sur "True", la zone d'édition apparaît en haut du contrôle GridWeb.

{{% alert color="primary" %}} 

 Pour activer cette fonctionnalité, vous devez importer le fichier "jquery.js" dans votre projet et le référencer dans votre ou vos pages .aspx pour le faire fonctionner. Vous pouvez télécharger l'archive jQuery à partir de<https://jqueryui.com/download/all/> et placez le ou les fichiers de bibliothèque dans un dossier du projet et ajoutez une référence au fichier de bibliothèque via<script> tag dans votre formulaire Web .aspx comme suit. Toutes les dernières versions de jQuery sont OK.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Contrôle GridWeb avec zone d'édition** 

![tâche : image_autre_texte](enable-gridweb-editbox_1.png)
### **Exemple**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
