---
title: Évitez la notation exponentielle des grands nombres lors de l'importation à partir de HTML
type: docs
weight: 600
url: /fr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

Parfois, votre HTML contient des nombres comme 1234567890123456 qui sont plus longs que 15 chiffres et lorsque vous importez votre HTML dans un fichier Excel, ces nombres sont convertis en notation exponentielle comme 1.23457E+15. Si vous le souhaitez, votre nombre doit être importé tel quel et non converti en notation exponentielle, alors veuillez utiliser[HtmlLoadOptions.KeepPrecisionHtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) propriété et définissez-la**vrai** lors du chargement de votre HTML.

{{% /alert %}} 
## **Évitez la notation exponentielle des grands nombres lors de l'importation à partir de HTML**
 L'exemple de code suivant explique l'utilisation de[HtmlLoadOptions.KeepPrecisionHtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)la propriété. Il importera le nombre tel qu'il est sans le convertir en notation exponentielle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
