---
title: Создать именованный диапазон в книге
type: docs
weight: 60
url: /ru/cpp/create-named-range-in-a-workbook/
---
## **Возможные сценарии использования**
 Aspose.Cells поддерживает создание именованного диапазона. Существуют разные способы создания именованного диапазона. Один из самых простых способов — сначала создать[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) объект, а затем установите его имя, используя[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) метод. Вы можете увидеть все именованные диапазоны внутри вашего файла Excel через Microsoft Excel*Менеджер имен*интерфейс.
## **Создать именованный диапазон в книге**
 В следующем примере кода показано, как создать*Именованный диапазон* через Aspose.Cells. Однажды,*Именованный диапазон* создан, он виден внутри[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) коллекция. Пожалуйста, смотрите[выходной файл excel](23167006.xlsx) генерируется кодом для ссылки.
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Консольный вывод**
 Следующий вывод консоли выводит значения[ПолучитьПолныйТекст](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) и `GetRefersTo` методы созданного*Именованный диапазон*в приведенном выше коде.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
