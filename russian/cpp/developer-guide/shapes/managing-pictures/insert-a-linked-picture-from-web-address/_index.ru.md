---
title: Вставка связанной картинки с веб адреса с помощью C++
linktitle: Вставить связанное изображение из веб адреса
type: docs
weight: 450
url: /ru/cpp/insert-a-linked-picture-from-web-address/
description: Узнайте, как вставлять связанную картинку из веб адреса в лист с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить изображение из интернета (http://) в таблицу. Для этого укажите URL изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение фактически не вставляется в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Использование Microsoft Excel**

В Microsoft Excel (например, 2007 год):

1. Нажмите меню **Вставка** и выберите **Изображение**.
1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения.

## **Использование Aspose.Cells for C++**

Aspose.Cells for C++ поддерживает добавление связанного изображения с помощью метода [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/). Этот метод возвращает объект [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). 

Следующий пример показывает, как добавить связанное изображение из веб-адреса в лист.

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
