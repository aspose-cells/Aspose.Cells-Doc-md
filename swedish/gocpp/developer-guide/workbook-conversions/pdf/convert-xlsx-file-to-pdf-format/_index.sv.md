---
title: Konvertera XLSX fil till PDF format med Golang via C++
linktitle: Konvertera XLSX fil till PDF format
type: docs
weight: 30
url: /sv/go-cpp/convert-xlsx-file-to-pdf-format/
description: Lär dig hur du konverterar Excel filer till PDF format med Aspose.Cells for C++ med hög precision och noggrannhet.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av programvara, hårdvara och operativsystem som används för att skapa dessa dokument. En PDF-fil kan innehålla vilken kombination av text, grafik och bilder som helst på ett enhetsoberoende och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar mindre plats än originalfilen.

Ibland behöver du konvertera en Microsoft Excel-fil till PDF. För detta krävs en snabb, säker, noggrann och pålitlig lösning som gör att du kan distribuera PDF-dokument världen över. Det finns många konverteringsverktyg som kan utföra denna uppgift. Men du måste se till att layouten för original-dokumentet behålls i output PDF-filen. Bilder, diagram, former, dataformat, teckensnitt, attribut, färger, sidinställningar, textorientering, ramar och diagram bör renderas exakt och precist. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) garanterar hög trohet i konverteringen.

Detta dokument är utformat för att ge en omfattande förståelse för hur ett Microsoft Excel-dokument (innehållande bilder, diagram, formatering etc.) kan konverteras till PDF. Därför visar det hur man skapar en enkel konsolapplikation i C++ som konverterar en Excel-fil till PDF med Aspose.Cells API. Konversionen utförs med hög precision och noggrannhet.

{{% /alert %}}

## **Konvertera Excel till PDF**

Detta exempel använder en Excel-fil (SampleInput.xlsx) som mall. Arbetsboken innehåller arbetsblad med diagram och bilder. Varje arbetsblad innehåller olika typer av format med typsnitt, attribut, färger, skuggningseffekter och kantlinjer. Det finns ett kolumndiagram på det första arbetsbladet och en bild på det sista.

### **Den förkonfigurerade Excelfilen**

Mallfilen har tre arbetsblad, inklusive diagram och bilder som media. Det första arbetsbladet har diagram, och det sista arbetsbladet har en bild, som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|

### **Konverteringsprocess**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa metoden [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) precis innan du konverterar kalkylbladet till PDF. Detta säkerställer att formelberoende värden omberäknas och att de korrekta värdena visas i PDF:en.

{{% /alert %}}

### **Resultat**

När ovanstående kod har körts skapas en PDF-fil i mappen Files i din programkatalog.
Följande skärmbilder visar PDF-sidorna. Observera att sidhuvuden och sidfötter också behålls i den utmatade PDF-filen.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|
