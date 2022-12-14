---
title: Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы.
type: docs
weight: 880
url: /ru/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells обеспечивает[PivotTable.IsExcel2003Совместимый](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)свойство, которое можно использовать, чтобы указать, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы. Если**истинный** , длина строки должна быть меньше или равна 255 символам, поэтому, если длина строки превышает 255 символов, она будет усечена. Если**ЛОЖЬ** , строка не будет иметь вышеупомянутого ограничения. Значение по умолчанию**истинный**.

{{% /alert %}} 
## **Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы.**
 В следующем примере кода объясняется использование[PivotTable.IsExcel2003Совместимый](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) имущество. Исходная строка имеет длину 383 символа. Но когда[PivotTable.IsExcel2003Совместимый](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) свойство установлено на**истинный** и сводная таблица обновляется, данные ячейки B5 сводной таблицы усекаются и становятся 255 символов. Однако, когда[PivotTable.IsExcel2003Совместимый](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) свойство установлено**ЛОЖЬ** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, загрузите[образец эксель файла](5472558.xlsx) используется в этом коде,[выходной файл excel](5472557.xlsx) сгенерированный им и его консольный вывод для справки. Также прочтите комментарии внутри кода, чтобы лучше понять это свойство.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Консольный вывод**
Вот вывод консоли приведенного выше примера кода, когда он выполняется с заданным[образец эксель файла](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
