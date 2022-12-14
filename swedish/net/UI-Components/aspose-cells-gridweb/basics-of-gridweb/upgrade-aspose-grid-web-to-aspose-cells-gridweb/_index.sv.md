---
title: Uppgradera Aspose.Grid.Web till Aspose.Cells.GridWeb
type: docs
weight: 30
url: /sv/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

För att göra det enklare att uppgradera underhåller vi ett dokument som beskriver information som är viktig för befintliga användare, särskilt de som har använt den äldre Aspose.Grid.Web och behöver uppgradera till den sammanslagna Aspose.Cells.GridWeb.

 Dessa är avsedda att vara korta anteckningar, och du bör kunna hitta mer information genom att titta på avsnitten i[Utvecklarguide](/cells/sv/net/developer-guide/).

{{% /alert %}}

## **Uppgradering till Aspose.Cells.GridWeb**

 Aspose.Grid.Webanvändare kan stöta på problem med att använda nya Aspose.Cells.GridWeb när de uppgraderar till den. Det bör noteras att Aspose.Grid.Web har bytt namn och blivit en del av Aspose.Cells så vi kommer inte att fortsätta eller göra ändringar i äldre versioner av kontrollen.

Det är inte svårt att uppgradera till den senaste Aspose.Cells.GridWeb-komponenten.

{{% alert color="primary" %}}

Det finns några ändringar i API:t eftersom klasserna med medlemmarna, strukturerna, uppräkningarna etc. förblir desamma. De flesta ändringarna har gjorts i kontrollens namnrymder och andra taggar eller attribut.

{{% /alert %}}

Följande är namnutrymmeslistan och andra attribut/taggar som ändras nu:

1. Namnutrymmet Aspose.Grid.Web har bytt namn till Aspose.Cells.GridWeb.
1. Namnutrymmet Aspose.Grid.Web.Data har bytt namn till Aspose.Cells.GridWeb.Data.
1. Namnutrymmet Aspose.Grid.Web.Design har bytt namn till Aspose.Cells.GridWeb.Design.
1. Namnutrymmet Aspose.Grid.Formula bytte namn till Aspose.Cells.GridFormula, och med de senaste utgåvorna av komponenten togs nämnda namnutrymme helt bort från det offentliga API:et.
1. Taggen agw:GridWeb har ändrats till acw:GridWeb i aspx-formen.
1. Den äldre Aspose.Grid.Webklientsökvägen, agw_klient, har ändrats till acw_klient för Aspose.Cells.GridWeb .
1.  Klientsökvägsinställningen i web.config-filen, till exempel:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 har ändrats till

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
