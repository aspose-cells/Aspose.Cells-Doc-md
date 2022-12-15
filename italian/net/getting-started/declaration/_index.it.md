---
title: Dichiarazione
type: docs
weight: 30
url: /it/net/declaration/
---
{{% alert color="primary" %}} 

In genere, tutti i componenti Aspose .NET richiedono il set di autorizzazioni Full Trust. Il motivo è che i componenti Aspose for .NET devono accedere alle impostazioni del registro, ai file di sistema diversi dalla directory virtuale per determinate operazioni come l'analisi dei caratteri, ecc. autorizzazioni impostate in molti casi.

{{% /alert %}} 
## **Sfida fiducia parziale/fiducia media**
provider di servizi Internet che ospitano più applicazioni di società diverse applicano per lo più un livello di sicurezza medio. Inoltre, a volte è necessario ospitare più applicazioni su un server condiviso, ad esempio in un ISP o in altri scenari, è necessario utilizzare il livello di attendibilità medio per limitare le applicazioni. Il livello di attendibilità medio di ASP.NET fornisce un ambiente di esecuzione vincolato adatto per isolare più applicazioni ospitate su server ISP. Nel caso di .NET 2.0, tale livello di sicurezza può impostare i seguenti vincoli che potrebbero influire sulla capacità di Aspose.Cells for .NET di funzionare correttamente, ad esempio:

- **RegistryPermission non è disponibile**. Ciò significa che non è possibile accedere al registro, necessario per enumerare i font installati durante il rendering di fogli di calcolo o altri documenti.
- **FileIOPermission è limitato**. Ciò significa che puoi accedere solo ai file nella gerarchia di directory virtuale della tua applicazione. Ciò significa potenzialmente che i caratteri non possono essere letti durante l'esportazione.
## **Usa Aspose.Cells for .NET sul set di autorizzazioni di attendibilità medio**
È possibile seguire alcuni consigli per eseguire Aspose.Cells for .NET su livello di attendibilità medio o ambiente server condiviso:

- Per impostare il file di licenza nel codice, è meglio chiamare il metodo License.SetLicense(Stream) dopo aver ottenuto il file di licenza nei flussi.
- La directory dei caratteri (a cui si può accedere con autorizzazione) deve essere impostata. Se non è possibile accedere al file sul server, aggiungere i file dei caratteri necessari all'applicazione.
- In modalità di attendibilità parziale, la conversione Shape-to-EMF non è supportata, quindi imposta il tipo di immagine esportata (per le forme) su un altro formato di immagine.

Vedere l'esempio seguente che dimostra come utilizzare/eseguire Aspose.Cells for .NET in modalità Medium Trust.

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





