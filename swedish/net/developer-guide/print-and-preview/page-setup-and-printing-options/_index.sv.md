---
title: Sidinställningar och utskriftsalternativ
type: docs
weight: 60
url: /sv/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Ibland måste utvecklare konfigurera sidinställningar och utskriftsinställningar för att styra utskriftsprocessen. Sidinställningar och utskriftsinställningar erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio.Net och tillämpar sidinställningar och utskriftsalternativ på ett kalkylblad med några enkla rader kod med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Arbeta med sid- och utskriftsinställningar**

För det här exemplet skapade vi en arbetsbok i Microsoft Excel och använder Aspose.Cells för att ställa in sidinställningar och utskriftsalternativ.

### **Använd Aspose.Cells för att ställa in alternativ för sidinställningar**

Skapa först ett enkelt kalkylblad i Microsoft Excel. Använd sedan sidinställningar på den. Genom att köra koden ändras alternativen för sidinställningar som på skärmdumpen nedan.

|**Utdatafil.**|
|:- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Skapa ett kalkylblad med lite data i Microsoft Excel:
 1. Öppna en ny arbetsbok i Microsoft Excel.
 1. Lägg till några data.
1. Ange alternativ för sidinställningar:
 Tillämpa sidinställningar på filen. Nedan finns en skärmdump av standardalternativen, innan de nya alternativen tillämpas.

|**Standardalternativ för sidinställningar.**|
|:- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner](https://downloads.aspose.com/cells/net) Aspose.Cells för .Net.
 1. Installera det på din utvecklingsdator.
 Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.
1. Skapa ett projekt:
 1. Starta Visual Studio. Netto.
 1. Skapa en ny konsolapplikation.
 Det här exemplet visar en C# konsolapplikation, men du kan också använda VB.NET.
1. Lägg till referenser:
 1. Det här exemplet använder Aspose.Cells så lägg till en referens till den komponenten i projektet. Till exempel:
 …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Skriv applikationen som anropar API:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Ställa in utskriftsalternativ**

Inställningar för sidinställningar ger också flera utskriftsalternativ (även kallade arkalternativ) som låter användare styra hur kalkylbladssidor skrivs ut. De tillåter användare att:

- Välj ett specifikt utskriftsområde i ett kalkylblad.
- Skriv ut titlar.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå dragkvalitet.
- Skriv ut kommentarer.
- Utskriftscellfel.
- Definiera sidordning.

Exemplet som följer tillämpar utskriftsalternativ på filen som skapats i exemplet ovan (PageSetup.xls). Skärmbilden nedan visar standardutskriftsalternativen innan nya alternativ tillämpas.

|**Inmatningsdokument**|
|:- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Genom att köra koden ändras utskriftsalternativen.

|**Utdatafil**|
|:- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
