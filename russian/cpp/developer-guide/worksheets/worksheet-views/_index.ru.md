---
title: Представления листа
type: docs
weight: 40
url: /ru/cpp/worksheet-views/
---

## **Предпросмотр разрывов страниц**
Все листы могут быть просмотрены в двух режимах:

- Обычный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид является видом рабочего листа по умолчанию. Предварительный просмотр разрывов страниц - это режим редактирования, который отображает рабочий лист так, как он будет отпечатан. Предварительный просмотр разрывов страниц показывает, какие данные будут на каждой странице, чтобы можно было настроить область печати и разрывы страниц. С помощью Aspose.Cells разработчики могут включать обычный вид или режим предварительного просмотра разрывов страниц.
### **Управление режимами просмотра**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получать доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления рабочими листами. Чтобы включить обычный или предварительный просмотр разрывов страниц, используйте метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) возвращает логическое значение, что означает, что он может хранить только **true** или **false** значение.
#### **Включение нормального режима**
Установите рабочий лист в обычный вид, установив метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в **false**.
#### **Включение предварительного просмотра разрывов страниц**
Установите любой рабочий лист в режим предварительного просмотра разрывов страниц, установив метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в **true**. Таким образом, рабочий лист переключается из обычного вида в предварительный просмотр разрывов страниц.

Ниже приведен полный пример, демонстрирующий, как использовать метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) для включения режима предварительного просмотра разрывов страниц для первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Коэффициент масштабирования**
### **Использование Microsoft Excel**
Microsoft Excel предоставляет возможность установить коэффициент масштабирования листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.
### **Aspose.Cells и коэффициент увеличения**
Aspose.Cells также позволяет разработчикам устанавливать коэффициент масштабирования листа. Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) представляющий файл Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) позволяющую получать доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления рабочими листами. Чтобы установить коэффициент масштабирования листа, используйте метод [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Коэффициент масштабирования устанавливается путем присвоения числового (целого) значения методу [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom).

Ниже приведен полный пример, демонстрирующий, как использовать метод [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) для установки коэффициента масштабирования первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Закрепить области**
### **Использование Microsoft Excel**
Закрепление области экрана - это функция, предоставляемая Microsoft Excel. Закрепление области экрана позволяет выбрать данные, которые останутся видимыми при прокрутке на листе.
### **Aspose.Cells и заморозка панелей**
Aspose.Cells также позволяет разработчикам применять замораживание областей для рабочих листов во время выполнения. Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) представляющий файл Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) позволяющую получать доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления рабочими листами. Для настройки замораживания областей вызовите метод [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Метод [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) принимает следующие параметры:

- **Строка**, индекс строки, с которой начнется закрепление.
- **Столбец**, индекс столбца, с которого начнется закрепление.
- **Закрепленные строки**, количество видимых строк в верхней панели.
- **Закрепленные столбцы**, количество видимых столбцов в левой панели.

Приведен ниже полный пример, показывающий, как использовать метод [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) для замораживания строк и столбцов (начиная с C4, представленной 4-й строкой и 3-м столбцом, где строки и столбцы начинаются с индекса 0) первого листа файла Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **Разделение областей экрана**
Если вам нужно разделить экран для получения двух разных представлений на одном листе, используйте разделение областей экрана. Microsoft Excel предлагает очень удобную функцию, которая позволяет просматривать более одной копии вашего листа и прокручивать каждую область листа независимо: разделение областей экрана.

Разделы работают одновременно. Если вы внесете изменение в один, изменение одновременно появится в другом. Aspose.Cells предоставляет функцию разделения панелей для пользователей.
### **Применение и удаление разделенных панелей**
#### **Разделение панелей**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) предоставляет широкий спектр методов для управления файлом Excel. Для реализации разделенных видов используйте метод [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Чтобы удалить разделенные панели, используйте метод [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

В примере мы используем простой шаблонный файл, который загружается, затем устанавливается функция разделенных панелей для ячейки на первом листе. Обновленный файл сохраняется.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Удаление панелей**
Удалите разделенные панели с помощью метода [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
