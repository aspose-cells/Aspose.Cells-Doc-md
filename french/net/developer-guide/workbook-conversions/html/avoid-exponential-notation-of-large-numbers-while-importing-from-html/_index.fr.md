---
title: Évitez la notation exponentielle des grands nombres lors de l'importation depuis HTML
type: docs
weight: 10
url: /fr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 Parfois, votre Html contient des nombres comme 1234567890123456 qui sont plus longs que 15 chiffres et lorsque vous importez votre HTML dans un fichier Excel, ces nombres sont convertis en notation exponentielle comme 1.23457E+15. Si vous le souhaitez, votre nombre doit être importé tel quel et non converti en notation exponentielle, alors veuillez utiliser[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) propriété et définissez-la**vrai** lors du chargement de votre HTML.

{{% /alert %}}

 L'exemple de code suivant explique l'utilisation de[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)propriété. Le API importera le nombre tel qu'il est sans le convertir en notation exponentielle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
