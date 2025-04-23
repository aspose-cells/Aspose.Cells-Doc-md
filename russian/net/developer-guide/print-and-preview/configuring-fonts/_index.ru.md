---
title: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Возможные сценарии использования**

API Aspose.Cells предоставляет возможность визуализации электронных таблиц в форматах изображений, а также преобразования их в форматы PDF и XPS. Для максимизации точности преобразования необходимо, чтобы используемые в электронных таблицах шрифты были доступны в системной папке шрифтов операционной системы. В случае отсутствия необходимых шрифтов API Aspose.Cells будет пытаться заменить необходимые шрифты имеющимися.

## **Выбор шрифтов**

Ниже приведен процесс, который API Aspose.Cells следует за кулисами.

1. API пытается найти шрифты на файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если API не может найти шрифты с точно таким же именем, он пытается использовать шрифт по умолчанию, указанный в свойстве [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) книги.
1. Если API не может найти шрифт, определенный в свойстве [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) книги, он пытается использовать шрифт, указанный в свойствах [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) или [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont).
1. Если API не может найти шрифт, определенный в свойствах [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) или [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), он пытается использовать шрифт, указанный в свойстве [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname).
1. Если API не может найти шрифт, определенный в свойстве [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname), он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты на файловой системе, он визуализирует электронную таблицу с использованием шрифта Arial.

{{% alert color="primary" %}}

В целом API Aspose.Cells по умолчанию сканируют каталоги шрифтов операционной системы на Windows, Linux, MacOS. Начиная с [Aspose.Cells for .NET 24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/), API дополнительно сканируют кэшированные шрифты Office в облаке по умолчанию.

{{% /alert %}}

## **Установка пользовательских каталогов шрифтов**

API Aspose.Cells ищут каталог шрифтов по умолчанию операционной системы для необходимых шрифтов. В случае, если требуемые шрифты отсутствуют в каталоге шрифтов системы, API ищут их в пользовательских (определенных пользователем) каталогах. Класс [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) предоставляет ряд способов установки пользовательских каталогов шрифтов, описанных ниже.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Этот метод полезен, если нужно установить только одну папку.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Этот метод полезен, когда шрифты находятся в нескольких папках, и пользователь хочет установить каждую папку отдельно, а не объединить все шрифты в одну папку.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Этот механизм полезен, когда пользователь хочет загружать шрифты из нескольких папок или одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

Оба метода [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) и [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) принимают второй параметр типа Boolean. Передача **true** в качестве второго параметра направит API Aspose.Cells на поиск файлов шрифтов в подпапках.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеперечисленных методов в начале приложения, то есть; перед вызовом любых других объектов API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Если все вышеперечисленные методы используются для установки источников шрифтов, то только последние настройки будут применены.

{{% /alert %}}

## **Механизм подстановки шрифтов**

API Aspose.Cells также предоставляет возможность указать запасной шрифт для целей рендеринга. Этот механизм полезен, когда необходимый шрифт недоступен на машине, где должно происходить преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы исходно требуемому шрифту. Для этого API Aspose.Cells предоставляет метод [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes), который принимает 2 параметра. Первый параметр имеет тип **string** и должен быть именем шрифта, который нужно заменить. Второй параметр является массивом типа **string**. Пользователи могут предоставить список имен шрифтов в замен исходного имени шрифта (указанного в первом параметре).

Вот простой сценарий использования.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Сбор информации**

Кроме вышеупомянутых методов, API Aspose.Cells также предоставляют средства для сбора информации о том, какие источники и замены были установлены.

1. Метод [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) возвращает массив типа [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase), содержащий список указанных источников шрифтов. Если источники не установлены, то метод [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) вернет пустой массив.
1. Метод [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) принимает параметр типа **string**, позволяющий указать имя шрифта, для которого установлена замена. Если для указанного имени шрифта не установлена замена, то метод [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) вернет null.

## **Продвинутые темы**
- [Установите шрифт по умолчанию при отображении электронной таблицы в изображения](/cells/ru/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Установите свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions для приоритета](/cells/ru/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Поддерживаемые форматы шрифтов](/cells/ru/net/supported-font-formats/)
- [Электронная таблица в изображение - установите формат пикселей для визуализированного изображения](/cells/ru/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}
