---
title: C++ ile Paylaşılan Formülü Ayarla
linktitle: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/cpp/setting-shared-formula/
description: Aspose.Cells kullanarak Excel çalışma sayfalarında paylaşılan formülleri C++ ile nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Çalışma sayfasında hesaplama yapacak bir fonksiyon eklemek istiyorsanız, bu makale Aspose.Cells kullanarak bu görevi nasıl başaracağınızı açıklar.

{{% /alert %}}

## Aspose.Cells kullanarak Paylaşılan Formül Ayarlama

Aşağıdaki örnek elektronik tabloya benzer biçimde veriyle dolu bir çalışma sayfasını varsayalım.

|**Giriş dosyası ile tek sütun veri**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Bir fonksiyon eklemek istiyorsunuz ve bu fonksiyon, verinin ilk satırı için satış vergisini hesaplayacak. Vergi **%9**. Satış vergisini hesaplayan formül şudur: **"=A2*0.09"**. Bu makale, bu formülü Aspose.Cells ile nasıl uygulayacağınızı açıklar.

Aspose.Cells, [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) özelliğini kullanarak bir formül belirtmenizi sağlar. Sütunun diğer hücrelerine (B3, B4, B5 ve benzeri) formül eklemek için iki seçenek bulunmaktadır.

İlk hücrede yaptığınız gibi, formülü her hücreye etkin şekilde ayarlayın, hücre referansını uygun şekilde güncelleyerek (A3*0.09, A4*0.09, A5*0.09 vb.). Bu, her satırın hücre referanslarının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'un her formülü ayrı ayrı çözümlemesi gerekir, bu büyük tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca, fazla kod satırı eklenir, ancak döngüler bunları biraz azaltabilir.

Başka bir yaklaşım, **paylaşılan bir formül** kullanmaktır. Paylaşılan formülle, formüller her satırın hücre referansları için otomatik olarak güncellenir, böylece vergi uygun şekilde hesaplanır. [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) yöntemi, birinci yöntemden daha verimlidir.

Aşağıdaki örnek, bunu nasıl kullanacağınızı göstermektedir.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
