---
title: Преобразование Листа в изображение с использованием параметров ImageOrPrint
type: docs
weight: 90
url: /ru/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Этот документ разработан для подробного понимания того, как преобразовать лист в файл изображения и применить различные параметры изображения и печати для изображения, такие как разрешение, сжатие TIFF, формат изображения и качество страницы.

{{% /alert %}}

## **Сохранение листов в изображения - различные подходы**

Иногда нужно представить свои листы в виде изображений. Вы можете вставлять изображения листов в ваши приложения или веб-страницы. Можно вставить изображения в документ Word, PDF, презентацию PowerPoint или использовать в других сценариях. Просто, вы хотите, чтобы лист был отображен как изображение для использования в другом месте. API Aspose.Cells for Python via .NET поддерживает преобразование листов Excel в изображения. Также, API поддерживает настройку различных параметров, таких как формат изображения, разрешение (по вертикали и горизонтали), качество изображения и другие настройки изображений и печати.

Вы можете попробовать автоматизацию Office, но у автоматизации Office есть свои недостатки. Существует несколько причин и проблем: например, безопасность, стабильность, масштабируемость и скорость, цена и функции. Короче говоря, есть множество причин, причем основной причиной является то, что сама Microsoft настоятельно рекомендует отказаться от использования автоматизации Office в программных решениях.

Эта статья показывает, как создать консольное приложение в Visual Studio .NET, выполнить преобразование листа в изображение с использованием различных параметров изображения и печати за несколько простых строк кода с помощью API Aspose.Cells for Python via .NET.

Вам нужно импортировать пространство имен [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) в вашу программу / проект. В нем есть несколько ценных классов, например, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) и т. Д.

Класс [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) представляет собой лист, который генерирует изображения для листа, у него есть перегруженный метод [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), который может непосредственно преобразовать лист в файл изображения с заданными вами атрибутами или параметрами. Он может возвращать объект System.Drawing.Bitmap, и вы можете сохранить файл изображения на диск/поток. Поддерживаются различные форматы изображений, например, BMP, PNG, GIFF, JPEG, TIFF, EMF и т. Д.

## **Использование Aspose.Cells для преобразования листа в изображение с помощью параметров ImageOrPrint**

### **Создание шаблонной книги в Microsoft Excel**

Я создал новую книгу в MS Excel и добавил некоторые данные на первый лист. Теперь я преобразую лист шаблона файла "Лист1" в файл изображения "SheetImage.tiff" и применю различные параметры изображения, такие как горизонтальное и вертикальное разрешение, сжатие Tiff и т. Д.

### **Преобразовать лист в файл изображения**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **Конвертация изображения с помощью WorkbookRender**

TIFF-изображение может содержать более одного кадра. Вы можете сохранить всю книгу в одно TIFF-изображение с несколькими кадрами или страницами:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

