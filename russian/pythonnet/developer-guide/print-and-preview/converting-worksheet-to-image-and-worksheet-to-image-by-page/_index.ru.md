---
title: Преобразование листа в изображение и Лист в изображение по странице
type: docs
weight: 80
url: /ru/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Этот документ предназначен для предоставления разработчикам подробного понимания того, как преобразовать лист в файл изображения и лист с несколькими страницами в файл изображения на страницу.

Иногда требуется показывать листы как изображения, например, для использования в приложениях или веб-страницах. Можно вставить изображения в документ Word, PDF, презентацию PowerPoint или использовать в других сценариях. Просто, вы хотите представить лист как изображение. API Aspose.Cells for Python via .NET поддерживает преобразование листов в файлах Excel в изображения. Также, API Aspose.Cells for Python via .NET поддерживает преобразование рабочей книги в несколько изображений, по одному на страницу.

Вы можете использовать автоматизацию Office для достижения этой цели, но у автоматизации Office есть свои недостатки. Существует несколько причин и проблем, например, безопасность, стабильность, масштабируемость/скорость, цена и функции. Короче говоря, есть много причин, но основная заключается в том, что сама компания Microsoft настоятельно рекомендует отказаться от автоматизации Office.

{{% /alert %}}

## **Использование Aspose.Cells для преобразования листа в файл изображения**

В этой статье показано, как создать консольное приложение в Visual Studio, преобразовать лист в изображение и преобразовать лист в одно изображение для каждого листа с помощью нескольких и простых строк кода, используя API Aspose.Cells for Python via .NET.

Вам нужно импортировать пространство имен [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) в вашу программу/проект. Оно имеет несколько ценных классов, таких как [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), и так далее. Класс [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) представляет рабочий лист для отображения изображений для рабочего листа и имеет перегруженный метод [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), который может преобразовать рабочий лист в файлы изображений напрямую с любыми установленными атрибутами или опциями. Он может возвращать объект System.Drawing.Bitmap, и вы можете сохранить файл изображения на диск/поток. Поддерживаются несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF и другие.

В этой статье объясняется, как конвертировать лист в изображение. Эта задача показывает, как использовать Aspose.Cells for Python via .NET для преобразования листа из шаблонной рабочей книги в файл изображение.


### **Преобразовать рабочий лист в файл изображения**

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook.xlsx** (1 рабочий лист). Затем преобразуйте рабочий лист шаблона в файл изображения под названием SheetImage.jpg.

Ниже приведен используемый компонентом код для выполнения этой задачи. Он преобразует Sheet1 в **Testbook.xlsx** в файл изображения, чтобы показать, насколько легко осуществляется это преобразование.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Использование Aspose.Cells для преобразования листа в изображение по страницам**

Этот пример показывает, как использовать Aspose.Cells for Python via .NET для преобразования листа из шаблонной рабочей книги с несколькими страницами в один файл изображения на страницу.

### **Преобразовать рабочий лист в изображение по страницам**

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook2.xlsx** (1 рабочий лист).

Теперь преобразуйте рабочий лист шаблона Sheet1 в файлы изображений (по одному файлу на страницу). Поскольку я уже создал консольное приложение для выполнения этой задачи, я пропущу шаги создания этого консольного приложения и перейду непосредственно к шагам преобразования рабочего листа.

Ниже приведенный код используется компонентом для выполнения этой задачи. Он преобразует Лист1 в файле Testbook2.xls в изображения по страницам.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

