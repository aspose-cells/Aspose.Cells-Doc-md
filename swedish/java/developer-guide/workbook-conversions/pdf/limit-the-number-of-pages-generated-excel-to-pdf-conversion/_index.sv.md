---
title: Begränsa antalet genererade sidor - Excel till PDF-konvertering
type: docs
weight: 60
url: /sv/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Ibland vill du skriva ut ett antal sidor till en utdata-PDF-fil. Aspose.Cells har möjlighet att sätta en gräns för hur många sidor som genereras vid konvertering av ett Excel-kalkylblad till PDF.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) precis innan du renderar den till PDF-format. Om du gör det säkerställs att formelberoende värden beräknas om och att de korrekta värdena återges i utdatafilen.

{{% /alert %}}
