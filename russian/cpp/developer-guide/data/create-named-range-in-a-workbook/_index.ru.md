---
title: Создать именованный диапазон в книге
type: docs
weight: 60
url: /ru/cpp/create-named-range-in-a-workbook/
---
##  **Возможные сценарии использования**
 Aspose.Cells поддерживает создание именованного диапазона. Существуют разные способы создания именованного диапазона. Один из самых простых способов — сначала создать[Диапазон](https://reference.aspose.com/cells/cpp/aspose.cells/range) объект, а затем установите его имя, используя[Диапазон.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) метод. Вы можете просмотреть все именованные диапазоны внутри файла Excel по номеру Microsoft Excel.*Менеджер имен*интерфейс.
##  **Создать именованный диапазон в книге**
 В следующем примере кода объясняется, как создать*Именованный диапазон* по номеру Aspose.Cells. Однажды*Именованный диапазон* создан, он виден внутри[Рабочая книга.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) коллекция. Пожалуйста, ознакомьтесь с[выходной файл Excel](23167006.xlsx) генерируется кодом для ссылки.
##  **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Консольный вывод**
 Следующий вывод консоли выводит значения[Получить полный текст](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) и[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) методы созданного*Именованный диапазон*в приведенном выше коде.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
