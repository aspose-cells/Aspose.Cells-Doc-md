---
title: Begränsa antalet genererade sidor  Excel till PDF konvertering
type: docs
weight: 180
url: /sv/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lär dig hur du begränsar antalet sidor som genereras vid rendering av Excel till PDF med Aspose.Cells för Python via .NET API.
keywords: Python Begränsa antalet sidor som genereras vid rendering av Excel till PDF, Begränsa antalet sidor som genereras vid sparande av Excel till PDF med Python, Python Ange antalet sidor som genereras vid konvertering av Excel till PDF, Kontrollera antalet sidor som genereras för Excel till PDF i Python
---

{{% alert color="primary" %}}

Ibland vill du skriva ut en rad sidor till en utdata-PDF-fil. Aspose.Cells för Python via .NET har möjlighet att sätta en gräns för hur många sidor som genereras när du konverterar ett Excelfil till PDF-filen.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

Om kalkylarket innehåller formler är det bäst att anropa [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metoden precis innan det renderas till PDF. Att göra detta säkerställer att formelberoende värden omräknas, och de korrekta värdena renderas i utdatafilen.

{{% /alert %}}
