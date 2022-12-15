---
title: Licensiering
type: docs
weight: 50
url: /sv/python-java/licensing/
---
{{% alert color="primary" %}} 

 Du kan installera en utvärderingsversion av**Aspose.Cells** for Python via Java med `pip install aspose-cells`. Utvärderingsversionen ger absolut samma möjligheter som den licensierade versionen av produkten. Dessutom blir utvärderingsversionen helt enkelt licensierad när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

 När du är nöjd med din utvärdering av**Aspose.Cells** , du kan[köpa en licens](https://purchase.aspose.com)på webbplatsen Aspose. Bekanta dig med de olika prenumerationstyperna som erbjuds. Om du har några frågor, tveka inte att kontakta Aspose säljteamet.

Varje Aspose-licens innehåller en ettårsprenumeration för gratis uppgraderingar till alla nya versioner eller korrigeringar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade användare och utvärderingsanvändare.

{{% /alert %}} {{% alert color="primary" %}} 

 Om du vill testa**Aspose.Cells** utan begränsningar i utvärderingsversionen, begär en 30-dagars tillfällig licens. Vänligen hänvisa till[Hur får man en tillfällig licens?](https://purchase.aspose.com/temporary-license) för mer information.

{{% /alert %}}

## **Begränsningar för utvärderingsversion**

 Utvärderingsversion av**Aspose.Cells** produkt (utan angiven licens) ger full produktfunktionalitet, men den är begränsad till att öppna 100 filer i ett program och ett extra kalkylblad med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

### **Första begränsningen: Antal öppnade filer**

När du kör ditt program kan du bara öppna 100 Excel-filer. Om din ansökan överstiger detta antal kommer ett undantag att kastas.

### **2:a begränsningen: Arbetsblad med utvärderingsvattenstämpel**

![todo:image_alt_text](licensing_1.png)

Detta kalkylblad kommer alltid att visas som det aktiva kalkylbladet. Endast i licensierad version kan du ställa in det aktiva kalkylbladet till andra kalkylblad.

## **Ställa in en licens**

Licensen är en XML-fil i vanlig text som innehåller detaljer som produktnamn, antal utvecklare den är licensierad till, prenumerationsutgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen; även ett oavsiktligt tillägg av en extra radbrytning i filen kommer att ogiltigförklara den.

Du måste ställa in en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsningar. Du behöver bara ange en licens en gång per ansökan eller process.

Licensen kan laddas från en fil på följande platser:

1. Explicit väg.
1. Arbetsmapp.

 Använd[License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) metod för att licensiera komponenten. Ofta är det enklaste sättet att ställa in en licens att lägga licensfilen i samma mapp som Aspose.Cells.jar och ange bara filnamnet utan sökväg som visas i följande exempel:

### **Exempel**

 I detta exempel**Aspose.Cells** kommer att försöka hitta licensfilen i din arbetsmapp.

{{< highlight "python" >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
