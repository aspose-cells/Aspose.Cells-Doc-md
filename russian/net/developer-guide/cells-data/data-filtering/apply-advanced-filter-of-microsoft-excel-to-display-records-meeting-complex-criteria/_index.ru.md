---
title: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 280
url: /ru/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Узнать, как применить расширенный фильтр в Microsoft Excel для отображения записей, соответствующих сложным критериям, с использованием API Aspose.Cells for .NET.
keywords: Применить расширенный фильтр, установить расширенный фильтр, добавить расширенный фильтр, создать расширенный фильтр, Как добавить расширенный фильтр к диапазону 
---

## **Возможные сценарии использования**

Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить Расширенный фильтр с помощью Microsoft Excel через команду *Данные > Расширенный*, как показано на этом скриншоте.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells также позволяет применить расширенный фильтр, используя метод [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter). Как и в Microsoft Excel, он принимает следующие параметры.

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

Приведенный ниже образец кода применяет расширенный фильтр к [Примерному файлу Excel](48496692.xlsx) и генерирует [Выходной файл Excel](48496691.xlsx). На скриншоте показаны оба файла для сравнения. Как видно на скриншоте, данные были отфильтрованы в выходном файле Excel в соответствии с сложными критериями.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
