---
title: Konvertera diagram till lokaliserad bild med Python via .NET
linktitle: Ställ in lokaliserad region
type: docs
weight: 50
url: /sv/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Lär dig hur du ställer in globaliseringskonfigurationer för diagram med Aspose.Cells för Python via .NET. Konfigurera diagram för att stödja flera språk och regionala format för korrekt visning av text, datum och nummer.
keywords: Aspose.Cells för Python via .NET, diagram, globaliseringsinställningar, flera språk, regionala format, visning, text, datum, nummer.
---

{{% alert color="primary" %}}

I detta ämne visar vi hur du konverterar ett diagram till en lokaliserad bild och hur du ställer in den lokaliserade regionen för ett diagram.

{{% /alert %}}

## **Scenario**

När kan det vara nödvändigt att ställa in den lokaliserade regionen för ett diagram?

Om du öppnar en XLSX-fil med ett diagram i Excel med spanska regionala inställningar, visas element som diagramtitel och legend på spanska. Men att spara detta diagram som en bild med Aspose.Cells kan resultera i att dessa element förblir på engelska som standard:

**![Globalt problem](GlobalIssue.png)**

Detta beror på att diagramlegenden i utdatafilen inte matchar Excels lokalisering. Du kan lösa detta genom att konfigurera diagrammets lokalisering.

## **Stödda element**

Följande diagramelement kommer att renderas enligt dina lokaliseringsinställningar:

| **Stödda element** | **Standardvärde (Engelska)** |
|-----------------------------|-----------------------------------|
| Axeltitel Namn | Axeltitel |
| Axelenhetens namn             | Hundratals, Tusentals...           |
| Diagramtitelns namn           | Diagramtitel                      |
| Legend Ökning Namn            | Ökning                          |
| Legend Minskning Namn         | Minskning                          |
| Legend Totalt Namn            | Totalt                              |
| Annat Namn                   | Annat                              |
| Serienamn                     | Serien                              |

