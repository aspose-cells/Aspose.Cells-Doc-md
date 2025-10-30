---
title: Inserisci un immagine collegata da indirizzo web con C++
linktitle: Inserisci un immagine collegata da un indirizzo web
type: docs
weight: 450
url: /it/cpp/insert-a-linked-picture-from-web-address/
description: Impara come inserire un immagine collegata da un indirizzo web in un foglio di lavoro usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte è necessario inserire un'immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell'immagine e l'immagine verrà scaricata ogni volta che il foglio di calcolo viene aperto in Microsoft Excel. L'immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

In Microsoft Excel (ad esempio 2007):

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.
1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine.

## **Utilizzando Aspose.Cells for C++**

Aspose.Cells for C++ supporta l'aggiunta di un'immagine collegata usando il metodo [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/). Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

L'esempio seguente mostra come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
