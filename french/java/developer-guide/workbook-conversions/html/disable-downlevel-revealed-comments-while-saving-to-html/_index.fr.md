---
title: Désactiver les commentaires de niveau inférieur révélés lors de l'enregistrement au HTML
type: docs
weight: 20
url: /fr/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel dans HTML, Aspose.Cells révèle les commentaires conditionnels de niveau inférieur. Ces commentaires conditionnels concernent principalement les anciennes versions d'Internet Explorer et ne sont pas pertinents pour les navigateurs Web modernes. Vous pouvez les lire en détail sur le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé au niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells vous permet d'éliminer ces commentaires révélés de niveau inférieur en définissant le[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)propriété à**vrai**.

## **Désactiver les commentaires de niveau inférieur révélés lors de l'enregistrement au HTML**

L'exemple de code suivant montre l'utilisation de[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)la propriété. La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie sur**vrai**. Veuillez télécharger le[exemple de fichier Excel](50528267.xlsx)utilisé dans ce code et le[sortie HTML](50528266.zip)fichier généré par celui-ci pour une référence.

![tâche : image_autre_texte](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
