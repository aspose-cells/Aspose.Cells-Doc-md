---
title: Ta reda på om cellvärdet börjar med citattecken
type: docs
weight: 270
url: /sv/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Lär dig hur du hittar om cellvärdet börjar med ett enkelt citattecken genom Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Hitta cellvärde som börjar med ett enkelt citattecken, Sök cellvärde som börjar med ett enkelt citattecken i Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET erbjuder nu egenskapen [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) för att hitta om cellvärdet börjar med ett enkelt citattecken. Innan denna egenskap fanns det inget sätt att skilja mellan strängar som exempelvis 'sample och 'sample etc.

{{% /alert %}}

Följande exempelkod förklarar att strängar som exempelvis sample och 'sample inte kan skiljas åt med egenskapen [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/). Därför måste vi använda egenskapen [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) för att skilja dem åt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
