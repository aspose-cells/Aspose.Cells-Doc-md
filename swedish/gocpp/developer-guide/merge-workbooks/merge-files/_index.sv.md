---
title: Sammanfoga filer med Golang via C++
linktitle: Slå samman filer
type: docs
weight: 20
url: /sv/go-cpp/merge-files/
description: Lär dig hur du effektivt sammanfogar Excel filer med Aspose.Cells for C++.
---

## **Introduktion**

Aspose.Cells tillhandahåller olika metoder för att slå ihop filer. För enkla filer med data, formatering och formler kan [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/)-metoden användas för att kombinera flera arbetsböcker, och [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/)-metoden för att kopiera kalkylblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att sammanfoga kan du märka att de tar mycket systemresurser. För att undvika detta, använd den [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) statiska metoden, ett mer effektivt sätt att slå ihop flera filer.

## **Slå samman filer med hjälp av Aspose.Cells**

Följande kodexempel visar hur man sammanfogar stora filer med [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/)-metoden. Det tar två enkla men stora filer, Book1.xls och Book2.xls. Filmerna innehåller endast formaterad data och formler.

{{% alert color="primary" %}}

Metoden [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) stöder endast sammanslagning av data, stilar, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte kan slås samman med denna metod. Dessutom används en cache-fil för att lagra tillfällig data för processen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
