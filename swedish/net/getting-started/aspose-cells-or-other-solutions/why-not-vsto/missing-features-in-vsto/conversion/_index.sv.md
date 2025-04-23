---
title: Konvertering
type: docs
weight: 30
url: /sv/net/conversion/
---

Aspose.Cells unika funktion som ger flexibilitet i versionskonverteringar utan att påverka arbetet.
SaveFormat är en uppräkning som kan konvertera dokumentet till följande filnamnstillägg i tabellen nedan.

|**Medlemsnamn** |**Värde** |**Beskrivning** |
| :- | :- | :- |
|CSV |1 |Representerar en CSV-fil. |
|Xlsx |6 |Representerar en xlsx-fil. |
|Xlsm |7 |Representerar en xlsm-fil som aktiverar makron. |
|Xltx |8 |Representerar en xltx-fil. |
|Xltm |9 |Representerar en xltm-fil som aktiverar makron. |
|TabDelimited |11 |Representerar en flikavgränsad textfil. |
|Html |12 |Representerar en html-fil. |
|MHtml |17 |Representerar en mhtml-fil. |
|ODS |14 |Representerar en ods-fil. |
|Excel97To2003 |5 |Representerar en Excel97-2003 xls-fil. |
|SpreadsheetML |15 |Representerar en Excel 2003 xml-fil. |
|Xlsb |16 |Representerar en xlsb-fil. |
|Auto |0 |Om filen sparas på disken överensstämmer filformatet med filnamnstillägget. <br>Om filen sparas på strömmen är filformatet xlsx. |
|Unknown |255 |Representerar oidentifierat format, kan inte sparas. |
|Pdf |13 |Representerar en Pdf-fil. |
|XPS |20 |Representerar en XPS-fil. |
|TIFF |21 |Representerar en TIFF-fil. |
|SVG |22 |Representerar en SVG-fil. |
|Dif |30 | Dataväxlingsformat. |
Här är kodutdrag som visar konvertering från xls till xlsx du kan göra det vice versa också

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Ladda ned provkoden**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
