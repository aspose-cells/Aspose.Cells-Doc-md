---
title: Представления рабочего листа
type: docs
weight: 40
url: /ru/cpp/worksheet-views/
---
## **Предварительный просмотр разрыва страницы**
Все рабочие листы можно просматривать в двух режимах:

- Нормальный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид — это вид рабочего листа по умолчанию. Предварительный просмотр разрыва страницы — это режим редактирования, в котором рабочий лист отображается в том виде, в котором он будет напечатан. Предварительный просмотр разрыва страницы показывает, какие данные будут размещены на каждой странице, поэтому вы можете настроить область печати и разрывы страниц. Используя Aspose.Cells, разработчики могут включить режимы обычного просмотра или предварительного просмотра с разрывом страницы.
### **Управление режимами просмотра**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы включить обычный режим или режим предварительного просмотра с разрывом страницы, используйте кнопку[Испажебреакпревью](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[Испажебреакпревью](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) возвращает логическое значение, что означает, что он может хранить только**истинный** или же**ЛОЖЬ** стоимость.
#### **Включение обычного просмотра**
Установите рабочий лист в обычный вид, установив[Испажебреакпревью](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс для**ЛОЖЬ**.
#### **Включение предварительного просмотра разрыва страницы**
Установите любой рабочий лист для предварительного просмотра разрыва страницы, установив[Испажебреакпревью](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс для**истинный**При этом рабочий лист переключается с обычного вида на предварительный просмотр разрыва страницы.

 Ниже приведен полный пример, демонстрирующий, как использовать[Испажебреакпревью](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)метод включения режима предварительного просмотра разрыва страницы для первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Коэффициент масштабирования**
### **Использование Microsoft Excel**
Microsoft Excel предоставляет функцию, которая позволяет пользователям устанавливать масштаб рабочего листа или коэффициент масштабирования. Эта функция помогает пользователям просматривать содержимое рабочего листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.
### **Aspose.Cells и коэффициент масштабирования**
 Aspose.Cells также позволяет разработчикам устанавливать коэффициент масштабирования рабочего листа. Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы установить коэффициент масштабирования рабочего листа, используйте кнопку[Увеличить](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class Коэффициент масштабирования задается путем присвоения числового (целочисленного) значения[Увеличить](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)метод.

 Ниже приведен полный пример, демонстрирующий, как использовать[Увеличить](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)метод для установки коэффициента масштабирования первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Замерзшие оконные стекла**
### **Использование Microsoft Excel**
Закрепить области — это функция, предоставляемая Microsoft Excel. Замораживание панелей позволяет выбрать данные, которые будут оставаться видимыми при прокрутке рабочего листа.
### **Aspose.Cells и стопорные панели**
 Aspose.Cells также позволяет разработчикам применять области закрепления к рабочим листам во время выполнения. Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы настроить стоп-панели, вызовите[Замерзшие оконные стекла](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[Замерзшие оконные стекла](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)метод принимает следующие параметры:

- **Строка**, индекс строки ячейки, с которой начнется замораживание.
- **Столбец**, индекс столбца ячейки, с которой начнется замораживание.
- **Замороженные строки**, количество видимых строк в верхней панели.
- **Замороженные столбцы**, количество видимых столбцов в левой панели

 Ниже приведен полный пример, который показывает, как использовать[Замерзшие оконные стекла](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)метод заморозки строк и столбцов (начиная с C4, представленных 4-й строкой и 3-м столбцом, где строки и столбцы начинаются с индекса 0) первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Разделить панели**
Если вам нужно разделить экран, чтобы получить два разных представления на одном листе, разделите панели. Microsoft Excel предлагает очень удобную функцию, позволяющую просматривать несколько копий рабочего листа и иметь возможность независимо прокручивать каждую панель рабочего листа: разделение панелей.

Панели работают одновременно. Если вы вносите изменения в один, это изменение одновременно появляется и в другом. Aspose.Cells предоставляет пользователям функцию разделения панелей.
### **Применение и удаление разделенных панелей**
#### **Разделение панелей**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)class предоставляет широкий спектр методов для управления файлом Excel. Чтобы реализовать разделенные представления, используйте[Расколоть](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс. Чтобы удалить разделенные панели, используйте[УдалитьСплит](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)метод.

В этом примере мы используем простой файл шаблона, который загружается, а затем к ячейке на первом рабочем листе применяется функция установки разделенных панелей. Обновленный файл сохраняется.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Удаление панелей**
 Удалите разделенные панели с помощью[УдалитьСплит](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)метод.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
