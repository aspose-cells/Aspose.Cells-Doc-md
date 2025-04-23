---
title: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Диалоговый лист — это устаревший формат листов. В этой статье предоставлены инструкции и пример кода, как программно определить, является ли лист в Excel Диалоговым листом с использованием библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python для Excel, диалог выбора листа в Excel в Python, диалог листа в python.
---

## **Возможные сценарии использования**

Диалоговый лист - это старый формат листа, который содержит диалоговое окно. Такой лист мог быть вставлен в старой версии Microsoft Excel, например, в 2003 году, как показано на этом скриншоте. Его также можно вставить с помощью VBA в новых версиях, например, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым или другим типом листа, с помощью свойства [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/), предоставляемого Aspose.Cells для Python via .NET. Если возвращается значение перечисления [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), то это означает, что вы имеете дело с диалоговым листом.

## **Определить, является ли рабочий лист диалоговым листом**

В следующем примере кода загружается [образец файла Excel](64716820.xlsx), который содержит диалоговый лист. Он проверяет свойство [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/), сравнивает его с [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), и затем выводит сообщение. Пожалуйста, обратитесь к выводу консоли приведенного ниже примера кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
