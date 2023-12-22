---
title: Управление именованным диапазоном в книге
type: docs
weight: 90
url: /ru/cpp/manipulate-named-range-in-a-workbook/
---
##  **Возможные сценарии использования**
 Aspose.Cells поддерживает манипуляции с существующими именованными диапазонами. Доступ ко всем существующим именованным диапазонам можно получить из[Рабочая книга.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) коллекция. Получив доступ к именованному диапазону, вы можете изменить его различные методы, например[Получить полный текст](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)и[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Управление именованным диапазоном в книге**
 Следующий пример кода считывает первый именованный диапазон внутри[исходный файл Excel](23167008.xlsx) и распечатывает его[Полный текст](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)и[Относится к](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) свойства в консоли. После этого он изменяет свойство `RefersTo` и сохраняет[выходной файл Excel](23167009.xlsx).
##  **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Консольный вывод**
 Следующий вывод консоли выводит значения[Полный текст](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)и[Относится к](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) члены существующих*Именованный диапазон*в приведенном выше коде.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
