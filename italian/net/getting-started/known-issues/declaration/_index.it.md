---
title: Permessi di fiducia sul server web
type: docs
weight: 30
url: /it/net/declaration/
---

{{% alert color="primary" %}} 

In generale, tutti i componenti Aspose .NET richiedono impostazioni di autorizzazione Full Trust. Il motivo è che i componenti Aspose per .NET devono accedere alle impostazioni del registro, ai file di sistema diversi dalla directory virtuale per determinate operazioni come l'analisi dei font, ecc. Inoltre, i componenti Aspose per .NET (compreso Aspose.Cells for .NET) si basano sulle classi di sistema di base .NET che richiedono anche impostazioni di autorizzazione Full Trust in molti casi.
<br/>
Trust di livello medio rimosso in .NET Core e .NET 5+. Trust di livello medio era il meccanismo di sicurezza nell'epoca del .NET Framework. Il trust di livello medio è stato gradualmente sostituito da politiche di sicurezza più flessibili. Suggeriamo agli utenti di dare priorità all'aggiornamento a .NET 5+ e di adottare il deployment containerizzato invece di affidarsi a livelli di trust tradizionali.

{{% /alert %}} 
## **Sfida di Trust parziale / medio**
I provider di servizi Internet che ospitano più applicazioni di diverse aziende in genere impongono un livello di sicurezza di Trust medio. Inoltre, a volte è necessario ospitare più applicazioni su un server condiviso, ad esempio in un ISP o in altri scenari, è necessario utilizzare il livello di Trust medio per limitare le applicazioni. Il livello di Trust medio di ASP.NET fornisce un ambiente di esecuzione limitato adatto all'isolamento di più applicazioni ospitate su server ISP. Nel caso di .NET 2.0, tale livello di sicurezza può impostare i seguenti vincoli che potrebbero influenzare la capacità di Aspose.Cells for .NET di funzionare correttamente, ad esempio:

- **RegistryPermission non è disponibile**. Ciò significa che non è possibile accedere al registro, il che è necessario per enumerare i font installati durante il rendering di fogli di calcolo o altri documenti.
- **FileIOPermission è limitato**. Ciò significa che è possibile accedere solo ai file nella gerarchia della directory virtuale dell'applicazione. Questo potenzialmente significa che i font non possono essere letti durante l'esportazione.
## **Usa Aspose.Cells for .NET su un set di autorizzazioni di Trust medio**
Puoi seguire alcune raccomandazioni per eseguire Aspose.Cells for .NET a livello di Trust medio o in un ambiente server condiviso:

- Per impostare il file di licenza nel tuo codice, è meglio chiamare il metodo License.SetLicense(Stream) dopo aver ottenuto il file di licenza in stream.
- Deve essere impostata la directory dei font (a cui potrebbe essere consentito l'accesso). Se non c'è modo di accedere al file sul server, aggiungere i file dei font necessari all'applicazione.
- In modalità di Trust parziale, la conversione da Shape a EMF non è supportata, quindi impostare il tipo di immagine esportata (per forme) in altri formati di immagine.

Guarda l'esempio in seguito che dimostra come utilizzare/eseguire Aspose.Cells for .NET in modalità di Trust medio.

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
