---
title: Удалить шарнирное соединение
type: docs
weight: 30
url: /ru/python-net/remove-pivot-connection/
description: Узнайте, как удалить поворотное соединение с помощью библиотеки Aspose.Cells for Python via .NET.
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---
##  **Возможные сценарии использования**

 Если вы хотите разъединить срез и сводную таблицу в Excel, вам нужно щелкнуть срез правой кнопкой мыши и выбрать пункт «Соединения отчетов...». В списке опций вы можете работать с флажком. Аналогично, если вы хотите программно разъединить срез и сводную таблицу с помощью Aspose.Cells for Python via .NET API, используйте[**Slicer.remove_pivot_connection(поворот)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/remove_pivot_connection/#aspose.cells.pivot.PivotTable)метод. Это отключит срез и сводную таблицу.

##  **Отсоединить срез и сводную таблицу**

Следующий пример кода загружает[образец файла Excel](remove-pivot-connection.xlsx)который содержит существующий срез. Он обращается к срезам, а затем отсоединяет срез и сводную таблицу. Наконец, он сохраняет книгу как[выходной файл Excel](remove-pivot-connection-out.xlsx). 


##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-Removing-Pivot-Connection.py" >}}