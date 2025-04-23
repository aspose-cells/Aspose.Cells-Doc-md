---
title: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
type: docs
weight: 10
url: /fr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

Parfois, votre HTML contient des nombres comme 1234567890123456 qui sont plus longs que 15 chiffres et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1.23457E+15. Si vous voulez que votre nombre soit importé tel quel et non converti en notation exponentielle, alors veuillez utiliser la propriété [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) et la définir à **true** lors du chargement de votre HTML.

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la propriété [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision). L'API importera le nombre tel quel sans le convertir en notation exponentielle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
