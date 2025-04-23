---
title: Добавить связь сводной таблицы
type: docs
weight: 30
url: /ru/java/add-pivot-connection/
description: Узнайте, как добавить связь сводной таблицы с библиотекой Aspose.Cells для Java.
keywords: Добавить связь сводной таблицы без Office 2013, Office 2016, Office 2019 и Office 365.
---

## **Возможные сценарии использования**

Если вы хотите связать срез и сводную таблицу в Excel, вам нужно щелкнуть правой кнопкой мыши на срезе и выбрать пункт "Связи отчетов...". В списке опций вы можете работать с флажком. Аналогично, если вы хотите связать срез и сводную таблицу с помощью программного интерфейса Aspose.Cells Java, используйте метод [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection-com.aspose.cells.PivotTable-). Он свяжет срез и сводную таблицу.

## **Ассоциировать фильтр и сводную таблицу**

Следующий образец кода загружает [образец файла Excel](add-pivot-connection.xlsx), содержащий существующий фильтр. Он получает доступ к фильтру, а затем ассоциирует фильтр и сводную таблицу. Наконец, он сохраняет рабочую книгу как [выходной файл Excel](add-pivot-connection-out.xlsx). 


## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
