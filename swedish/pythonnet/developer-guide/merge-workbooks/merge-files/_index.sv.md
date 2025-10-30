---
title: Slå samman filer
type: docs
weight: 20
url: /sv/python-net/merge-files/
---

## **Introduktion**

Aspose.Cells för Python via .NET erbjuder olika sätt att slå ihop filer. För enkla filer med data, formatering och formler kan [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine)-metoden användas för att kombinera flera arbetsböcker, och [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy)-metoden kan användas för att kopiera arbetsblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att slå samman kan du upptäcka att de tar mycket systemresurser. För att undvika detta, använd den statiska [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)-metoden, ett mer effektivt sätt att slå samman flera filer.

## **Fusionera filer med Aspose.Cells för Python via .NET**

Följande kodexempel illustrerar hur man sammanfogar stora filer med hjälp av metoden [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files). Den tar två enkla men stora filer, Book1.xls och Book2.xls. Filerna innehåller bara formaterad data och formler.

{{% alert color="primary" %}}

Metoden [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) stöder endast sammanfogning av data, format, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte sammanfogas med denna metod. Dessutom används en cachelagrad fil för att lagra tillfälliga data för processen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
