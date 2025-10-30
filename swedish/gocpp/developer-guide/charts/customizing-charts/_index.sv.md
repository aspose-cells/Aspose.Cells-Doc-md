---
title: Anpassa diagram med Golang via C++
linktitle: Anpassa diagram
description: Lär dig hur du anpassar diagram i Aspose.Cells for C++. Vår guide visar hur du ändrar diagramlayout, lägger till och formaterar dataserier, justerar axlar och tillämpar olika formateringsalternativ för att förbättra utseendet och användbarheten av dina diagram.
keywords: Aspose.Cells for C++, diagram, anpassning, layouter, dataserier, axlar, formatering, utseende, användbarhet.
type: docs
weight: 40
url: /sv/go-cpp/customizing-charts/
---


## **Skapa Anpassade Diagram**

Hittills har vi när vi diskuterat diagram sett på standarddiagram som har sina standardinställningar. Vi definierar bara datakällan, ställer in några få egenskaper, och diagrammet skapas med dess standardformat. Men Aspose.Cells API:er stöder också att skapa anpassade diagram som tillåter utvecklare att skapa diagram med egna formateringsinställningar.

Utvecklare kan skapa anpassade diagram vid körning med Aspose.Cells.

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells representeras av ett [**Series**](https://reference.aspose.com/cells/go-cpp/series/)-objekt medan ett [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-objekt fungerar som en samling av [**Series**](https://reference.aspose.com/cells/go-cpp/series/)-objekt. Vid skapandet av ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (insamlade i [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-objekt).

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar pip-, linje-, kolumn- och stapeldiagram, men fler diagram kommer att stödas i framtida versioner.

{{% /alert %}}
