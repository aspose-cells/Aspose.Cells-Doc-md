---
title: Déclaration
type: docs
weight: 30
url: /fr/net/declaration/
---
{{% alert color="primary" %}} 

Généralement, tous les composants Aspose .NET nécessitent un ensemble d'autorisations de confiance totale. La raison en est que les composants Aspose for .NET doivent accéder aux paramètres de registre, aux fichiers système autres que le répertoire virtuel pour certaines opérations telles que l'analyse des polices, etc. fixé dans de nombreux cas.

{{% /alert %}} 
## **Défi de confiance partielle/confiance moyenne**
Les fournisseurs de services Internet hébergeant plusieurs applications de différentes sociétés appliquent généralement un niveau de sécurité de confiance moyenne. De plus, vous devez parfois héberger plusieurs applications sur un serveur partagé, comme dans un FAI ou d'autres scénarios, vous devez utiliser le niveau de confiance moyen pour limiter les applications. Le niveau de confiance moyen ASP.NET fournit un environnement d'exécution contraint qui convient pour isoler plusieurs applications hébergées sur des serveurs ISP. Dans le cas de .NET 2.0, un tel niveau de sécurité peut définir les contraintes suivantes qui pourraient affecter la capacité de Aspose.Cells for .NET à fonctionner correctement, par exemple :

- **RegistryPermission n'est pas disponible**. Cela signifie que vous ne pouvez pas accéder au registre, qui est nécessaire pour énumérer les polices installées lors du rendu des feuilles de calcul ou d'autres documents.
- **FileIOPermission est limité**Cela signifie que vous ne pouvez accéder qu'aux fichiers de la hiérarchie de répertoires virtuels de votre application. Cela signifie potentiellement que les polices ne peuvent pas être lues lors de l'exportation.
## **Utilisez Aspose.Cells for .NET sur un ensemble d'autorisations de confiance moyenne**
Vous pouvez suivre certaines recommandations pour exécuter Aspose.Cells for .NET sur un niveau de confiance moyen ou un environnement de serveur partagé :

- Pour définir le fichier de licence dans votre code, il est préférable d'appeler la méthode License.SetLicense(Stream) après avoir obtenu le fichier de licence dans les flux.
- Le répertoire des polices (accessible avec autorisation) doit être défini. S'il n'y a aucun moyen d'accéder au fichier sur le serveur, veuillez ajouter les fichiers de police nécessaires à votre application.
- En mode de confiance partielle, la conversion Shape-to-EMF n'est pas prise en charge. Par conséquent, définissez le type d'image exportée (pour les formes) sur un autre format d'image.

Consultez l'exemple suivant qui montre comment utiliser/exécuter Aspose.Cells for .NET en mode Medium Trust.

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





