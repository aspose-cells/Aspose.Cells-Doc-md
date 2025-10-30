---
title: Tillförlitlighetsbehörigheter på webbservern
type: docs
weight: 30
url: /sv/net/declaration/
---

{{% alert color="primary" %}} 

Generellt sett kräver alla Aspose .NET-komponenter fulla behörigheter. Anledningen är att Aspose för .NET-komponenter behöver åtkomst till registerinställningar, systemfiler förutom virtuell katalog för vissa operationer som att tolka typsnitt etc. Dessutom baseras Aspose för .NET-komponenter (inklusive Aspose.Cells for .NET) på .NET-kärnsystemklasser som också kräver att fulla behörigheter är inställda i många fall.
<br/>
Medium Trust har tagits bort i .NET Core och .NET 5+. Medium Trust är säkerhetsmekanismen under .NET Framework. Medium Trust har gradvis ersatts av mer flexibla säkerhetspolicyer. Vi föreslår att användare prioriterar uppgradering till .NET 5+ och att anta containeriserad distribution istället för att förlita sig på traditionella tillitsnivåer.

{{% /alert %}} 
## **Delvis förtroende / Medium förtroende-utmaning**
Internetleverantörer som hostar flera applikationer från olika företag i allmänhet verkställer en säkerhetsnivå med medium förtroende. Dessutom måste du ibland vara värd för flera applikationer på en delad server, som till exempel hos en internetleverantör eller i andra scenarier, då måste du använda medium förtroendenivån för att begränsa applikationerna. ASP.NETs medium förtroendenivå tillhandahåller en begränsad körningsmiljö som är lämplig för att isolera flera applikationer som är värd för ISP-servrar. I fallet med .NET 2.0 kan en sådan säkerhetsnivå ställa in de följande begränsningarna som kan påverka förmågan hos Aspose.Cells for .NET att fungera korrekt, till exempel:

- **RegistryPermission är inte tillgängligt**. Detta innebär att du inte kan komma åt registret, vilket krävs för att uppräkna installerade typsnitt när du renderar kalkylblad eller andra dokument.
- **FileIOPermission är begränsad**. Detta innebär att du endast kan komma åt filer i din applikations virtuella kataloghierarki. Detta innebär potentiellt att typsnitt inte kan läsas under exporten.
## **Använd Aspose.Cells for .NET på Medium Trust-behörsinställningar**
Du kan följa några rekommendationer för att köra Aspose.Cells for .NET på Medium Trust-nivå eller i en delad servermiljö:

- För att ange licensfil i din kod är det bättre att du ska anropa metoden License.SetLicense(Stream) istället efter att ha erhållit licensfilen i strömmar.
- Katalogen med typsnitt (som kan kommas åt med behörighet) måste anges. Om det inte finns något sätt att komma åt filen på servern, lägg till de nödvändiga typsnittsfilerna i din applikation.
- I delvis förtroendeläge stöds inte Shape-to-EMF-konvertering, så ställ in exportbildtypen (för former) till andra bildformat.

Se följande exempel som visar hur Aspose.Cells for .NET används/körs i Medium Trust-läge.

{{< highlight csharp >}}

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





{{< app/cells/assistant language="csharp" >}}
