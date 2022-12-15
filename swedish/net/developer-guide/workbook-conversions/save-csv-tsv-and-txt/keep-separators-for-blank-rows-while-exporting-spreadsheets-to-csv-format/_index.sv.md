---
title: Behåll separatorer för tomma rader medan du exporterar kalkylark till CSV-format
type: docs
weight: 160
url: /sv/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Behåll separatorer för tomma rader medan du exporterar kalkylark till CSV-format**

Aspose.Cells ger möjlighet att behålla radavgränsare samtidigt som kalkylblad konverteras till CSV-format. För detta kan du använda**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**egendom av**[TxtSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions)**klass.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**är en boolesk egenskap. För att behålla separatorerna för tomma rader när du konverterar Excel-filen till CSV, ställ in**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**egendom till**Sann**.

Följande exempelkod laddar[käll Excel-fil](84378743.xlsx). Det sätter sig**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**egendom till**Sann** och sparar den som[output.csv](84378744.csv) . Skärmdumpen visar jämförelsen mellan källfilen i Excel, standardutdata som genereras vid konvertering av kalkylarket till CSV och utdata som genereras genom inställning**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** till**Sann**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
