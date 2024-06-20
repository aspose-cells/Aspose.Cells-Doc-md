---
title: Uppgradera Aspose.Grid.Web till Aspose.Cells.GridWeb
type: docs
weight: 30
url: /sv/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: Den här artikeln introducerar hur man uppgraderar i GridWeb.
---

{{% alert color="primary" %}}

För att göra uppgraderingen enklare upprätthåller vi en dokumentation som beskriver viktig information för befintliga användare, särskilt de som har använt den äldre Aspose.Grid.Web och behöver uppgradera till Aspose.Cells.GridWeb.

Dessa är avsedda att vara kortfattade anteckningar, och du bör kunna hitta mer information genom att titta på avsnitten av [Utvecklarguide](/cells/sv/net/aspose-cells-gridweb/developer-guide/).

{{% /alert %}}

## **Uppgradering till Aspose.Cells.GridWeb**

Användare av Aspose.Grid.Web kan stöta på problem när de uppgraderar till den nya Aspose.Cells.GridWeb. Det ska noteras att Aspose.Grid.Web har fått namnändring och blivit en del av Aspose.Cells så vi kommer inte fortsätta eller göra ändringar i äldre versioner av kontrollen. 

Det är inte svårt att uppgradera till den senaste Aspose.Cells.GridWeb-komponenten.

{{% alert color="primary" %}}

Det finns några ändringar i API:en eftersom klasserna med medlemmar, strukturer, uppräkningar osv. förblir desamma. De flesta ändringar har gjorts i kontrollens namnrymden och andra taggar eller attribut.

{{% /alert %}}

Följande är listan över namnrymd och andra attribut/taggar som har ändrats nu:

1. Aspose.Grid.Web-namnrymden har döpts om till Aspose.Cells.GridWeb.
1. Aspose.Grid.Web.Data-namnrymden har döpts om till Aspose.Cells.GridWeb.Data.
1. Aspose.Grid.Web.Design-namnrymden har döpts om till Aspose.Cells.GridWeb.Design.
1. Aspose.Grid.Formula-namnrymden har döpts om till Aspose.Cells.GridFormula, och med de senaste versionerna av komponenten har denna namnrymd tagits bort helt från den publika API:n.
1. Taggen agw:GridWeb har ändrats till acw:GridWeb i aspx-formuläret.
1. Den äldre Aspose.Grid.Web-klientens sökväg, agw_client, har ändrats till acw_client för Aspose.Cells.GridWeb.
1. Klientsökväginställningen i web.config-filen, till exempel: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

har ändrats till 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
