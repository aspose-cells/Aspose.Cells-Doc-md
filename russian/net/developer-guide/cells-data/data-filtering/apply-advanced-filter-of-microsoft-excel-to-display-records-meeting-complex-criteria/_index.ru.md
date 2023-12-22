---
title: Применить расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 280
url: /ru/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Узнайте, как применить расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям, с помощью Aspose.Cells for .NET API.
keywords: Apply Advanced Filter, Set Advanced Filter, Add Advanced Filter, Create Advanced Filter, How to add Advanced Filter to a range 
---
##  **Возможные сценарии использования**

 Microsoft Excel позволяет подать заявку*Расширенный фильтр* на данных рабочего листа для отображения записей, соответствующих сложным критериям. Вы можете применить расширенный фильтр с Microsoft Excel через его*Данные > Дополнительно*команду, как показано на этом снимке экрана.

![задача: image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells также позволяет применять расширенный фильтр с помощью[**Рабочий лист.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)метод. Как и Microsoft Excel, он принимает следующие параметры.

**isFilter**

Указывает, используется ли фильтрация списка.

**списокдиапазон**

Диапазон списка.

**критерииДиапазон**

Критерии варьируются.

**скопировать в**

Диапазон, в который копируются данные.

**уникальныйRecordOnly**

Отображение или копирование только уникальных строк.

##  **Применить расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям**

Следующий пример кода применяет расширенный фильтр к[Пример файла Excel](48496692.xlsx) и генерирует[Выходной файл Excel](48496691.xlsx). На скриншоте показаны оба файла для сравнения. Как вы можете видеть на скриншоте, данные внутри выходного файла Excel были отфильтрованы по сложным критериям.

![задача: image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
