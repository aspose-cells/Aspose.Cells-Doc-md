---
title: Pdf
type: docs
weight: 220
url: /ru/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование книги Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.

{{% /alert %}}

##  **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и частными лицами. Это стандартный формат документов, и разработчиков программного обеспечения часто просят найти способ конвертировать файлы Excel Microsoft в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и обеспечивает высокую визуальную точность преобразования.

{{% alert color="primary" %}}

 Aspose.Cells for .NET напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF, Aspose.Cells for .NET заполняется**PDF Производитель** поле со значением, например, «Aspose.Cells v23.2».

 Обратите внимание, что вы можете изменить эту информацию в выходных документах, выполнив**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)** свойство.

{{% /alert %}}

###  **Прямое преобразование**

 Aspose.Cells for .NET поддерживает преобразование электронных таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel по адресу PDF, используя**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**сорт'**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод.**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод обеспечивает**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**член перечисления, преобразующий собственные файлы Excel в формат PDF.

Выполните следующие шаги, чтобы напрямую преобразовать таблицы Excel в формат PDF:

1.  Создать экземпляр объекта**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**класс, вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона или пропустить этот шаг, если создаете книгу с нуля.
1. Выполняйте любую работу (ввод данных, применение форматирования, установку формул, вставку изображений или других объектов рисования и т. д.) в электронной таблице с помощью API-интерфейсов Aspose.Cells'.
1.  Когда код электронной таблицы будет готов, вызовите**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**сорт'**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**метод сохранения таблицы.

 Формат файла должен быть PDF, поэтому выберите*Pdf* (предварительно определенное значение) из**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**перечисление для создания окончательного документа PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **Расширенное преобразование**

 Вы также можете использовать**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class для установки различных атрибутов для преобразования. Установка различных свойств**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Класс дает вам контроль над настройками печати, шрифта, безопасности и сжатия для вывода PDF. Наиболее важным свойством является**[Соответствие](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**что позволяет сохранять файлы Excel в файлы PDF, соответствующие стандарту PDF/A.

####  **Сохранение книги в файлах, соответствующих PDF/A**

 Приведенный ниже фрагмент кода демонстрирует, как использовать**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**класс для сохранения файлов Excel в формате PDF, совместимом с PDF/A.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Обратите внимание,**[Соответствие](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**свойство было добавлено с выпуском Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

####  **Установите время создания PDF.**

 С**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class, вы можете получить или установить время создания PDF. Следующий код демонстрирует использование**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** Свойство, позволяющее установить время создания файла PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **Установите параметр ContentCopyForAccessibility.**

С**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** класс, вы можете получить или установить PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** возможность контролировать доступ к контенту в преобразованном PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **Экспортировать пользовательские свойства на номер PDF.**

С**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** вы можете экспортировать пользовательские свойства из исходной книги в файл PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**перечислитель предназначен для указания способа экспорта свойств. Эти свойства можно просмотреть в Adobe Acrobat Reader, щелкнув «Файл», а затем «Свойства», как показано на следующем изображении. Файл шаблона «sourceWithCustProps.xlsx» можно скачать.[здесь](sourceWithCustProps.xlsx) для тестирования и вывода PDF доступен файл "outSourceWithCustProps"[здесь](outSourceWithCustProps.pdf) для анализа.

![задача: image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **Атрибуты конверсии**

Мы работаем над улучшением функций конвертации с каждой новой версией. Преобразование Excel Aspose.Cell в PDF все еще имеет несколько ограничений. MapChart не поддерживается при преобразовании в формат PDF. Кроме того, некоторые объекты рисования поддерживаются недостаточно хорошо.

В следующей таблице перечислены все функции, которые полностью или частично поддерживаются при экспорте в PDF с использованием Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты электронной таблицы, но она определяет те функции, которые не поддерживаются или частично поддерживаются для преобразования в PDF. .

|**Элемент документа**|**Атрибут**|**Поддерживается**|**Примечания**|
| :- | :- | :- | :- |
|Выравнивание| |Да| |
|Настройки фона| |Да| |
|Граница|Цвет|Да| |
|Граница|Стиль линии|Да| |
|Граница|Ширина линии|Да| |
|Cell Данные| |Да| |
|Комментарии| |Да| |
|Условное форматирование| |Да| |
|Свойства документа| |Да| |
|Рисование объектов| |Частично|Тени и трехмерные эффекты для рисованных объектов поддерживаются недостаточно хорошо; WordArt и SmartArt поддерживаются частично.|
|Шрифт|Размер|Да| |
|Шрифт|Цвет|Да| |
|Шрифт|Стиль|Да| |
|Шрифт|Подчеркнуть|Да| |
|Шрифт|Последствия|Да||
|Изображений| |Да| |
|Гиперссылка| |Да| |
|Графики| |Частично|MapChart не поддерживается.|
|Объединен Cells| |Да| |
|Разрыв страницы| |Да| |
|Настройка страницы|Верхний/нижний колонтитул|Да| |
|Настройка страницы|Поля|Да| |
|Настройка страницы|Ориентация страницы|Да| |
|Настройка страницы|Размер страницы|Да| |
|Настройка страницы|Область печати|Да| |
|Настройка страницы|Печать заголовков|Да| |
|Настройка страницы|Масштабирование|Да| |
|Высота строки/ширина столбца| |Да| |
|Язык RTL (справа налево)| |Да| |

{{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** непосредственно перед преобразованием таблицы в формат PDF. Это обеспечит перерасчет зависимых от формулы значений и отображение правильных значений в PDF.

{{% /alert %}}

##  **Предварительные темы**
- [Добавить PDF В закладки](/cells/ru/net/add-pdf-bookmarks/)
- [Добавьте PDF закладки с именованными пунктами назначения.](/cells/ru/net/add-pdf-bookmarks-with-named-destinations/)
- [Избегайте пустой страницы в выводе PDF, когда нечего печатать](/cells/ru/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Измените шрифт только для определенных символов Юникода, сохранив его в PDF.](/cells/ru/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Управляйте загрузкой внешних ресурсов в книге MS Excel при рендеринге по номеру PDF.](/cells/ru/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Преобразование файла XLSX в формат PDF](/cells/ru/net/convert-xlsx-file-to-pdf-format/)
- [Конвертировать файл Excel в формат PDF, совместимый с PDFA-1a.](/cells/ru/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в PDF](/cells/ru/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создать PdfBookmarkEntry для листа диаграммы](/cells/ru/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Поместить все столбцы рабочего листа на одну страницу PDF](/cells/ru/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получите DrawObject и Bound при рендеринге до PDF, используя класс DrawObjectEventHandler.](/cells/ru/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получайте предупреждения о замене шрифта при рендеринге файла Excel](/cells/ru/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при рендеринге Excel по номеру PDF](/cells/ru/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничить количество создаваемых страниц — преобразование Excel до PDF](/cells/ru/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Распечатать комментарии, сохранив номер PDF.](/cells/ru/net/print-comments-while-saving-to-pdf/)
- [Отображение надстроек Office при преобразовании Excel в PDF](/cells/ru/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Рендеринг одной страницы PDF на лист Excel — преобразование Excel в PDF](/cells/ru/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отображение дополнительных символов Юникода в выводе PDF по Aspose.Cells](/cells/ru/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Повторная выборка добавленных изображений — преобразование Excel в PDF](/cells/ru/net/resampling-added-images-excel-to-pdf-conversion/)
- [Сохраните каждый рабочий лист в отдельный файл PDF.](/cells/ru/net/save-each-worksheet-to-a-different-pdf-file/)
- [Сохраните Excel в PDF со стандартным или минимальным размером.](/cells/ru/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохраните указанные рабочие листы по номеру PDF.](/cells/ru/net/save-specified-worksheets-to-pdf/)
- [Безопасные PDF Документы](/cells/ru/net/secure-pdf-documents/)
- [Укажите, как пересекать строку в выводе PDF и изображении.](/cells/ru/net/specify-how-to-cross-string-in-output-pdf-and-image/)
