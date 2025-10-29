---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/python-net/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как отсортировать данные в столбце с использованием пользовательского списка с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, сортировка данных в столбце с пользовательским списком, сортировка данных в Python по пользовательскому списку.
---

## **Возможные сценарии использования**

Вы можете отсортировать данные в столбце с использованием пользовательского списка. Это можно сделать с помощью метода [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Однако этот метод работает только, если элементы пользовательского списка не содержат запятых. Если они содержат запятые, такие как "США,US", "Китай,CN" и т. Д., то вы должны использовать метод [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Здесь последний параметр не является строкой, а массивом строк.

## **Сортировка данных в столбце с пользовательским списком**

В следующем образце кода объясняется, как использовать метод [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) для сортировки данных с пользовательским списком. Пожалуйста, посмотрите [образцовый файл Excel](50528327.xlsx), используемый в этом коде, и [выходной файл Excel](50528328.xlsx), созданный им. Ниже приведен скриншот, показывающий эффект кода на образцовом файле Excel при исполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
