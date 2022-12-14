---
title: Скопируйте VBA Macro UserForm DesignerStorage из шаблона в целевую книгу
type: docs
weight: 130
url: /ru/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет копировать проект VBA из одного файла Excel в другой файл Excel. Проект VBA состоит из различных типов модулей, т. е. Document, Procedural, Designer и т. д. Все модули можно скопировать с помощью простого кода, но для модуля Designer есть некоторые дополнительные данные, называемые хранилищем Designer, к которым необходимо получить доступ или скопировать. Следующие два метода относятся к Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Скопируйте VBA Macro UserForm DesignerStorage из шаблона в целевую книгу**

См. следующий пример кода. Он копирует проект VBA из[шаблон файла Excel](50528345.xlsm) в пустую книгу и сохраняет ее как[выходной файл Excel](50528346.xlsm). Если вы откроете проект VBA внутри файла шаблона Excel, вы увидите форму пользователя, как показано ниже. Пользовательская форма состоит из Designer Storage, поэтому она будет скопирована с помощью[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)а также[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)методы.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

На следующем снимке экрана показан выходной файл Excel и его содержимое, скопированное из файла шаблона Excel. Когда вы нажимаете кнопку 1, она открывает форму пользователя VBA, которая сама имеет командную кнопку, которая показывает окно сообщения при нажатии.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
