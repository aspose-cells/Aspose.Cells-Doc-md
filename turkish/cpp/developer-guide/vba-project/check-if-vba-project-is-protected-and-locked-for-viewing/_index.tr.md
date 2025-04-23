---
title: VBA Projesi Korundu ve Görüntülemeye Kilitlendi mi diye C++ ile Kontrol Edin
linktitle: C# da Bir Çalışbookun VBA Projesinin Korunup Görüntüleme İçin Kilitli Olup Olmadığını Kontrol Et
type: docs
weight: 30
url: /tr/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Excel dosyalarında VBA Projesinin korunduğunu ve görüntülenmeye kilitlendiğini nasıl kontrol edileceğini Aspose.Cells for C++ kullanarak öğrenin.
---

## VBA Projesinin Korunduğunu ve Görüntülemeye Kilitlendiğini Kontrol Etme (C++)

 Aspose.Cells, bir Excel dosyasının VBA (Visual Basic for Applications) Projesinin korunduğunu ve görüntülemeye kilitlendiğini kontrol etmenize olanak tanır. Bunun için API, [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) özelliği sağlar. Eğer korundusa, [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) özelliği **true** döner.

## **Örnek Kod**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](43352065.xlsm) yükler ve VBA (Visual Basic for Applications) Projesinin korunduğunu ve görüntülemeye kilitli olup olmadığını kontrol eder. Ayrıca, İstediğinizde bunun Konsol Çıktısını da görebilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

Sağlanan [örnek Excel dosyası](43352065.xlsm) ile yukarıdaki örnek kodun çalıştırılması durumunda elde edilen konsol çıkışı budur.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
