---
title: Найдите, является ли рабочий лист диалоговым листом
type: docs
weight: 100
url: /ru/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Возможные сценарии использования**

Диалоговый лист — это старый формат листа, который содержит диалоговое окно. Такой лист может быть вставлен более старой версией Microsoft Excel, например 2003 года, как показано на этом снимке экрана. Его также можно вставить с помощью VBA в более новых версиях, например Microsoft Excel 2016.

![дело:изображение_альтернативный_текст](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым листом или другим типом листа с[**Рабочий лист.Тип**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)свойство, предоставленное Aspose.Cells. Если оно возвращает значение перечисления[**Тип Листа.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), то это означает, что вы имеете дело с диалоговым листом.

## **Найдите, является ли рабочий лист диалоговым листом**

Следующий пример кода загружает[образец файла Excel](64716841.xlsx)который содержит диалоговый лист. Он проверяет[**Рабочий лист.Тип**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)свойство сравнивает его с[**Тип Листа.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)а затем печатает сообщение. Дополнительные сведения см. в выводе на консоль примера кода, приведенного ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
