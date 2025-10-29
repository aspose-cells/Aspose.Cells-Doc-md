---
title: Désactiver la révélation des commentaires de niveau inférieur lors de l enregistrement en HTML avec Golang via C++
linktitle: Désactiver les commentaires révélés en mode dégradé
type: docs
weight: 20
url: /fr/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Éliminer les commentaires de niveau inférieur lors de l enregistrement des fichiers Excel en HTML en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

 Lorsque vous enregistrez votre fichier Excel en HTML, Aspose.Cells révèle les commentaires conditionnels en mode dégradé. Ces commentaires conditionnels concernent principalement les anciennes versions d’Internet Explorer et sont sans intérêt pour les navigateurs Web modernes. Vous pouvez en savoir plus en détail via le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

 Aspose.Cells vous permet d’éliminer ces commentaires révélés en mode dégradé en réglant la propriété [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) à **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

 Le code d'exemple ci-dessous montre l’utilisation de la propriété [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée à true. Veuillez télécharger le [fichier Excel d'exemple](50528257.xlsx) utilisé dans ce code ainsi que le [HTML généré](50528258.zip) pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
