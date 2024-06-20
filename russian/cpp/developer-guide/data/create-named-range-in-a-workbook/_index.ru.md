---
title: Создание Именованного Диапазона в Рабочей Книге
type: docs
weight: 60
url: /ru/cpp/create-named-range-in-a-workbook/
---

## **Возможные сценарии использования**
Aspose.Cells поддерживает создание именованного диапазона. Существуют разные способы создания именованного диапазона. Один из самых простых способов - сначала создать объект [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range), а затем установить его имя, используя метод [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname). Вы можете увидеть все именованные диапазоны в вашем файле Excel через интерфейс Microsoft Excel *Менеджера Имен*.
## **Создание Именованного Диапазона в Рабочей Книге**
В следующем образце кода объясняется, как создать *Именованный Диапазон* с помощью Aspose.Cells. После создания *Именованного Диапазона* он виден в коллекции [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames). Пожалуйста, обратитесь к [выходному файлу Excel](23167006.xlsx), сгенерированному кодом для справки.
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Вывод в консоль**
Следующий вывод в консоли печатает значения методов [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) и [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) созданного *Именованного Диапазона* в вышеприведенном коде.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
