---
title: C++ ile Bir Çalışma Kitabında Belirli Çalışma Sayfalarını Yükleme
linktitle: Aşağıdaki örnek kod, örnek excel dosyasını grafikleri olmadan yükler ve çıktı PDF formatında kaydeder.
type: docs
weight: 100
url: /tr/cpp/load-specific-worksheets-in-a-workbook/
description: Aspose.Cells kullanarak belirli çalışma sayfalarını yüklemeyi öğrenin, böylece performansı artırabilir ve bellek kullanımını azaltabilirsiniz.
---

{{% alert color="primary" %}}

 Varsayılan olarak, Aspose.Cells tüm çalışma sayfasını belleğe yükler. Sadece belirli sayfaların yüklenmesi de mümkündür; bu, performansı artırabilir ve daha az bellek kullanabilir. Bu yöntem, büyük ve çok sayfalı bir çalışma kitabıyla çalışırken faydalıdır.

{{% /alert %}}

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter {
public:
    CustomLoad() : LoadFilter(LoadDataFilterOptions::All) {}

    // Override StartSheet to customize loading behavior
    void StartSheet(Worksheet& sheet) override {
        // Custom logic for loading specific worksheet
    }
};

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Define a new Workbook
    Workbook workbook;

    // Load the workbook with the specified worksheet only
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new CustomLoad());

    // Create the workbook with custom load options
    workbook = Workbook(srcDir + u"TestData.xlsx", loadOptions);

    // Perform your desired task

    // Save the workbook
    workbook.Save(srcDir + u"outputFile.out.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

 İşte `CustomLoad` sınıfının uygulaması.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter
{
public:
    CustomLoad() : LoadFilter() {}
    ~CustomLoad() {}

    void StartSheet(Worksheet& sheet) override
    {
        if (sheet.GetName() == u"Sheet2")
        {
            // Load everything from worksheet "Sheet2"
            SetLoadDataFilterOptions(LoadDataFilterOptions::All);
        }
        else
        {
            // Load nothing
            SetLoadDataFilterOptions(LoadDataFilterOptions::Structure);
        }
    }
};
```
{{< app/cells/assistant language="cpp" >}}
