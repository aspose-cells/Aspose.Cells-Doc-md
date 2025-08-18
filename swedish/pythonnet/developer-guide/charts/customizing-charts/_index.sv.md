---
title: Anpassa diagram
description: Lär dig hur du anpassar diagram i Aspose.Cells för Python via .NET. Vår guide visar hur du ändrar diagramlayouter, lägger till och formaterar datserier, justerar axlar och tillämpar olika formateringsalternativ för att förbättra utseendet och användbarheten av dina diagram.
keywords: Aspose.Cells för Python via .NET, diagram, anpassning, layouter, datserier, axlar, formatering, utseende, användbarhet.
type: docs
weight: 40
url: /sv/python-net/customizing-charts/
---


## **Skapa Anpassade Diagram**

Hittills har vi när vi diskuterat diagram tittat på standarddiagram med deras standardformateringsinställningar. Vi definierar bara datakällan, sätter några egenskaper, och diagrammet skapas med sina standardformat. Men Aspose.Cells för Python via .NET API:er stödjer även skapandet av anpassade diagram som tillåter utvecklare att skapa diagram med egna formatinställningar.

Utvecklare kan skapa anpassade diagram i realtid med Aspose.Cells för Python via .NET.

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells för Python via .NET representeras av ett [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)-objekt medan [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)-objektet fungerar som en samling av [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)-objekt. När man skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (samlade i [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)-objektet).

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

För närvarande stöder Aspose.Cells för Python via .NET bara anpassade diagram som kombinerar paj, linje, kolumn och staplade kolumndiagram, men fler diagram kommer att stödas i framtida versioner.

{{% /alert %}}
