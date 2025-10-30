---
title: Rendera en PDF sida per Excel ark  Excel till PDF konvertering med Golang via C++
type: docs
weight: 100
url: /sv/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Konvertera Excel ark till PDF format med en sida för varje kalkylblad med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}} 

När du arbetar med stora Microsoft Excel-filer (t.ex. en arbetsbok med många blad, varje med 50 kolumner och 300 eller fler rader med data) kanske du vill att PDF-utgången ska visa en sida per kalkylblad, oavsett storleken på bladet. Detta innebär att varje sida sannolikt kommer att ha en radikalt annorlunda sidstorlek. Detta kan uppnås med hjälp av Aspose.Cells for C++.

{{% /alert %}} 

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Om [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) är inställt på **true**, kommer allt innehåll i kalkylbladet att renderas till en PDF-sida.

{{% /alert %}} {{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler är det bäst att anropa [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) precis innan du konverterar kalkylbladet till PDF. Detta säkerställer att formelberoende värden omberäknas, och de korrekta värdena visas i PDF:en.

{{% /alert %}}
