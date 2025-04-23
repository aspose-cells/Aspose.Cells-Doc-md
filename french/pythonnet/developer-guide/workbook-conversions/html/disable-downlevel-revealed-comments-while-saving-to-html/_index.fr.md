---
title: Désactiver les commentaires révélés de niveau inférieur lors de l enregistrement en HTML
type: docs
weight: 20
url: /fr/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel au format HTML, Aspose.Cells pour Python via .NET révèle des Commentaires Conditionnels en niveaux inférieurs. Ces commentaires conditionnels concernent principalement les anciennes versions d'Internet Explorer et sont sans pertinence pour les navigateurs modernes. Vous pouvez en lire les détails à l'adresse suivante.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells pour Python via .NET vous permet d’éliminer ces Commentaires Révélés en niveaux inférieurs en réglant la propriété [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) sur **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie sur true. Veuillez télécharger le [fichier Excel d'exemple](50528257.xlsx) utilisé dans ce code et le [HTML de sortie](50528258.zip) généré pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
