---
title: Добавить сводное соединение
type: docs
weight: 30
url: /ru/java/add-pivot-connection/
description: Узнайте, как добавить сводное соединение с библиотекой Aspose.Cells Java.
keywords: Add pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **Возможные сценарии использования**

 Если вы хотите связать слайсер и сводную таблицу в Excel, вам нужно щелкнуть слайсер правой кнопкой мыши и выбрать пункт «Отчет о подключениях ...». В списке опций вы можете работать с флажком. Точно так же, если вы хотите программно связать срез и сводную таблицу с помощью Aspose.Cells Java API, используйте[**Slicer.addPivotConnection (сводная таблица)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/) метод. Он свяжет слайсер и сводную таблицу.

## **Свяжите слайсер и сводную таблицу**

Следующий пример кода загружает[образец файла Excel](add-pivot-connection.xlsx)который содержит существующий слайсер. Он обращается к слайсеру, а затем связывает слайсер и сводную таблицу. Наконец, он сохраняет книгу как[выходной файл Excel](add-pivot-connection-out.xlsx). 


## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}