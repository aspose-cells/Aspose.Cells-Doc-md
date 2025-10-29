---
title: Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу
type: docs
weight: 130
url: /ru/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells для Python via .NET позволяет копировать VBA-проект из одного Excel-файла в другой. VBA-проект включает в себя различные типы модулей, такие как Документ, Процедурный, Конструктор и др. Все модули можно скопировать с помощью простого кода, но для модуля Конструктора требуется доступ к дополнительным данным, называемым Designer Storage, которые нужно получить или скопировать. Следующие два метода работают с Designer Storage.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу**

Пожалуйста, ознакомьтесь со следующим образцовым кодом. Он копирует проект VBA из [шаблонного файла Excel](50528345.xlsm) в пустую книгу и сохраняет его как [выходной файл Excel](50528346.xlsm). Если вы откроете проект VBA внутри шаблонного файла Excel, вы увидите пользовательскую форму, как показано ниже. Пользовательская форма состоит из хранилища дизайнера, поэтому оно будет скопировано с использованием методов [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) и [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

На следующем снимке экрана показан выходной файл Excel и его содержимое, скопированные из шаблонного файла Excel. При нажатии на кнопку 1 открывается пользовательская форма VBA, которая сама содержит кнопку команды, показывающую сообщение при нажатии.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
