---
title: Omvandling
type: docs
weight: 30
url: /sv/net/conversion/
---
Aspose.Cells unik funktion som ger flexibilitet vid versionskonverteringar utan att påverka arbetet.
SaveFormat är en uppräkning som kan konvertera dokument i tilläggen som anges nedan i tabellen.

|**Medlemsnamn** |**Värde** |**Beskrivning** |
|:- |:- |:- |
| CSV|1 | Representerar en CSV-fil.|
| Xlsx|6 | Representerar en xlsx-fil.|
| Xlsm|7 | Representerar en xlsm-fil som aktiverar makron.|
| Xltx|8 | Representerar en xltx-fil.|
| Xltm|9 | Representerar en xltm-fil som aktiverar makron.|
| TabDelimited|11 | Representerar en tabbavgränsad textfil.|
| Html|12 | Representerar en html-fil.|
| MHtml|17 | Representerar en mhtml-fil.|
| ODS|14 | Representerar en ods-fil.|
| Excel97To2003|5 | Representerar en Excel97-2003 xls-fil.|
| SpreadsheetML|15 | Representerar en Excel 2003 xml-fil.|
| Xlsb|16 | Representerar en xlsb-fil.|
| Bil|0 |Om du sparar filen på disken, överensstämmer filformatet med filnamnets förlängning.<br> Om du sparar filen i strömmen är filformatet xlsx.|
| Okänd|255 | Representerar okänt format, kan inte sparas.|
| Pdf|13 | Representerar en pdf-fil.|
| XPS|20 | Representerar en XPS-fil.|
| TIFF|21 | Representerar en TIFF-fil.|
| SVG|22 | Representerar en SVG-fil.|
| Dif|30 | Datautbytesformat.|
Nedan är kodavsnitt som visar konvertering från xls till xlsx, du kan också göra det tvärtom

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Ladda ner exempelkod**
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
