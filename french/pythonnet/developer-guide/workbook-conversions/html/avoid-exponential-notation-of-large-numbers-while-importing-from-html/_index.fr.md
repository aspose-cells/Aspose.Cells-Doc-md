---
title: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
type: docs
weight: 10
url: /fr/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Ce sujet vous montre comment éviter la notation exponentielle des grands nombres lors de l importation à partir du HTML en utilisant Aspose.Cells pour Python via NET.
keywords: Éviter la notation exponentielle des grands nombres lors de l importation à partir du HTML, conserver la précision lors de l importation du html.
---

{{% alert color="primary" %}}

Parfois, votre HTML contient des nombres comme 1234567890123456 qui sont plus longs que 15 chiffres et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1.23457E+15. Si vous voulez que votre nombre soit importé tel quel et non converti en notation exponentielle, alors veuillez utiliser la propriété [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) et la définir à **true** lors du chargement de votre HTML.

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la propriété [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/). L'API importera le nombre tel quel sans le convertir en notation exponentielle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
