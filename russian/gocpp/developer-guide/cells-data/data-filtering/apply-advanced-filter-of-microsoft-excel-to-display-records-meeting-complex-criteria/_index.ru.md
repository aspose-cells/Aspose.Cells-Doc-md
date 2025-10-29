---
title: Применение расширенного фильтра Microsoft Excel для отображения записей, отвечающих сложным условиям, с помощью Golang через C++
linktitle: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 280
url: /ru/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Узнайте, как применять расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным условиям, используя API Aspose.Cells for C++.
keywords: Применить расширенный фильтр, установить расширенный фильтр, добавить расширенный фильтр, создать расширенный фильтр, Как добавить расширенный фильтр к диапазону
---

## **Возможные сценарии использования**

Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить расширенный фильтр через команду *Данные > Расширенный*, как показано на скриншоте.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells также позволяет использовать расширенный фильтр с помощью метода [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/). Аналогично Microsoft Excel, он принимает следующие параметры.

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

Следующий пример кода применяет расширенный фильтр к [пробному Excel-файлу](48496692.xlsx) и создает [выходной Excel-файл](48496691.xlsx). Скриншот показывает оба файла для сравнения. Внутри скриншота видно, что данные были отфильтрованы внутри выходного файла согласно сложным условиям.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
