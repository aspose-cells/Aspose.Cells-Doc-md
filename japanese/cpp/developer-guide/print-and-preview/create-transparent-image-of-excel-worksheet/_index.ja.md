--- 
title: C++を使ったExcelシートの透過画像の作成 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /ja/cpp/create-transparent-image-of-excel-worksheet/ 
description: Aspose.Cells を使用して Excel シートの透過画像を生成（C++） 
--- 

{{% alert color="primary" %}} 

時々、ワークシートの画像を透明なイメージとして生成する必要があります。埋められていないセルに透明性を適用したい場合があります。Aspose.Cellsは透明性をワークシートイメージに適用するための[**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/)プロパティを提供しています。このプロパティが **false** の場合、埋められていないセルは白色で描画され、 **true** の場合、埋められていないセルは透明に描画されます。 

{{% /alert %}} 

以下のワークシートイメージでは、透明性が適用されていません。埋められていないセルは白色で描画されます。

|**透明度なしの出力: セルの背景は白です**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

以下のワークシート画像では、透明度が適用されました。塗りつぶしのないセルは透明です。

|**透明度を有効にした出力**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

次のサンプルコードは、Excelワークシートから透明な画像を生成します。

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
