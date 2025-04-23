---
title: Sidlayout och utskriftsalternativ
type: docs
weight: 60
url: /sv/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Ibland behöver utvecklare konfigurera sidinställningar och utskriftsinställningar för att styra utskriftsprocessen. Sidinställningar och utskriftsalternativ erbjuder många valmöjligheter och stöds fullt ut i Aspose.Cells för Python via .NET.

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio.Net och tillämpar sidinställningar och utskriftsalternativ på ett arbetsblad med några enkla kodrader med Aspose.Cells för Python via .NET API.

{{% /alert %}}

## **Arbeta med Sid- och Utskriftsalternativ**

För detta exempel skapade vi ett arbetsbok i Microsoft Excel och använder Aspose.Cells för Python via .NET för att ställa in sidinställningar och utskriftsalternativ.

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


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
