---
title: Trouvez si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 270
url: /fr/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Apprenez comment trouver si la valeur de la cellule commence par un guillemet simple via l API Aspose.Cells for .NET.
keywords: Trouver si la valeur de la cellule commence par un guillemet simple, Rechercher si la valeur de la cellule commence par un guillemet simple
---

{{% alert color="primary" %}}

Aspose.Cells fournit maintenant la propriété [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) pour déterminer si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de distinguer entre les chaînes comme échantillon et 'échantillon etc.

{{% /alert %}}

Le code d'exemple suivant explique que les chaînes comme échantillon et 'échantillon ne peuvent pas être différenciées avec la propriété [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue). Nous devons donc utiliser la propriété [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) pour les distinguer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
{{< app/cells/assistant language="csharp" >}}
