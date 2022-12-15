---
title: Общедоступный API Изменения в Aspose.Cells 8.4.1
type: docs
weight: 140
url: /ru/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.4.0 до 8.4.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-1/) а также[удалены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-1/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Механизм изменения подключения к базе данных**
Класс Aspose.Cells.ExternalConnections.ExternalConnection уже содержит метод и свойства, которые можно использовать для проверки сведений о подключении к базе данных, хранящихся в электронной таблице. Большинство свойств, связанных с классом Aspose.Cells.ExternalConnections.ExternalConnection, были доступны только для чтения до выпуска Aspose.Cells for .NET 8.4.1. В этом выпуске API также предоставил поддержку для управления параметрами подключения к базе данных.

В следующем фрагменте кода показано, как динамически изменять параметры подключения к базе данных.

**C#**

{{< highlight "csharp" >}}

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



Вот несколько наиболее важных свойств, предоставляемых классом {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**Имя свойства**|**Описание**|
|:- |:- |
|ФонОбновить|Указывает, можно ли обновить соединение в фоновом режиме (асинхронно).<br> Значение true, если предпочтительное использование соединения — асинхронное обновление в фоновом режиме;<br>false, если предпочтительным использованием соединения является синхронное обновление на переднем плане.|
|СоединениеОписание|Указывает описание пользователя для этого подключения.|
|Идентификатор соединения|Указывает уникальный идентификатор этого соединения.|
|Реквизиты для входа|Указывает метод проверки подлинности, который будет использоваться при установлении (или повторном установлении) соединения.|
|IsDeleted|Указывает, было ли удалено связанное подключение к книге. верно, если<br>соединение было удалено; в противном случае ложно.|
|Новый| Истинно, если соединение не было обновлено в первый раз; в противном случае ложно. Этот<br>состояние может произойти, когда пользователь сохраняет файл до завершения запроса.|
|KeepAlive|Истинно, когда приложение для работы с электронными таблицами должно прилагать усилия для поддержания соединения.<br> открытым. При значении false приложение должно закрыть соединение после получения<br>Информация.|
|Имя|Задает имя соединения. Каждое соединение должно иметь уникальное имя.|
|одкфайл| Указывает полный путь к внешнему файлу подключения, из которого это подключение было<br> созданный. Если во время попытки обновления данных происходит сбой подключения и reconnectionMethod=1,<br> затем приложение для работы с электронными таблицами попытается снова использовать информацию из файла внешнего подключения.<br>вместо объекта подключения, встроенного в книгу.|
|Толькоусеконнектионфиле| Указывает, должно ли приложение для работы с электронными таблицами всегда и только использовать<br> информация о подключении во внешнем файле подключения, указанном атрибутом odcFile<br> при обновлении соединения. Если false, то приложение для работы с электронными таблицами<br>должен следовать процедуре, указанной атрибутом reconnectionMethod|
|Параметры|Получает ConnectionParameterCollection для ODBC или веб-запроса.|
|ReConnectionMethod|Укажите тип reconnectionMethod|
|ОбновитьВнутренний|Указывает количество минут между автоматическими обновлениями соединения.|
|Обновить при загрузке|Истинно, если это соединение должно обновляться при открытии файла; в противном случае ложно.|
|Сохранять данные|Истинно, если внешние данные, полученные через соединение для заполнения таблицы, должны быть сохранены.<br>с рабочей тетрадью; в противном случае ложно.|
|Сохраните пароль|Истинно, если пароль должен быть сохранен как часть строки подключения; в противном случае Ложь.|
|Исходный файл| Используется, когда внешний источник данных основан на файлах. При подключении к таким данным<br> источник не работает, приложение для работы с электронными таблицами пытается напрямую подключиться к этому файлу. Может быть<br>выраженный в URI или системной нотации пути к файлу.|
|SSOID|Идентификатор для единого входа (SSO), используемый для аутентификации между промежуточным<br>сервер электронной таблицыML и внешний источник данных.|
|Тип|Указывает тип источника данных.|

### **Возможность форматирования подстроки текста DataLabels**
Aspose.Cells for .NET 8.4.1 предоставил метод DataLabels.Characters для извлечения экземпляра класса FontSetting, который соответствует подстроке ChartPoints.DataLabels. В свою очередь, экземпляр класса FontSetting можно использовать для форматирования подстроки DataLabels с различными настройками и цветом шрифта.

В следующем фрагменте кода показано, как использовать метод DataLabels.Characters.

**C#**

{{< highlight "csharp" >}}

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


### **Возможность установки желаемых размеров изображения для экспорта электронных таблиц и диаграмм**
Aspose.Cells for .NET 8.4.1 предоставил метод ImageOrPrintOptions.SetDesiredSize для установки размеров результирующего изображения при экспорте электронных таблиц и диаграмм в изображения. Метод ImageOrPrintOptions.SetDesiredSize принимает два параметра целочисленного типа, где первый — это желаемая ширина, а второй — желаемая высота.

В следующем фрагменте кода показано, как установить нужные размеры при экспорте рабочего листа в PNG.

**C#**

{{< highlight "csharp" >}}

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

То же свойство также можно использовать для преобразования диаграмм в изображения.

{{% /alert %}} 


### **Преобразование комментариев в PDF**
В выпуске v8.4.1 Aspose.Cells API предоставил свойство PageSetup.PrintComments и перечисление PrintCommentsType, чтобы облегчить отображение комментариев при преобразовании электронных таблиц в формат PDF. Перечисление PrintCommentsType имеет следующие константы.

- PrintCommentsType.PrintNoComments: комментарии не должны отображаться.
- PrintCommentsType.PrintInPlace: комментарии должны отображаться там, где они размещены.
- PrintCommentsType.PrintSheetEnd: комментарии должны отображаться в конце рабочего листа.

В следующем примере кода показано использование свойства PageSetup.PrintComments для отображения комментариев с использованием всех возможных значений перечисления PrintCommentsType.

**C#**

{{< highlight "csharp" >}}

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


### **Переместить рабочие листы в Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop предоставляет метод WorksheetCollection.MoveTo, который можно использовать для перемещения рабочего листа в указанный индекс. Вышеупомянутый метод принимает индексы (начиная с нуля) исходного рабочего листа и целевого рабочего листа в качестве параметров.

В следующем примере кода показано использование свойства WorksheetCollection.MoveTo.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Добавлено свойство Workbook.IsLicensed**
Aspose.Cells for .NET 8.4.1 открыл Workbook.IsLicensed, который может помочь определить, была ли успешно загружена лицензия. Если вы получите доступ к этому свойству до установки лицензии, оно вернет false и наоборот, однако лицензия должна быть действительной.

В следующем примере кода показано использование свойства Workbook.IsLicensed.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET 8.4.1 предоставляет свойство SVGFitToViewPort для класса ImageOrPrintOptions, которое можно использовать для включения атрибута viewBox для формата файла SVG при экспорте электронных таблиц или диаграмм в формат SVG. Значение по умолчанию для этого свойства равно false, поэтому базовый XML-файл для SVG-файла, сгенерированный без установки вышеупомянутого свойства, не будет включать атрибут viewBox.

В следующем примере кода показано использование свойства ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight "csharp" >}}

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
### **Метод Workbook.ValidateFormula устарел**
Используйте метод Cell.Formula для проверки формулы.
