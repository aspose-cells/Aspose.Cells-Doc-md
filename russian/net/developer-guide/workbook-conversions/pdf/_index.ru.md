---
title: PDF
type: docs
weight: 220
url: /ru/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование книги Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.

{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и отдельными лицами. Это стандартный формат документов, и разработчиков программного обеспечения часто просят найти способ конвертировать Microsoft файлы Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и обеспечивает высокую визуальную точность преобразования.

{{% alert color="primary" %}}

 Aspose.Cells for .NET непосредственно записывает информацию о API и номере версии в выходных документах. Например, при преобразовании документа в PDF Aspose.Cells for .NET заполняет**Заявление** поле со значением «Aspose.Cells» и**PDF-продюсер**поле со значением, например 'Aspose.Cells v17.9'.

Обратите внимание, что вы не можете поручить Aspose.Cells for .NET изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

### **Прямое преобразование**

 Aspose.Cells for .NET поддерживает преобразование электронных таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF, используя**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** учебный класс'**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод.**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод обеспечивает**[SaveFormat.Pdf] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**член перечисления, который преобразует собственные файлы Excel в формат PDF.

Выполните следующие шаги, чтобы напрямую преобразовать электронные таблицы Excel в формат PDF:

1.  Создать экземпляр объекта**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)**class, вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона или пропустить этот шаг, если создаете книгу с нуля.
1. Выполняйте любую работу (ввод данных, применение форматирования, установка формул, вставка рисунков или других объектов рисования и т. д.) в электронной таблице с помощью API-интерфейсов Aspose.Cells'.
1. Когда код электронной таблицы будет готов, вызовите**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** учебный класс'**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**метод сохранения таблицы.

 Формат файла должен быть PDF, поэтому выберите*PDF* (заранее определенное значение) из**[Сохранить формат] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**перечисление для создания окончательного PDF-документа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Расширенное преобразование**

 Вы также можете выбрать использование**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** класс для установки различных атрибутов для преобразования. Установка различных свойств**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class дает вам контроль над настройками печати, шрифта, безопасности и сжатия для выходного PDF. Наиболее важным свойством является**[Соответствие](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**который позволяет сохранять файлы Excel в PDF-файлы, совместимые с PDF/A.

#### **Сохранение рабочей книги в файлах PDF/A Complied**

 Приведенный ниже фрагмент кода демонстрирует, как использовать**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**класс для сохранения файлов Excel в формате PDF, совместимом с PDF/A.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Обратите внимание,**[Соответствие](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**свойство было добавлено с выпуском Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Установите время создания PDF**

 С**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class вы можете получить или установить время создания PDF. Следующий код демонстрирует использование**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** свойство, чтобы установить время создания файла PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Установите параметр ContentCopyForAccessibility**

С**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** класс, вы можете получить или установить PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** возможность контролировать доступ к содержимому в преобразованном PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Экспорт пользовательских свойств в PDF**

С**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class вы можете экспортировать пользовательские свойства исходной книги в PDF.**[PdfCustomPropertiesExport] (https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**перечислитель предназначен для указания способа экспорта свойств. Эти свойства можно просмотреть в Adobe Acrobat Reader, щелкнув «Файл», а затем параметр «Свойства», как показано на следующем рисунке. Файл шаблона "sourceWithCustProps.xlsx" можно скачать[здесь](sourceWithCustProps.xlsx) для тестирования и вывода доступен PDF-файл "outSourceWithCustProps"[здесь](outSourceWithCustProps.pdf) для анализа.

![дело:изображение_альтернативный_текст](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Атрибуты конверсии**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Aspose.Cell Excel в PDF по-прежнему имеет несколько ограничений. Некоторое форматирование электронной таблицы может быть потеряно при преобразовании в формат PDF. Кроме того, некоторые объекты рисования еще не поддерживаются.

В следующей таблице перечислены все функции, которые полностью или частично поддерживаются при экспорте в PDF с помощью Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты электронной таблицы, но в ней указаны те функции, которые не поддерживаются или частично поддерживаются для преобразования в PDF. .

|**Элемент документа**|**Атрибут**|**Поддерживается**|**Заметки**|
|:- |:- |:- |:- |
|Выравнивание||Да||
|Настройки фона||Да||
|Граница|Цвет|Да||
|Граница|Стиль линии|Да||
|Граница|Ширина линии|Да||
|Cell Данные||Да||
|Комментарии||Да||
|Условное форматирование||Да||
|Свойства документа||Да||
|Объекты рисования||Частично|Поддерживаемые объекты: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Шрифт|Размер|Да||
|Шрифт|Цвет|Да||
|Шрифт|Стиль|Да||
|Шрифт|Подчеркнуть|Да||
|Шрифт|Последствия|Частично|Поддерживается только эффект зачеркивания|
|Картинки||Да||
|Гиперссылка||Да||
|Графики||Частично||
|Объединено Cells||Да||
|Разрыв страницы||Да||
|Настройка страницы|Верхний/нижний колонтитул|Да||
|Настройка страницы|Поля|Да||
|Настройка страницы|Ориентация страницы|Да||
|Настройка страницы|Размер страницы|Да||
|Настройка страницы|Область печати|Да||
|Настройка страницы|Печать заголовков|Да||
|Настройка страницы|Масштабирование|Да||
|Высота строки/ширина столбца||Да||
|Язык RTL (справа налево)||Да||

{{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** непосредственно перед рендерингом электронной таблицы в формат PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}

## **Предварительные темы**
- [Добавить закладки PDF](/cells/ru/net/add-pdf-bookmarks/)
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/net/add-pdf-bookmarks-with-named-destinations/)
- [Избегайте пустой страницы в выходном PDF-файле, когда нечего печатать](/cells/ru/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Измените шрифт только на определенные символы Unicode при сохранении в PDF](/cells/ru/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Управление загрузкой внешних ресурсов в книгу MS Excel при рендеринге в PDF](/cells/ru/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Преобразование файла XLS в формат PDF](/cells/ru/net/convert-an-xls-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразование файла XLS с изображениями или диаграммами в PDF](/cells/ru/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создайте PdfBookmarkEntry для листа диаграммы](/cells/ru/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Подогнать все столбцы рабочего листа на одной странице PDF](/cells/ru/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получить DrawObject и Bound при рендеринге в PDF с помощью класса DrawObjectEventHandler](/cells/ru/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получение предупреждений о замене шрифта при рендеринге файла Excel](/cells/ru/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при рендеринге Excel в PDF](/cells/ru/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества генерируемых страниц - преобразование Excel в PDF](/cells/ru/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в PDF](/cells/ru/net/print-comments-while-saving-to-pdf/)
- [Рендеринг надстроек Office при преобразовании Excel в PDF](/cells/ru/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Рендеринг одной страницы PDF на лист Excel - Преобразование Excel в PDF](/cells/ru/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Визуализация дополнительных символов Unicode в выходном PDF по Aspose.Cells](/cells/ru/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Передискретизация добавленных изображений - Преобразование Excel в PDF](/cells/ru/net/resampling-added-images-excel-to-pdf-conversion/)
- [Сохраните каждый рабочий лист в другой файл PDF](/cells/ru/net/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF со стандартным или минимальным размером](/cells/ru/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Безопасные PDF-документы](/cells/ru/net/secure-pdf-documents/)
- [Укажите, как пересекать строку в выходном PDF-файле и изображении](/cells/ru/net/specify-how-to-cross-string-in-output-pdf-and-image/)
