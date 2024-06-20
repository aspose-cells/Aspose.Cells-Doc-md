---
title: Slå samman filer
type: docs
weight: 20
url: /sv/net/merge-files/
---

## **Introduktion**

Aspose.Cells tillhandahåller olika sätt att sammanfoga filer. För enkla filer med data, formatering och formler kan metoden [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) användas för att kombinera flera arbetsböcker, och metoden [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) kan användas för att kopiera arkmallar till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att kombinera kanske du upptäcker att de tar mycket systemresurser. För att undvika detta, använd den statiska metoden [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles), ett mer effektivt sätt att sammanfoga flera filer.

## **Slå samman filer med hjälp av Aspose.Cells**

Följande kodexempel illustrerar hur man sammanfogar stora filer med hjälp av metoden [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles). Den tar två enkla men stora filer, Book1.xls och Book2.xls. Filerna innehåller bara formaterad data och formler.

{{% alert color="primary" %}}

Metoden [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) stöder endast sammanfogning av data, format, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte sammanfogas med denna metod. Dessutom används en cachelagrad fil för att lagra tillfälliga data för processen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
