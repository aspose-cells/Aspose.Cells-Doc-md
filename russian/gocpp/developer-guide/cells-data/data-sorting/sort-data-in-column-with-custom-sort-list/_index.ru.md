---
title: Сортировка данных в столбце с пользовательским списком сортировки с помощью Golang через C++
linktitle: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как отсортировать данные в столбце с использованием пользовательского списка, применяя API Aspose.Cells for C++.
keywords: Сортировка данных в столбце с помощью пользовательского списка, Сортировка данных по пользовательскому списку.
---

## **Возможные сценарии использования**

Вы можете отсортировать данные в столбце, используя пользовательский список. Это можно сделать с помощью метода [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Однако этот метод работает только в случае, если элементы в пользовательском списке не содержат запятых. Если там есть запятые, как в "USA,US", "China,CN" и т.д., тогда необходимо использовать метод [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Здесь последний параметр — не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком**

Следующий пример кода показывает, как использовать метод [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) для сортировки данных с помощью пользовательского списка сортировки. Пожалуйста, посмотрите на [пример файла Excel](50528327.xlsx), используемый в этом коде, и [сгенерированный выходной файл Excel](50528328.xlsx). Следующий скриншот показывает эффект работы кода на примере файла Excel при выполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
