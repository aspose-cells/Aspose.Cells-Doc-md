---
title: Anpassa diagram
description: Lär dig hur du anpassar diagram i Aspose.Cells for .NET. Vår guide kommer att visa dig hur du ändrar diagramlayouter, lägger till och formaterar data serier, justerar axlar och tillämpar olika formateringsalternativ för att förbättra utseendet och användbarheten för dina diagram.
keywords: Aspose.Cells for .NET, diagram, anpassning, layouter, data serier, axlar, formatering, utseende, användbarhet.
type: docs
weight: 40
url: /sv/net/customizing-charts/
---

{{% alert color="primary" %}}

## **Skapa Anpassade Diagram**

Hittills när vi har diskuterat diagram har vi tittat på standarddiagram som har sina standardformateringsinställningar. Vi definierar bara datakällan, ställer in några egenskaper, och diagrammet skapas med sina standardformatinställningar. Men Aspose.Cells API:er stödjer också skapandet av anpassade diagram som gör det möjligt för utvecklare att skapa diagram med sina egna formateringsinställningar.

Utvecklare kan skapa anpassade diagram vid körning med Aspose.Cells.

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells representeras av ett [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)-objekt medan ett [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)-objekt fungerar som en samling av [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)-objekt. Vid skapandet av ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (insamlade i [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)-objekt).

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar pie-, linje-, stapel- och stapelstapeldiagram men fler diagram kommer att stödjas i framtida versioner.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
