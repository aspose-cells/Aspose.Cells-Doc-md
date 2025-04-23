---
title: Конвертировать между форматами Excel
type: docs
weight: 20
url: /ru/net/convert-between-excel-formats/
---

## **Преобразование Excel в PDF**

**PDF**-файлы широко используются для обмена документами между организациями, государственными секторами и отдельными лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы **PDF**.
**Aspose.Cells** поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную отчетливость при преобразовании.

Aspose.Cells for .NET поддерживает преобразование электронных таблиц в PDF независимо от другого программного обеспечения. Сохраните файл Excel в PDF с помощью метода Save класса Workbook. Метод Save предоставляет член перечисления SaveFormat.Pdf, который преобразует исходные файлы Excel в формат PDF.

**Преобразование** непосредственно из электронной таблицы в PDF, а не с использованием стороннего инструмента или внешнего API, имеет несколько **преимуществ**:

1. Прямое преобразование не требует временных файлов, потому что весь процесс может быть выполнен в памяти.
1. Необходим XML-файл, поэтому большие файлы можно легко конвертировать.
1. Скорость конвертации намного выше.

**Для конвертации файлов в формат PDF:**

1. Создайте объект класса **Workbook**, вызвав его пустой конструктор.
1. Можно **открыть/загрузить** существующий шаблонный файл или пропустить этот шаг, если создается книга таблицы с нуля.
1. Выполните необходимую работу (ввод данных, применение форматирования, установка формул, вставка изображений или других объектов рисования и т. д.) на электронной таблице с помощью API Aspose.Cells.
1. Когда код электронной таблицы завершен, вызовите **метод Save класса Workbook** для сохранения электронной таблицы. Формат файла должен быть PDF, поэтому выберите Pdf (заранее определенное значение) из перечисления SaveFormat для генерации итогового PDF-документа.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Конвертация Excel в MHTML**

**MHTML** объединяет обычный HTML с внешними ресурсами (например, содержимое, обычно связанное, такие как изображения, анимации, аудио и т. д.) в один файл. Они используются для электронных писем с расширением файлов .mht.
Aspose.Cells поддерживает чтение и запись файлов MHTML.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Преобразование Excel в XPS**

Иногда вам нужно преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.), по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного листа.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Загрузить образец кода**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
