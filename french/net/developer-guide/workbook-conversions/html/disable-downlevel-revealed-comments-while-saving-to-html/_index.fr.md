---
title: Désactiver les commentaires révélés de niveau inférieur lors de l enregistrement en HTML
type: docs
weight: 20
url: /fr/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel au format HTML, Aspose.Cells révèle les commentaires conditionnels de niveau inférieur. Ces commentaires conditionnels sont principalement pertinents pour les anciennes versions d'Internet Explorer et sont hors de propos pour les navigateurs Web modernes. Vous pouvez en savoir plus à leur sujet en détail via le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells vous permet d'éliminer ces commentaires révélés de niveau inférieur en définissant la propriété [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) sur **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie sur true. Veuillez télécharger le [fichier Excel d'exemple](50528257.xlsx) utilisé dans ce code et le [HTML de sortie](50528258.zip) généré pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
