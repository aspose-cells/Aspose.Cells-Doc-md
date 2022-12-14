---
title: Найдите, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/net/find-if-the-worksheet-is-dialog-sheet/
---
## **Возможные сценарии использования**

Диалоговый лист — это старый формат листа, который содержит диалоговое окно. Такой лист может быть вставлен более старой версией Microsoft Excel, например 2003 года, как показано на этом снимке экрана. Его также можно вставить с помощью VBA в более новых версиях, например Microsoft Excel 2016.

![дело:изображение_альтернативный_текст](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым листом или другим типом листа с[**Рабочий лист.Тип**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)свойство, предоставленное Aspose.Cells. Если оно возвращает значение перечисления[**Тип Листа.Диалог**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), значит, вы имеете дело с диалоговым листом.

## **Найдите, является ли рабочий лист диалоговым листом**

 Следующий пример кода загружает[образец файла Excel](64716820.xlsx) который содержит диалоговый лист. Он проверяет[**Рабочий лист.Тип**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)свойство сравнивает его с[**Тип Листа.Диалог**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) а затем печатает сообщение. Дополнительные сведения см. в выводе на консоль примера кода, приведенного ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
