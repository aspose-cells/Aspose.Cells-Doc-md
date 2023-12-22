---
title: Просмотры рабочих листов
type: docs
weight: 40
url: /ru/cpp/worksheet-views/
---
##  **Предварительный просмотр разрыва страницы**
Все рабочие листы можно просматривать в двух режимах:

- Нормальный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид — это вид листа по умолчанию. Предварительный просмотр разрыва страницы — это режим редактирования, в котором лист отображается в том виде, в каком он будет напечатан. Предварительный просмотр разрыва страницы показывает, какие данные будут размещены на каждой странице, поэтому вы можете настроить область печати и разрывы страниц. Используя Aspose.Cells, разработчики могут включить режимы обычного просмотра или предварительного просмотра разрыва страницы.
###  **Управление режимами просмотра**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы включить обычный режим предварительного просмотра или режим разрыва страницы, используйте команду[SetIsPageBreakПредварительный просмотр](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[IsPageBreakПредварительный просмотр](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) возвращает логическое значение, что означает, что он может хранить только**истинный** или**ЛОЖЬ** ценить.
####  **Включение обычного просмотра**
Установите рабочий лист в обычный вид, установив[SetIsPageBreakПредварительный просмотр](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)класс в *false**.
####  **Включение предварительного просмотра разрыва страницы**
Установите для любого листа предварительный просмотр разрыва страницы, установив[SetIsPageBreakПредварительный просмотр](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)класс на *true**. При этом лист переключается из обычного вида в режим предварительного просмотра разрыва страницы.

Ниже приведен полный пример, демонстрирующий, как использовать[SetIsPageBreakПредварительный просмотр](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)метод, позволяющий включить режим предварительного просмотра разрыва страницы для первого листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Коэффициент масштабирования**
###  **Использование Microsoft Excel**
Microsoft Excel предоставляет функцию, которая позволяет пользователям устанавливать масштаб или коэффициент масштабирования рабочего листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить любое значение коэффициента масштабирования.
###  **Aspose.Cells и коэффициент масштабирования**
 Aspose.Cells также позволяет разработчикам устанавливать коэффициент масштабирования листа. Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы установить коэффициент масштабирования рабочего листа, используйте[УстановитьZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт. Коэффициент масштабирования устанавливается путем присвоения числового (целого) значения[УстановитьZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)метод.

Ниже приведен полный пример, демонстрирующий, как использовать[УстановитьZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)метод для установки коэффициента масштабирования первого листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Замерзшие оконные стекла**
###  **Использование Microsoft Excel**
Зафиксировать панели — это функция, предоставляемая Excel Microsoft. Закрепление панелей позволяет выбирать данные, которые останутся видимыми при прокрутке листа.
###  **Aspose.Cells и замораживающие стекла**
 Aspose.Cells также позволяет разработчикам применять закрепленные области к рабочим листам во время выполнения. Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы настроить области закрепления, вызовите команду[Замерзшие оконные стекла](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Замерзшие оконные стекла](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)метод принимает следующие параметры:

- *Строка**: индекс строки ячейки, с которой начнется замораживание.
- *Столбец**: индекс столбца ячейки, с которой начнется замораживание.
- *Закрепленные строки** — количество видимых строк на верхней панели.
- *Закрепленные столбцы**, количество видимых столбцов на левой панели.

 Ниже приведен полный пример, показывающий, как использовать[Замерзшие оконные стекла](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)метод замораживания строк и столбцов (начиная с C4, представленного 4-й строкой и 3-м столбцом, где строки и столбцы начинаются с индекса 0) первого листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Разделить панели**
Если вам нужно разделить экран, чтобы получить два разных представления на одном листе, разделите панели. Microsoft Excel предлагает очень удобную функцию, которая позволяет вам просматривать более одной копии вашего листа, а также иметь возможность прокручивать каждую область вашего листа независимо: разделение панелей.

Панели работают одновременно. Если вы внесете изменение в один, изменение одновременно появится и в другом. Aspose.Cells предоставляет пользователям функцию разделения панелей.
###  **Применение и удаление разделенных панелей**
####  **Разделение панелей**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Класс предоставляет широкий спектр методов управления файлом Excel. Чтобы реализовать разделенные представления, используйте[Расколоть](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт. Чтобы удалить разделенные панели, используйте команду[УдалитьSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)метод.

В этом примере мы используем простой файл шаблона, который загружается, затем функция установки разделения панелей применяется к ячейке на первом листе. Обновленный файл сохраняется.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Удаление панелей**
 Удалите разделенные панели с помощью[УдалитьSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)метод.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
