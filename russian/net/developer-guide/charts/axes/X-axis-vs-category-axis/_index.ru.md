---
title: Ось X против категориальной оси
description: Узнайте, как отличить X ось от оси категорий в Aspose.Cells for .NET. Наше руководство поможет вам понять различия в их использовании и свойствах, а также настроить их в соответствии с вашими потребностями.
keywords: Aspose.Cells for .NET, X ось, ось категорий, разница, использование, свойства, конфигурация.
type: docs
weight: 180
url: /ru/net/X-axis-vs-category-axis/
---

## **Возможные сценарии использования**
Существуют разные типы осей X. В то время как ось Y является осью типа значения, ось X может быть осью типа категории или осью типа значения. Используя ось значения, данные рассматриваются как непрерывно изменяющиеся числовые данные, и маркер располагается в точке вдоль оси, которая изменяется в соответствии с их числовым значением. Используя категориальную ось, данные рассматриваются как последовательность нечисловых текстовых меток, и маркер располагается в точке вдоль оси в соответствии с ее положением в последовательности. Приведенный ниже пример иллюстрирует разницу между осями значения и категории.
Наши примерные данные показаны в [файле примеров таблиц](sample.png) ниже. Первый столбец содержит наши данные оси X, которые могут рассматриваться как категории или как значения. Обратите внимание, что числа не равномерно распределены, и они даже не появляются в числовом порядке.

![todo:image_alt_text](sample.png)
## **Обрабатывайте ось X и категориальную ось, подобно Microsoft Excel**
Мы отобразим эти данные на двух типах диаграмм: первая диаграмма - XY (точечная) диаграмма для оси X как оси значений, вторая диаграмма - линейная диаграмма для оси X как категориальной оси.

![todo:image_alt_text](compare.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
{{< app/cells/assistant language="csharp" >}}
