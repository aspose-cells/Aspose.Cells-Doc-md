---
title: Trouver si la valeur de la cellule commence par un guillemet simple avec Golang via C++
linktitle: Trouvez si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 270
url: /fr/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Apprenez comment vérifier si la valeur d une cellule commence par une marque de citation simple via l API Aspose.Cells for C++.
keywords: Trouver si la valeur de la cellule commence par un guillemet simple, Rechercher si la valeur de la cellule commence par un guillemet simple
---

{{% alert color="primary" %}}

Aspose.Cells fournit maintenant la propriété [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) pour déterminer si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de distinguer entre les chaînes comme échantillon et 'échantillon etc.

{{% /alert %}}

Le code d'exemple suivant explique que les chaînes comme échantillon et 'échantillon ne peuvent pas être différenciées avec la propriété [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Nous devons donc utiliser la propriété [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) pour les distinguer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
