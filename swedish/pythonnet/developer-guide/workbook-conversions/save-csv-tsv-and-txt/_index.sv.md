---
title: Konvertera Excel till CSV, TSV och Txt
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/python-net/convert-excel-to-csv-tsv-and-txt/
description: Konvertera Excel till CSV, TSV och Txt genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Konvertera Excel till CSV, TSV och Txt, Konvertera Excel till CSV, TSV och Txt i Python via NET, Python Konvertera arbetsbok till CSV, TSV och Txt.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET gör det möjligt att konvertera excel-, ods-, json- och andra filformat till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV, osv.) sparar både Microsoft Excel och Aspose.Cells for Python via .NET som standard endast innehållet i det aktiva kalkylbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan ändra samma exempel för att spara din fil som CSV. Som standard är [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) komma, så ange inte ett separator om du sparar i CSV-format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Fortsatta ämnen**
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
