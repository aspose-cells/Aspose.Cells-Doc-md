---
title: Convertir Excel en PDF avec C++
linktitle: Convertir Excel en PDF
type: docs
weight: 220
url: /fr/cpp/convert-excel-to-pdf/
description: Apprenez comment convertir les classeurs Excel en format PDF en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion des classeurs Excel en PDF. Dans cet exemple, nous verrons la conversion complète d'un classeur Excel en PDF.

{{% /alert %}}

## **Conversion du classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre organisations, secteurs gouvernementaux, et particuliers. C'est un format de document standard, et les développeurs de logiciels sont souvent sollicités pour trouver un moyen de convertir les fichiers Microsoft Excel en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{% alert color="primary" %}}

Aspose.Cells for C++ écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors de la génération d'un document en PDF, Aspose.Cells for C++ remplit le champ **PDf Producer** avec une valeur, par exemple 'Aspose.Cells v23.2'.

Veuillez noter que vous pouvez modifier ces informations dans les documents de sortie en utilisant la propriété [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **Conversion directe**

Aspose.Cells for C++ prend en charge la conversion de feuilles de calcul en PDF indépendamment des autres logiciels. Il suffit d'enregistrer un fichier Excel en PDF en utilisant la méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). La méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) fournit le membre d'énumération [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) qui convertit les fichiers Excel natifs en format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1. Instancier un objet de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier de modèle existant ou sauter cette étape si vous créez le classeur à partir de zéro.
1. Effectuez n'importe quel travail (données d'entrée, mise en forme, application de formules, insertion d'images ou autres objets de dessin, etc.) sur la feuille de calcul en utilisant les API d'Aspose.Cells.
1. Une fois le code de la feuille de calcul terminé, appelez la méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) pour enregistrer la feuille de calcul.

Le format de fichier doit être PDF, il faut donc sélectionner *Pdf* (une valeur prédéfinie) dans l'énumération [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) pour générer le document PDF final.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"output.pdf";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the document in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Document saved successfully in PDF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Conversion avancée**

Vous pouvez également choisir d'utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) pour définir différents attributs pour la conversion. La modification des propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) vous donne le contrôle sur les paramètres d'impression, la police, la sécurité et la compression pour le PDF de sortie.

La propriété la plus importante est [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), qui vous permet de définir le niveau de conformité aux normes PDF. Actuellement, vous pouvez enregistrer au format PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u. Notez qu'avec le format PDF/A, la taille du fichier de sortie est plus grande que celle d'un PDF classique.

#### **Enregistrement du classeur en fichiers conformes PDF/A**

