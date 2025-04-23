---
title: Deklaration
type: docs
weight: 30
url: /de/net/declaration/
---

{{% alert color="primary" %}} 

Generell erfordern alle Aspose .NET-Komponenten Full-Trust-Berechtigungen. Der Grund dafür ist, dass Aspose für .NET-Komponenten auf Registryeinstellungen, Systemdateien und andere als virtuelles Verzeichnis benötigt, um bestimmte Operationen wie das Parsen von Schriften usw. durchzuführen. Darüber hinaus sind Aspose für .NET-Komponenten (einschließlich Aspose.Cells for .NET) auf Kern-.NET-Systemklassen basierend, die in vielen Fällen ebenfalls Full-Trust-Berechtigungen erfordern.

{{% /alert %}} 
## **Teilweiser Vertrauen / Mittleres Vertrauen-Herausforderung**
 Internetdienstanbieter, die mehrere Anwendungen von verschiedenen Unternehmen hosten, setzen in der Regel ein Medium-Trust-Sicherheitsniveau durch. Manchmal müssen Sie zudem mehrere Anwendungen auf einem gemeinsam genutzten Server hosten, beispielsweise bei einem Internetdienstanbieter oder in anderen Szenarien, und Sie müssen das Sicherheitsniveau Medium Trust verwenden, um die Anwendungen einzuschränken. Das ASP.NET Medium Trust-Level bietet eine eingeschränkte Ausführungsumgebung, die für die Isolierung mehrerer Anwendungen, die auf ISP-Servern gehostet werden, geeignet ist. Bei .NET 2.0 können solche Sicherheitsstufen die folgenden Einschränkungen festlegen, die die Fähigkeit von Aspose.Cells for .NET beeinträchtigen könnten, ordnungsgemäß zu funktionieren:

- **RegistryPermission ist nicht verfügbar**. Dies bedeutet, dass Sie nicht auf die Registrierung zugreifen können, was zum Auflisten installierter Schriftarten beim Rendern von Tabellenkalkulationen oder anderen Dokumenten erforderlich ist.
- Die **FileIOPermission ist eingeschränkt**. Dies bedeutet, dass Sie nur auf Dateien im hierarchischen virtuellen Verzeichnis Ihrer Anwendung zugreifen können. Dies bedeutet potenziell, dass Schriften beim Export nicht gelesen werden können.
## **Verwenden von Aspose.Cells for .NET bei Medium Trust-Berechtigungen**
Es gibt einige Empfehlungen, um Aspose.Cells for .NET auf dem Sicherheitsniveau Medium Trust oder in einer gemeinsam genutzten Serverumgebung auszuführen:

- Um die Lizenzdatei in Ihrem Code festzulegen, sollten Sie besser die Methode License.SetLicense(Stream) aufrufen, nachdem Sie die Lizenzdatei in Streams erhalten haben.
- Das Verzeichnis der Schriften (auf das mit Berechtigung zugegriffen werden kann) muss festgelegt sein. Wenn es keine Möglichkeit gibt, auf die Datei auf dem Server zuzugreifen, fügen Sie bitte die benötigten Schriftdateien Ihrer Anwendung hinzu.
- Im teilweisen Vertrauensmodus wird die Konvertierung von Form zu EMF nicht unterstützt. Legen Sie daher den exportierten Bildtyp (für Formen) auf andere Bildformate fest.

Sehen Sie sich das folgende Beispiel an, das zeigt, wie Sie Aspose.Cells for .NET im Sicherheitsniveau Medium Trust ausführen können.

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
