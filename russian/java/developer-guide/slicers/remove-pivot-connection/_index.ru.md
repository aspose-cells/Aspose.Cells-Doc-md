---
title: Удалить сводное соединение
type: docs
weight: 30
url: /ru/java/remove-pivot-connection/
description: Узнайте, как удалить сводное соединение с библиотекой Aspose.Cells Java.
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **Возможные сценарии использования**

Если вы хотите разъединить слайсер и сводную таблицу в Excel, вам нужно щелкнуть слайсер правой кнопкой мыши и выбрать пункт «Отчет о подключениях ...». В списке опций вы можете работать с флажком. Точно так же, если вы хотите программно разъединить слайсер и сводную таблицу с помощью Aspose.Cells API, используйте[**Slicer.removePivotConnection (сводная таблица)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable)) метод. Это отключит слайсер и сводную таблицу.

## **Удаление слайсера**

Следующий пример кода загружает[образец файла Excel](remove-pivot-connection.xlsx)который содержит существующий слайсер. Он обращается к слайсерам, а затем разъединяет слайсер и сводную таблицу. Наконец, он сохраняет книгу как[выходной файл Excel](remove-pivot-connection-out.xlsx). 


## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}