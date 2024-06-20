---
title: Введите данные ячейки рабочего листа GridWeb в формате процентов
type: docs
weight: 1010
url: /ru/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **Возможные сценарии использования**
GridWeb теперь поддерживает ввод данных ячейки в формате процентов, например, 3%, и данные в ячейке автоматически форматируются как 3,00%. Однако вы должны установить стиль ячейки в формат процента, который соответствует GridTableItemStyle.NumberType 9 или 10. Число 9 отформатирует 3% как 3%, а число 10 отформатирует 3% как 3,00%.

{{% alert color="primary" %}} 

Если вы не установили стиль ячейки в формат процента, то введенные данные 3% будут отображаться как 0,03.

{{% /alert %}} 
## **Введите данные ячейки рабочего листа GridWeb в формате процентов**
В следующем образце кода устанавливается стиль ячейки A1 GridTableItemStyle.NumberType как 10, поэтому введенные данные 3% автоматически форматируются как 3,00%, как показано на скриншоте.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **Образец кода**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






