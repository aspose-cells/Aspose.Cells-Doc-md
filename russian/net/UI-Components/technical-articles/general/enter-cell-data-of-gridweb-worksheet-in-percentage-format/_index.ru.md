---
title: Введите Cell Данные рабочего листа GridWeb в процентном формате.
type: docs
weight: 80
url: /ru/net/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **Возможные сценарии использования**
Теперь GridWeb поддерживает ввод данных ячейки в процентном формате, например 3%, и данные в ячейке будут автоматически отформатированы как 3,00%. Однако вам нужно будет установить стиль ячейки в Процентный формат, который имеет GridTableItemStyle.NumberType 9 или 10. Число 9 будет форматировать 3% как 3%, а число 10 будет форматировать 3% как 3,00%.

{{% alert color="primary" %}} 

Если вы не установили для стиля ячейки Процентный формат, то входные данные 3% будут отображаться как 0,03.

{{% /alert %}} 
## **Введите Cell Данные рабочего листа GridWeb в процентном формате.**
В следующем примере кода для ячейки A1 GridTableItemStyle.NumberType задается значение 10, поэтому входные данные 3% автоматически форматируются как 3,00%, как показано на снимке экрана.

![дело:изображение_альтернативный_текст](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Образец кода**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
