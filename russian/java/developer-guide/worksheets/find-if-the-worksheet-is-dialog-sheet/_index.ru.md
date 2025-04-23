---
title: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 100
url: /ru/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Возможные сценарии использования**

Диалоговый лист - это старый формат листа, который содержит диалоговое окно. Такой лист может быть вставлен в старой версии Microsoft Excel, например 2003, как показано на этом снимке экрана. Он также может быть вставлен с помощью VBA в новых версиях, например в Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым листом или каким-либо другим типом листа, с помощью свойства [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type), предоставляемого Aspose.Cells. Если возвращается значение перечисления [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), то это означает, что вы работаете с диалоговым листом.

## **Определить, является ли рабочий лист диалоговым листом**

Следующий образец кода загружает [образец Excel-файла](64716841.xlsx), который содержит диалоговый лист. Он проверяет свойство [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type), сравнивает его с [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) и затем выводит сообщение. Пожалуйста, ознакомьтесь с выводом консоли приведенного ниже образца кода для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
