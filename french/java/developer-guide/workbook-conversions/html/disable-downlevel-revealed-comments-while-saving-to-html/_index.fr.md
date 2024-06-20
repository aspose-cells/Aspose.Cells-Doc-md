---
title: Désactiver les commentaires révélés de niveau inférieur lors de l enregistrement en HTML
type: docs
weight: 20
url: /fr/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, alors Aspose.Cells révèle des commentaires conditionnels de bas niveau. Ces commentaires conditionnels sont principalement pertinents pour les anciennes versions d'Internet Explorer et sont sans objet pour les navigateurs Web modernes. Vous pouvez en savoir plus à leur sujet en détail sur le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells vous permet d'éliminer ces commentaires révélés de bas niveau en définissant la [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) propriété sur **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

L'exemple de code suivant montre l'utilisation de la propriété [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie sur **true**. Veuillez télécharger le [fichier Excel d'exemple](50528267.xlsx) utilisé dans ce code et le [fichier HTML de sortie](50528266.zip) généré pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
