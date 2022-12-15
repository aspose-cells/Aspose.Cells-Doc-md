---
title: Laddar GridWeb-data i Async Mode
type: docs
weight: 40
url: /sv/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

När du skapar en arbetsbok med stora datamängder, eller läser en stor Microsoft Excel-fil, kommer det säkert att ta mer tid och resurser att göra det. Det totala minnet som processen kommer att ta är alltid ett problem. Det finns åtgärder som kan vidtas för att hantera utmaningen. Aspose.Cells.GridWeb tillhandahåller några relevanta alternativ och API:er för att sänka, minska och optimera minnesanvändningen. Det kan också hjälpa processen att fungera mer effektivt och köras snabbare. För ett kalkylblad som innehåller data med stora celler kan du ladda datamängden asynkront, vilket kan förbättra den övergripande prestandan för användarens upplevelse.

{{% /alert %}} 

Använd alternativet GridWeb.EnableAsync för att optimera minne och prestanda för celldata. När du bygger en stor datamängd för celler. När du ställer in alternativet på sant kommer dataladdningen att baseras på det aktuella synliga området Windows endast. Kort sagt, när du rullar i kalkylbladets cellers data i GridWeb, kommer det att ladda ny Windows-data endast baserat på den aktuella rullningspositionen.

Följande exempel visar hur du aktiverar GridWebs asynkroniseringsläge.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
