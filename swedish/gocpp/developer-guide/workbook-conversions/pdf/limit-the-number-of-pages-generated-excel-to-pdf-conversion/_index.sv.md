---
title: Begränsa antal genererade sidor  Excel till PDF konvertering med Golang via C++
linktitle: Begränsa antalet genererade sidor
type: docs
weight: 180
url: /sv/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lär dig hur du begränsar antalet sidor som genereras vid konvertering av Excel till PDF med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

Ibland vill du skriva ut en serie sidor till en utdatan PDF-fil. Aspose.Cells har förmågan att begränsa antalet sidor som genereras vid konvertering av ett Excel-kalkylark till PDF-filformat.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) precis innan du renderar det till PDF. Det säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i den utdatafil som genereras.

{{% /alert %}}
