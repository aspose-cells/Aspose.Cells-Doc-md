---
title: Управление VBA кодами Excel файлов, поддерживающих макросы с помощью C++
linktitle: Проект макросов
type: docs
weight: 200
url: /ru/cpp/manage-vba-project/
description: Добавление модуля VBA и изменение VBA или макроса с помощью библиотеки Aspose.Cells в C++.
---

## **Добавить модуль VBA в C++**
{{% alert color="primary" %}}

Aspose.Cells позволяет добавлять новые модули VBA и код макроса с помощью Aspose.Cells. Пожалуйста, используйте метод [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) для добавления нового модуля VBA внутри рабочей книги.

{{% /alert %}}

Следующий пример создает новую рабочую книгу, добавляет модуль VBA и код макроса и сохраняет результат в формате XLSM. После открытия файла XLSM в Microsoft Excel и выбора команд меню **Разработчик > Visual Basic**, вы увидите модуль с именем "TestModule" и внутри него — следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Вот образец кода для создания файла XLSM с модулем VBA и кодом макроса.

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

## **Изменение VBA или макроса с помощью C++**

{{% alert color="primary" %}} 

Вы можете изменить код VBA или макроса с помощью Aspose.Cells. Aspose.Cells добавил следующие пространства имен и классы для чтения и изменения проекта VBA в файле Excel.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса в исходном файле Excel с помощью Aspose.Cells.

{{% /alert %}} 

Следующий пример загружает исходный Excel-файл, содержащий следующий VBA или макрос-код:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

После выполнения образца кода Aspose.Cells, VBA или макрос-код будет изменен следующим образом:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Вы можете загрузить [исходный файл Excel](5112508.xlsm) и [файл Excel для вывода](5112511.xlsm) по указанным ссылкам.

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

## **Дополнительные темы**
- [Добавить ссылку на библиотеку в проект VBA в рабочей книге](/cells/ru/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Назначить макрос элементу управления формы](/cells/ru/cpp/assign-macro-to-form-control/)
- [Проверить, действителен ли цифровая подпись кода VBA](/cells/ru/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Проверить, подписан ли код VBA](/cells/ru/cpp/check-if-vba-code-is-signed/)
- [Проверка, подписан ли VBA-проект в рабочей книге](/cells/ru/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Проверить, защищен ли и заблокирован для просмотра проект VBA](/cells/ru/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу](/cells/ru/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Цифрово подписать проект кода VBA c сертификатом](/cells/ru/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Экспортировать сертификат VBA в файл или поток](/cells/ru/cpp/export-vba-certificate-to-file-or-stream/)
- [Фильтрация VBA-проекта при загрузке рабочей книги](/cells/ru/cpp/filter-vba-project-while-loading-a-workbook/)
- [Узнать, защищен ли проект VBA](/cells/ru/cpp/find-out-if-vba-project-is-protected/)
- [Защитить паролем проект VBA книги Excel](/cells/ru/cpp/password-protect-the-vba-project-of-excel-workbook/)
