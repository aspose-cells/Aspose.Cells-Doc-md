---
title: C++ ile Excel Makro aktif Çalışma Kitabının VBA Kodlarını Yönetin
linktitle: Makro Projesi
type: docs
weight: 200
url: /tr/cpp/manage-vba-project/
description: VBA Modülü ekleyin ve Aspose.Cells kütüphanesi kullanarak VBA veya Makroyu düzenleyin.
---

## **C++ ile VBA Modülü ekleyin**
{{% alert color="primary" %}}

Aspose.Cells, yeni bir VBA Modülü ve Makro Kodu eklemenizi sağlar. Lütfen çalışma kitabına yeni VBA Modülü eklemek için [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) yöntemini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler, ve çıktıyı XLSM formatında kaydeder. Çıktı XLSM dosyasını Microsoft Excel'de açtıktan sonra **Geliştirici > Görsel Temel** menüsüne tıklarsanız, "TestModule" adında bir modül görürsünüz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aşağıdaki örnek kod, VBA Modülü ve Makro Kodu içeren kaynak Excel dosyasını yükler

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

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **C++ ile VBA veya Makroyu Düzenle**

{{% alert color="primary" %}} 

VBA veya Makro Kodunu, Aspose.Cells kullanarak değiştirebilirsiniz. Aspose.Cells, Excel dosyasındaki VBA projeyi okumak ve değiştirmek için aşağıdaki ad alanını ve sınıfları eklemiştir.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyasındaki VBA veya Makro Kodunu değiştirmeyi gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, içindeki VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells örnek kodunun çalıştırılmasından sonra, VBA veya Makro kodu şöyle değişecektir:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Verilen bağlantılardan [kaynak Excel dosyasını](5112508.xlsm) ve [çıktı Excel dosyasını](5112511.xlsm) indirebilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gelişmiş Konular**
- [Çalışma kitabında VBA Projesine Kütüphane Referansı Ekle](/cells/tr/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Makroyu Form Kontrole Ata](/cells/tr/cpp/assign-macro-to-form-control/)
- [VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et](/cells/tr/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA Kodunun İmzalı Olup Olmadığını Kontrol Et](/cells/tr/cpp/check-if-vba-code-is-signed/)
- [Bir çalışma kitabındaki VBA Projesinin İmzalanıp İmzalanmadığını Kontrol Edin](/cells/tr/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA Projesinin Korunup Görüntülemeye Kilitli Olup Olmadığını Kontrol Edin](/cells/tr/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama](/cells/tr/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Sertifika ile Bir VBA Kod Projesini Dijital Olarak İmzalama](/cells/tr/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA Sertifikasını Dosyaya veya Akışa Aktarma](/cells/tr/cpp/export-vba-certificate-to-file-or-stream/)
- [Bir çalışma kitabı yüklenirken VBA Projesini Filtrele](/cells/tr/cpp/filter-vba-project-while-loading-a-workbook/)
- [VBA Projesinin Korunup Korunmadığını Bulma](/cells/tr/cpp/find-out-if-vba-project-is-protected/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruma](/cells/tr/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
