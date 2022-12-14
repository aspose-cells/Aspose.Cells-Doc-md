---
title: Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement au format HTML
type: docs
weight: 20
url: /fr/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement au format HTML**
Lorsque le fichier Excel est converti en HTML, Aspose.Cells ajoute des commentaires conditionnels de niveau inférieur dans le fichier HTML de sortie. Ces commentaires conditionnels concernent principalement les anciennes versions d'Internet Explorer et ne sont pas pertinents dans les navigateurs modernes. Pour plus d'informations sur les commentaires conditionnels révélés au niveau inférieur, veuillez visiter le lien suivant

[Commentaire conditionnel - Commentaire conditionnel révélé au niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Pour supprimer les commentaires conditionnels révélés par Downlevel, Aspose.Cells fournit le[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)propriété. Réglage de la[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) propriété à**Vrai**supprimera les commentaires conditionnels révélés par Downlevel dans le fichier HTML de sortie.

L'image suivante montre les commentaires conditionnels révélés par Downlevel qui seront supprimés dans le fichier HTML de sortie

![tâche : image_autre_texte](Disable-Downlevel-Revealed-Comments.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
