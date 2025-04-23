---
title: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
type: docs
weight: 600
url: /fr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

Parfois, votre HTML contient des nombres comme 1234567890123456 qui sont plus longs que 15 chiffres et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1,23457E+15. Si vous voulez que votre nombre soit importé tel quel et non converti en notation exponentielle, veuillez utiliser la propriété [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) et la définir à **true** lors du chargement de votre HTML.

{{% /alert %}} 
## **Éviter la notation exponentielle des grands nombres lors de l'importation depuis HTML**
Le code d'exemple suivant explique l'utilisation de la propriété [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision). Il importera le nombre tel quel sans le convertir en notation exponentielle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
{{< app/cells/assistant language="java" >}}
