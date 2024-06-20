---
title: Désactiver les commentaires révélés de niveau inférieur lors de l enregistrement en HTML
type: docs
weight: 20
url: /fr/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**
Lorsque le fichier Excel est converti en HTML, Aspose.Cells ajoute des commentaires conditionnels révélés de niveau inférieur dans le fichier HTML de sortie. Ces commentaires conditionnels sont principalement liés aux anciennes versions d'Internet Explorer et sont inutiles dans les navigateurs modernes. Pour plus d'informations sur les commentaires conditionnels révélés de niveau inférieur, veuillez visiter le lien suivant

[Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://fr.wikipedia.org/wiki/Commentaire_conditionnel#Commentaire_conditionnel_révélé_de_niveau_inférieur)

Pour supprimer les commentaires conditionnels révélés de niveau inférieur, Aspose.Cells propose la propriété [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments). Définir la propriété [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) sur **True** supprimera les commentaires conditionnels révélés de niveau inférieur dans le fichier HTML de sortie.

L'image suivante montre les commentaires conditionnels révélés de niveau inférieur qui seront supprimés dans le fichier HTML de sortie

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
