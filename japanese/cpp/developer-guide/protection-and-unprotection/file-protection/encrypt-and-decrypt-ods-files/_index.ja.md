---  
title: C++を使用してODSファイルを暗号化および復号化する方法  
linktitle: ODSファイルの暗号化と複合化  
type: docs  
weight: 10  
url: /ja/cpp/encrypt-and-decrypt-ods-files/  
description: Aspose.Cells for C++を使用してODSファイルをパスワード保護し暗号化します。このライブラリは純粋なC++です。  
---  

{{% alert color="primary" %}}  
OpenOffice.orgは、ファイルのパスワード保護と暗号化に対応した高機能なオフィススイートです。ただし、暗号化されたODSファイルは、パスワードを入力後にOpenOfficeのみで開くことができます。Excelでは暗号化されたODSファイルを開くことはできず、警告メッセージが表示されることがあります。暗号化オプションは、他のファイルタイプとは異なり、ODSファイルには適用されません。  
Aspose.Cellsを使用すれば、ODSファイルの暗号化と復号化が可能です。復号化されたODSファイルは、ExcelとOpenOfficeの両方で開くことができます。  
{{% /alert %}}  

## **OpenOffice Calcで暗号化**  
1. **名前を付けて保存**を選択し、**パスワードを設定して保存**ボックスをクリックします。  
1. **保存**ボタンをクリックします。  
1. 開いた「パスワードの設定」ウィンドウの「開くためのパスワードを入力」および「パスワードを確認」フィールドに希望するパスワードを入力します。  
1. ファイルを保存するために **OK** ボタンをクリックします。  

## **Aspose.Cells for C++を使ってODSファイルを暗号化**  
ODSファイルを暗号化するには、ファイルを読み込んで保存する前に[**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)の値を実際のパスワードに設定します。出力される暗号化されたODSファイルは、OpenOfficeでのみ開くことができます。  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an ODS file
    Workbook workbook(sourceDir + u"sampleODSFile.ods");

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the ODS file
    workbook.Save(outputDir + u"outputEncryptedODSFile.ods");

    std::cout << "ODS file password protected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## **Aspose.Cells for C++を使ってODSファイルの暗号を解除**  

ODSファイルの復号化には、[**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/)プロパティにパスワードを入力してファイルを読み込みます。ファイルの読み込みが完了したら、[**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)の文字列をnullに設定します。  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an encrypted ODS file
    LoadOptions loadOptions(LoadFormat::Ods);

    // Set original password
    loadOptions.SetPassword(u"1234");

    // Load the encrypted ODS file with the appropriate load options
    Workbook workbook(sourceDir + u"sampleEncryptedODSFile.ods", loadOptions);

    // Set the password to null
    workbook.GetSettings().SetPassword(nullptr);

    // Save the decrypted ODS file
    workbook.Save(outputDir + u"outputDecryptedODSFile.ods");

    std::cout << "Decrypted ODS file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
