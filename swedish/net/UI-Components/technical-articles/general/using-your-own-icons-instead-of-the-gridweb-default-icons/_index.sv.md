---
title: Använd dina egna ikoner istället för GridWeb standardikoner
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb, ikon, ikoner
description: Denna artikel beskriver hur du använder ikoner i GridWeb.
---

{{% alert color="primary" %}} 

Ibland vill du använda dina egna ikoner (bilder) istället för Aspose.Cells.GridWeb-kontrollens standardikoner. Denna artikel förklarar hur du gör detta.

{{% /alert %}} 

Standardikonsen för kontrollen finns i URL-sökvägen "/acw_client/". Fil sökvägen kan vara: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" som standard. Du hittar filer som submit.gif, save.gif etc. i den mappen. Om du vill byta ut dessa bilder med dina egna, lägg till en konfigurationssektion i web.config-filen för din webbapplikation.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Du har kanske märkt att denna konfiguration endast påverkar kontrollbildsökvägen och påverkar inte klient-script sökvägen för kontrollen. Till exempel, om du kör din sida med GridWeb-kontrollen och kollar på källfilen i webbläsaren kan du hitta att egenskapen acw_client_path för gridens DIV-element fortfarande säger: “/yourApp/webform1.aspx/”. I vissa fall kan du behöva omdefiniera klient-skript sökvägen. För att tvinga kontrollen att använda den omdefinierade bildsökvägen som klient-skripts sökväg, lägg till en annan konfigurationsinställning i appSettings-sektionen.
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Denna konfiguration träder endast i kraft med den licensierade kontrollen.

{{% /alert %}}
