---
title: Ställa in sidalternativ
type: docs
weight: 10
url: /sv/net/setting-page-options/
---
{{% alert color="primary" %}}

Ibland är det nödvändigt att konfigurera sidinställningar för kalkylblad för att styra utskriften. Dessa sidinställningar erbjuder olika alternativ.

{{% /alert %}}

## **Ställa in sidalternativ**

Alternativ för sidinställningar stöds fullt ut i Aspose.Cells. Den här artikeln förklarar hur du ställer in sidalternativ med Aspose.Cells och visar kodexempel för inställning:

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass.

 De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) egenskap som används för att ställa in sidinställningarna för kalkylbladet. Faktum är att detta[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) egendom är ett föremål för[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass används för att ställa in olika sidlayoutalternativ för ett utskrivet kalkylblad. De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class tillhandahåller olika egenskaper som används för att ställa in sidinställningar. Några av dessa egenskaper diskuteras nedan.

### **Sidorientering**

Sidorienteringen kan ställas in på stående eller liggande med hjälp av[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**Orientering**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) fast egendom. De[**Orientering**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) egenskapen accepterar ett av de fördefinierade värdena i[**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)uppräkning, listad nedan.

|**Sidorienteringstyper**|**Beskrivning**|
|:- |:- |
|Landskap|Landskapsorientering|
|Porträtt|Stående format|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **Skalningsfaktor**

 Det är möjligt att minska eller förstora ett kalkylblads storlek genom att justera skalfaktorn med[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)fast egendom.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **FitToPages-alternativ**

 För att anpassa innehållet i kalkylbladet till ett visst antal sidor, använd[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) och[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)egenskaper. Dessa egenskaper används också för att skala kalkylblad.

{{% alert color="primary" %}}

 Du kan antingen välja[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) eller den[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) egendom men inte båda samtidigt.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **Pappersformat**

 Ställ in pappersstorleken som kalkylbladen ska skrivas ut till med hjälp av[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**Pappersformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) fast egendom. De[**Pappersformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) egenskapen accepterar ett av de fördefinierade värdena i[**PaperSizeType**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)uppräkning, listad nedan.

|**Pappersstorlekstyper**|**Beskrivning**|
|:- |:- |
|PaperLetter|Letter (8-1/2 tum x 11 tum)|
|PaperLetterSmall|Letter Small (8-1/2 tum x 11 tum)|
|PaperTabloid|Tabloid (11 tum x 17 tum)|
|PaperLedger|Ledbok (17 tum x 11 tum)|
|Paper Legal|Legal (8-1/2 tum x 14 tum)|
|PaperStatement|Statement (5-1/2 tum x 8-1/2 tum)|
|PaperExecutive|Executive (7-1/4 tum x 10-1/2 tum)|
|PapperA3|A3 (297 mm x 420 mm)|
|PapperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PapperA5|A5 (148 mm x 210 mm)|
|PapperB4|JIS B4 (257 mm x 364 mm)|
|PapperB5|JIS B5 (182 mm x 257 mm)|
|PaperFolio|Folio (8-1/2 tum x 13 tum)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|Papper 10x14|10 tum x 14 tum.|
|Papper 11x17|11 tum x 17 tum.|
|PaperNote|Obs (8-1/2 tum x 11 tum)|
|Papperskuvert 9|Kuvert #9 (3-7/8 tum x 8-7/8 tum)|
|Papperskuvert10|Kuvert #10 (4-1/8 tum x 9-1/2 tum)|
|Papperskuvert11|Kuvert #11 (4-1/2 tum x 10-3/8 tum)|
|Papperskuvert12|Kuvert #12 (4-1/2 tum x 11 tum)|
|Papperskuvert14|Kuvert #14 (5 tum x 11-1/2 tum)|
|Pappersark|C storlek blad|
|Pappersark|D storlek blad|
|PaperESheet|E-storlek ark|
|PaperEnvelopeDL|Kuvert DL (110 mm x 220 mm)|
|PaperEnvelopeC5|Kuvert C5 (162 mm x 229 mm)|
|PaperEnvelopeC3|Kuvert C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Kuvert C4 (229 mm x 324 mm)|
|PaperEnvelopeC6|Kuvert C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Kuvert C65 (114 mm x 229 mm)|
|PaperEnvelopeB4|Kuvert B4 (250 mm x 353 mm|
|PaperEnvelopeB5|Kuvert B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Kuvert B6 (176 mm x 125 mm)|
|PaperEnvelopeItalien|Kuvert Italien (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 tum x 7-1/2 tum)|
|PaperEnvelopePersonligt|Kuvert (3-5/8 tum x 6-1/2 tum)|
|PaperFanfoldUS|US Standard Fanfold (14-7/8 tum x 11 tum)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 tum x 12 tum)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 tum x 13 tum)|
|PapperISOB4|B4 (ISO) 250 x 353 mm|
|PaperJapanese Postcard|Japanskt vykort (100 mm x 148 mm)|
|Papper 9x11|9 tum x 11 tum.|
|Papper 10x11|10 tum x 11 tum.|
|Papper 15x11|15 tum x 11 tum.|
|PaperEnvelopeInvite|Kuvertinbjudan (220 mm x 220 mm)|
|PaperLetterExtra|US Letter Extra 9 \275 x 12 tum|
|PaperLegalExtra|US Legal Extra 9 \275 x 15 tum|
|PaperTabloidExtra|US Tabloid Extra 11,69 x 18 tum|
|PaperA4Extra|A4 Extra 9,27 x 12,69 tum|
|PaperLetterTransverse|Bokstav tvärgående 8 \275 x 11 tum|
|PapperA4Tvärgående|A4 Tvärgående 210 x 297 mm|
|PaperLetterExtraTransverse|Bokstav extra tvärgående 9\275 x 12 tum|
|PaperSuperA|SuperA/SuperA/A4 227 x 356 mm|
|PaperSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PaperLetterPlus|US Letter Plus 8,5 x 12,69 tum|
|PaperA4Plus|A4 Plus 210 x 330 mm|
|PapperA5Tvärgående|A5 Tvärgående 148 x 210 mm|
|PaperJISB5Tvärgående|B5 (JIS) Tvärgående 182 x 257 mm|
|PaperA3Extra|A3 Extra 322 x 445 mm|
|PaperA5Extra|A5 Extra 174 x 235 mm|
|PaperISOB5Extra|B5 (ISO) Extra 201 x 276 mm|
|PapperA2|A2 420 x 594 mm|
|PapperA3Tvärgående|A3 Tvärgående 297 x 420 mm|
|PaperA3ExtraTransvers|A3 Extra tvärgående 322 x 445 mm|
|PaperJapanese DoublePostcard|Japanskt dubbelvykort 200 x 148 mm|
|PapperA6|A6 105 x 148 mm|
|PaperJapanese EnvelopeKaku2|Japanskt kuvert Kaku #2|
|PaperJapanese EnvelopeKaku3|Japanskt kuvert Kaku #3|
|PaperJapaneseEnvelopeChou3|Japanskt kuvert Chou #3|
|PaperJapaneseEnvelopeChou4|Japanskt kuvert Chou #4|
|PaperLetterRotated|11 tum x 8,5 tum|
|PaperA3Roterat|420 mm x 297 mm|
|PaperA4Roterad|297mm x 210mm|
|PaperA5 Roterat|210 mm x 148 mm|
|PaperJISB4Roterad|B4 (JIS) Roterad 364 x 257 mm|
|PaperJISB5Roterad|B5 (JIS) Roterad 257 x 182 mm|
|PaperJapanese PostcardRotated|Japanskt vykort roterat 148 x 100 mm|
|PaperJapanese DoublePostcardRotated|Dubbelt japanskt vykort roterat 148 x 200 mm|
|PapperA6 Roterat|A6 Roterad 148 x 105 mm|
|PaperJapanese EnvelopeKaku2Roterad|Japanskt kuvert Kaku #2 roterat|
|PaperJapanese EnvelopeKaku3Roterad|Japanskt kuvert Kaku #3 roterat|
|PaperJapaneseEnvelopeChou3Rotated|Japanskt kuvert Chou #3 roterat|
|PaperJapaneseEnvelopeChou4Rotated|Japanskt kuvert Chou #4 roterat|
|PaperJISB6|B6 (JIS) 128 x 182 mm|
|PaperJISB6Roterad|B6 (JIS) Roterad 182 x 128 mm|
|Papper 12x11|12 x 11 tum|
|PaperJapaneseEnvelopeYou4|Japanskt kuvert Du #4|
|PaperJapaneseEnvelopeYou4Rotated|Japanskt kuvert som du #4 roterat|
|PaperPRC16K|PRC 16K 146 x 215 mm|
|PaperPRC32K|PRC 32K 97 x 151 mm|
|PapperPRCBig32K|PRC 32K(Big) 97 x 151 mm|
|PappersPRCEnvelope1|PRC Envelope #1 102 x 165 mm|
|PaperPRCEnvelope2|PRC Envelope #2 102 x 176 mm|
|PappersPRCEnvelope3|PRC Envelope #3 125 x 176 mm|
|PappersPRCEnvelope4|PRC Envelope #4 110 x 208 mm|
|PaperPRCEnvelope5|PRC Envelope #5 110 x 220 mm|
|PaperPRCEnvelope6|PRC Envelope #6 120 x 230 mm|
|PaperPRCEnvelope7|PRC Envelope #7 160 x 230 mm|
|PaperPRCEnvelope8|PRC Envelope #8 120 x 309 mm|
|PaperPRCEnvelope9|PRC Envelope #9 229 x 324 mm|
|PaperPRCEnvelope10|PRC Envelope #10 324 x 458 mm|
|PapperPRC16KRoterat|PRC 16K roterad|
|PapperPRC32KRoterat|PRC 32K roterad|
|PapperPRCBig32KRoterat|PRC 32K(Big) Roterad|
|PaperPRCEnvelope1Roterat|PRC Envelope #1 Rotated 165 x 102 mm|
|PaperPRCEnvelope2Rotated|PRC Kuvert #2 Roterat 176 x 102 mm|
|PaperPRCEnvelope3Rotated|PRC Kuvert #3 Roterat 176 x 125 mm|
|PaperPRCEnvelope4Rotated|PRC Kuvert #4 Roterat 208 x 110 mm|
|PaperPRCEnvelope5Rotated|PRC Kuvert #5 Roterat 220 x 110 mm|
|PaperPRCEnvelope6Roterat|PRC Kuvert #6 Roterat 230 x 120 mm|
|PaperPRCEnvelope7Rotated|PRC Kuvert #7 Roterat 230 x 160 mm|
|PaperPRCEnvelope8Rotated|PRC Kuvert #8 Roterat 309 x 120 mm|
|PaperPRCEnvelope9Roterad|PRC Envelope #9 Rotated 324 x 229 mm|
|PaperPRCEnvelope10Roterat|PRC Envelope #10 Roterat 458 x 324 mm|
|PapperB3|vanlig B3(13,9 x 19,7 tum)|
|PaperBusinessCard|Visitkort (90 mm x 55 mm)|
|PaperThermal|Termisk (3 x 11 tum)|
|Beställnings|Representerar den anpassade pappersstorleken.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **Utskriftskvalitet**

 Ställ in utskriftskvaliteten för de arbetsblad som ska skrivas ut med[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**Utskriftskvalitet**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)fast egendom. Mätenheten för utskriftskvalitet är Dots Per Inches (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **Första sidnummer**

 Starta numreringen av kalkylbladssidor med hjälp av[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**FirstPageNumber**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) fast egendom. De[**FirstPageNumber**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)egenskapen ställer in sidnumret på den första kalkylbladssidan och nästa sidor numreras i stigande ordning.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
