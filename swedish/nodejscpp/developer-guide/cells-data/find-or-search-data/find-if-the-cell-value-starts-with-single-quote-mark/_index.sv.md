---
title: Ta reda på om cellvärdet börjar med citattecken
type: docs
weight: 270
url: /sv/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Lär dig hur du i hitta om cellvärdet börjar med ett enkelt citattecken via API et Aspose.Cells for Node.js via C++.
keywords: Hitta cellvärde som börjar med ett enkelt citattecken Node.js via C++, Sök cellvärde som börjar med ett enkelt citattecken Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller nu [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)-metoden för att ta reda på om cellvärdet börjar med ett enkelt citattecken. Innan denna funktion fanns det inget sätt att skilja mellan strängar som sample och 'sample' osv.

{{% /alert %}}

Följande exempel förklarar att strängar som sample och 'sample' inte kan skiljas med [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)-metoden. Därför måste vi använda [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)-metoden för att särskilja dem.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
