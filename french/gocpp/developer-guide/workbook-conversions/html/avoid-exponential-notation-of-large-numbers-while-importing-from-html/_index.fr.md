---
title: Éviter la notation exponentielle pour les grands nombres lors de l importation depuis HTML avec Golang via C++
linktitle: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
type: docs
weight: 10
url: /fr/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Apprenez comment éviter la notation exponentielle des grands nombres lors de l importation depuis HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, votre HTML contient des nombres comme 1234567890123456 qui ont plus de 15 chiffres, et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1.23457E+15. Si vous souhaitez que votre numéro soit importé tel quel et non converti en notation exponentielle, veuillez utiliser la propriété [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) et la définir sur **true** lors du chargement de votre HTML.

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la propriété [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/). L'API importera le nombre tel quel sans le convertir en notation exponentielle.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
