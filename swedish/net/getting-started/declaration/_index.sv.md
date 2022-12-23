---
title: Deklaration
type: docs
weight: 30
url: /sv/net/declaration/
---
{{% alert color="primary" %}} 

allmänhet kräver alla Aspose .NET komponenter Full Trust-behörighetsuppsättning. Anledningen är att Aspose for .NET komponenter behöver komma åt registerinställningar, andra systemfiler än virtuella kataloger för vissa operationer som att tolka typsnitt etc. Dessutom kräver Aspose for .NET komponenter (inklusive Aspose.Cells Aspose.Cells 0717 klasser som är baserade på 8 core 0717, 8481 8417 och 8 core 8417) inställt i många fall.

{{% /alert %}} 
## **Partiell Trust / Medium Trust Challenge**
Internetleverantörer som är värd för flera applikationer från olika företag tillämpar oftast en Medium Trust-säkerhetsnivå. Dessutom, ibland behöver du vara värd för flera applikationer på en delad server, till exempel i en ISP eller andra scenarier, måste du använda medelstor förtroendenivå för att begränsa applikationerna. ASP.NET Medium förtroendenivå tillhandahåller en begränsad exekveringsmiljö som är lämplig för att isolera flera applikationer som finns på ISP-servrar. I fallet med .NET 2.0 kan en sådan säkerhetsnivå ställa in följande begränsningar som kan påverka förmågan för Aspose.Cells for .NET att fungera korrekt, till exempel:

- **RegistryPermission är inte tillgängligt**. Det betyder att du inte kan komma åt registret, som krävs för att räkna upp installerade teckensnitt när du renderar kalkylblad eller andra dokument.
- **FileIOPermission är begränsad**Det betyder att du bara kan komma åt filer i din applikations virtuella kataloghierarki. Detta innebär potentiellt att teckensnitt inte kan läsas under export.
## **Använd Aspose.Cells for .NET på Medium Trust Permissions Set**
Du kan följa några rekommendationer för att köra Aspose.Cells for .NET på Medium Trust-nivå eller delad servermiljö:

- För att ställa in licensfilen i din kod, är det bättre att du anropar metoden License.SetLicense(Stream) istället efter att ha hämtat licensfilen i strömmar.
- Typsnittens katalog (som kan nås med tillstånd) måste ställas in. Om det inte finns något sätt att komma åt filen på servern, lägg till de nödvändiga teckensnittsfilerna i din applikation.
- I partiellt förtroendeläge stöds inte Shape-to-EMF-konvertering, så ställ in den exporterade bildtypen (för former) till ett annat bildformat.

Se följande exempel som visar hur man använder/kör Aspose.Cells for .NET i Medium Trust-läge.

{{< highlight "csharp" >}}

 // Instantiate the License object

Aspose.Cells.License lic = new Aspose.Cells.License();

// Get the license file into stream

System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

// Set the License stream

lic.SetLicense(stream);

// Close the stream

stream.Close();

// Set the fonts directory

CellsHelper.FontDir = MapPath("~") + @"\Fonts";

//Open the template file

Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

// Set the image type to other format instead of using the default image type, that is, EMF

pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

// Save the PDF file

workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

// Save the XLSX file

workbook.Save(MapPath("~") + @"\dest.xlsx");



{{< /highlight >}}





