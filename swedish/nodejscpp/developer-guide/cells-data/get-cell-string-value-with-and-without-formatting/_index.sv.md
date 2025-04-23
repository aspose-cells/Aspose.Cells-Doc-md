---
title: Hämta cellsträngvärde med och utan formatering
type: docs
weight: 240
url: /sv/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Lär dig hur du får cellens strängvärde med och utan formatering via Aspose.Cells for Node.js via C++ API.
keywords: Hämta cellens strängvärde med och utan formatering Node.js via C++, Hämta cellens strängvärde med och utan formatering Node.js via C++, Hämta cellens strängvärde med och utan formatering Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en metod [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) som kan användas för att få cellens strängvärde med eller utan formatering. Anta att du har en cell med värdet 0.012345 och att du har format den för att visa endast två decimaler. Då visas den som 0.01 i Excel. Du kan hämta strängvärden både som 0.01 och som 0.012345 med hjälp av [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)-metoden. Den tar enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) som parameter med följande värden.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Följande kodexempel förklarar användningen av [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)-metoden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

