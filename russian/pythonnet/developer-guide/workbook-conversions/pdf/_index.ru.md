---
title: Pdf
type: docs
weight: 220
url: /ru/python-net/convert-excel-to-pdf/
description: Узнайте, как конвертировать Excel в PDF с помощью Aspose.Cells для Python via .NET API.
keywords: Python конвертировать Excel в PDF, конвертировать Excel в PDF с помощью Python, сохранить Excel в PDF с помощью Python, Excel в PDF на Python
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET поддерживает преобразование рабочей книги Excel в PDF. В этом примере мы увидим полное преобразование рабочей книги Excel в PDF.

{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells для Python via .NET поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET напрямую записывает информацию о API и номере версии в выходных документах. Например, при визуализации документа в PDF, Aspose.Cells для Python via .NET заполняет поле **PDF Producer** значением, например 'Aspose.Cells для Python via .NET v23.2'.

Обратите внимание, что вы можете изменить эту информацию в выходных документах с помощью свойства [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Прямое преобразование**

Aspose.Cells для Python via .NET поддерживает конвертацию из электронных таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF с помощью метода [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Метод [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) обеспечивает член перечисления [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/), который конвертирует исходные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните любую работу (введение данных, применение форматирования, установка формул, вставка изображений или других рисунков и т. д.) в электронной таблице с использованием API Aspose.Cells для Python via .NET.
1. Когда код таблицы завершен, вызовите метод [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), чтобы сохранить таблицу.

Формат файла должен быть PDF, поэтому выберите *PDF* (предопределенное значение) из перечисления [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) для создания конечного PDF-документа.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Расширенное преобразование**

Также можно использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) для установки различных атрибутов конвертации. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) дает вам контроль над параметрами печати, шрифтами, безопасностью и сжатием для выводного PDF. Самое важное свойство - [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/), которое позволяет сохранять файлы Excel в формате PDF/A.

#### **Сохранение книги в формате PDF/A**

Ниже приведен фрагмент кода, демонстрирующий использование класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) для сохранения файлов Excel в формате PDF/A.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Обратите внимание, что свойство [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) было добавлено с выпуском Aspose.Cells для Python via .NET для .NET 5.3.0.

{{% /alert %}}

#### **Установить время создания PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) вы можете получать или устанавливать время создания PDF. В следующем коде демонстрируется использование свойства [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) для установки времени создания файла PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Установите опцию ContentCopyForAccessibility**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) вы можете получать или устанавливать параметр PDF [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) для контроля доступа к содержимому в созданном PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Экспорт пользовательских свойств в PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) можно экспортировать пользовательские свойства из исходной книги в формат PDF. Перечислитель [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) предназначен для указания способа экспорта свойств. Эти свойства можно увидеть в Adobe Acrobat Reader, нажав на файл, а затем на опцию свойств, как показано на следующем изображении. Файл шаблона "sourceWithCustProps.xlsx" можно загрузить [здесь](sourceWithCustProps.xlsx) для тестирования, а файл PDF "outSourceWithCustProps" доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Атрибуты преобразования**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Excel в PDF от Aspose.Cells все еще имеет несколько ограничений. Карта заполнения не поддерживается при преобразовании в формат PDF. Кроме того, некоторые объекты рисования не поддерживаются хорошо.

В таблице ниже перечислены все полностью или частично поддерживаемые функции при экспортировании в PDF с использованием Aspose.Cells для Python via .NET. Эта таблица не является окончательной и не содержит все атрибуты электронных таблиц, но идентифицирует те функции, которые не поддерживаются или поддерживаются частично при конверсии в PDF.

|**Элемент документа**|**Атрибут**|**Поддерживается**|**Примечания**|
| :- | :- | :- | :- |
|Выравнивание| |Да| |
|Настройки фона| |Да| |
|Граница|Цвет|Да| |
|Граница|Стиль линии|Да| |
|Граница|Толщина линии|Да| |
|Данные ячейки| |Да| |
|Комментарии| |Да| |
|Условное форматирование| |Да| |
|Свойства документа| |Да| |
|Объекты рисования| |Частично|Тени и трехмерные эффекты для объектов рисования плохо поддерживаются; WordArt и SmartArt поддерживаются частично.|
|Шрифт|Размер|Да| |
|Шрифт|Цвет|Да| |
|Шрифт|Стиль|Да| |
|Шрифт|Подчеркивание|Да| |
|Шрифт|Эффекты|Да| |
|Изображения| |Да| |
|Гиперссылка| |Да| |
|Диаграммы| |Частично|Карта диаграмм не поддерживается.|
|Объединенные ячейки| |Да| |
|Разрыв страницы| |Да| |
|Настройка страницы|Верхний/нижний колонтитул|Да| |
|Настройка страницы|Поля|Да| |
|Настройка страницы|Ориентация страницы|Да| |
|Настройка страницы|Размер страницы|Да| |
|Настройка страницы|Область печати|Да| |
|Настройка страницы|Печатные заголовки|Да| |
|Настройка страницы|Масштабирование|Да| |
|Высота строки/Ширина столбца| |Да| |
|Язык справа налево (RTL)| |Да| |

{{% alert color="primary" %}}

Если ваша электронная таблица содержит формулы, лучше вызвать метод [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) непосредственно перед рендерингом таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формул, и правильное отображение этих значений в PDF.

{{% /alert %}}

## **Продвинутые темы**
- [Добавить закладки PDF](/cells/ru/python-net/add-pdf-bookmarks/)
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Избегание пустой страницы в выходном PDF, когда нет ничего для печати](/cells/ru/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Преобразовать файл XLSX в формат PDF](/cells/ru/python-net/convert-xlsx-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в формат PDF](/cells/ru/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создание PdfBookmarkEntry для листа с диаграммой](/cells/ru/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Заполнить все столбцы листа Excel на одной странице PDF](/cells/ru/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Игнорировать ошибки при преобразовании Excel в PDF](/cells/ru/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества создаваемых страниц - Преобразование Excel в PDF](/cells/ru/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в формат PDF](/cells/ru/python-net/print-comments-while-saving-to-pdf/)
- [Рендеринг офисных надстроек при преобразовании Excel в PDF](/cells/ru/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Отображать одну страницу PDF для каждого листа Excel - Преобразование Excel в PDF](/cells/ru/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells](/cells/ru/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Добавление изображений с изменением размера - Преобразование Excel в PDF](/cells/ru/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Сохранить каждый лист в отдельный файл PDF](/cells/ru/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF с обычным или минимальным размером](/cells/ru/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохранить указанные листы в формат PDF](/cells/ru/python-net/save-specified-worksheets-to-pdf/)
- [Защищенные документы в формате PDF](/cells/ru/python-net/secure-pdf-documents/)
- [Указание способа пересечения строк в выходном PDF и изображении](/cells/ru/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
