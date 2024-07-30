---
title: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Лист диалога  это старый формат листа. Эта статья предоставляет инструкции и пример кода для программного определения, является ли лист Excel листом диалога с использованием библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, Python найдите тип диалога листа Excel, диалог лист на Python.
---

## **Возможные сценарии использования**

Диалоговый лист - это старый формат листа, который содержит диалоговое окно. Такой лист мог быть вставлен в старой версии Microsoft Excel, например, в 2003 году, как показано на этом скриншоте. Его также можно вставить с помощью VBA в новых версиях, например, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым листом или другим типом листа с помощью свойства [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/), предоставленного Aspose.Cells для Python via .NET. Если оно возвращает значение перечисления [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), это означает, что вы имеете дело с диалоговым листом.

## **Определить, является ли рабочий лист диалоговым листом**

В следующем примере кода загружается [образец файла Excel](64716820.xlsx), который содержит диалоговый лист. Он проверяет свойство [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/), сравнивает его с [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), и затем выводит сообщение. Пожалуйста, обратитесь к выводу консоли приведенного ниже примера кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
