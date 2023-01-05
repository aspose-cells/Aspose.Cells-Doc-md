---
title: Управление кодами VBA книги Excel с поддержкой макросов.
linktitle: Макропроект
type: docs
weight: 200
url: /ru/net/manage-vba-project/
description: Добавьте модуль VBA и измените VBA или макрос с помощью библиотеки Aspose.Cells.
---
## **Добавьте модуль VBA в C#**
{{% alert color="primary" %}}

 Aspose.Cells позволяет добавить новый модуль VBA и код макроса с помощью Aspose.Cells. Пожалуйста, используйте[**Книга.VbaProject.Модули.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) метод добавления нового модуля VBA в книгу

{{% /alert %}}

В следующем примере кода создается новая книга, добавляется новый модуль VBA и код макроса, а выходные данные сохраняются в формате XLSM. Один раз вы откроете выходной файл XLSM в Microsoft Excel и щелкните значок**Разработчик > Visual Basic** команд меню, вы увидите модуль с именем «TestModule», а внутри него вы увидите следующий код макроса.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Вот пример кода для создания выходного файла XLSM с модулем VBA и кодом макроса.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Изменить VBA или макрос в C#**

{{% alert color="primary" %}} 

Вы можете изменить код VBA или макроса, используя Aspose.Cells. Aspose.Cells добавил следующее пространство имен и классы для чтения и изменения проекта VBA в файле Excel.

- Aspose.Cells.Vba
- VbaProject
- ВбаМодулеКоллекция
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса внутри исходного файла Excel, используя Aspose.Cells.

{{% /alert %}} 

Следующий пример кода загружает исходный файл Excel, внутри которого находится следующий код VBA или макроса.

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

После выполнения образца кода Aspose.Cells код VBA или макроса будет изменен следующим образом.

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Вы можете скачать[исходный файл Excel](5112508.xlsm) и[выходной файл Excel](5112511.xlsm) по указанным ссылкам.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Предварительные темы**
- [Добавить ссылку на библиотеку в проект VBA в книге](/cells/ru/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Назначить макрос элементу управления формой](/cells/ru/net/assign-macro-to-form-control/)
- [Проверьте, действительна ли цифровая подпись кода VBA](/cells/ru/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Проверьте, подписан ли код VBA](/cells/ru/net/check-if-vba-code-is-signed/)
- [Проверьте, подписан ли проект VBA в рабочей книге](/cells/ru/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Проверьте, защищен ли проект VBA и заблокирован для просмотра](/cells/ru/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Скопируйте VBA Macro UserForm DesignerStorage из шаблона в целевую книгу](/cells/ru/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Цифровая подпись проекта кода VBA с помощью сертификата](/cells/ru/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Экспорт сертификата VBA в файл или поток](/cells/ru/net/export-vba-certificate-to-file-or-stream/)
- [Фильтровать проект VBA при загрузке книги](/cells/ru/net/filter-vba-project-while-loading-a-workbook/)
- [Узнайте, защищен ли проект VBA](/cells/ru/net/find-out-if-vba-project-is-protected/)
- [Защита паролем проекта VBA книги Excel](/cells/ru/net/password-protect-the-vba-project-of-excel-workbook/)

