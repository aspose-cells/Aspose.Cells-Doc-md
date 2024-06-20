---
title: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 70
url: /ru/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Возможные сценарии использования**
Диалоговый лист - это старый формат листа, который содержит диалоговое окно. Такой лист может быть вставлен в старой версии Microsoft Excel, например 2003, как показано на этом снимке экрана. Он также может быть вставлен с помощью VBA в новых версиях, например в Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **Определить, является ли рабочий лист диалоговым листом**
Aspose.Cells для Python via Java предоставляет возможность проверить, является ли лист диалоговым листом. Для этого предоставляется свойство [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type). Если [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) возвращает значение перечисления [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), то это означает, что вы имеете дело с диалоговым листом.

В следующем фрагменте кода показано, как проверить диалоговый лист. Ниже приведен вывод консоли, сгенерированный кодом для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Вывод в консоль**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
