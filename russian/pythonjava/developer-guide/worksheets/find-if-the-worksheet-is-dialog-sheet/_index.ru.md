---
title: Найдите, является ли рабочий лист диалоговым листом
type: docs
weight: 70
url: /ru/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **Возможные сценарии использования**
Диалоговый лист — это старый формат листа, который содержит диалоговое окно. Такой лист может быть вставлен более старой версией Microsoft Excel, например 2003 года, как показано на этом снимке экрана. Его также можно вставить с помощью VBA в более новых версиях, например Microsoft Excel 2016.

![дело:изображение_альтернативный_текст](DialogSheet.png)
## **Найдите, является ли рабочий лист диалоговым листом**
Aspose.Cells for Python via Java предоставляет вам возможность проверить, является ли рабочий лист диалоговым листом. Для этого он предоставляет[Рабочий лист.Тип](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)имущество. Если[Рабочий лист.Тип](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)возвращает значение перечисления[Тип Листа.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), то это означает, что вы имеете дело с диалоговым листом.

В следующем фрагменте кода показано, как проверить диалоговое окно. Вывод консоли, сгенерированный кодом, приведен ниже для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Консольный вывод**
Рабочий лист представляет собой диалоговый лист.
