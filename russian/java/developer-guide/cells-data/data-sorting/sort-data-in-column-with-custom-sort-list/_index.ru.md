---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 210
url: /ru/java/sort-data-in-column-with-custom-sort-list/
---

## **Возможные сценарии использования**

Вы можете сортировать данные в столбце с помощью пользовательского списка. Это можно сделать с помощью метода [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-). Однако этот метод работает только если элементы в пользовательском списке не содержат запятых внутри них. Если в списке есть запятые, например "USA, US", "China, CN" и т.д., тогда нужно использовать тот же метод. В этом случае последний параметр — не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком**

В следующем образце кода объясняется, как использовать метод DataSorter.AddKey(int key, SortOrder order, String[] customList) для сортировки данных с помощью пользовательского списка сортировки. Пожалуйста, ознакомьтесь с [образцом Excel-файла](50528359.xlsx), используемым в этом коде, и [выходным Excel-файлом](50528358.xlsx), сгенерированным им. Ниже показан эффект кода на образец Excel-файла при выполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
