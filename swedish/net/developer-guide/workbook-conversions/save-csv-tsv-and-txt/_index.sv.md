---
title: Konvertera Excel till CSV, TSV och Txt
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/net/convert-excel-to-csv-tsv-and-txt/
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att konvertera Excel-, ODS-, JSON- och andra filformat till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan ändra samma exempel för att spara din fil som CSV. Som standard är [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) komma, så ange inte ett separator om du sparar i CSV-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Fortsatta ämnen**
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
