---
title: Hata Kontrol Seçeneklerini Kullanmak C++ ile
linktitle: Hata Kontrolü Seçeneklerini Kullanma
type: docs
weight: 140
url: /tr/cpp/use-error-checking-options/
description: Bu makalede, C++ API veya Kütüphanesini kullanarak, sayılar gibi Excel çalışma sayfalarında hata kontrolü seçeneklerini programlı olarak kullanmanın örnek kodlarını bulacaksınız.
keywords: excel de metin olarak mağaza numarasını C++ kullanarak saklama, excel seçeneklerinde hata kontrolü C++
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların hata kontrol seçeneklerini ve kurallarını tanımlamalarına izin verir. Kullanıcılar, formüller oluştururken sık ​​sık hata kontrolleri görür, bir hücrenin sağ üst köşesinde küçük bir üçgen, bir hücrede bir sorun olduğunda vurgulanır. Excel, kullanıcılara hücreyle ilgili yaygın problemleri düzeltmelerine yardımcı olacak bilgiler sağlar.

{{% /alert %}}

## **Hata türleri**

Formülün bir sonuç döndüremeyeceği anlamına gelen hatalar - örneğin bir sayıyı sıfıra bölmek gibi - derhal dikkat gerektirir ve hücrede bir hata değeri görüntülenir. Yeşil üçgeni tıklamak, bir ünlem işareti gösterir, buna tıklamak, bir liste seçeneği açar.

Hata, seçenekler kullanılarak çözülebilir veya yok sayılabilir. Bir hatayı yok saymak, o hatanın daha sonra yapılan hata kontrollerinde görünmeyeceği anlamına gelir.

Aspose.Cells, hata kontrolü seçeneği özellikleri sağlar. Örneğin, metin olarak saklanan sayılar, formül hesaplama hataları ve doğrulama hataları gibi farklı türde hata kontrollerini yöneten [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) sınıfı. İstenen hata kontrolünü ayarlamak için [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/) numarasını kullanın.

## **Metin Olarak Saklanan Sayılar**

Bazen, sayılar hücrelerde metin olarak biçimlendirilmiş ve saklanmış olabilir. Bu, hesaplamalarda sorunlara neden olabilir veya karışık sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilmiş sayılar, hücrede sağa hizalanmış olarak değil, sola hizalanmış olarak bırakılır. Bir hücrelerde matematiksel bir işlem yapması gereken bir formül değeri döndürmezse, formülün başvurduğu hücrelerdeki hizalama kontrol edilmelidir - bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.

Metin olarak saklanan sayıları hızlı bir şekilde gerçek sayılara dönüştürmek için hata kontrol seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:

1. **Araçlar** menüsünde **Seçenekler**'i tıklayın.
1. Hata Kontrolü sekmesini seçin.
   **Metin olarak saklanan sayı** seçeneği varsayılan olarak işaretlidir.
1. Bu seçeneği devre dışı bırakın.

Aşağıdaki örnek kod, Aspose.Cells API'lerini kullanarak bir çalışma sayfasındaki metin olarak saklanan sayılar hata kontrol seçeneğini devre dışı bırakmanın nasıl yapıldığını göstermektedir.

```cpp
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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
