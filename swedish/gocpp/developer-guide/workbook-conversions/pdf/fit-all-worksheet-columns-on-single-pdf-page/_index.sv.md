---
title: Anpassa alla kalkylbladskolumner till en PDF sida med Golang via C++
linktitle: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 160
url: /sv/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Generera en PDF som passar all kalkylbladets kolumner på en sida med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}}

Ibland vill du skapa en PDF-fil som passar alla kalkylbladets kolumner på en sida. Egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) ger denna funktion mycket lätt. Komplexa beräkningar som höjd och bredd för den resulterande PDF:en hanteras internt och baseras på data i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) säkerställer att alla kolumner i ett kalkylblad renderas till en PDF-sida, även om rader kan sträcka sig över flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) för att rendera ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den genererade PDF-filen visa innehållet i väldigt liten storlek. Det är fortfarande läsbart när det skalas upp i en visningsapplikation som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
