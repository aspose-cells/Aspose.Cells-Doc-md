---
title: Erklärung
type: docs
weight: 30
url: /de/net/declaration/
---
{{% alert color="primary" %}} 

Im Allgemeinen erfordern alle Aspose .NET-Komponenten die Berechtigung „Voll vertrauenswürdig“. Der Grund dafür ist, dass Aspose for .NET-Komponenten für bestimmte Vorgänge wie das Analysieren von Schriftarten usw. auf Registrierungseinstellungen und andere Systemdateien als das virtuelle Verzeichnis zugreifen müssen. Darüber hinaus basieren Aspose for .NET-Komponenten (einschließlich Aspose.Cells for .NET) auf .NET-Kernsystemklassen, die ebenfalls Berechtigungen für volles Vertrauen erfordern in vielen Fällen eingestellt.

{{% /alert %}} 
## **Teilweise Vertrauenswürdigkeit/mittlere Vertrauensherausforderung**
Internetdienstanbieter, die mehrere Anwendungen von verschiedenen Unternehmen hosten, erzwingen meistens eine mittlere Vertrauenswürdigkeitsstufe. Darüber hinaus müssen Sie manchmal mehrere Anwendungen auf einem gemeinsam genutzten Server hosten, z. B. bei einem ISP oder in anderen Szenarien, und Sie müssen die Vertrauensebene „Mittel“ verwenden, um die Anwendungen einzuschränken. Die ASP.NET-Vertrauensstufe Medium bietet eine eingeschränkte Ausführungsumgebung, die zum Isolieren mehrerer Anwendungen geeignet ist, die auf ISP-Servern gehostet werden. Im Fall von .NET 2.0 kann eine solche Sicherheitsstufe die folgenden Einschränkungen festlegen, die beispielsweise die Fähigkeit von Aspose.Cells for .NET beeinträchtigen könnten, ordnungsgemäß zu funktionieren:

- **RegistryPermission ist nicht verfügbar**. Dies bedeutet, dass Sie nicht auf die Registrierung zugreifen können, die zum Auflisten installierter Schriftarten beim Rendern von Tabellenkalkulationen oder anderen Dokumenten erforderlich ist.
- **FileIOPermission ist eingeschränkt**Das bedeutet, dass Sie nur auf Dateien in der virtuellen Verzeichnishierarchie Ihrer Anwendung zugreifen können. Dies bedeutet möglicherweise, dass Schriftarten während des Exports nicht gelesen werden können.
## **Verwenden Sie Aspose.Cells for .NET auf Medium Trust Permissions Set**
Sie können einige Empfehlungen befolgen, um Aspose.Cells for .NET auf mittlerer Vertrauensstufe oder in einer gemeinsam genutzten Serverumgebung auszuführen:

- Um die Lizenzdatei in Ihrem Code festzulegen, sollten Sie stattdessen die License.SetLicense(Stream)-Methode aufrufen, nachdem Sie die Lizenzdatei in Streams erhalten haben.
- Das Verzeichnis der Schriftarten (auf das mit Erlaubnis zugegriffen werden konnte) muss festgelegt werden. Wenn es keine Möglichkeit gibt, auf die Datei auf dem Server zuzugreifen, fügen Sie bitte die benötigten Schriftdateien zu Ihrer Anwendung hinzu.
- Im teilweise vertrauenswürdigen Modus wird die Form-zu-EMF-Konvertierung nicht unterstützt, also legen Sie den exportierten Bildtyp (für Formen) auf ein anderes Bildformat fest.

Sehen Sie sich das folgende Beispiel an, das zeigt, wie Sie Aspose.Cells for .NET im Medium Trust-Modus verwenden/ausführen.

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





