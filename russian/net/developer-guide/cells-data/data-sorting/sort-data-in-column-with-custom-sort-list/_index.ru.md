---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/net/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как сортировать данные в столбце с помощью пользовательского списка с помощью API Aspose.Cells for .NET.
keywords: Сортировка данных в столбце с помощью пользовательского списка, Сортировка данных по пользовательскому списку.
---

## **Возможные сценарии использования**

Вы можете сортировать данные в столбце с помощью пользовательского списка. Это можно сделать с помощью метода [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2). Однако этот метод работает, только если элементы в пользовательском списке не содержат запятых. Если они содержат запятые, например, "USA,US", "China,CN" и т. д., то нужно использовать [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) метод. Здесь последний параметр не является строкой, а массивом строк.

## **Сортировка данных в столбце с пользовательским списком**

В следующем образце кода объясняется, как использовать метод [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) для сортировки данных с помощью пользовательского списка. Пожалуйста, посмотрите [образец Excel-файла](50528327.xlsx), использованный в этом коде, и [выходной Excel-файл](50528328.xlsx), сгенерированный им. Ниже показан эффект кода на образцовом Excel-файле при выполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
{{< app/cells/assistant language="csharp" >}}
