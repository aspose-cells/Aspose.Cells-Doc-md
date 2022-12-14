---
title: Konvertera Excel till CSV, TSV och Txt
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att konvertera excel, ods, json och andra formatfiler till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok i text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV, etc.) sparar både Microsoft Excel och Aspose.Cells endast innehållet i det aktiva kalkylbladet som standard.

Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda källarbetsboken som kan vara valfri Microsoft Excel- eller OpenOffice-kalkylarksfil (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med valfritt antal kalkylblad.

När koden exekveras konverterar den data från alla ark i arbetsboken till TXT-format.

 Du kan ändra samma exempel för att spara din fil i CSV. Som standard,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**är komma, så ange inte en avgränsare om du sparar i CSV-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkylbladsdata utan formatering. Filen är en sorts vanlig textfil som kan ha några anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Förhandsämnen**
- [Behåll separatorer för tomma rader medan du exporterar kalkylark till CSV-format](/cells/sv/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till CSV-format](/cells/sv/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
