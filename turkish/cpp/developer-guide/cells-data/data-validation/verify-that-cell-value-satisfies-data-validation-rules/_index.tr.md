---
title: Hücre Doğrulama Kurallarını Sağlayıp Sağlamadığını Kontrol Edin (C++)
linktitle: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 210
url: /tr/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for C++ API’sini kullanarak Hücre Değerinin Veri Doğrulama Kurallarını Sağlayıp Sağlamadığını nasıl teyit edeceğinizi öğrenin.
keywords: Hücre Doğrulama Değeri Al, Hücre Doğrulama Değeri Al, Bir değerin hücreye uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulayın
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hücrelere veri doğrulama kuralları ekleme imkanı tanır. Örneğin, ondalık doğrulama, yalnızca 10 ile 20 arasında sayıların girilmesine izin verir. Kullanıcı farklı bir sayı girerse, Microsoft Excel hata mesajı gösterir ve doğru aralıkta sayı girmesini ister. Bir sayıyı kopyalayıp yapıştırırsanız, diyelim ki 3, Excel doğrulama kontrolü yapmaz veya hata mesajı göstermez.

Bazen, bir değerin hücreye uygulanan veri doğrulama kurallarını programlı olarak karşılayıp karşılamadığını doğrulamak gereklidir. Yukarıdaki durumda, örneğin, giriş başarısız olmalıdır.

{{% /alert %}} 

## **Giriş**
Aspose.Cells, hücre değerlerini programlı olarak doğrulamak için [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) metodunu sağlar. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa, **False** döner, karşılıyorsa **True** döner.

Aşağıdaki örnek kod, [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) metodunun nasıl çalıştığını gösterir. İlk olarak, C1 hücresine 3 değeri girilir. Bu, veri doğrulama kuralını karşılamadığından, metod **False** döner. Daha sonra, C1 hücresine 15 değeri girilir. Bu değer doğrulama kuralını karşıladığından, metod **True** döner. Aynı şekilde, 30 değeri için **False** döner.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Çıktı**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
