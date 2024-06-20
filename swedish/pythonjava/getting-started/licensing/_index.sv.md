---
title: Licensiering
type: docs
weight: 50
url: /sv/python-java/licensing/
---

{{% alert color="primary" %}} 

Du kan installera en utvärderingsversion av **Aspose.Cells** för Python via Java med `pip install aspose-cells`. Utvärderingsversionen har exakt samma funktionalitet som den licensierade versionen av produkten. Dessutom blir utvärderingsversionen helt licensierad när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

När du är nöjd med din utvärdering av **Aspose.Cells**, kan du [köpa en licens](https://purchase.aspose.com) på Aspose-webbplatsen. Bli bekant med de olika prenumerationstyperna som erbjuds. Om du har några frågor, tveka inte att kontakta Aspose-försäljningsteamet.

Varje Aspose-licens har ett års prenumeration för gratis uppgraderingar till alla nya versioner eller fixar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade och utvärderingsanvändare.

{{% /alert %}} {{% alert color="primary" %}} 

Om du vill testa **Aspose.Cells** utan begränsningar i utvärderingsversionen, begär en 30-dagars tillfällig licens. Vänligen se [Hur man får en tillfällig licens?](https://purchase.aspose.com/temporary-license) för mer information.

{{% /alert %}}

## **Begränsningar för utvärderingsversionen**

Utvärderingsversion av **Aspose.Cells**-produkten (utan specificerad licens) tillhandahåller full produktfunktionalitet, men är begränsad till att öppna 100 filer i ett program och en extra arbetsbok med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

### **1: a Begränsning: Antal öppnade filer**

Vid körning av ditt program kan du endast öppna 100 Excel-filer. Om din applikation överskrider detta antal kommer ett undantag kastas.

### **2: a Begränsning: Arbetsbok med utvärderingsvattenstämpel**

![todo:image_alt_text](licensing_1.png)

Denna arbetsbok kommer alltid att visas som aktiv arbetsbok. Endast i licensierad version kan du ange den aktiva arbetsboken till andra arbetsböcker.

## **Inställning av en licens**

Licensen är en vanlig text XML-fil som innehåller detaljer som produktens namn, antalet utvecklare den är licensierad till, prenumerations utgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen; även det oavsiktliga tillskottet av en extra radbrytning i filen kommer ogiltigförklara den.

Du behöver aktivera en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsningar. Du behöver bara aktivera en licens en gång per applikation eller process.

Licensen kan laddas från en fil på följande platser:

1. Explicit sökväg.
1. Arbetsmapp.

Använd metoden [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) för att licensiera komponenten. Ofta är det enklaste sättet att ange en licens att placera licensfilen i samma mapp som Aspose.Cells.jar och ange bara filnamnet utan sökväg enligt följande exempel:

### **Exempel**

I detta exempel kommer **Aspose.Cells** att försöka hitta licensfilen i din arbetsmapp.

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
