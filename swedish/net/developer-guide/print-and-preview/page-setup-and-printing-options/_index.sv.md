---
title: Sidlayout och utskriftsalternativ
type: docs
weight: 60
url: /sv/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Ibland behöver utvecklare konfigurera sidlayout och utskriftsalternativ för att kontrollera utskriftsprocessen. Sidlayouts- och utskriftsalternativen erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio.Net och tillämpar sidlayout och utskriftsalternativ på ett kalkylblad med några enkla rader kod med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Arbeta med Sid- och Utskriftsalternativ**

För detta exempel skapade vi en arbetsbok i Microsoft Excel och använde Aspose.Cells för att ställa in sidlayouts- och utskriftsalternativ.

### **Användning av Aspose.Cells för att ställa in sidlayoutalternativ**

Skapa först ett enkelt arbetsblad i Microsoft Excel. Tillämpa sedan sidlayoutalternativ på det. När koden utförs ändras sidlayoutalternativen enligt skärmdumpen nedan.

|**Utdatafil.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Skapa ett arbetsblad med viss data i Microsoft Excel:
   1. Öppna en ny arbetsbok i Microsoft Excel.
   1. Lägg till viss data.
1. Ange sidlayoutalternativ:
   Tillämpa sidlayoutalternativ på filen. Här är en skärmdump av de förvalda alternativen, innan de nya alternativen tillämpas.

|**Standard sidlayoutalternativ.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner](https://downloads.aspose.com/cells/net) Aspose.Cells för .Net.
   1. Installera det på din utvecklingsdator.
      Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.
1. Skapa ett projekt:
   1. Starta Visual Studio. Net.
   1. Skapa en ny konsolapplikation.
      Detta exempel kommer att visa en C#-konsolapplikation, men du kan också använda VB.NET.
1. Lägg till referenser:
   1. Detta exempel använder Aspose.Cells så lägg till en referens till den komponenten i projektet. Till exempel:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Skriv applikationen som använder API:et:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Inställa utskriftsalternativ**

Sidlayoutinställningar ger också flera utskriftsalternativ (även kallade bladalternativ) som låter användarna styra hur arksidor skrivs ut. De tillåter användarna att:

- Välj ett specifikt utskriftsområde av ett kalkylblad.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Exemplet som följer tillämpar utskriftsalternativ på filen skapad i exemplet ovan (PageSetup.xls). Skärmdumpen nedan visar de standardutskriftsalternativen innan nya alternativ tillämpas.

|**Inmatningsdokument**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Körning av koden ändrar utskriftsalternativen.

|**Utmatningsfil**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
