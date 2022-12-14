---
title: Använda dina egna ikoner istället för GridWebs standardikoner
type: docs
weight: 10
url: /sv/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

Ibland kanske du vill använda dina egna ikoner (bilder) istället för Aspose.Cells.GridWeb-kontrollens standardikoner. Den här artikeln förklarar hur du gör detta.

{{% /alert %}} 

Kontrollens standardikoner finns i URL-sökvägen "/acw_klient/". Filsökvägen kan vara: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_klient" som standard. Du hittar filer som submit.gif, save.gif etc. i den mappen. Om du vill ersätta dessa bilder med dina egna, lägg till en konfigurationssektion till web.config-filen i din webbapplikation.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Du kanske har märkt att den här konfigurationen bara påverkar sökvägen för kontrollbilden och inte påverkar sökvägen till kontrollens klientskript. Om du till exempel kör din sida med GridWeb-kontrollen och kontrollerar källfilen i webbläsaren kan du upptäcka att acw_ klient_path-egenskapen för rutnätets DIV-element säger fortfarande: "/yourApp/webform1.aspx/". I vissa fall kan du behöva omdefiniera klientskriptsökvägen. För att tvinga kontrollen att använda den omdefinierade bildsökvägen som klientskriptsökväg, lägg till ytterligare en konfigurationsinställning i sektionen appSettings
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Denna konfiguration kommer endast att träda i kraft med den licensierade kontrollen.

{{% /alert %}}
