---
title: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Возможные сценарии использования**

API-интерфейсы Aspose.Cells позволяют отображать электронные таблицы в форматах изображений, а также преобразовывать их в форматы PDF и XPS. Чтобы максимизировать точность преобразования, необходимо, чтобы шрифты, используемые в электронной таблице, были доступны в каталоге шрифтов операционной системы по умолчанию. Если необходимые шрифты отсутствуют, API-интерфейсы Aspose.Cells попытаются заменить требуемые шрифты доступными.

## **Выбор шрифтов**

Ниже показан процесс, которому Aspose.Cells API следуют за сценой.

1. API пытается найти шрифты в файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1.  Если API не может найти шрифты с точно такими же именами, он пытается использовать шрифт по умолчанию, указанный в рабочей книге.[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) имущество.
1.  Если API не может найти шрифт, определенный в рабочей книге[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) свойство, он пытается использовать шрифт, указанный в[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) или же[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) имущество.
1.  Если API не может найти шрифт, определенный в[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) или же[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) свойство, он пытается использовать шрифт, указанный в[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) имущество.
1.  Если API не может найти шрифт, определенный в[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) свойство, он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты в файловой системе, он отображает электронную таблицу с использованием Arial.

{{% alert color="primary" %}}

 API-интерфейсы Aspose.Cells всегда сканируют каталог шрифтов операционной системы по умолчанию, за одним исключением: когда аргументы JVM**-DAspose.Cells.FontDirExc="ВашКаталогШрифта"**установлены. В этом случае API-интерфейсы Aspose.Cells пропустят сканирование каталога шрифтов операционной системы по умолчанию и будут искать только путь, указанный в вышеупомянутых аргументах JVM.

{{% /alert %}}

## **Установить папки пользовательских шрифтов**

 Aspose.Cells API-интерфейсы выполняют поиск требуемых шрифтов в каталоге шрифтов операционной системы по умолчанию. Если требуемые шрифты недоступны в системном каталоге шрифтов, API-интерфейсы выполняют поиск в пользовательских (определяемых пользователем) каталогах.[**Конфигурации шрифтов**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)class предоставил несколько способов установки пользовательских каталогов шрифтов, как описано ниже.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): Этот метод удобен, если необходимо установить только одну папку.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): этот метод удобен, когда шрифты находятся в нескольких папках, и пользователь хочет установить все папки по отдельности, а не объединять все шрифты в одной папке.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): этот механизм полезен, когда пользователь хочет загрузить шрифты из нескольких папок или одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

 Обе[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) методы принимают второй параметр логического типа. Прохождение**истинный**в качестве второго параметра направит API Aspose.Cells на поиск файлов шрифтов во вложенных папках.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеупомянутых методов при запуске приложения, то есть; перед вызовом любых других объектов Aspose.Cells API.

{{% /alert %}} {{% alert color="primary" %}}

Если для установки источников шрифта используется более одного из вышеупомянутых методов, вступят в силу только последние настройки.

{{% /alert %}}

## **Механизм замены шрифта**

Aspose.Cells API-интерфейсы также предоставляют возможность указать замещающий шрифт для целей рендеринга. Этот механизм удобен, когда требуемый шрифт недоступен на машине, на которой должно выполняться преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы первоначально необходимому шрифту. Для этого API-интерфейсы Aspose.Cells предоставили метод FontConfigs.setFontSubstitutes, который принимает 2 параметра. Первый параметр имеет тип**Нить** , которое должно быть названием шрифта, который необходимо заменить. Второй параметр представляет собой массив типа**Нить**. Пользователи могут предоставить список имен шрифтов в качестве заменителей исходного шрифта (указанного в первом параметре).

Вот простой сценарий использования.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Сбор информации**

В дополнение к вышеупомянутым методам API-интерфейсы Aspose.Cells также предоставляют средства для сбора информации о том, какие источники и замены были установлены.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): Этот метод возвращает массив типа[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)содержащий список указанных источников шрифтов. В случае, если источники не были установлены,[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) вернет пустой массив.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): этот метод принимает параметр типа**Нить** позволяет указать имя шрифта, для которого установлена замена. В случае, если для указанного имени шрифта не была установлена замена, то[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) метод вернет null.
