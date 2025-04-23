---
title: Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу
type: docs
weight: 130
url: /ru/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет скопировать проект VBA из одного файла Excel в другой файл Excel. Проект VBA состоит из различных типов модулей, таких как Документ, Процедурный, Дизайнерский и т. д. Все модули могут быть скопированы с помощью простого кода, но для дизайнерского модуля требуется дополнительные данные, называемые хранилищем дизайнера, которые необходимо получить или скопировать. Следующие два метода работают с хранилищем дизайнера.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу**

Пожалуйста, ознакомьтесь со следующим образцовым кодом. Он копирует проект VBA из [шаблонного файла Excel](50528345.xlsm) в пустую книгу и сохраняет его как [выходной файл Excel](50528346.xlsm). Если вы откроете проект VBA внутри шаблонного файла Excel, вы увидите пользовательскую форму, как показано ниже. Пользовательская форма состоит из хранилища дизайнера, поэтому оно будет скопировано с использованием методов [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) и [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

На следующем снимке экрана показан выходной файл Excel и его содержимое, скопированные из шаблонного файла Excel. При нажатии на кнопку 1 открывается пользовательская форма VBA, которая сама содержит кнопку команды, показывающую сообщение при нажатии.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
