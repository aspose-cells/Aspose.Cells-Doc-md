---
title: Konvertera Excel till CSV,TSV och Txt
linktitle: Spara som CSV,TSV och Txt
type: docs
weight: 40
url: /sv/python-net/convert-excel-to-csv-tsv-and-txt/
description: Konvertera Excel till CSV,TSV och Txt genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET gör det möjligt att konvertera excel, ods, json och andra formatfiler till CSV, TSV och TXT.

{{% /alert %}}

##  **Spara arbetsbok till text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV, etc.), sparar både Microsoft Excel och Aspose.Cells for Python via .NET endast innehållet i det aktiva kalkylbladet som standard.

Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda källarbetsboken som kan vara valfri Microsoft Excel- eller OpenOffice-kalkylarksfil (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med valfritt antal kalkylblad.

När koden exekveras konverterar den data från alla ark i arbetsboken till formatet TXT.

 Du kan ändra samma exempel för att spara din fil till CSV. Som standard,**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**är komma, så ange inte en avgränsare om du sparar i formatet CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Spara textfiler med anpassad separator**

Textfiler innehåller kalkylbladsdata utan formatering. Filen är en sorts vanlig textfil som kan ha några anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **Förhandsämnen**
- [Behåll avgränsare för tomma rader när du exporterar kalkylblad till CSV-format](/cells/sv/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till formatet CSV](/cells/sv/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
