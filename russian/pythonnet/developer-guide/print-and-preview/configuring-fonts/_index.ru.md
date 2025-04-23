---
title: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Возможные сценарии использования**

API Aspose.Cells для Python via .NET обеспечивает возможность отображения таблиц в графических форматах, а также их преобразование в PDF и XPS. Для максимального качества преобразования необходимо, чтобы шрифты, используемые в таблице, были доступны в стандартной директории шрифтов операционной системы. В случае отсутствия необходимых шрифтов, API Aspose.Cells для Python via .NET попытается заменить их доступными шрифтами.

## **Выбор шрифтов**

Ниже приведён процесс, который API Aspose.Cells для Python via .NET выполняет за кулисами.

1. API пытается найти шрифты на файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если API не может найти шрифты с точно таким же именем, он пытается использовать шрифт по умолчанию, указанный в свойстве [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) книги.
1. Если API не может найти шрифт, определенный в свойстве [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) книги, он пытается использовать шрифт, указанный в свойствах [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) или [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font).
1. Если API не может найти шрифт, определенный в свойствах [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) или [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), он пытается использовать шрифт, указанный в свойстве [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name).
1. Если API не может найти шрифт, определенный в свойстве [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name), он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты на файловой системе, он визуализирует электронную таблицу с использованием шрифта Arial.

## **Установка пользовательских каталогов шрифтов**

API Aspose.Cells для Python via .NET ищет необходимые шрифты в стандартной директории шрифтов операционной системы. Если нужных шрифтов нет, они ищутся по пользовательским папкам. Класс [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) предоставляет различные способы настройки пользовательских директорий шрифтов, подробно описанные ниже.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Этот метод полезен, если нужно установить только одну папку.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Этот метод полезен, когда шрифты находятся в нескольких папках, и пользователь хочет установить каждую папку отдельно, а не объединить все шрифты в одну папку.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Этот механизм полезен, когда пользователь хочет загружать шрифты из нескольких папок или одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

Оба метода [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) и [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) принимают второй параметр типа Boolean. Передача **true** в качестве второго параметра направит API Aspose.Cells для Python via .NET искать шрифты во вложенных папках.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеупомянутых методов в начале приложения, то есть до вызова любых других объектов Aspose.Cells for Python via .NET API.

{{% /alert %}} {{% alert color="primary" %}}

Если все вышеперечисленные методы используются для установки источников шрифтов, то только последние настройки будут применены.

{{% /alert %}}

## **Механизм подстановки шрифтов**

API Aspose.Cells for Python via .NET также предоставляет возможность указать заменяющий шрифт для целей отображения. Этот механизм полезен, когда необходимый шрифт недоступен на машине, на которой происходит преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы исходному шрифту. Для этого API Aspose.Cells for Python via .NET предоставляет метод [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list), который принимает 2 параметра. Первый параметр — это строка **string**, которая должна содержать название шрифта, который нужно заменить. Второй параметр — массив строк **string**. Пользователи могут указать список имен шрифтов в качестве замены исходному шрифту (указанному в первом параметре).

Вот простой сценарий использования.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Сбор информации**

В дополнение к вышеупомянутым методам, API Aspose.Cells for Python via .NET также предоставляет средства для сбора информации о том, какие источники и замены были установлены.

1. Метод [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) возвращает массив типа [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase), содержащий список указанных источников шрифтов. Если источники не установлены, то метод [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) вернет пустой массив.
1. Метод [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) принимает параметр типа **string**, позволяющий указать имя шрифта, для которого установлена замена. Если для указанного имени шрифта не установлена замена, то метод [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) вернет null.

## **Продвинутые темы**
- [Установите шрифт по умолчанию при отображении электронной таблицы в изображения](/cells/ru/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Установите свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions для приоритета](/cells/ru/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Поддерживаемые форматы шрифтов](/cells/ru/python-net/supported-font-formats/)
- [Электронная таблица в изображение - установите формат пикселей для визуализированного изображения](/cells/ru/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

