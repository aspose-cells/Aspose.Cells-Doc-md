--- 
title: Erstellen eines transparenten Bildes des Excel Arbeitsblatts mit C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /de/cpp/create-transparent-image-of-excel-worksheet/ 
description: Erzeugen Sie transparente Bilder von Excel Arbeitsblättern mit Aspose.Cells und C++. 
--- 

{{% alert color="primary" %}} 

Manchmal müssen Sie das Bild Ihres Arbeitsblatts als transparentes Bild generieren. Sie möchten Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells bietet die [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/)-Eigenschaft, um Transparenz auf das Arbeitsblattbild anzuwenden. Wenn diese Eigenschaft **false** ist, werden Zellen ohne Füllfarben mit weißer Farbe gezeichnet, und wenn sie **true** ist, werden Zellen ohne Füllfarben transparent gezeichnet. 

{{% /alert %}} 

In der folgenden Arbeitsblattansicht wurde keine Transparenz angewendet. Die Zellen ohne Füllfarben sind weiß gezeichnet.

|**Ausgabe ohne Transparenz: Der Zellenhintergrund ist weiß**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Während in der folgenden Arbeitsblattansicht Transparenz angewendet wurde. Die Zellen ohne Füllfarben sind transparent.

|**Ausgabe mit aktivierter Transparenz**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

Der folgende Beispielscode generiert ein transparentes Bild aus einem Excel-Arbeitsblatt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleCreateTransparentImage.xlsx");

    // Apply different image or print options
    ImageOrPrintOptions imgOption;
    imgOption.SetImageType(static_cast<ImageType>(5)); // Png
    imgOption.SetHorizontalResolution(200);
    imgOption.SetVerticalResolution(200);
    imgOption.SetOnePagePerSheet(true);

    // Apply transparency to the output image
    imgOption.SetTransparent(true);

    // Create image after applying image or print options
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOption);
    sr.ToImage(0, outputDir + u"outputCreateTransparentImage.png");

    std::cout << "Image created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
