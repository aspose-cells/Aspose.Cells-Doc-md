---
title: Konvertera XLSX fil till PDF format
type: docs
weight: 30
url: /sv/net/convert-xlsx-file-to-pdf-format/
---

{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av den programvara, hårdvara och operativsystem som används för att skapa dessa dokument. En PDF-fil kan vara dokument med vilken kombination av text, grafik och bilder som helst på ett enhets- och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar upp mindre utrymme än den ursprungliga filen.

Ibland behöver du konvertera en Microsoft Excel-fil till PDF. För detta krävs en snabb, säker, noggrann och tillförlitlig lösning som låter dig distribuera PDF-dokument över hela världen. Det finns många konverteringsverktyg som kan utföra denna uppgift. Men du måste se till att layouten i den ursprungliga Excel-dokumentet bibehålls i den resulterande PDF-filen. Bilder, diagram, former, dataformatering, teckensnitt, attribut, färger, sidinställningar, textorientering, ramar, diagram etc. ska renderas korrekt och exakt. [Aspose.Cells](https://products.aspose.com/cells/net/) säkerställer högfidelitetskonvertering.

Denna dokument är utformat för att ge omfattande förståelse för hur en Microsoft Excel-fil (som innehåller bilder, diagram, formatering etc.) kan konverteras till PDF. I det syftet visar det hur man skapar en enkel konsolapplikation i Visual Studio.Net som konverterar en Excel-fil till PDF med hjälp av Aspose.Cells API. Konverteringen utförs med hög grad av precision och noggrannhet.

{{% /alert %}}

## **Konvertera Excel till PDF**

Detta exempel använder en Excelfil (SampleInput.xlsx) som mall. Arbetsboken innehåller kalkylblad med diagram och bild. Varje kalkylblad innehåller olika typer av format med teckensnitt, attribut, färger, skuggningseffekter och ramar. Det finns en kolumngrafik på det första kalkylbladet och en bild på det sista.

### **Den förkonfigurerade Excelfilen**

Mallfilen har tre kalkylblad, inklusive diagram och bild som Media. Det första kalkylbladet har diagram och det sista kalkylbladet har en bild som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|

### **Konverteringsprocess**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

Om kalkylarket innehåller formler är det bäst att anropa [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)-metoden precis innan rendering av kalkylarket till PDF. Genom att göra det säkerställs att formelberoende värden beräknas på nytt och korrekta värden renderas i PDF:n.

{{% /alert %}}

### **Resultat**

När ovanstående kod har körts skapas en PDF-fil i mappen Files i din programkatalog.
Följande skärmbilder visar PDF-sidorna. Observera att sidhuvuden och sidfötter också behålls i den utmatade PDF-filen.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|
{{< app/cells/assistant language="csharp" >}}
