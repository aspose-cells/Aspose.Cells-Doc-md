---
title: C++でExcelマクロ対応ブックのVBAコードを管理する
linktitle: マクロプロジェクト
type: docs
weight: 200
url: /ja/cpp/manage-vba-project/
description: Aspose.Cellsライブラリを使用してVBAモジュールとマクロを追加・変更する。
---

## **C++でVBAモジュールを追加する**
{{% alert color="primary" %}}

Aspose.Cellsを使えば、新しいVBAモジュールとマクロコードを追加できます。新しいVBAモジュールをブック内に追加するには [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) メソッドを使用してください。

{{% /alert %}}

以下のサンプルコードは、新しいブックを作成し、新しいVBAモジュールとマクロコードを追加し、出力をXLSM形式で保存します。一度Microsoft Excelで出力されたXLSMファイルを開き、「開発」>「Visual Basic」メニューコマンドをクリックすると、「TestModule」という名前のモジュールが表示され、その中に以下のマクロコードが見えます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

VBAモジュールとマクロコードを含む出力XLSMファイルを生成するためのサンプルコードは次のとおりです。

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

## **C++でVBAまたはマクロを変更する**

{{% alert color="primary" %}} 

Aspose.Cellsを使用してVBAまたはマクロコードを変更できます。Aspose.Cellsは、Excelファイル内のVBAプロジェクトを読み取り、変更するための次の名前空間とクラスを追加しました。

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

この記事では、Aspose.Cellsを使用してソースExcelファイル内のVBAまたはマクロコードを変更する方法を説明します。

{{% /alert %}} 

以下のサンプルコードは、内側にVBAまたはマクロコードを含むソースExcelファイルを読み込みます：

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cellsのサンプルコードを実行すると、VBAまたはマクロコードが次のように変更されます：

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

提供されたリンクから [ソースExcelファイル](5112508.xlsm) と [出力Excelファイル](5112511.xlsm) をダウンロードできます。

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

## ** 高度なトピック**
- [ブック内のVBAプロジェクトにライブラリの参照を追加する](/cells/ja/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [フォームコントロールにマクロを割り当てる](/cells/ja/cpp/assign-macro-to-form-control/)
- [VBAコードのデジタル署名が有効かどうかをチェックする](/cells/ja/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [VBAコードが署名されているかを確認する](/cells/ja/cpp/check-if-vba-code-is-signed/)
- [ブックのVBAプロジェクトに署名がされているか確認する](/cells/ja/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [VBAプロジェクトが保護されており、閲覧用にロックされているかを確認する](/cells/ja/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー](/cells/ja/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [証明書でVBAコードプロジェクトにデジタル署名する](/cells/ja/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA証明書をファイルまたはストリームにエクスポートする](/cells/ja/cpp/export-vba-certificate-to-file-or-stream/)
- [ブックを読み込む際にVBAプロジェクトをフィルタリングする](/cells/ja/cpp/filter-vba-project-while-loading-a-workbook/)
- [VBAプロジェクトが保護されているかを調べる](/cells/ja/cpp/find-out-if-vba-project-is-protected/)
- [ExcelワークブックのVBAプロジェクトをパスワードで保護する](/cells/ja/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
