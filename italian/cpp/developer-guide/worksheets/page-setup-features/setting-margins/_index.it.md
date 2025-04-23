---
title: Impostare margini con C++
linktitle: Impostazione dei margini
type: docs
weight: 20
url: /it/cpp/setting-margins/
description: Impara come impostare i margini di un foglio di lavoro Excel utilizzando C++. Questa guida copre impostazione margini di pagina, centramento del contenuto e configurazione dei margini di intestazione e piè di pagina in modo programmatico con Aspose.Cells for C++.
keywords: impostare margine foglio di lavoro Excel al centro C++, impostare margine intestazione e piè di pagina C++
---

{{% alert color="primary" %}}

Aspose.Cells supporta completamente le opzioni di impostazione della pagina di Microsoft Excel. Gli sviluppatori potrebbero dover configurare le impostazioni del layout di pagina per controllare il processo di stampa dei fogli di lavoro. Questo argomento discute come utilizzare Aspose.Cells per configurare i margini di pagina.

{{% /alert %}}

## **Impostazione margini**

 Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene la collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro del file Excel. Un foglio di lavoro viene rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

 La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce la proprietà [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) usata per impostare le opzioni di configurazione della pagina per un foglio di lavoro. L'attributo [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) è un oggetto della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) che permette agli sviluppatori di impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) fornisce varie proprietà e metodi usati per impostare le opzioni di configurazione della pagina.

### **Margini di Pagina**

 Imposta margini di pagina (sinistra, destra, superiore, inferiore) utilizzando membri della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Alcuni dei metodi sono elencati di seguito e vengono usati per specificare i margini di pagina:

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

### **Centra sulla Pagina**

 È possibile centrare qualcosa su una pagina orizzontalmente e verticalmente. Per questo, ci sono alcuni membri utili della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) e [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

### **Margini Intestazione e Piè di Pagina**

 Imposta i margini di intestazione e piè di pagina con membri della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) come [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) e [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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
