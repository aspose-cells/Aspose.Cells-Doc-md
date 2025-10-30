---
title: Licensiering
type: docs
weight: 21
url: /sv/python-net/licensing/
---

{{% alert color="primary" %}}

Du kan enkelt ladda ner en utvärderingsversion av Aspose.Cells Python via .Net från dess [nedladdningssida](https://pypi.org/project/aspose-cells-python/) @ Pypi repos. Utvärderingsversionen erbjuder exakt samma funktioner som licensierad version av komponenten. Dessutom blir utvärderingsversionen automatiskt licensierad när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

{{% /alert %}}

## **Begränsningar för utvärderingsversionen**

Utvärderingsversionen av Aspose.Cells Python via .Net-produkt (utan angiven licens) ger full produktfunktionalitet, men är begränsad till att öppna 100 filer i ett program och en extra arbetsblad med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

- **Antal öppnade filer** (Aspose.Cells Python via .Net)
  När du kör ditt program kan du endast öppna 100 Excel-filer med Aspose.Cells Python via .Net-biblioteket. Om din applikation överstiger detta antal kommer ett undantag att kastas.


Dessutom kommer ett arbetsblad med utvärderingsvattenstämpel alltid att visas som det aktiva arbetsbladet i den genererade excelfilen med hjälp av Aspose.Cells Python via biblioteket. Endast i licensierad version kan du ange det aktiva arbetsbladet till andra arbetsblad. I den genererade PDF- eller bildfilen av Aspose.Cells Python via kommer en utvärderingsvattenstämpel att klistras in längst upp i dokumentet/bilden.

{{% alert color="primary" %}}

Om du vill testa Aspose.Cells Python via utan utvärderingsversionsbegränsningar kan du också begära en [30 dagar temporär licens](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Tillämpning av en licens i Aspose.Cells Python via-komponenten**

Licensen är en vanlig text XML-fil som innehåller detaljer såsom produktens namn, antal utvecklare det är licensierat till, prenumerationsutgångsdatum med mera. Filen är digitalt signerad, så ändra inte filen. Även oavsiktlig tillägg av en extra radbrytning i filen kommer att ogiltigförklara den. Du behöver sätta en licens innan du använder Aspose.Cells Python via om du vill undvika dess utvärderingsbegränsning. Det är endast nödvändigt att sätta en licens en gång per applikation (eller process). Licensen kan laddas från en fil.

Aspose.Cells Python via försöker hitta licensen på explicita sökvägsplatser.

Det finns två vanliga metoder för att tillämpa en licens från en fil.

### **Att tillämpa en licens från skiva**

Det enklaste sättet att sätta en licens är att placera licensfilen på den explicita sökvägen.

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

När du anropar set_license-metoden ska licensnamnet vara samma som din licensfilnamn. Till exempel kan du ändra licensfilnamnet till **Aspose.Cells.lic.xml**. Sedan i din kod bör du använda det modifierade licensnamnet (**Aspose.Cells.lic.xml**) för set_license-metoden.

{{% /alert %}}


{{< app/cells/assistant language="python-net" >}}
