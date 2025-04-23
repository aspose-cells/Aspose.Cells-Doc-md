---
title: Удалить связь сводной таблицы
type: docs
weight: 30
url: /ru/net/remove-pivot-connection/
description: Узнайте, как удалить связь с сводной таблицей с библиотекой Aspose.Cells.
keywords: Удалите связь сводной таблицы без офиса 2013, офис 2016, офис 2019 и офиса 365.
---

## **Возможные сценарии использования**

Если вы хотите отсоединить срезку и сводную таблицу в Excel, вам нужно щелкнуть правой кнопкой мыши по срезке и выбрать пункт "Связи отчетов...". В списке опций вы можете оперировать флажком. Точно так же, если вы хотите отсоединить срезку и сводную таблицу программно с помощью API Aspose.Cells, пожалуйста, используйте метод [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/removepivotconnection/). Он отсоединит срезку и сводную таблицу.

## **Отсоединить срезку и сводную таблицу**

Следующий образец кода загружает [образец файла Excel](remove-pivot-connection.xlsx), содержащий существующую срезку. Он получает доступ к срезке, а затем отсоединяет срезку и сводную таблицу. Наконец, он сохраняет книгу как [выходной файл Excel](remove-pivot-connection-out.xlsx). 


## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Removing-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
