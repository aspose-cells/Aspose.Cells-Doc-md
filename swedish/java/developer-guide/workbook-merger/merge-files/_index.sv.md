---
title: Slå samman filer
type: docs
weight: 10
url: /sv/java/merge-files/
---
## **Introduktion**

 Aspose.Cells ger olika sätt att sammanfoga filer. För enkla filer med data, formatering och formler,[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) ) metod kan användas för att kombinera flera arbetsböcker, och[**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)metod kan användas för att kopiera arbetsblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att slå samman kan du upptäcka att de tar mycket systemresurser. För att undvika detta, använd den statiska metoden CellsHelper.mergeFiles, ett mer effektivt sätt att slå samman flera filer.

## **Slå ihop filer med Aspose.Cells**

Följande exempelkod illustrerar hur man slår samman stora filer med metoden CellsHelper.mergeFiles. Det krävs två enkla men stora filer, MyBook1.xls och MyBook2.xls. Filerna innehåller endast formaterade data och formler.

{{% alert color="primary" %}}

Metoden CellsHelper.mergeFiles stöder endast sammanslagning av data, stilar, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte slås samman med den här metoden. Dessutom används en cachad fil för att lagra temporär data för processen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
