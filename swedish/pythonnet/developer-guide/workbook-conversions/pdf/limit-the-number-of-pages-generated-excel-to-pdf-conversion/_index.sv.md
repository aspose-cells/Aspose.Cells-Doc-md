---
title: Begränsa antalet genererade sidor - Excel till PDF konvertering
type: docs
weight: 180
url: /sv/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lär dig hur du begränsar antalet sidor som genereras när du renderar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

Ibland vill du skriva ut ett antal sidor till en utdatafil PDF. Aspose.Cells for Python via .NET har möjlighet att sätta en gräns för hur många sidor som genereras när ett Excel-kalkylblad konverteras till filformatet PDF.

{{% /alert %}}

##  **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metod precis innan den renderas till PDF. Att göra säkerställer att formelberoende värden beräknas om och att de korrekta värdena återges i utdatafilen.

{{% /alert %}}
