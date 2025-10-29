---
title: Манипулирование именованным диапазоном в книге
type: docs
weight: 90
url: /ru/cpp/manipulate-named-range-in-a-workbook/
---

## **Возможные сценарии использования**
Aspose.Cells поддерживает манипуляции существующими именованными диапазонами. Все существующие именованные диапазоны можно получить из коллекции [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/). После доступа к именованному диапазону, можно изменить его различные методы, например [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) и [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Манипулирование именованным диапазоном в книге**
Приведенный ниже образец кода считывает первый именованный диапазон внутри [исходного файла Excel](23167008.xlsx) и печатает его свойства [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) и [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) в консоли. Затем он изменяет свойство `RefersTo` и сохраняет [выходной файл Excel](23167009.xlsx).
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Вывод в консоль**
Приведенный ниже вывод консоли выводит значения членов [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) и [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) существующего *именованного диапазона* из вышеуказанного кода.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
