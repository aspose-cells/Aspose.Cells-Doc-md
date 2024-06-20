---
title: Konvertera Excel till JSON
type: docs
weight: 300
url: /sv/python-java/convert-excel-to-json/
description: Lär dig hur man konverterar excelfil till json med Aspose.Cells för Python via Java.
keywords: Exportera arbetsbok till json utan Office 2013, Office 2016, Office 2019 och Office 365
---

{{% alert color="primary" %}}

Aspose.Cells för Python via Java stöder konvertering av en arbetsbok till Json (JavaScript Object Notation)-fil.

{{% /alert %}}

## **Konvertera Excel-arbetsbok till JSON**

Behöver inte fundera över hur man konverterar Excel-arbetsboken till JSON, eftersom Aspose.Cells för Python via Java-biblioteket har bästa lösningen. Aspose.Cells för Python via Java API:et ger stöd för att konvertera kalkylblad till JSON-format. För att exportera arbetsboken till JSON, ange [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) som andra parameter för [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\))-metoden. Du kan också använda [**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions)-klassen för att specificera ytterligare inställningar för att exportera kalkylblad till JSON.

Följande kodexempel demonstrerar export av Excel-arbetsbok till Json. Se koden för att konvertera [källfilen](sample.xlsx) till Json-filen som genererats av koden för referens.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

Följande kodexempel som använder JsonSaveOptions-klassen för att ange ytterligare inställningar demonstrerar export av Excel-arbetsbok till Json. Se koden för att konvertera [källfilen](sample.xlsx) till Json-filen som genererats av koden för referens.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
