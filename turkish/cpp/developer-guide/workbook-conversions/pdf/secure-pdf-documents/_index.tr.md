---
title: C++ ile Güvenli PDF Belgeleri
linktitle: Güvenli PDF Belgeleri
type: docs
weight: 120
url: /tr/cpp/secure-pdf-documents/
description: Owner ve kullanıcı şifreleri kullanarak PDF belgelerini güvenli hale getirmeyi öğrenin.
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler şifrelenmiş PDF dosyalarıyla çalışmak zorunda kalabilir. Örneğin:

- Belgeleri sahip ve kullanıcı şifreleri ile güvence altına almak, böylece herkes tarafından açılamamasını sağlamak.
- Doküman açıldıktan sonra kısıtlamalar veya izinler belirlemek. Örneğin: doküman içeriğinin yazdırılabilir veya çıkarılabilir olup olmadığını sınırlamak.

Bu makale, elektronik tabloları PDF'ye kaydederken PDF güvenlik seçeneklerini nasıl geçireceğinizi açıklar.

{{% /alert %}}

 Aspose.Cells, güvenlikle ilgili işler için [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) sağlar. PDF'ye kaydederken sahibi ve kullanıcı şifreleri ayarlayabilirsiniz. Şifreler, şifreli PDF dosyasını görüntülemek için gerekli olacaktır.

- Kullanıcı şifresi null veya boş dize olabilir, bu durumda kullanıcıdan PDF belgesini açarken herhangi bir parola gerekli olmayacaktır.
Doğru sahip şifresi ile PDF belgeyi açmak belgeye tam erişim sağlar (belirtilen herhangi bir erişim kısıtlaması olmadan).
- Doğru kullanıcı parolasıyla PDF belgesinin doğru şekilde açılması (veya herhangi bir kullanıcı parolası olmayan bir belgenin açılması) belirtilen izinlerle sınırlı erişim sağlar.

Aşağıdaki örnek kod, Aspose.Cells ile PDF'leri güvence altına alma işlemi hakkında bilgi verir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) çağrılması en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin gösterilmesini sağlar.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
