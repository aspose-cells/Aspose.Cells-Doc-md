---
title: Применить расширенный фильтр Microsoft Excel для отображения записей, отвечающих сложным критериям
type: docs
weight: 190
url: /ru/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Возможные сценарии использования**
 Microsoft Excel позволяет применять*Расширенный фильтр* на данных рабочего листа для отображения записей, соответствующих сложным критериям. Вы можете применить расширенный фильтр с Microsoft Excel через его*Данные > Дополнительно*команду, как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells также позволяет применять расширенный фильтр с помощью[Рабочий лист.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) метод. Как и Microsoft Excel, он принимает следующие параметры.

**isFilter**

Указывает, используется ли фильтрация списка.

**списокдиапазон**

Диапазон списка.

**критерииДиапазон**

Диапазон критериев.

**скопировать в**

Диапазон, в который копируются данные.

**уникальныйRecordOnly**

Только отображение или копирование уникальных строк.
## **Применить расширенный фильтр Microsoft Excel для отображения записей, отвечающих сложным критериям**
Следующий пример кода применяет расширенный фильтр к[Образец файла Excel](48496702.xlsx) и генерирует[Выходной файл Excel](48496705.xlsx). На скриншоте показаны оба файла для сравнения. Как вы можете видеть на снимке экрана, данные в выходном файле Excel были отфильтрованы в соответствии со сложными критериями.

![дело:изображение_альтернативный_текст](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
