---
title: Encrypt and Decrypt Excel files with C++
linktitle: Encrypt and Decrypt Excel files
type: docs
weight: 10
url: /cpp/encrypt-and-decrypt-excel-files/
description: How to encrypt and decrypt Excel files using C++. Lock and unlock Excel files.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel (97–365) enables you to encrypt and password‑protect your spreadsheets. It uses algorithms provided by a cryptographic service provider (CSP), a set of cryptographic algorithms with different properties. The default CSP is “Office 97/2000 Compatible” or “Weak Encryption (XOR)”. It’s important to choose the proper encryption key length. Some CSPs don’t support more than 40 or 56 bits. That is considered weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the “Microsoft Strong Cryptographic Provider”. To give you an idea, 128‑bit encryption is what banks use to secure connections with their online banking systems.

Aspose.Cells allows you to encrypt and password‑protect Microsoft Excel files with your desired encryption type.

{{% /alert %}}

## **Using Microsoft Excel**

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**. A dialog will appear.  
2. Select the **Security** tab.  
3. Enter a password and click **Advanced**.  
4. Choose the encryption type and confirm the password.

## **Encrypting Excel file with Aspose.Cells**

The following example shows how to encrypt and password‑protect an Excel file using the Aspose.Cells API.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify XOR encryption type
    workbook.SetEncryptionOptions(EncryptionType::XOR, 40);

    // Specify strong encryption type (RC4, Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password‑protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Workbook encrypted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Specifying the “Password to modify” Option**

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"SpecifyPasswordToModifyOption.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Set the password for modification
    workbook.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Password for modification set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Decrypting Excel file with Aspose.Cells**

It is very easy to open a password‑protected Excel file and decrypt it using the Aspose.Cells API, as shown in the following code:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create load options and set password
    LoadOptions loadOptions;
    loadOptions.SetPassword(u"password");

    // Open encrypted Excel file
    Workbook workbook(u"Book1.xlsx", loadOptions);

    // Remove password protection
    workbook.GetSettings().SetPassword(nullptr);

    // Save the modified workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Password removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advanced topics**

- [Encrypt and Decrypt ODS files](/cells/cpp/encrypt-and-decrypt-ods-files/)
- [Setting Strong Encryption Type](/cells/cpp/setting-strong-encryption-type/)
- [Specify Author while Write‑Protecting Workbook](/cells/cpp/specify-author-while-write-protecting-workbook/)
- [Verify Password of Encrypted Files](/cells/cpp/verify-password-of-encrypted-excel-and-ods-files/)
{{< app/cells/assistant language="cpp" >}}
