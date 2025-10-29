---
title: Modifier la police uniquement pour les caractères Unicode spécifiques lors de l enregistrement en PDF avec C++
linktitle: Modifier la police sur les caractères Unicode
type: docs
weight: 260
url: /fr/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Apprenez comment changer la police de certains caractères Unicode lors de l enregistrement en PDF en utilisant Aspose.Cells avec C++. 
---

{{% alert color="primary" %}}

Certains caractères Unicode ne sont pas affichables par la police spécifiée par l'utilisateur. Un de ces caractères Unicode est **Non-breaking Hyphen** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais il peut être affiché avec d'autres polices comme **Arial Unicode MS**.

Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase en police spécifique comme Times New Roman, Aspose.Cells change la police de l'ensemble du mot ou de la phrase en une police pouvant afficher ce caractère comme Arial Unicode MS.

Cependant, ce comportement est indésirable pour certains utilisateurs, et ils souhaitent que seule la police de ce caractère spécifique soit modifiée au lieu de changer la police de tout le mot ou la phrase.

Pour résoudre ce problème, Aspose.Cells fournit la propriété `PdfSaveOptions.IsFontSubstitutionCharGranularity`, qui doit être réglée à `true` afin que seule la police du caractère spécifique qui ne peut pas être affiché soit modifiée en une police affichable, et le reste du mot ou de la phrase reste dans sa police d'origine.

{{% /alert %}}

## **Exemple**

La capture d'écran suivante compare les deux fichiers PDF générés par le code d'exemple ci-dessous.

Une est générée sans régler la propriété `PdfSaveOptions.IsFontSubstitutionCharGranularity`, et l'autre a été générée après avoir défini la propriété `PdfSaveOptions.IsFontSubstitutionCharGranularity` à `true`.

Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière a changé de Times New Roman à Arial Unicode MS à cause du tiret insécable. Alors que dans le deuxième PDF, seule la police du tiret insécable a changé.

|**Premier fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Second fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Code d'exemple**

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style style = cell1.GetStyle();
    style.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(style);
    cell2.SetStyle(style);

    // Put the values inside the cell
    cell1.PutValue(u"Hello without Non-Breaking Hyphen");
    cell2.PutValue(u"Hello\u2011 with Non-Breaking Hyphen");

    // Autofit the columns
    worksheet.AutoFitColumns();

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.pdf");

    // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
    PdfSaveOptions opts;
    opts.SetIsFontSubstitutionCharGranularity(true);
    workbook.Save(outDir + u"SampleOutput2_out.pdf", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
