---
title: Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement au format HTML
type: docs
weight: 20
url: /fr/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel au format HTML, Aspose.Cells révèle les commentaires conditionnels de niveau inférieur. Ces commentaires conditionnels concernent principalement les anciennes versions d'Internet Explorer et ne sont pas pertinents pour les navigateurs Web modernes. Vous pouvez les lire en détail sur le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé au niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells vous permet d'éliminer ces commentaires révélés de niveau inférieur en définissant le[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) propriété à**vrai**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement au format HTML**

L'exemple de code suivant montre l'utilisation de[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) propriété. La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie sur true. Veuillez télécharger le[exemple de fichier Excel](50528257.xlsx) utilisé dans ce code et le[sortie HTML](50528258.zip) généré par celui-ci pour une référence.

![tâche : image_autre_texte](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
