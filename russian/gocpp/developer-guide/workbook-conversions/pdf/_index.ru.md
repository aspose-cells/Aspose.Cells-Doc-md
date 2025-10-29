---
title: Преобразование Excel в PDF с помощью Golang через C++
linktitle: Преобразование Excel в PDF
type: docs
weight: 220
url: /ru/go-cpp/convert-excel-to-pdf/
description: Узнайте, как преобразовать рабочие книги Excel в формат PDF с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование рабочих книг Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.

{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными структурами и отдельными лицами. Это стандартный формат документа, и разработчикам часто требуется найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}}

Aspose.Cells for C++ напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF, Aspose.Cells for C++ заполняет поле **Производитель PDF** значением, например 'Aspose.Cells v23.2'.

Обратите внимание, что вы можете изменить эту информацию в выходных документах, используя свойство [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **Прямое преобразование**

Aspose.Cells for C++ поддерживает преобразование из таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF, используя метод [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) класса [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/). Метод [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) предоставляет член перечисления [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/), который преобразует нативные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), вызвав его конструктор без параметров.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните работу (ввод данных, применение форматирования, установка формул, вставка изображений или других графических объектов и т.д.) на листе, используя API Aspose.Cells.
1. Когда код для листа завершен, вызовите метод [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) класса [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) для сохранения листа.

Формат файла должен быть PDF, поэтому выберите *Pdf* (предопределенное значение) из перечисления [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/), чтобы сгенерировать итоговый PDF документ.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf.go" >}}
### **Расширенное преобразование**

Также вы можете использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) для установки различных атрибутов преобразования. Настройка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) позволяет контролировать параметры печати, шрифта, безопасности и сжатия для выходного PDF.

Самое важное свойство — это [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), которое позволяет установить уровень соответствия стандартам PDF. В настоящее время можно сохранять в PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u. Обратите внимание, что при использовании формата PDF/A размер итогового файла больше, чем у обычного PDF.

#### **Сохранение книги в формате PDF/A**

Ниже приведен пример кода, демонстрирующий, как использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) для сохранения файлов Excel в PDF/A-совместимый формат PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-1.go" >}}
{{% alert color="primary" %}}

Обратите внимание, свойство [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) было добавлено с выпуском Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Установить время создания PDF**

С классом [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) вы можете получать или устанавливать время создания PDF. Следующий код демонстрирует использование свойства [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcreatedtime/) для установки времени создания файла PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-2.go" >}}
#### **Установите опцию ContentCopyForAccessibility**

С классом [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) вы можете получать или устанавливать опцию [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) PDF для контроля доступа к содержимому в преобразованном PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-3.go" >}}
#### **Экспорт пользовательских свойств в PDF**

С классом [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) вы можете экспортировать пользовательские свойства исходной книги в PDF. Для указания способа экспорта свойств предоставляется перечислитель [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/). Эти свойства можно просматривать в Adobe Acrobat Reader, нажав файл и выбрав свойства, как показано на следующем изображении. Шаблон файла «sourceWithCustProps.xlsx» можно скачать [здесь](sourceWithCustProps.xlsx) для тестирования, а выходной PDF-файл «outSourceWithCustProps» доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-4.go" >}}
### **Атрибуты преобразования**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Excel в PDF с помощью Aspose.Cells все еще имеет некоторые ограничения. MapChart не поддерживается при конвертации в формат PDF. Также некоторые объекты рисования не поддерживаются хорошо.

Следующая таблица перечисляет все функции, которые полностью или частично поддерживаются при экспорте в PDF с использованием Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты таблицы, но выявляет те функции, которые не поддерживаются или частично поддерживаются при конвертации в PDF.

| **Элемент документа** | **Атрибут** | **Поддерживается** | **Примечания** |
| :- | :- | :- | :- |
| Выравнивание |  | Да |  |
| Настройки фона |  | Да |  |
| Граница | Цвет | Да |  |
| Граница | Стиль линии | Да |  |
| Граница | Толщина линии | Да |  |
| Данные ячейки |  | Да |  |
| Комментарии |  | Да |  |
| Условное форматирование |  | Да |  |
| Свойства документа |  | Да |  |
| Объекты рисования |  | Частично | Тени и 3D-эффекты для объектов рисования не поддерживаются хорошо; WordArt и SmartArt частично поддерживаются. |
| Шрифт | Размер | Да |  |
| Шрифт | Цвет | Да |  |
| Шрифт | Стиль | Да |  |
| Шрифт | Подчеркивание | Да |  |
| Шрифт | Эффекты | Да |  |
| Изображения |  | Да |  |
| Гиперссылка |  | Да |  |
| Диаграммы |  | Частично | MapChart не поддерживается. |
| Объединенные ячейки |  | Да |  |
| Разрыв страницы |  | Да |  |
| Настройка страницы | Верхний/нижний колонтитул | Да |  |
| Настройка страницы | Поля | Да |  |
| Настройка страницы | Ориентация страницы | Да |  |
| Настройка страницы | Размер страницы | Да |  |
| Настройка страницы | Область печати | Да |  |
| Настройка страницы | Заголовки печати | Да |  |
| Настройка страницы | Масштабирование | Да |  |
| Высота строки/ширина столбца |  | Да |  |
| Связь с RTL (слева направо) языком |  | Да |  |

{{% alert color="primary" %}}

Если в вашей таблице есть формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) перед преобразованием таблицы в PDF. Это обеспечит перерасчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}

## **Продвинутые темы**
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Изменить шрифт только для определенных символов Unicode при сохранении в формате PDF](/cells/ru/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Преобразовать файл XLSX в формат PDF](/cells/ru/cpp/convert-xlsx-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в формат PDF](/cells/ru/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создание PdfBookmarkEntry для листа с диаграммой](/cells/ru/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Заполнить все столбцы листа Excel на одной странице PDF](/cells/ru/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler](/cells/ru/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получить предупреждения о замене шрифта при преобразовании файла Excel](/cells/ru/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при преобразовании Excel в PDF](/cells/ru/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества создаваемых страниц - Преобразование Excel в PDF](/cells/ru/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в формат PDF](/cells/ru/cpp/print-comments-while-saving-to-pdf/)
- [Рендеринг офисных надстроек при преобразовании Excel в PDF](/cells/ru/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Отображать одну страницу PDF для каждого листа Excel - Преобразование Excel в PDF](/cells/ru/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells](/cells/ru/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Добавление изображений с изменением размера - Преобразование Excel в PDF](/cells/ru/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Сохранить каждый лист в отдельный файл PDF](/cells/ru/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF с обычным или минимальным размером](/cells/ru/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохранить указанные листы в формат PDF](/cells/ru/cpp/save-specified-worksheets-to-pdf/)
- [Защищенные документы в формате PDF](/cells/ru/cpp/secure-pdf-documents/)
- [Указание способа пересечения строк в выходном PDF и изображении](/cells/ru/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
