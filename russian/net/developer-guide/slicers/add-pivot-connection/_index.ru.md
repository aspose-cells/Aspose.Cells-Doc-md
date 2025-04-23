---
title: Добавить связь сводной таблицы
type: docs
weight: 30
url: /ru/net/add-pivot-connection/
description: Узнайте, как добавить связь измерения с библиотекой Aspose.Cells.
keywords: Добавить связь сводной таблицы без Office 2013, Office 2016, Office 2019 и Office 365.
---

## **Возможные сценарии использования**

Если вы хотите связать срез и сводную таблицу в Excel, вам нужно щелкнуть правой кнопкой мыши на срезе и выбрать пункт "Связи отчета...". В параметрах вы можете оперировать флажком. Точно так же, если вы хотите связать срез и сводную таблицу с использованием программного интерфейса Aspose.Cells API, пожалуйста, используйте метод [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/addpivotconnection/). Он свяжет срез и сводную таблицу.

## **Ассоциировать фильтр и сводную таблицу**

Следующий образец кода загружает [образец файла Excel](add-pivot-connection.xlsx), содержащий существующий фильтр. Он получает доступ к фильтру, а затем ассоциирует фильтр и сводную таблицу. Наконец, он сохраняет рабочую книгу как [выходной файл Excel](add-pivot-connection-out.xlsx). 


## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Adding-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
