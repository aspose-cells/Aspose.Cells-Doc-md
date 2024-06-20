---
title: Ladda GridWeb data i Async läge
type: docs
weight: 40
url: /sv/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: Denna artikel beskriver hur man använder async läge för att få bättre prestanda i GridWeb.
keywords: GridWeb,prestanda,async,async läge
---

{{% alert color="primary" %}} 

När du skapar en arbetsbok med stora datamängder eller läser in en stor Microsoft Excel-fil tar det säkerligen längre tid och resurser att göra det. Den totala minnesanvändningen är alltid en oro. Det finns åtgärder som kan vidtas för att hantera utmaningen. Aspose.Cells.GridWeb tillhandahåller några relevanta alternativ och API: er för att sänka, minska och optimera minnesanvändningen. Det kan också hjälpa processen att arbeta mer effektivt och snabbare. För en kalkylblad som innehåller stora celler med data kan du ladda in datasetet asynkront vilket kan förbättra den övergripande prestandan för användarupplevelsen.

{{% /alert %}} 

Använd alternativet GridWeb.EnableAsync för att optimera minnet och prestandan för celldata. När du bygger en stor datamängd för celler. När du anger alternativet som true kommer dataladdningen att baseras på det aktuella synliga fönsterområdet endast. Kort sagt, när du bläddrar i kalkylbladets celldata i GridWeb kommer det att ladda nya fönsterdata baserat på den aktuella scrollpositionen endast.

Följande exempel visar hur du aktiverar GridWebs async-läge.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
