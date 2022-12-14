---
title: Licensiering
type: docs
weight: 21
url: /sv/python-net/licensing/
---
{{% alert color="primary" %}}

 Du kan enkelt ladda ner en utvärderingsversion av Aspose.Cells Python via .Net från dess[nedladdningssida](https://pypi.org/project/aspose-cells-python/) @ Pypi repos. Utvärderingsversionen ger absolut samma möjligheter som den licensierade versionen av komponenten. Dessutom blir utvärderingsversionen helt enkelt licensierad när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

{{% /alert %}}

## **Begränsningar för utvärderingsversion**

Utvärderingsversion av Aspose.Cells Python via .Net-produkt (utan angiven licens) ger full produktfunktionalitet, men den är begränsad till att öppna 100 filer i ett program och ett extra kalkylblad med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

- **Antal öppnade filer** (Aspose.Cells Python via .Net)
 När du kör ditt program kan du bara öppna 100 Excel-filer med Aspose.Cells Python via .Net-biblioteket. Om din ansökan överstiger detta antal kommer ett undantag att kastas.


Dessutom kommer ett kalkylblad med utvärderingsvattenstämpel alltid att visas som det aktiva kalkylbladet i den genererade excel-filen med Aspose.Cells Python via bibliotek. Endast i licensierad version kan du ställa in det aktiva kalkylbladet till andra kalkylblad. I utdata-PDF- eller bildfilen av Aspose.Cells Python via, skulle en utvärderingsvattenstämpel klistras överst i dokumentet/bilden.

{{% alert color="primary" %}}

 Om du vill testa Aspose.Cells Python via utan utvärderingsversionsbegränsningar kan du också begära en[30 dagars tillfällig licens](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Applicera en licens i Aspose.Cells Python via komponent**

Licensen är en XML-fil i vanlig text som innehåller detaljer som produktnamn, antal utvecklare den är licensierad till, prenumerationsutgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen. Även oavsiktligt tillägg av en extra radbrytning i filen kommer att ogiltigförklara den. Du måste ställa in en licens innan du använder Aspose.Cells Python via om du vill undvika dess utvärderingsbegränsning. Det krävs bara att ställa in en licens en gång per ansökan (eller process). Licensen kan laddas från en fil.

Aspose.Cells Python via försöker hitta licensen på explicita sökvägsplatser.

Det finns två vanliga metoder för att tillämpa en licens från fil.

### **Applicera en licens från disk**

Det enklaste sättet att ställa in en licens är att lägga licensfilen i den explicita sökvägen.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

När du ringer till setet_licensmetoden, bör licensnamnet vara detsamma som för ditt licensfilnamn. Du kan till exempel ändra licensfilens namn till **Aspose.Cells.lic.xml**. Sedan ska du i din kod använda det modifierade licensnamnet (**Aspose.Cells.lic.xml**) för uppsättningen_licensmetoden.

{{% /alert %}}


