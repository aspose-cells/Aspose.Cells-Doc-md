---
title: Как запустить Aspose.Cells в Blazor
type: docs
weight: 138
url: /ru/net/how-to-run-aspose-cells-in-blazor/
description: Узнайте, как запустить Aspose.Cells в Blazor.
keywords: C# Run Aspose.Cells in Blazor, Use Aspose.Cells in Blazor
---
##  Обзор

 Чтобы запустить Aspose.Cells в Blazor, вам потребуются платформы .NET6 (или более поздние версии), по сравнению с предыдущими платформами (.netcore31 или более ранние), важное отличие касается графической библиотеки. В этом официальном[Microsoft Документ](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), в нем объясняется, что для выпусков .NET6 или более поздних версий графическая библиотека «System.Drawing.Common» будет поддерживаться только на Windows, и даются рекомендации по замене графической библиотеки.

Для продукта Apose.Cells мы провели оценку и завершили миграцию графической библиотеки. Мы используем SkiaSharp вместо System.Drawing.Common в системах, отличных от Windows, как предложено в официальной документации Microsoft. Обратите внимание, что это критическое изменение вступит в силу в версии Aspose.Cells 22.10.1 или более поздней версии для .Net6.

##  Первое приложение Blazor с номером Aspose.Cells

В этом примере вы создаете простое серверное приложение blazor, которое добавляет некоторые данные и графику и преобразует их в изображения для отображения на веб-странице. В процессе создания проекта вы можете настроить параметры в соответствии со своими потребностями. Например, если вы установите флажок «Включить Docker», приложение blazor можно будет собрать и запустить в Docker.

###  Создайте первое приложение Blazor

Давайте воспользуемся инструментом VS2022 в качестве примера, чтобы создать первое приложение blazor с номером Aspose.Cells, выполните следующие действия:
1. Выберите «Файл» -> «Новый» -> «Проект» и отфильтруйте его, используя ключевое слово blazer, чтобы выбрать соответствующий шаблон проекта.
<br>
<img src="1.png" width=70% />
1. Задайте имя проекта «BlazorTest» и выберите путь.
<br>
<img src="2.png" width=70% />
1. Настройте библиотеки и другие параметры, используемые в проекте. Наконец, нажмите кнопку «Создать», чтобы создать свой первый проект блейзера.
<br>
<img src="3.png" width=70% />
1. После входа в проект нажмите «Зависимости» под проектом и выберите «Управление пакетами NuGet...», чтобы добавить библиотеку Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. Введите ключевые слова для фильтрации и установите последнюю версию библиотеки Aspose.Cells. Одновременно будут установлены зависимые библиотеки, такие как SkiaSharp.
<br>
<img src="5.png" width=70% />
1. Дважды щелкните файл «Index.razor», чтобы отредактировать и импортировать необходимую библиотеку. Добавьте некоторые данные и графику и преобразуйте их в графику для отображения.
<br>
<img src="5.png" width=70% />
1. Скомпилируйте и запустите проект, и вы получите следующие результаты.
<br>
<img src="7.png" width=70% />

###  Пример кода в первом приложении Blazor

Следующий пример кода включен в файл Index.razor:
```
@page "/"
@using SkiaSharp;
@using Aspose.Cells;
@using Aspose.Cells.Drawing;
@using Aspose.Cells.Rendering;


<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />

<img src="@imageSrc" />

@code
{
    private string imageSrc;

    public Index()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "test data for blazor";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}

```