---
title: Hitta om cellvärdet börjar med enkel citattecken med Golang via C++
linktitle: Ta reda på om cellvärdet börjar med citattecken
type: docs
weight: 270
url: /sv/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Lär dig hur du hittar om cellvärdet börjar med ett enkelt citattecken via API et Aspose.Cells for C++.
keywords: Hitta cellvärde som börjar med ett enkelt citattecken, Sök cellvärde som börjar med ett enkelt citattecken
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller nu egenskapen [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) för att hitta om cellvärdet börjar med ett enkelt citattecken. Innan denna egenskap fanns det inget sätt att skilja mellan strängar som exempelvis sample och 'sample osv.

{{% /alert %}}

Följande exempelkod förklarar att strängar som exempelvis sample och 'sample inte kan skiljas åt med egenskapen [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Därför måste vi använda egenskapen [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) för att skilja dem åt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
