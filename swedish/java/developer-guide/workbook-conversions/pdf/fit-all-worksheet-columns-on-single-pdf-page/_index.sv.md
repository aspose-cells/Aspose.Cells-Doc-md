---
title: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 70
url: /sv/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Ibland vill du generera en PDF-fil som passar alla kalkylbladets kolumner på en enda sida. Egenskapen [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) ger denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar såsom höjden och bredden på utdata-PDF-sidan hanteras internt och baseras på datan i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) säkerställer att alla kolumner på ett kalkylblad renderas till en enda PDF-sida, även om rader kan expandera till flera sidor beroende på datan i kalkylbladet.

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den renderade PDF-filen visa innehållet i mycket liten storlek. Det är fortfarande läsbart när det skalar upp i en visningsapplikation såsom Acrobat Reader.

{{% /alert %}}

Följande exempelkod visar hur man använder egenskapen [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) för att rendera ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Om din kalkylblad innehåller formler är det bäst att anropa [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) metoden strax före rendering av kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden omberäknas och de korrekta värdena visas i PDF:n.

{{% /alert %}}
