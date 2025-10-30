---
title: C++ ile Excel Dosyası Yüklenirken Uyarıları Alma
linktitle: Excel Dosyası Yüklenirken Uyarıları Al
type: docs
weight: 110
url: /tr/cpp/get-warnings-while-loading-excel-file/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını yüklerken uyarıları nasıl yakalayacağınızı ve yönetileceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

 Bazen kullanıcı, biraz bozuk ama yine de yüklenebilir olan bir çalışma kitabını yüklemeye çalışır. Bu gibi durumlarda, Aspose.Cells çalışma kitabını yüklerken uyarılar fırlatır. Bu uyarıları yakalayabilir ve [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) arayüzünü uygulayarak ve [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/) özelliğini ayarlayarak yönetebilirsiniz.

## **Excel Dosyası Yüklenirken Uyarıları Al**

 Aşağıdaki örnek kod, bir Excel dosyasını yüklerken uyarıları nasıl alacağınızı açıklar. Kod, yükleme sırasında [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) uyarısı atanmış bir örnek Excel dosyasını (sampleDuplicateDefinedName.xlsx) yükler. Bu uyarı, [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/) yöntemi tarafından yakalanır ve uyarı mesajları konsola yazdırılır. Ardından, çalışma kitabını bir [çıktı Excel dosyası](outputDuplicateDefinedName.xlsx) olarak kaydeder. Eğer örnek Excel dosyasını Microsoft Excel'de açarsanız, bu uyarıyı da göreceksiniz, aşağıdaki ekran görüntüsünde gösterildiği gibi. Bu kodun konsol çıktısını da kontrol etmeyi unutmayın.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

Yukarıdaki kodun, verilen [örnek excel dosyası](sampleDuplicateDefinedName.xlsx) ile çalıştırıldığında konsol çıktısı şöyledir.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
