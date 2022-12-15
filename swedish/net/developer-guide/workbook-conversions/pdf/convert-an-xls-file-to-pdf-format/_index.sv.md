---
title: Konvertera en XLS-fil till PDF-format
type: docs
weight: 30
url: /sv/net/convert-an-xls-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av programvara, hårdvara och operativsystem som används för att skapa dessa dokument. En PDF-fil kan vara dokument med valfri kombination av text, grafik och bilder på ett enhetsoberoende och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar mindre plats än originalfilen.

Ibland måste du konvertera en Microsoft Excel-fil till PDF. För detta behöver du en snabb, säker, korrekt och pålitlig lösning som låter dig distribuera PDF-dokument över hela världen. Det finns många konverteringsverktyg som kan utföra denna uppgift. Men du måste se till att layouten för det ursprungliga Excel-dokumentet behålls i utdata-PDF-filen. Bilder, dataformatering, typsnitt, attribut, färger, sidinställningar, textorientering, ramar, diagram etc. ska återges exakt och exakt.[Aspose.Cells](https://products.aspose.com/cells/net/) säkerställer högfientlig konvertering.

Detta dokument är utformat för att ge en omfattande förståelse för hur ett Microsoft Excel-dokument (som innehåller bilder, diagram, formatering etc.) kan konverteras till PDF. För detta ändamål visar den hur man skapar en enkel konsolapplikation i Visual Studio.Net som konverterar en Excel-fil till PDF med Aspose.Cells API. Konverteringen utförs med hög grad av precision och noggrannhet.

{{% /alert %}}

## **Konvertera Excel till PDF**

Det här exemplet använder en Excel-fil (SampleInput.xlsx) som mall. Arbetsboken innehåller arbetsblad med diagram och bild. Varje kalkylblad innehåller olika typer av format som använder typsnitt, attribut, färger, skuggningseffekter och ramar. Det finns ett kolumndiagram på det första kalkylbladet och en bild på det sista.

### **Excel-mallen**

Mallfilen har tre kalkylblad, inklusive diagram och bild som media. Det första kalkylbladet har diagram och det sista kalkylbladet har en bild som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
|:- |:- |
| Det första arbetsbladet**(Försäljningsprognos)**| Det andra arbetsbladet**(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Det tredje arbetsbladet**(Datainmatning)**| Det sista arbetsbladet**(Bild)**|

### **Konverteringsprocess**

1. Ladda ner och installera Aspose.Cells:
 1. Ladda ner Aspose.Cells for .NET.
 1. Installera det på din utvecklingsdator.
1. Skapa ett projekt och lägg till referenser:
 1. Starta Visual Studio.Net.
 1. Skapa en ny konsolapplikation.
 1. Lägg till en referens till …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Lägg till konverteringskoden till projektet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}}

Om kalkylarket innehåller formler är det bäst att anropa Workbook.CalculateFormula() precis innan du renderar kalkylarket till PDF. Genom att göra det säkerställs att formelberoende värden beräknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}

### **Resultat**

när ovanstående kod har körts skapas en PDF-fil i mappen Filer i din programkatalog.
Följande skärmdumpar visar PDF-sidorna. Observera att sidhuvuden och sidfötter också finns kvar i PDF-filen.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
|:- |:- |
| Det första arbetsbladet**(Försäljningsprognos)**| Det andra arbetsbladet**(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Det tredje arbetsbladet**(Datainmatning)**| Det sista arbetsbladet**(Bild)**|
