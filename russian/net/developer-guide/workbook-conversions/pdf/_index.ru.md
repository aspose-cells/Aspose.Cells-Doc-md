---
title: Pdf
type: docs
weight: 220
url: /ru/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование книги Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.

{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}}

Aspose.Cells for .NET напрямую записывает информацию о API и номере версии в выходных документах. Например, при визуализации документа в PDF Aspose.Cells for .NET заполняет поле **PDF Producer** значением, например, 'Aspose.Cells v23.2'.

Обратите внимание, что вы можете изменить эту информацию в выходных документах с помощью свойства [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Прямое преобразование**

Aspose.Cells for .NET поддерживает конвертацию из таблиц в формат PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF, используя метод класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Метод [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) класса предоставляет член перечисления [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index), который преобразует исходные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните любую работу (ввод данных, применение форматирования, задание формул, вставка изображений или других объектов рисования и т. д.) на электронной таблице, используя API Aspose.Cells.
1. Когда код таблицы завершен, вызовите метод [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), чтобы сохранить таблицу.

Формат файла должен быть PDF, поэтому выберите *Pdf* (предопределенное значение) из перечисления [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) для создания окончательного документа PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Расширенное преобразование**

Вы также можете использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) для установки различных атрибутов конвертации. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) позволяет контролировать настройки печати, шрифта, безопасности и сжатия для выходного PDF. 

Самым важным свойством является [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance), позволяющий устанавливать уровень соответствия стандартам PDF. В настоящее время можно сохранять в форматах PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u. Обратите внимание, что при формате PDF/A размер выходного файла больше, чем у обычного файла PDF.

#### **Сохранение книги в формате PDF/A**

Ниже приведен фрагмент кода, демонстрирующий использование класса [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) для сохранения файлов Excel в формате PDF/A.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Обратите внимание, что свойство [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) добавлено в версии Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Установить время создания PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) вы можете получать или устанавливать время создания PDF. В следующем коде демонстрируется использование свойства [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) для установки времени создания файла PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Установите опцию ContentCopyForAccessibility**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) вы можете получать или устанавливать параметр PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) для контроля доступа к содержимому в созданном PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Экспорт пользовательских свойств в PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) можно экспортировать пользовательские свойства из исходной книги в формат PDF. Перечислитель [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport) предназначен для указания способа экспорта свойств. Эти свойства можно увидеть в Adobe Acrobat Reader, нажав на файл, а затем на опцию свойств, как показано на следующем изображении. Файл шаблона "sourceWithCustProps.xlsx" можно загрузить [здесь](sourceWithCustProps.xlsx) для тестирования, а файл PDF "outSourceWithCustProps" доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Атрибуты преобразования**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Excel в PDF от Aspose.Cells все еще имеет несколько ограничений. Карта заполнения не поддерживается при преобразовании в формат PDF. Кроме того, некоторые объекты рисования не поддерживаются хорошо.

В таблице ниже перечислены все функции, которые полностью или частично поддерживаются при экспорте в формат PDF с помощью Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты таблиц, но она идентифицирует те функции, которые не поддерживаются или поддерживаются частично для преобразования в PDF.

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

Если ваша таблица содержит формулы, лучше вызвать [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед отображением таблицы в формате PDF. Это обеспечит пересчет значений, зависящих от формулы, и правильное отображение значений в PDF.

{{% /alert %}}

## **Продвинутые темы**
- [Добавить закладки PDF](/cells/ru/net/add-pdf-bookmarks/)
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/net/add-pdf-bookmarks-with-named-destinations/)
- [Избегание пустой страницы в выходном PDF, когда нет ничего для печати](/cells/ru/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Изменить шрифт только для определенных символов Unicode при сохранении в формате PDF](/cells/ru/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Контроль загрузки внешних ресурсов в книге MS Excel во время преобразования в PDF](/cells/ru/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Преобразовать файл XLSX в формат PDF](/cells/ru/net/convert-xlsx-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в формат PDF](/cells/ru/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создание PdfBookmarkEntry для листа с диаграммой](/cells/ru/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Заполнить все столбцы листа Excel на одной странице PDF](/cells/ru/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler](/cells/ru/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получить предупреждения о замене шрифта при преобразовании файла Excel](/cells/ru/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при преобразовании Excel в PDF](/cells/ru/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества создаваемых страниц - Преобразование Excel в PDF](/cells/ru/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в формат PDF](/cells/ru/net/print-comments-while-saving-to-pdf/)
- [Рендеринг офисных надстроек при преобразовании Excel в PDF](/cells/ru/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Отображать одну страницу PDF для каждого листа Excel - Преобразование Excel в PDF](/cells/ru/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells](/cells/ru/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Добавление изображений с изменением размера - Преобразование Excel в PDF](/cells/ru/net/resampling-added-images-excel-to-pdf-conversion/)
- [Сохранить каждый лист в отдельный файл PDF](/cells/ru/net/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF с обычным или минимальным размером](/cells/ru/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохранить указанные листы в формат PDF](/cells/ru/net/save-specified-worksheets-to-pdf/)
- [Защищенные документы в формате PDF](/cells/ru/net/secure-pdf-documents/)
- [Указание способа пересечения строк в выходном PDF и изображении](/cells/ru/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
