---
title: Ось дат
description: Узнайте, как управлять осью дат в Aspose.Cells for .NET. Наша инструкция поможет вам понять, как работать с различными форматами дат, временными шкалами и частотами меток делений.
keywords: Aspose.Cells for .NET, ось дат, управление, форматы дат, временные шкалы, частоты меток делений.
type: docs
weight: 200
url: /ru/net/date-axis/
---

## **Возможные сценарии использования**
При создании диаграммы на основе данных листа, использующих даты, и даты построены вдоль горизонтальной (категорийной) оси в диаграмме, Aspose.Cells автоматически изменяет категорийную ось на ось дат (временной масштаб).
Ось дат отображает даты в хронологическом порядке с определенными интервалами или базовыми единицами, такими как количество дней, месяцев или лет, даже если даты на листе не расположены последовательно или в тех же базовых единицах.
По умолчанию Aspose.Cells определяет базовые единицы для оси дат на основе наименьшего различия между любыми двумя датами в данных листе. Например, если у вас есть данные о ценах на акции, где наименьшее различие между датами составляет семь дней, Excel устанавливает базовую единицу в дни, но вы можете изменить базовую единицу на месяцы или годы, если хотите увидеть динамику акций за более длительный период времени.
## **Обработка оси дат, подобно Microsoft Excel**
Пожалуйста, посмотрите примерный код, который создает новый файл Excel и помещает значения диаграммы в первый лист. 
Затем мы добавляем диаграмму и устанавливаем тип [**Axis**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
на [**TimeScale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/), а затем устанавливаем базовые единицы в Дни.

![todo:image_alt_text](excel.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
{{< app/cells/assistant language="csharp" >}}