Le morceau de code ci-dessous montre comment utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) pour enregistrer des fichiers Excel au format PDF/A compatible.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate new workbook
    Workbook workbook;

    // Insert a value into the A1 cell in the first worksheet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(U16String(u"Testing PDF/A"));

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set the compliance type
    pdfSaveOptions.SetCompliance(PdfCompliance::PdfA1b);

    // Save the file
    workbook.Save(outDir + u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file created successfully with PDF/A-1b compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Veuillez noter que la propriété [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) a été ajoutée avec la version Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Définir l'heure de création du PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/), vous pouvez obtenir ou définir l'heure de création du PDF. Le code suivant illustre l'utilisation de la propriété [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcreatedtime/) pour définir l'heure de création du fichier PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"Book1.xlsx";

    // Load excel file containing charts
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions options;
	options.SetCreatedTime(Date{ 2025,01,01 });

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(srcDir + u"output.pdf", options);

    std::cout << "Workbook saved to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Définir l'option ContentCopyForAccessibility**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/), vous pouvez obtenir ou définir l'option [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) du PDF pour contrôler l'accès au contenu dans le PDF converti.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"BookWithSomeData.xlsx";

    // Load excel file containing some data
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOpt;

    // Create an instance of PdfSecurityOptions
    PdfSecurityOptions securityOptions;

    // Set AccessibilityExtractContent to false
    securityOptions.SetAccessibilityExtractContent(false);

    // Set the security option in the PdfSaveOptions
    pdfSaveOpt.SetSecurityOptions(securityOptions);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(outDir + u"outFile.pdf", pdfSaveOpt);

    std::cout << "Workbook saved to PDF format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Exporter les propriétés personnalisées vers un PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/), vous pouvez exporter les propriétés personnalisées du classeur source vers le PDF. L'énumérateur [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être visualisées dans Adobe Acrobat Reader en cliquant sur Fichier puis Propriétés, comme illustré ci-dessous. Le fichier modèle "sourceWithCustProps.xlsx" peut être téléchargé [ici](sourceWithCustProps.xlsx) pour tester, et le fichier PDF de sortie "outSourceWithCustProps" est disponible [ici](outSourceWithCustProps.pdf) pour analyse.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load excel file containing custom properties
    U16String inputFilePath(u"sourceWithCustProps.xlsx");
    Workbook workbook(inputFilePath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set CustomPropertiesExport property to PdfCustomPropertiesExport::Standard
    pdfSaveOptions.SetCustomPropertiesExport(PdfCustomPropertiesExport::Standard);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    U16String outputFilePath(u"outSourceWithCustProps.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Attributs de conversion**

Nous travaillons à améliorer les fonctionnalités de conversion à chaque nouvelle version. La conversion Excel en PDF d'Aspose.Cells comporte encore quelques limitations. MapChart n'est pas supporté lors de la conversion en PDF. De plus, certains objets de dessin ne sont pas bien pris en charge.

Le tableau suivant liste toutes les fonctionnalités entièrement ou partiellement supportées lors de l'exportation en PDF avec Aspose.Cells. Ce tableau n'est pas définitif et ne couvre pas toutes les attributs du tableur, mais il identifie celles qui ne sont pas prises en charge ou partiellement supportées pour la conversion en PDF.

| Élément du document | Attribut | Pris en charge | Notes |
| :- | :- | :- | :- |
| Alignement |  | Oui |  |
| Paramètres de fond |  | Oui |  |
| Bordure | Couleur | Oui |  |
| Bordure | Style de ligne | Oui |  |
| Bordure | Largeur de ligne | Oui |  |
| Données de la cellule |  | Oui |  |
| Commentaires |  | Oui |  |
| Mise en forme conditionnelle |  | Oui |  |
| Propriétés du document |  | Oui |  |
| Objets de dessin |  | Partiellement | Les effets d'ombre et 3D pour les objets de dessin ne sont pas bien pris en charge ; WordArt et SmartArt sont partiellement supportés. |
| Police | Taille | Oui |  |
| Police | Couleur | Oui |  |
| Police | Style | Oui |  |
| Police | Soulignement | Oui |  |
| Police | Effets | Oui |  |
| Images |  | Oui |  |
| Lien hypertexte |  | Oui |  |
| Graphiques |  | Partiellement | MapChart n'est pas supporté. |
| Cellules fusionnées |  | Oui |  |
| Saut de page |  | Oui |  |
| Mise en page | En-tête/Pied de page | Oui |  |
| Mise en page | Marges | Oui |  |
| Mise en page | Orientation de la page | Oui |  |
| Mise en page | Taille de la page | Oui |  |
| Mise en page | Zone d'impression | Oui |  |
| Mise en page | Titres à imprimer | Oui |  |
| Mise en page | Escalabilité | Oui |  |
| Hauteur des lignes/largeur des colonnes |  | Oui |  |
| Langue RTL (de droite à gauche) |  | Oui |  |

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de rendre la feuille de calcul en format PDF. Cela garantira que les valeurs dépendantes des formules sont recalculées, et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter des signets PDF avec des destinations nommées](/cells/fr/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Changer la police uniquement pour des caractères Unicode spécifiques lors de l'enregistrement au format PDF](/cells/fr/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Convertir un fichier XLSX au format PDF](/cells/fr/cpp/convert-xlsx-file-to-pdf-format/)
- [Convertir un fichier Excel au format PDF compatible avec PDFA-1a](/cells/fr/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir un fichier XLS avec des images ou des graphiques au format PDF](/cells/fr/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Créer une entrée PdfBookmark pour une feuille de graphique](/cells/fr/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF](/cells/fr/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Obtenir DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler](/cells/fr/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Obtenir des avertissements de substitution de police lors du rendu du fichier Excel](/cells/fr/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorer les erreurs lors du rendu Excel vers PDF](/cells/fr/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limiter le nombre de pages généré - Conversion Excel vers PDF](/cells/fr/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimer les commentaires lors de l'enregistrement au format PDF](/cells/fr/cpp/print-comments-while-saving-to-pdf/)
- [Rendre les compléments Office lors de la conversion Excel en PDF](/cells/fr/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendre une page PDF par feuille de calcul Excel - Conversion Excel en PDF](/cells/fr/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendre les caractères supplémentaires Unicode dans le PDF final par Aspose.Cells](/cells/fr/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Redimensionner les images ajoutées - Conversion Excel en PDF](/cells/fr/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Sauvegarder chaque feuille de calcul dans un fichier PDF différent](/cells/fr/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Enregistrer Excel en PDF avec une taille standard ou minimale](/cells/fr/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Enregistrer des feuilles de calcul spécifiées au format PDF](/cells/fr/cpp/save-specified-worksheets-to-pdf/)
- [Sécuriser les documents PDF](/cells/fr/cpp/secure-pdf-documents/)
- [Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image](/cells/fr/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="cpp" >}}
