---
title: Удалить связь сводной таблицы
type: docs
weight: 30
url: /ru/java/remove-pivot-connection/
description: Узнайте, как удалить связь сводной таблицы с помощью библиотеки Aspose.Cells для Java.
keywords: Удалите связь сводной таблицы без офиса 2013, офис 2016, офис 2019 и офиса 365.
---

## **Возможные сценарии использования**

Если вы хотите отсоединить срезку и сводную таблицу в Excel, вам нужно щелкнуть правой кнопкой мыши по срезке и выбрать пункт "Связи отчетов...". В списке опций вы можете оперировать флажком. Точно так же, если вы хотите отсоединить срезку и сводную таблицу программно с помощью API Aspose.Cells, пожалуйста, используйте метод [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable)). Он отсоединит срезку и сводную таблицу.

## **Удаление срезки**

Следующий образец кода загружает [образец файла Excel](remove-pivot-connection.xlsx), содержащий существующую срезку. Он получает доступ к срезке, а затем отсоединяет срезку и сводную таблицу. Наконец, он сохраняет книгу как [выходной файл Excel](remove-pivot-connection-out.xlsx). 


## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
