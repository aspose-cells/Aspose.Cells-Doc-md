---
title: Ось даты
description: Узнайте, как управлять осью даты по номеру Aspose.Cells for Java. Наше руководство поможет вам понять, как работать с различными форматами дат, шкалами времени и частотой галочек.
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /ru/java/date-axis/
---
##  **Возможные сценарии использования**
Когда вы создаете диаграмму из данных листа, в которых используются даты, и даты откладываются вдоль горизонтальной оси (категорий) на диаграмме, Aspose.cells автоматически меняет ось категорий на ось даты (шкалы времени).
Ось даты отображает даты в хронологическом порядке через определенные интервалы или базовые единицы, например количество дней, месяцев или лет, даже если даты на листе расположены не в последовательном порядке или в одних и тех же базовых единицах.
По умолчанию Aspose.cells определяет базовые единицы для оси дат на основе наименьшей разницы между любыми двумя датами в данных рабочего листа. Например, если у вас есть данные о ценах на акции, где наименьшая разница между датами составляет семь дней, Excel задает в качестве базовой единицы дни, но вы можете изменить базовую единицу на месяцы или годы, если хотите увидеть динамику акций за период. более длительный период времени.
##  **Обработка оси даты, например Microsoft Excel**
 См. следующий пример кода, который создает новый файл Excel и помещает значения диаграммы на первый лист.
 Затем мы добавляем диаграмму и устанавливаем тип[**Ось**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
 к[**Шкала времени**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) а затем установите базовые единицы измерения на «Дни».

![задача: image_alt_text](excel.png)

 Следующий пример кода генерирует[выходной файл Excel](DateAxis.xlsx).

##  **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
