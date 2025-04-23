---
title: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 190
url: /ru/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Возможные сценарии использования**
Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить Расширенный фильтр с помощью Microsoft Excel через команду *Данные > Расширенный*, как показано на этом скриншоте.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells также позволяет применять расширенный фильтр с помощью метода [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter-boolean-java.lang.String-java.lang.String-java.lang.String-boolean-). Так же, как в Microsoft Excel, он принимает следующие параметры.

**isFilter**

Указывает, фильтровать ли список на месте.

**listRange**

Диапазон списка.

**criteriaRange**

Диапазон критериев.

**copyTo**

Диапазон, куда копируются данные.

**uniqueRecordOnly**

Отображение или копирование только уникальных строк.
## **Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям**
Приведенный ниже образец кода применяет расширенный фильтр к [Образцовому файлу Excel](48496702.xlsx) и создает [Выходной файл Excel](48496705.xlsx). На снимке экрана показаны оба файла для сравнения. Как видно на снимке экрана, данные были отфильтрованы внутри выходного файла Excel в соответствии с комплексными критериями.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
{{< app/cells/assistant language="java" >}}
