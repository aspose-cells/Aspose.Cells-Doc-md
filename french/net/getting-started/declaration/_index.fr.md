---
title: Déclaration
type: docs
weight: 30
url: /fr/net/declaration/
---

{{% alert color="primary" %}} 

En général, tous les composants Aspose .NET nécessitent des autorisations Full Trust. La raison en est que les composants Aspose pour .NET ont besoin d'accéder aux paramètres du registre, aux fichiers système autres que le répertoire virtuel pour certaines opérations telles que l'analyse des polices, etc. De plus, les composants Aspose pour .NET (y compris Aspose.Cells for .NET) sont basés sur les classes système .NET de base qui nécessitent également des autorisations Full Trust dans de nombreux cas.

{{% /alert %}} 
## **Défi de confiance partielle / moyenne confiance**
La plupart du temps, les fournisseurs de services Internet hébergeant plusieurs applications de différentes entreprises imposent principalement un niveau de sécurité de moyenne confiance. De plus, parfois, vous devez héberger plusieurs applications sur un serveur partagé, tel que chez un fournisseur de services Internet ou dans d'autres scénarios, vous devez utiliser le niveau de confiance moyenne pour restreindre les applications. Le niveau de confiance moyen ASP.NET fournit un environnement d'exécution restreint qui convient à l'isolation de plusieurs applications hébergées sur des serveurs de fournisseurs de services Internet. Dans le cas de .NET 2.0, un tel niveau de sécurité peut définir les contraintes suivantes qui pourraient affecter la capacité de Aspose.Cells for .NET à fonctionner correctement, par exemple :

- **RegistryPermission n'est pas disponible**. Cela signifie que vous ne pouvez pas accéder au registre, ce qui est nécessaire pour énumérer les polices installées lors du rendu de feuilles de calcul ou d'autres documents.
- **FileIOPermission est restreint**. Cela signifie que vous ne pouvez accéder qu'aux fichiers dans la hiérarchie de répertoires virtuels de votre application. Cela signifie potentiellement que les polices ne peuvent pas être lues lors de l'exportation.
## **Utiliser Aspose.Cells for .NET sur l'ensemble des autorisations de confiance moyenne**
Vous pouvez suivre certaines recommandations pour exécuter Aspose.Cells for .NET en mode de confiance moyenne ou dans un environnement de serveur partagé :

- Pour définir le fichier de licence dans votre code, il est préférable d'appeler la méthode License.SetLicense(Stream) après avoir obtenu le fichier de licence dans des flux.
- Le répertoire des polices (auquel vous pouvez accéder avec une autorisation) doit être défini. S'il n'y a aucun moyen d'accéder au fichier sur le serveur, veuillez ajouter les fichiers de polices nécessaires à votre application.
- En mode de confiance partielle, la conversion de la forme en EMF n'est pas prise en charge, donc définissez le type d'image exportée (pour les formes) sur d'autres formats d'image.

Voir l'exemple suivant qui démontre comment utiliser/exécuter Aspose.Cells for .NET en mode de confiance moyenne.

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





