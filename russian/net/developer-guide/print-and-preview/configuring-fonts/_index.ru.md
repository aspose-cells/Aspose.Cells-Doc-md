---
title: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Возможные сценарии использования**

API-интерфейсы Aspose.Cells позволяют отображать электронные таблицы в форматах изображений, а также преобразовывать их в форматы PDF и XPS. Чтобы максимизировать точность преобразования, необходимо, чтобы шрифты, используемые в электронной таблице, были доступны в каталоге шрифтов операционной системы по умолчанию. Если необходимые шрифты отсутствуют, API-интерфейсы Aspose.Cells попытаются заменить требуемые шрифты доступными.

## **Выбор шрифтов**

Ниже показан процесс, которому Aspose.Cells API следуют за сценой.

1. API пытается найти шрифты в файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1.  Если API не может найти шрифты с точно такими же именами, он пытается использовать шрифт по умолчанию, указанный в рабочей книге.**[DefaultStyle.Font] (https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** имущество.
1.  Если API не может найти шрифт, определенный в рабочей книге**[DefaultStyle.Font] (https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** свойство, он пытается использовать шрифт, указанный в**[PdfSaveOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** или же**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** имущество.
1.  Если API не может найти шрифт, определенный в**[PdfSaveOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** или же**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** свойство, он пытается использовать шрифт, указанный в**[FontConfigs.DefaultFontName] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** имущество.
1.  Если API не может найти шрифт, определенный в**[FontConfigs.DefaultFontName] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** свойство, он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты в файловой системе, он отображает электронную таблицу с использованием Arial.

## **Установить папки пользовательских шрифтов**

 Aspose.Cells API-интерфейсы выполняют поиск требуемых шрифтов в каталоге шрифтов операционной системы по умолчанию. Если требуемые шрифты недоступны в системном каталоге шрифтов, API-интерфейсы выполняют поиск в пользовательских (определяемых пользователем) каталогах.**[Конфигурации шрифтов] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**class предоставил несколько способов установки пользовательских каталогов шрифтов, как описано ниже.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: этот метод удобен, если необходимо установить только одну папку.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: этот метод удобен, когда шрифты находятся в нескольких папках, и пользователь хочет установить все папки по отдельности, а не объединять все шрифты в одной папке.
1. **[FontConfigs.SetFontSources] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: этот механизм полезен, когда пользователь хочет загрузить шрифты из нескольких папок или из одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

 Обе**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** методы принимают второй параметр логического типа. Прохождение**истинный** поскольку второй параметр будет указывать API Aspose.Cells для поиска файлов шрифтов во вложенных папках.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеупомянутых методов при запуске приложения, то есть; перед вызовом любых других объектов Aspose.Cells API.

{{% /alert %}} {{% alert color="primary" %}}

Если для установки источников шрифта используются все вышеперечисленные методы, вступят в силу только последние настройки.

{{% /alert %}}

## **Механизм замены шрифта**

 Aspose.Cells API-интерфейсы также предоставляют возможность указать замещающий шрифт для целей рендеринга. Этот механизм удобен, когда требуемый шрифт недоступен на машине, на которой должно выполняться преобразование. Пользователи могут предоставить список имен шрифтов в качестве альтернативы первоначально необходимому шрифту. Для этого API Aspose.Cells предоставили**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** метод, который принимает 2 параметра. Первый параметр имеет тип**нить** , которое должно быть названием шрифта, который необходимо заменить. Второй параметр представляет собой массив типа**нить**Пользователи могут предоставить список имен шрифтов в качестве замены исходного имени шрифта (указывается в первом параметре).

Вот простой сценарий использования.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Сбор информации**

В дополнение к вышеупомянутым методам API-интерфейсы Aspose.Cells также предоставляют средства для сбора информации о том, какие источники и замены были установлены.

1. **[FontConfigs.GetFontSources] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** метод возвращает массив типа**[FontSourceBase] (https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**содержащий список указанных источников шрифтов. В случае, если источники не были установлены,**[FontConfigs.GetFontSources] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**метод вернет пустой массив.
1. **[FontConfigs.GetFontSubstitutes] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** метод принимает параметр типа**нить** позволяет указать имя шрифта, для которого установлена замена. В случае, если для указанного имени шрифта не была установлена замена, то**[FontConfigs.GetFontSubstitutes] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**метод вернет ноль.

## **Предварительные темы**
- [Установить шрифт по умолчанию при рендеринге электронной таблицы в изображения](/cells/ru/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Установите свойство DefaultFont PdfSaveOptions и ImageOrPrintOptions, чтобы иметь приоритет](/cells/ru/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Поддерживаемые форматы шрифтов](/cells/ru/net/supported-font-formats/)
- [Рабочий лист в изображение - установите формат пикселей для визуализированного изображения](/cells/ru/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
