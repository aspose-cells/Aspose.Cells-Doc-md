---
title: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Возможные сценарии использования**

API Aspose.Cells предоставляет возможность визуализации электронных таблиц в форматах изображений, а также преобразования их в форматы PDF и XPS. Для максимизации точности преобразования необходимо, чтобы используемые в электронных таблицах шрифты были доступны в системной папке шрифтов операционной системы. В случае отсутствия необходимых шрифтов API Aspose.Cells будет пытаться заменить необходимые шрифты имеющимися.

## **Выбор шрифтов**

Ниже приведен процесс, который API Aspose.Cells следует за кулисами.

1. API пытается найти шрифты на файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если API не может найти шрифты с точно таким же именем, он пытается использовать шрифт по умолчанию, указанный в свойстве [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) книги.
1. Если API не может найти шрифт, определенный в свойстве [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) книги, он пытается использовать шрифт, указанный в свойствах [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) или [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont).
1. Если API не может найти шрифт, определенный в свойствах [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) или [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont), он пытается использовать шрифт, указанный в свойстве [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName).
1. Если API не может найти шрифт, определенный в свойстве [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName), он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты на файловой системе, он визуализирует электронную таблицу с использованием шрифта Arial.

{{% alert color="primary" %}}

Обычно API Aspose.Cells сканирует стандартные каталоги шрифтов операционной системы на Windows, Linux, MacOS по умолчанию. Начиная с [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/), API дополнительно сканируют кешированные облачные каталоги шрифтов Office по умолчанию.

{{% /alert %}}

{{% alert color="primary" %}}

API Aspose.Cells всегда сканируют стандартный каталог шрифтов операционной системы, за исключением случая, когда установлены JVM аргументы **-DAspose.Cells.FontDirExc="YourFontDir"**. В этом случае API пропустит сканирование стандартных каталогов и будет искать только по указанному пути, как описано выше.

{{% /alert %}}

## **Установка пользовательских каталогов шрифтов**

API Aspose.Cells ищет каталог шрифтов операционной системы по умолчанию для необходимых шрифтов. В случае отсутствия необходимых шрифтов в каталоге шрифтов системы API выполняет поиск по пользовательским (заданным пользователем) каталогам. Класс [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) предоставляет несколько способов установки пользовательских каталогов шрифтов, описанных ниже.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-): Этот метод полезен, если нужно установить только одну папку.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-): Этот метод полезен, когда шрифты находятся в нескольких папках, и пользователь хочет установить каждую папку отдельно, а не объединить все шрифты в одну папку.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-): Этот механизм полезен, когда пользователь хочет загружать шрифты из нескольких папок или одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

И [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-), и методы [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-) принимают логический второй параметр. Передача **true** вторым параметром направит API Aspose.Cells на поиск файлов шрифтов во вложенных папках.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеупомянутых методов в начале приложения, то есть перед вызовом любых других объектов API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Если для установки источников шрифтов было использовано более одного из вышеупомянутых методов, будут применены только последние настройки.

{{% /alert %}}

## **Механизм подстановки шрифтов**

API Aspose.Cells также обеспечивает возможность указать запасной шрифт для целей рендеринга. Этот механизм полезен, когда необходимый шрифт недоступен на машине, где должно происходить преобразование. Пользователи могут предоставить список названий шрифтов в качестве альтернативы исходно требуемому шрифту. Для этого API Aspose.Cells предоставляют метод setFontSubstitutes, который принимает 2 параметра. Первый параметр имеет тип String, который должен быть именем шрифта, который требуется заменить. Второй параметр - массив типа String. Пользователи могут предоставить список названий шрифтов в качестве заменителей для оригинального шрифта (указанного в первом параметре).

Вот простой сценарий использования.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Сбор информации**

Кроме вышеупомянутых методов, API Aspose.Cells также предоставляют средства для сбора информации о том, какие источники и замены были установлены.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Этот метод возвращает массив типа [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource), содержащий список указанных источников шрифтов. В случае отсутствия установленных источников метод [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) вернет пустой массив.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-): Этот метод принимает параметр типа **String**, позволяя указать имя шрифта, для которого задано замещение. В случае, если для указанного имени шрифта замещение не было установлено, метод [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-) вернет null.
{{< app/cells/assistant language="java" >}}
