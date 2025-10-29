---
title: Управление кодами VBA для книги Excel с поддержкой макросов.
linktitle: Проект макросов
type: docs
weight: 200
url: /ru/python-net/manage-vba-project/
description: Добавить модуль VBA и изменить VBA или макрос с помощью библиотеки Aspose.Cells для Python via .NET.
---

## **Добавить модуль VBA в Python**
{{% alert color="primary" %}}

Aspose.Cells позволяет добавлять новый модуль VBA и макрос коды с помощью Aspose.Cells для Python via .NET. Пожалуйста, используйте метод [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/) для добавления нового модуля VBA внутри рабочей книги

{{% /alert %}}

В следующем образце кода создается новая книга и добавляется новый модуль VBA и код макроса, и сохраняется в формате XLSM. Когда вы откроете файл XLSM в Microsoft Excel и нажмете команды **Разработчик > Визуальный Basic**, вы увидите модуль под названием "TestModule" и внутри него будет следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Вот образец кода для создания файла XLSM с модулем VBA и кодом макроса.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **Редактирование VBA или Макроса в Python**

{{% alert color="primary" %}} 

Вы можете редактировать VBA или макрос коды, используя Aspose.Cells для Python via .NET. Aspose.Cells для Python via .NET добавил следующий пространственный пакет и классы для чтения и редактирования проекта VBA в файле Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Эта статья покажет вам, как изменить VBA или макрос внутри исходного файла Excel, используя Aspose.Cells для Python via .NET.

{{% /alert %}} 

Приведенный ниже образец кода загружает исходный файл Excel с встроенным VBA-кодом или макросом.

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

После выполнения примера кода Aspose.Cells для Python via .NET, VBA или макрос код будет изменен следующим образом

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Вы можете загрузить [исходный файл Excel](5112508.xlsm) и [файл Excel для вывода](5112511.xlsm) по указанным ссылкам.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **Продвинутые темы**
- [Добавить ссылку на библиотеку в проект VBA в книге](/cells/ru/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [Проверить, действителен ли цифровая подпись кода VBA](/cells/ru/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [Проверить, подписан ли код VBA](/cells/ru/python-net/check-if-vba-code-is-signed/)
- [Проверить, подписан ли проект VBA в книге Excel](/cells/ru/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [Проверить, защищен ли и заблокирован для просмотра проект VBA](/cells/ru/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Цифрово подписать проект кода VBA c сертификатом](/cells/ru/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [Экспортировать сертификат VBA в файл или поток](/cells/ru/python-net/export-vba-certificate-to-file-or-stream/)
- [Фильтрация проекта VBA при загрузке книги](/cells/ru/python-net/filter-vba-project-while-loading-a-workbook/)
- [Узнать, защищен ли проект VBA](/cells/ru/python-net/find-out-if-vba-project-is-protected/)
- [Защитить паролем проект VBA книги Excel](/cells/ru/python-net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="python-net" >}}
