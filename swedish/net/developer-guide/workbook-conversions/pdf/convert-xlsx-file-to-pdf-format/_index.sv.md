---
title: Konvertera XLSX-fil till PDF-format
type: docs
weight: 30
url: /sv/net/convert-xlsx-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av programvaran, hårdvaran och operativsystemet som används för att skapa dessa dokument. En PDF-fil kan vara dokument med valfri kombination av text, grafik och bilder på ett enhetsoberoende och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar mindre plats än originalfilen.

Ibland behöver du konvertera en Microsoft Excel-fil till PDF. För detta behöver du en snabb, säker, korrekt och pålitlig lösning som låter dig distribuera PDF-dokument över hela världen. Det finns många konverteringsverktyg som kan utföra denna uppgift. Men du måste se till att layouten för det ursprungliga Excel-dokumentet behålls i utdatafilen PDF. Bilder, diagram, former, dataformatering, typsnitt, attribut, färger, sidinställningar, textorientering, ramar, diagram etc. bör återges exakt och exakt.[Aspose.Cells](https://products.aspose.com/cells/net/) säkerställer högfientlig konvertering.

Detta dokument är utformat för att ge en övergripande förståelse för hur ett Microsoft Excel-dokument (som innehåller bilder, diagram, formatering etc.) kan konverteras till PDF. För detta ändamål visar den hur man skapar en enkel konsolapplikation i Visual Studio.Net som konverterar en Excel-fil till PDF med Aspose.Cells API. Konverteringen utförs med hög grad av precision och noggrannhet.

{{% /alert %}}

##  **Konvertera Excel till PDF**

Det här exemplet använder en Excel-fil (SampleInput.xlsx) som mall. Arbetsboken innehåller arbetsblad med diagram och bild. Varje kalkylblad innehåller olika typer av format som använder typsnitt, attribut, färger, skuggningseffekter och ramar. Det finns ett kolumndiagram på det första kalkylbladet och en bild på det sista.

###  **Excel-mallen**

Mallfilen har tre kalkylblad, inklusive diagram och bild som media. Det första kalkylbladet har diagram och det sista kalkylbladet har en bild som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| Det första arbetsbladet**(Försäljningsprognos)**| Det andra arbetsbladet**(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Det tredje arbetsbladet**(Datainmatning)**| Det sista arbetsbladet**(Bild)**|

###  **Konverteringsprocess**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[Arbetsbok. BeräknaFormel](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)metod precis innan kalkylarket renderas till PDF. Om du gör det säkerställer du att formelberoende värden räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}

###  **Resultat**

När ovanstående kod har körts skapas en PDF-fil i mappen Filer i din programkatalog.
Följande skärmdumpar visar PDF-sidorna. Observera att sidhuvuden och sidfötter också finns kvar i utdatafilen PDF.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| Det första arbetsbladet**(Försäljningsprognos)**| Det andra arbetsbladet**(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Det tredje arbetsbladet**(Datainmatning)**| Det sista arbetsbladet**(Bild)**|
