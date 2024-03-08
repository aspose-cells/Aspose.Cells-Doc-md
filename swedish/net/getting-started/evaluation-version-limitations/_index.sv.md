---
title: Begränsningar för utvärderingsversion
type: docs
weight: 110
url: /sv/net/evaluation-version-limitations/
description: Aspose.Cells for .NET tillhandahåller olika planer för köp eller erbjuder en gratis provperiod och en 30-dagars tillfällig licens för utvärdering med användning av licens- och prenumerationspolicyer i C#.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **Så här får du utvärderingsversionen av Aspose.Cells**

 Du kan ladda ner en utvärderingsversion av**Aspose.Cells** för NET från[dess nedladdningssida](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) Maven repos. Utvärderingsversionen ger absolut samma möjligheter som den licensierade versionen av produkten. Dessutom blir utvärderingsversionen helt enkelt licensierad när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

 När du är nöjd med din utvärdering av *Aspose.Cells** kan du[köpa en licens](https://purchase.aspose.com) på webbplatsen Aspose. Bekanta dig med de olika prenumerationstyperna som erbjuds. Om du har några frågor, tveka inte att kontakta Aspose säljteamet.

Varje Aspose-licens innehåller en ettårsprenumeration för gratis uppgraderingar till alla nya versioner eller korrigeringar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade användare och utvärderingsanvändare.

##  **Hur man testar Aspose.Cells utan begränsningar för utvärderingsversion**

 Om du vill testa**Aspose.Cells** utan begränsningar i utvärderingsversionen, begär en 30-dagars tillfällig licens. Vänligen hänvisa till[Hur får man en tillfällig licens?](https://purchase.aspose.com/temporary-license)för mer information.


##  **Begränsningar för utvärderingsversion**

 Utvärderingsversion av**Aspose.Cells** produkt (utan angiven licens) ger full produktfunktionalitet, men den är begränsad till att öppna 100 filer i ett program och ett extra kalkylblad med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

###  **Första begränsningen: Antal öppnade filer**

När du kör ditt program kan du bara öppna 100 Excel-filer. Om din ansökan överstiger detta antal kommer ett undantag att kastas.

###  **2:a begränsningen: Arbetsblad med utvärderingsvattenstämpel**
Detta kalkylblad kommer alltid att visas som det aktiva kalkylbladet. Endast i licensierad version kan du ställa in det aktiva kalkylbladet till andra kalkylblad.
<br>
<image src="1.png" width="70%" />
<br>

###  **3:e begränsning: vanlig text med utvärderingsinformation**
I utdatafilen för ren text av Aspose.Cells, skulle en utvärderingsinformation läggas till i slutet av dokumentet.
<br>
<image src="2.png" width="70%" />
<br>

###  **4:e begränsningen: PDF och bild med utvärderingsvattenstämpel**
I utgången PDF eller bildfilen av Aspose.Cells, skulle en utvärderingsvattenstämpel klistras överst i dokumentet/bilden. Du kan inte dölja utvärderingsupphovsrättsvarningen (det extra kalkylbladet) i GridWeb-kontrollen också, den kommer alltid att läggas till (i slutet i kalkylbladsflikarna) i kontrollen.
<br>
<image src="3.png" width="70%" />
<br>

###  **Femte begränsningen: Inställningar för konfigurationsfil (Aspose.Cells.GridWeb)**
Du kan inte specificera om skriptsökvägen genom att lägga till följande kodrader i konfigurationssektionen (t.ex. i web.config-filen). Acw_client är en mapp som innehåller filer och Aspose.Cells.GridWeb använder denna mapp för att hantera sin interna konfiguration, den har skriptfiler, bildfiler och andra filer för att specificera GridWebs beteende och ställa in andra operationer. Konfigurationsfilen används för att förhindra att kontrollen använder de inbäddade klientresurserna (bilder, skript, etc.) vilket är användbart i vissa fall/scenarier. Dessutom kommer dessa konfigurationsinställningar i web.config-filen endast att träda i kraft med den LICENSERADE versionen av kontrollen.

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Dessa inställningar kan vara obligatoriska i vissa fall/scenarier om du använder Aspose.Cells.GridWeb-kontroll i filsystemwebbplatser eller MS Ajax-tillägg etc.

{{% /alert %}}