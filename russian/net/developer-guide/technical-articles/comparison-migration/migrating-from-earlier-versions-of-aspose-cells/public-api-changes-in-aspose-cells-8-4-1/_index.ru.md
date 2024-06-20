---
title: Изменения в публичном API в Aspose.Cells 8.4.1
type: docs
weight: 140
url: /ru/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.4.0 до 8.4.1, которые могут быть интересны разработчикам модулей / приложений. Он включает не только новые и обновленные публичные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-1/), а также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Механизм модификации подключения к базе данных**
Класс Aspose.Cells.ExternalConnections.ExternalConnection уже содержал методы и свойства, которые можно использовать для проверки деталей подключения к базе данных, сохраненных в электронных таблицах. Большинство свойств, связанных с классом Aspose.Cells.ExternalConnections.ExternalConnection, были доступны только для чтения до релиза Aspose.Cells for .NET 8.4.1. С этим релизом API предоставило поддержку изменения настроек подключения к базе данных.

Ниже приведен фрагмент кода, показывающий, как динамически изменить настройки подключения к базе данных.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



Вот несколько наиболее важных свойств, предоставленных классом {Aspose.Cells.ExternalConnections.ExternalConnection}.

|**Имя свойства**|**Описание**|
| :- | :- |
|BackgroundRefresh|Указывает, может ли происходить обновление подключения в фоновом режиме (асинхронно). <br>true, если предпочтительное использование соединения - асинхронное обновление в фоновом режиме; <br>false, если предпочтительное использование соединения - синхронное обновление на переднем плане.|
|ConnectionDescription|Указывает описание пользователя для этого соединения|
|ConnectionId|Указывает уникальный идентификатор этого соединения.|
|Credentials|Указывает метод аутентификации, который будет использоваться при установлении (или повторном установлении) соединения.|
|IsDeleted|Указывает, было ли удалено связанное подключение к книге Excel. true, если<br>подключение было удалено; в противном случае, false.
|IsNew|True, если подключение еще не было обновлено впервые; в противном случае, false. Это <br>состояние может возникнуть, когда пользователь сохраняет файл до завершения выполнения запроса.
|KeepAlive|True, когда приложение для работы с электронными таблицами должно прилагать усилия для поддержания открытого подключения. Когда false, приложение должно закрыть подключение после получения информации.
|Name|Указывает имя подключения. Каждое подключение должно иметь уникальное имя.
|OdcFile|Указывает полный путь к внешнему файлу подключения, из которого было создано это подключение. Если подключение не удается во время попытки обновления данных, и reconnectionMethod=1, <br>то приложение для работы с электронными таблицами попытается снова использовать информацию из внешнего файла подключения вместо объекта подключения, встроенного в книге Excel.
|OnlyUseConnectionFile|Указывает, должно ли приложение для работы с электронными таблицами всегда и только использовать информацию о подключении во внешнем файле подключения, указанном в атрибуте odcFile при <br>обновлении подключения. Если false, то приложение для работы с электронными таблицами <br>должно следовать процедуре, указанной в атрибуте reconnectionMethod.
|Parameters|Получает ConnectionParameterCollection для ODBC или веб-запроса.
|ReConnectionMethod|Указывает тип reconnectionMethod.
|RefreshInternal|Указывает количество минут между автоматическими обновлениями подключения.
|RefreshOnLoad|True, если это подключение должно быть обновлено при открытии файла; в противном случае, false.
|SaveData|True, если внешние данные, полученные через подключение для заполнения таблицы, должны быть сохранены<br>вместе с книгой Excel; в противном случае, false.
|SavePassword|True, если пароль должен быть сохранен в виде части строки подключения; в противном случае, false.
|SourceFile|Используется, когда внешний источник данных является файловым. Когда подключение к такому источнику данных не выполняется, приложение для работы с электронными таблицами пытается подключиться непосредственно к этому файлу. Может быть <br>выражен в URI или системно-специфической нотации пути к файлу.
|SSOId|Идентификатор для единого входа в систему (SSO), используемый для аутентификации между промежуточным сервером <br>для работы с электронными таблицами и внешним источником данных.
|Type|Указывает тип источника данных.

### **Возможность форматировать подстроку текста DataLabels**
Aspose.Cells for .NET 8.4.1 предоставляет метод DataLabels.Characters для получения экземпляра класса FontSetting, соответствующего подстроке DataLabels точек диаграммы. В свою очередь, экземпляр класса FontSetting можно использовать для форматирования подстроки DataLabels с различными настройками шрифта и цвета.

В следующем фрагменте кода показано, как использовать метод DataLabels.Characters.

**C#**

{{< highlight csharp >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Возможность установить желаемые размеры изображения для экспорта электронных таблиц и диаграмм**
Aspose.Cells for .NET 8.4.1 предоставляет метод SetDesiredSize класса ImageOrPrintOptions для установки размеров результирующего изображения при экспорте электронных таблиц и диаграмм в изображения. Метод SetDesiredSize класса ImageOrPrintOptions принимает два параметра типа integer, где первый - желаемая ширина, а второй - желаемая высота.

Приведенный ниже фрагмент кода показывает, как установить желаемые размеры при экспорте рабочего листа в формат PNG.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Та же характеристика также может использоваться для преобразования диаграмм в изображения.

{{% /alert %}} 


### **Отображение комментариев в формат PDF**
С выпуском v8.4.1 API Aspose.Cells предоставил свойство PageSetup.PrintComments и перечисление PrintCommentsType для облегчения отображения комментариев при преобразовании электронных таблиц в формат PDF. В перечислении PrintCommentsType есть следующие константы.

- PrintCommentsType.PrintNoComments: Комментарии не воспроизводятся.
- PrintCommentsType.PrintInPlace: Комментарии воспроизводятся в их местоположении.
- PrintCommentsType.PrintSheetEnd: Комментарии воспроизводятся в конце листа.

Следующий образец кода демонстрирует использование свойства PageSetup.PrintComments для отображения комментариев с использованием всех возможных значений перечисления PrintCommentsType.

**C#**

{{< highlight csharp >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Перемещение листов в Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop предоставляет метод WorksheetCollection.MoveTo, который можно использовать для перемещения листа на указанный индекс. Указанный метод принимает индексы (с нуля) исходного листа и целевого листа в качестве параметров.

Приведенный ниже образец кода демонстрирует использование свойства WorksheetCollection.MoveTo.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Добавлено свойство Workbook.IsLicensed**
Aspose.Cells for .NET 8.4.1 предоставил свойство Workbook.IsLicensed, которое может быть очень полезным для определения успешной загрузки лицензии или нет. Если обратиться к этому свойству перед установкой лицензии, оно вернет false, и наоборот, однако лицензия должна быть действительной.

Приведенный ниже образец кода демонстрирует использование свойства Workbook.IsLicensed.

**C#**

{{< highlight csharp >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **Добавлено свойство ImageOrPrintOptions.SVGFitToViewPort.**
Aspose.Cells for .NET 8.4.1 добавил свойство SVGFitToViewPort для класса ImageOrPrintOptions, которое может использоваться для включения атрибута viewBox для формата файла SVG при экспорте электронных таблиц или диаграмм в формат SVG. Значение по умолчанию этого свойства равно false, поэтому базовый XML-файл для файла SVG, сгенерированного без установки вышеперечисленного свойства, не будет содержать атрибута viewBox.

Следующий образец кода демонстрирует использование свойства ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **Устаревшие API**
### **Устаревший метод Workbook.ValidateFormula**
Используйте метод Cell.Formula для проверки формулы.
