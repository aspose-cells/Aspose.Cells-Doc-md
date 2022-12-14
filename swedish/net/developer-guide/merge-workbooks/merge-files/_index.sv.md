---
title: Slå samman filer
type: docs
weight: 20
url: /sv/net/merge-files/
---
## **Introduktion**

 Aspose.Cells ger olika sätt att sammanfoga filer. För enkla filer med data, formatering och formler,[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) metod kan användas för att kombinera flera arbetsböcker, och[**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)metod kan användas för att kopiera arbetsblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att slå samman kan du upptäcka att de tar mycket systemresurser. För att undvika detta, använd[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)statisk metod, ett mer effektivt sätt att slå samman flera filer.

## **Slå ihop filer med Aspose.Cells**

 Följande exempelkod illustrerar hur man slår ihop stora filer med hjälp av[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)metod. Det krävs två enkla men stora filer, Book1.xls och Book2.xls. Filerna innehåller endast formaterade data och formler.

{{% alert color="primary" %}}

 De[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) Metoden stöder endast sammanslagning av data, stilar, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte slås samman med den här metoden. Dessutom används en cachad fil för att lagra temporär data för processen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
