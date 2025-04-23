---
title: Slå samman filer
type: docs
weight: 10
url: /sv/java/merge-files/
---

## **Introduktion**

Aspose.Cells erbjuder olika sätt för att slå ihop filer. För enkla filer med data, formatering och formler kan metoden [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) användas för att kombinera flera arbetsböcker, och [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-) metod kan användas för att kopiera kalkylblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att slå ihop kan du upptäcka att de tar mycket systemresurser. För att undvika detta, använd static-metoden CellsHelper.mergeFiles, en mer effektiv metod för att slå ihop flera filer.

## **Slå samman filer med hjälp av Aspose.Cells**

Följande exempelkod illustrerar hur man slår samman stora filer med hjälp av metoden CellsHelper.mergeFiles. Den tar två enkla men stora filer, MyBook1.xls och MyBook2.xls. Filerna innehåller endast formaterad data och formler.

{{% alert color="primary" %}}

Metoden CellsHelper.mergeFiles stöder endast sammanfogning av data, stilar, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kan inte sammanfogas med denna metod. Dessutom används en cachefil för att lagra tillfällig data för processen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
{{< app/cells/assistant language="java" >}}
