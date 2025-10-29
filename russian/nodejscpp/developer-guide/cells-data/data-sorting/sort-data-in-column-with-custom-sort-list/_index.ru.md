---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как сортировать данные в столбце, используя пользовательский список, с помощью API Aspose.Cells for Node.js via C++.
keywords: Сортировка данных в столбце с помощью пользовательского списка, Сортировка данных по пользовательскому списку.
---

## **Возможные сценарии использования**

Вы можете сортировать данные в столбце, используя пользовательский список. Это можно сделать с помощью метода [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-). Однако этот метод работает только если элементы в пользовательском списке не содержат запятых внутри. Если есть запятые, как "USA,US", "China,CN" и т.д., необходимо использовать метод [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-). Здесь последний параметр не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком**

Следующий пример кода объясняет, как использовать метод [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) для сортировки данных с помощью пользовательского списка сортировки. Посмотрите пример файла Excel, используемый в этом коде, и выходной файл Excel, созданный им. Следующий снимок показывает эффект работы кода на примере Excel при выполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
