---
title: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 280
url: /ru/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Узнайте, как применить расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям, используя API Aspose.Cells для Python via .NET.
keywords: Библиотека Python для Excel, применение расширенного фильтра Python, установка расширенного фильтра Python, добавление расширенного фильтра Python, создание расширенного фильтра Python, Как добавить расширенный фильтр к диапазону с помощью Python.
---

## **Возможные сценарии использования**

Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить Расширенный фильтр с помощью Microsoft Excel через команду *Данные > Расширенный*, как показано на этом скриншоте.

![todo:image_alt_text](1.png)

Aspose.Cells для Python via .NET также позволяет применять Расширенный фильтр с использованием метода [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool). Как и в Microsoft Excel, он принимает следующие параметры.

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

![todo:image_alt_text](2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
{{< app/cells/assistant language="python-net" >}}
