---
title: Добавить опорное соединение
type: docs
weight: 30
url: /ru/python-net/add-pivot-connection/
description: Узнайте, как добавить поворотное соединение с помощью библиотеки Aspose.Cells for Python via .NET.
keywords: Add pivot connection without office 2013, office 2016, office 2019 and office 365.
---
##  **Возможные сценарии использования**

Если вы хотите связать срез и сводную таблицу в Excel, вам нужно щелкнуть срез правой кнопкой мыши и выбрать пункт «Соединения отчетов...». В списке опций вы можете работать с флажком. Аналогично, если вы хотите связать срез и сводную таблицу с помощью Aspose.Cells for Python via .NET API программно, используйте[**Slicer.add_pivot_connection(поворот)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/add_pivot_connection/#aspose.cells.pivot.PivotTable)метод. Он свяжет срез и сводную таблицу.

##  **Ассоциированный срез и сводная таблица**

Следующий пример кода загружает[образец файла Excel](add-pivot-connection.xlsx)который содержит существующий срез. Он обращается к срезу, а затем связывает срез и сводную таблицу. Наконец, он сохраняет книгу как[выходной файл Excel](add-pivot-connection-out.xlsx). 


##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-Adding-Pivot-Connection.py" >}}