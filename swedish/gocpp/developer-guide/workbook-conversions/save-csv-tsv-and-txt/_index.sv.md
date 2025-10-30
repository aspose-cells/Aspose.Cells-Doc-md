---
title: Konvertera Excel till CSV, TSV och Txt med Golang via C++
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Konvertera enkelt Excel filer till CSV , TSV och TXT format med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att konvertera Excel, ODS, JSON och andra formatfiler till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil som CSV. Som standard är [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) ett komma, så specificera inte en separator om du sparar till CSV-format.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Fortsatta ämnen**
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
