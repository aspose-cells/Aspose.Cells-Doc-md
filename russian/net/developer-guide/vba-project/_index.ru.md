---
title: Управление кодами VBA для книги Excel с поддержкой макросов.
linktitle: Проект макросов
type: docs
weight: 200
url: /ru/net/manage-vba-project/
description: Добавление модуля VBA и изменение VBA или макроса с помощью библиотеки Aspose.Cells.
---

## **Добавление модуля VBA на C#**
{{% alert color="primary" %}}

Aspose.Cells позволяет добавить новый модуль VBA и код макроса, используя Aspose.Cells. Пожалуйста, используйте метод [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index), чтобы добавить новый модуль VBA внутри книги.

{{% /alert %}}

В следующем образце кода создается новая книга и добавляется новый модуль VBA и код макроса, и сохраняется в формате XLSM. Когда вы откроете файл XLSM в Microsoft Excel и нажмете команды **Разработчик > Визуальный Basic**, вы увидите модуль под названием "TestModule" и внутри него будет следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Вот образец кода для создания файла XLSM с модулем VBA и кодом макроса.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Изменение VBA или макроса на C#**

{{% alert color="primary" %}} 

Вы можете изменить код VBA или макроса с помощью Aspose.Cells. Aspose.Cells добавил следующие пространства имен и классы для чтения и изменения проекта VBA в файле Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса в исходном файле Excel с помощью Aspose.Cells.

{{% /alert %}} 

Приведенный ниже образец кода загружает исходный файл Excel с встроенным VBA-кодом или макросом.

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

После выполнения приведенного выше образца кода Aspose.Cells код VBA или макрос будет изменен таким образом.

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Вы можете загрузить [исходный файл Excel](5112508.xlsm) и [файл Excel для вывода](5112511.xlsm) по указанным ссылкам.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Продвинутые темы**
- [Добавить ссылку на библиотеку в проект VBA в книге](/cells/ru/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Назначить макрос элементу управления формы](/cells/ru/net/assign-macro-to-form-control/)
- [Проверить, действителен ли цифровая подпись кода VBA](/cells/ru/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Проверить, подписан ли код VBA](/cells/ru/net/check-if-vba-code-is-signed/)
- [Проверить, подписан ли проект VBA в книге Excel](/cells/ru/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Проверить, защищен ли и заблокирован для просмотра проект VBA](/cells/ru/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу](/cells/ru/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Цифрово подписать проект кода VBA c сертификатом](/cells/ru/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Экспортировать сертификат VBA в файл или поток](/cells/ru/net/export-vba-certificate-to-file-or-stream/)
- [Фильтрация проекта VBA при загрузке книги](/cells/ru/net/filter-vba-project-while-loading-a-workbook/)
- [Узнать, защищен ли проект VBA](/cells/ru/net/find-out-if-vba-project-is-protected/)
- [Защитить паролем проект VBA книги Excel](/cells/ru/net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="csharp" >}}
