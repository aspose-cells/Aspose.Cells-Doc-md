---
title: Укажите, совместим ли сводная таблица с Excel2003 при обновлении сводной таблицы
type: docs
weight: 880
url: /ru/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет свойство [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible), которое позволяет указать, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы. Если **true**, строка должна быть не более 255 символов, поэтому, если строка превышает 255 символов, она будет усечена. Если **false**, строка не будет иметь указанного ограничения. Значение по умолчанию - **true**.

{{% /alert %}} 
## **Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы**
В следующем образце кода объясняется использование свойства [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible). Исходная строка длиной 383 символа. Но когда свойство [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) установлено в **true**, и сводная таблица обновляется, данные ячейки B5 сводной таблицы усекаются и становятся длиной 255 символов. Однако, когда свойство [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) установлено в **false** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, скачайте [образец файла Excel](5472558.xlsx), использованный в этом коде, [выходной файл Excel](5472557.xlsx), сгенерированный им, и вывод консоли для вашего справочного материала. Пожалуйста, также прочитайте комментарии внутри кода для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Вывод в консоль**
Вот вывод консоли вышеприведенного образца кода при его выполнении с данным [образцом файла Excel](5472558.xlsx).



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
