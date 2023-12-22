---
title: Введите Cell Данные рабочего листа GridWeb в процентном формате.
type: docs
weight: 1010
url: /ru/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **Возможные сценарии использования**
GridWeb теперь позволяет пользователям вводить данные ячеек в процентном формате, например 3%, и данные в ячейке автоматически будут отформатированы как 3,00%. Однако вам придется установить стиль ячейки в процентном формате, который представляет собой либо GridTableItemStyle.NumberType, либо 9, либо 10. Число 9 будет форматировать 3% как 3%, а число 10 будет форматировать 3% как 3,00%.

{{% alert color="primary" %}} 

Если вы не установили стиль ячейки «Процентный формат», то входные данные 3% будут отображаться как 0,03.

{{% /alert %}} 
##  **Введите Cell Данные рабочего листа GridWeb в процентном формате.**
В следующем примере кода ячейке A1 GridTableItemStyle.NumberType присваивается значение 10, поэтому входные данные 3% автоматически форматируются как 3,00%, как показано на снимке экрана.

![задача: image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **Образец кода**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






