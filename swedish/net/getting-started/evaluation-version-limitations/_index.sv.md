---
title: Begränsningar för utvärderingsversion
type: docs
weight: 110
url: /sv/net/evaluation-version-limitations/
description: Aspose.Cells for .NET erbjuder olika planer för köp eller erbjuder en Gratis test och en 30 dagars provlicens för utvärdering med licensiering och prenumerationspolicyer i C#.
keywords: Begränsningar i utvärderingsversionen, Antal öppnade filer i utvärderingsversionen, Utvärderingsvattenstämpel med utvärderingsversion.
---

## **Hur man får utvärderingsversionen av Aspose.Cells**

Du kan ladda ner en utvärderingsversion av **Aspose.Cells** för NET från [dess nedladdningssida](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. Utvärderingsversionen tillhandahåller precis samma funktioner som den licensierade versionen av produkten. Dessutom blir utvärderingsversionen en licensierad version när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

När du är nöjd med din utvärdering av **Aspose.Cells**, kan du [köpa en licens](https://purchase.aspose.com) på Aspose-webbplatsen. Bli bekant med de olika prenumerationstyperna som erbjuds. Om du har några frågor, tveka inte att kontakta Aspose-försäljningsteamet.

Varje Aspose-licens har ett års prenumeration för gratis uppgraderingar till alla nya versioner eller fixar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade och utvärderingsanvändare.

## **Hur man testar Aspose.Cells utan begränsningar i utvärderingsversionen**

Om du vill testa **Aspose.Cells** utan begränsningar i utvärderingsversionen, begär en 30-dagars tillfällig licens. Vänligen se [Hur man får en tillfällig licens?](https://purchase.aspose.com/temporary-license) för mer information.


## **Begränsningar för utvärderingsversionen**

Utvärderingsversion av **Aspose.Cells**-produkten (utan specificerad licens) tillhandahåller full produktfunktionalitet, men är begränsad till att öppna 100 filer i ett program och en extra arbetsbok med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

### **1: a Begränsning: Antal öppnade filer**

Vid körning av ditt program kan du endast öppna 100 Excel-filer. Om din applikation överskrider detta antal kommer ett undantag kastas.

### **2: a Begränsning: Arbetsbok med utvärderingsvattenstämpel**
Denna arbetsbok kommer alltid att visas som aktiv arbetsbok. Endast i licensierad version kan du ange den aktiva arbetsboken till andra arbetsböcker.
<br>
<image src="1.png" width="70%" />
<br>

### **3: e Begränsning: Ren text med utvärderingsinformation**
I utdatafilen i vanlig textformat av Aspose.Cells kommer ett utvärderingsmeddelande att läggas till i slutet av dokumentet. Vid spara till vanlig text (såsom CSV och TSV) visas endast innehållet i det första arbetsbladet.
<br>
<image src="2.png" width="70%" />
<br>

### **4: e Begränsning: PDF och bild med utvärderingsvattenstämpel**
I den utdata PDF- eller bildfilen från Aspose.Cells kommer ett utvärderingsvattenstämpel att klistras in högst upp i dokumentet/bilden. Du kan inte dölja Upphovsrättsvarningen för utvärdering (den extra kalkylbladet) i GridWeb-kontrollen heller, den kommer alltid att läggas till (i slutet av kalkylbladsflikarna) i kontrollen.
<br>
<image src="3.png" width="70%" />
<br>

### **5:e Begränsning: Konfigurationsfilinställningar (Aspose.Cells.GridWeb)**
Du kan inte återspecificera skriptstigen genom att lägga till följande rader kod i konfigurationsavsnittet (t.ex. i web.config-filen). acw_client är en mapp som innehåller filer och Aspose.Cells.GridWeb använder den här mappen för att hantera sin interna konfiguration, den har skriptfiler, bildfiler och andra filer för att ange GridWebs beteende och ställa in andra operationer. Konfigurationsfilen används för att förhindra att kontrollen använder inbäddade klientresurser (bilder, skript etc.) vilket är användbart i vissa fall / scenarier. Dessutom kommer dessa konfigurationsinställningar i web.config-filen endast att ha effekt med en Licensierad version av kontrollen.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Dessa inställningar kan vara obligatoriska i vissa fall / scenarier om du använder Aspose.Cells.GridWeb-kontrollen i Filsystemwebbplatser eller med MS Ajax-tillägg osv.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
