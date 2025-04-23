---
title: Güçlü Şifreleme Türü Ayarlama C++ ile
linktitle: Güçlü Şifreleme Türü Ayarlama
type: docs
weight: 60
url: /tr/cpp/setting-strong-encryption-type/
description: Aspose.Cells ile Excel dosyalarına güçlü şifreleme ve parola koruması nasıl uygulanır öğrenin.
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) elektronik tabloları şifrelemeye ve parola koruması sağlamaya olanak tanır. Bunun için bir Kripto Servis Sağlayıcı tarafından sağlanan algoritmayı kullanır. Kripto Servis Sağlayıcısı (veya CSP), farklı özelliklere sahip bir dizi kriptografik algoritmadır. Varsayılan CSP 'Office 97/2000 Uyumlu'dur. Bu, bazı kamuya bilinen güvenlik sorunları olan bir CSP'dir. 'Zayıf şifreleme (XOR)' veya 'Office 97/2000 Uyumlu' şifreleme türleriyle korunan elektronik tablolar kolayca kırılabilir.

Bu sorunu aşmak için Microsoft Excel tarafından sağlanan güçlü şifreleme türlerinden birini kullanın. Şifreleme türünü en güçlü CSP'ye değiştirebilirsiniz. Güçlü şifreleme için en az 128 bitlik bir anahtar uzunluğu gereklidir, örneğin, 'Microsoft Güçlü Kriptografik Sağlayıcı'.

Aspose.Cells API'sı kullanarak güçlü şifreleme türü ile Excel dosyalarını da şifreleyebilir ve parola koruyabilirsiniz.

{{% /alert %}}

## **Microsoft Excel'de Şifreleme Uygulama**
Microsoft Excel'de dosya şifrelemeyi uygulamak için (örneğin 2007):

1. **Araçlar** menüsünden **Seçenekler**'i seçin.
1. **Güvenlik** sekmesini seçin.
1. **Açmak için Parola** alanı için bir değer girin.
1. **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells ile Şifreleme Uygulama**
Aşağıdaki kod örnekleri bir dosyaya güçlü şifreleme uygular ve bir şifre ayarlar.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "File encrypted and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
