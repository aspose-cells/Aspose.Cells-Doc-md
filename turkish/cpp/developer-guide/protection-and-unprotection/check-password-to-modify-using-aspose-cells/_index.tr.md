---
title: Aspose.Cells ile Çalışma Sayfasını Parola ile Koruma ve Kontrol Etme
linktitle: Düzenleme parolası kontrolü yapma
type: docs
weight: 2400
url: /tr/cpp/check-password-to-modify-using-aspose-cells/
description: Aspose.Cells kullanarak verilen parolanın Parola ile koruma ile eşleşip eşleşmediğini kontrol edin.
---

{{% alert color="primary" %}}

Bazen, verilen parolanın **Parola ile koruma** ile otomatik olarak eşleşip eşleşmediğini kontrol etmeniz gerekir. Aspose.Cells, kullanabileceğiniz WorkbookSettings.WriteProtection.ValidatePassword() yöntemi sağlar.

{{% /alert %}}

## **Microsoft Excel'de Değiştirme Şifresini Kontrol Etme**

Microsoft Excel'de çalışma kitapları oluştururken **Açma Şifresi** ve **Değiştirme Şifresi** atayabilirsiniz. Bu şifreleri belirlemek için Microsoft Excel'in sağladığı arayüzü gösteren bu ekran görüntüsüne bakınız.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells Kullanarak Değiştirme Şifresini Kontrol Etme**

Aşağıdaki örnek kod, [kaynak Excel](5112232.xlsx) dosyasını yükler. Dosyanın Açma Şifresi 1234 ve Değiştirme Şifresi 5678'dir. Kod önce 567'nin doğru Değiştirme Şifresi olup olmadığını kontrol eder ve yanlış döndürür, ardından 5678'in Değiştirme Şifresi olup olmadığını kontrol eder ve doğru döndürür.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun [kaynak Excel](5112232.xlsx) dosyasını yükledikten sonraki Konsol Çıkışı burada.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
