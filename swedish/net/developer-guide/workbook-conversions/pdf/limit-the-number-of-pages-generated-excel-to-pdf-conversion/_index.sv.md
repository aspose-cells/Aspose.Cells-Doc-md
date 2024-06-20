---
title: Begränsa antalet genererade sidor  Excel till PDF konvertering
type: docs
weight: 180
url: /sv/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Ibland vill du skriva ut en serie sidor till en utdatan PDF-fil. Aspose.Cells har förmågan att begränsa antalet sidor som genereras vid konvertering av ett Excel-kalkylark till PDF-filformat.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) precis innan du renderar det till PDF. Det säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i den utdatafil som genereras.

{{% /alert %}}
