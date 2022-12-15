---
title: Управление именованным диапазоном в книге
type: docs
weight: 90
url: /ru/cpp/manipulate-named-range-in-a-workbook/
---
## **Возможные сценарии использования**
 Aspose.Cells поддерживает работу с существующими именованными диапазонами. Доступ ко всем существующим именованным диапазонам можно получить из[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) коллекция. Как только вы получите доступ к именованному диапазону, вы можете изменить его различные методы, например[ПолучитьПолныйТекст](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)а также[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Управление именованным диапазоном в книге**
 Следующий пример кода считывает первый именованный диапазон внутри[исходный файл excel](23167008.xlsx) и печатает его[Полный текст](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)а также[Относится к](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) свойства на консоли. После этого он изменяет свойство `RefersTo` и сохраняет[выходной файл excel](23167009.xlsx).
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Консольный вывод**
 Следующий вывод консоли выводит значения[Полный текст](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)а также[Относится к](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) члены существующих*Именованный диапазон*в приведенном выше коде.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
