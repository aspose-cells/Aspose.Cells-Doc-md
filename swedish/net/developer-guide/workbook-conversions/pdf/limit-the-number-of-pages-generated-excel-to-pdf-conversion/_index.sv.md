---
title: Begränsa antalet genererade sidor - Excel till PDF-konvertering
type: docs
weight: 180
url: /sv/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Ibland vill du skriva ut ett antal sidor till en utdata-PDF-fil. Aspose.Cells har möjlighet att sätta en gräns för hur många sidor som genereras vid konvertering av ett Excel-kalkylblad till PDF-filformat.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) precis innan du renderar den till PDF. Att göra säkerställer att formelberoende värden räknas om och att de korrekta värdena återges i utdatafilen.

{{% /alert %}}
