---
title: Configuration des marges avec C++
linktitle: Réglage des marges
type: docs
weight: 20
url: /fr/cpp/setting-margins/
description: Apprenez à définir les marges d une feuille Excel en utilisant C++. Ce guide couvre la définition des marges de page, la centration du contenu, et la configuration des marges d en tête et de pied de page de manière programmée avec Aspose.Cells for C++.
keywords: définir la marge de la feuille Excel au centre c++, définir la marge de l en tête et du pied de page de la feuille c++
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge pleinement les options de configuration de la mise en page de Microsoft Excel. Les développeurs peuvent avoir besoin de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler le processus d'impression. Ce sujet traite de l'utilisation d'Aspose.Cells pour configurer les marges de la page.

{{% /alert %}}

## **Réglage des marges**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

 La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit la propriété [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) utilisée pour définir les options de mise en page pour une feuille de calcul. L'attribut [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) est un objet de la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) qui permet aux développeurs de définir différentes options de disposition pour une feuille imprimée. La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) offre diverses propriétés et méthodes pour définir les options de mise en page.

### **Marges de la page**

Définir les marges de la page (gauche, droite, haut, bas) en utilisant les membres de la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Voici quelques méthodes utilisées pour spécifier les marges de la page :

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Centrer sur la page**

Il est possible de centrer quelque chose horizontalement et verticalement sur une page. Pour cela, il existe des membres utiles de la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) et [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Marges d'en-tête et de pied de page	**

Définir les marges d'en-tête et de pied de page avec les membres de classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) tels que [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) et [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
