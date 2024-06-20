---
title: Введите данные ячейки рабочего листа GridWeb в формате процентов
type: docs
weight: 80
url: /ru/net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: В этой статье представлено введение данных ячейки в формате процентов в GridWeb .
---


## **Возможные сценарии использования**
GridWeb теперь поддерживает ввод данных ячейки в формате процентов, например, 3%, и данные в ячейке автоматически форматируются как 3,00%. Однако вы должны установить стиль ячейки в формат процента, который соответствует GridTableItemStyle.NumberType 9 или 10. Число 9 отформатирует 3% как 3%, а число 10 отформатирует 3% как 3,00%.

{{% alert color="primary" %}} 

Если вы не установили стиль ячейки в формат процента, то введенные данные 3% будут отображаться как 0,03.

{{% /alert %}} 
## **Введите данные ячейки рабочего листа GridWeb в формате процентов**
В следующем образце кода устанавливается стиль ячейки A1 GridTableItemStyle.NumberType как 10, поэтому введенные данные 3% автоматически форматируются как 3,00%, как показано на скриншоте.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Образец кода**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
