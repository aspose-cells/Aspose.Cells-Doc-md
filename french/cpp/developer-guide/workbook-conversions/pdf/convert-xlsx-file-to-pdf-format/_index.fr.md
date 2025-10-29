---
title: Convertir un fichier XLSX en PDF avec C++
linktitle: Convertir un fichier XLSX au format PDF
type: docs
weight: 30
url: /fr/cpp/convert-xlsx-file-to-pdf-format/
description: Apprenez comment convertir des fichiers Excel en format PDF en utilisant Aspose.Cells for C++ avec une grande précision et exactitude.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) représente des documents indépendamment du logiciel, du matériel et du système d'exploitation utilisés pour créer ces documents. Un fichier PDF peut contenir une combinaison de texte, graphiques et images de manière indépendante du dispositif et de la résolution. Les fichiers PDF sont souvent compressés, ce qui leur permet de prendre moins d'espace que le fichier original.

Parfois, vous avez besoin de convertir un fichier Microsoft Excel en PDF. Pour cela, vous avez besoin d'une solution rapide, sûre, précise et fiable qui vous permet de distribuer des documents PDF dans le monde entier. Il existe de nombreux outils de conversion capables d'effectuer cette tâche. Mais vous devez vous assurer que la mise en page du document Excel d'origine est conservée dans le fichier PDF de sortie. Les images, graphiques, formes, mise en forme des données, polices, attributs, couleurs, paramètres de mise en page, orientation du texte, bordures, graphiques, etc., doivent être rendus avec précision et exactitude. [Aspose.Cells](https://products.aspose.com/cells/cpp/) garantit une conversion de haute fidélité.

Ce document est conçu pour fournir une compréhension complète de la façon dont un document Microsoft Excel (contenant des images, des graphiques, des formats, etc.) peut être converti en PDF. À cette fin, il montre comment créer une application console simple en C++ qui convertit un fichier Excel en PDF en utilisant l'API Aspose.Cells. La conversion est effectuée avec un haut degré de précision et d'exactitude.

{{% /alert %}}

## **Conversion d'Excel en PDF**

Cet exemple utilise un fichier Excel (SampleInput.xlsx) comme modèle. Le classeur contient des feuilles avec des graphiques et des images. Chaque feuille contient différents types de formats utilisant des polices, des attributs, des couleurs, des effets de shading, et des bordures. Il y a un graphique en colonnes sur la première feuille et une image sur la dernière.

### **Le fichier Excel modèle**

Le fichier modèle comporte trois feuilles, y compris des graphiques et des images en tant que médias. La première feuille comporte des graphiques, et la dernière une image, comme montré dans les captures d'écran ci-dessous.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|

### **Processus de conversion**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de rendre la feuille en PDF. Cela garantit que les valeurs dépendantes des formules seront recalculées et que les bonnes valeurs seront affichées dans le PDF.

{{% /alert %}}

### **Résultat**

Lorsque le code ci-dessus est exécuté, un fichier PDF est créé dans le dossier Files de votre répertoire d'application.
Les captures d'écran suivantes montrent les pages PDF. Notez que les en-têtes et pieds de pages sont également conservés dans le fichier PDF de sortie.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|
{{< app/cells/assistant language="cpp" >}}
