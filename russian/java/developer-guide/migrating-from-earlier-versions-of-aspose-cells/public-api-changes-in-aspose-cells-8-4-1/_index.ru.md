---
title: Общедоступный API Изменения в Aspose.Cells 8.4.1
type: docs
weight: 150
url: /ru/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.4.0 до 8.4.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-1/) а также[удалены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-1/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Механизм изменения подключения к базе данных**
Класс com.aspose.cells.ExternalConnection уже содержит метод и свойства, которые можно использовать для проверки сведений о подключении к базе данных, хранящихся в электронной таблице. Большинство свойств, связанных с классом ExternalConnection, были доступны только для чтения до выпуска Aspose.Cells for Java 8.4.1. В этом выпуске API также предоставил поддержку для управления параметрами подключения к базе данных.

В следующем фрагменте кода показано, как динамически изменять параметры подключения к базе данных.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

Вот несколько наиболее важных свойств, предоставляемых классом {ExternalConnection}}.

|**Имя свойства** |**Описание** |
|:- |:- |
| ФонОбновить|Указывает, можно ли обновить соединение в фоновом режиме (асинхронно).<br> Значение true, если предпочтительное использование соединения — асинхронное обновление в фоновом режиме;<br> false, если предпочтительным использованием соединения является синхронное обновление на переднем плане.|
| СоединениеОписание| Указывает описание пользователя для этого подключения.|
| Идентификатор соединения| Указывает уникальный идентификатор этого соединения.|
| Реквизиты для входа| Указывает метод проверки подлинности, который будет использоваться при установлении (или повторном установлении) соединения.|
| IsDeleted|Указывает, было ли удалено связанное подключение к книге. верно, если<br> соединение было удалено; в противном случае ложно.|
| Новый| Истинно, если соединение не было обновлено в первый раз; в противном случае ложно. Этот<br> состояние может произойти, когда пользователь сохраняет файл до завершения запроса.|
| KeepAlive|Истинно, когда приложение для работы с электронными таблицами должно прилагать усилия для поддержания соединения.<br> открытым. При значении false приложение должно закрыть соединение после получения<br> Информация.|
| Имя| Задает имя соединения. Каждое соединение должно иметь уникальное имя.|
| одкфайл| Указывает полный путь к внешнему файлу подключения, из которого это подключение было<br> созданный. Если во время попытки обновления данных происходит сбой подключения и reconnectionMethod=1,<br> затем приложение для работы с электронными таблицами попытается снова использовать информацию из файла внешнего подключения.<br> вместо объекта подключения, встроенного в книгу.|
| Толькоусеконнектионфиле| Указывает, должно ли приложение для работы с электронными таблицами всегда и только использовать<br> информация о подключении во внешнем файле подключения, указанном атрибутом odcFile<br> при обновлении соединения. Если false, то приложение для работы с электронными таблицами<br>должен следовать процедуре, указанной атрибутом reconnectionMethod|
| Параметры| Получает ConnectionParameterCollection для ODBC или веб-запроса.|
| ReConnectionMethod| Укажите тип reconnectionMethod|
|ОбновитьВнутренний| Указывает количество минут между автоматическими обновлениями соединения.|
| Обновить при загрузке| Истинно, если это соединение должно обновляться при открытии файла; в противном случае ложно.|
| Сохранять данные|Истинно, если внешние данные, полученные через соединение для заполнения таблицы, должны быть сохранены.<br> с рабочей тетрадью; в противном случае ложно.|
| Сохраните пароль| Истинно, если пароль должен быть сохранен как часть строки подключения; в противном случае Ложь.|
| Исходный файл| Используется, когда внешний источник данных основан на файлах. При подключении к таким данным<br> источник не работает, приложение для работы с электронными таблицами пытается напрямую подключиться к этому файлу. Может быть<br> выраженный в URI или системной нотации пути к файлу.|
|SSOID|Идентификатор для единого входа (SSO), используемый для аутентификации между промежуточным<br> сервер электронной таблицыML и внешний источник данных.|
| Тип| Указывает тип источника данных.|

### **Возможность форматирования подстроки текста DataLabels**
Aspose.Cells for Java 8.4.1 предоставил метод DataLabels.characters для извлечения экземпляра класса FontSetting, который соответствует подстроке ChartPoints.DataLabels. В свою очередь, экземпляр класса FontSetting можно использовать для форматирования подстроки DataLabels с различными настройками и цветом шрифта.

В следующем фрагменте кода показано, как использовать метод DataLabels.characters.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Возможность установки желаемых размеров изображения для экспорта электронных таблиц и диаграмм**
Aspose.Cells for Java 8.4.1 предоставил метод ImageOrPrintOptions.setDesiredSize для установки размеров результирующего изображения при экспорте электронных таблиц и диаграмм в изображения. Метод ImageOrPrintOptions.setDesiredSize принимает два параметра целочисленного типа, где первый — это желаемая ширина, а второй — желаемая высота.

В следующем фрагменте кода показано, как установить нужные размеры при экспорте рабочего листа в PNG.

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Тот же метод можно использовать и для преобразования диаграмм в изображения.

{{% /alert %}} 

### **Преобразование комментариев в PDF**
 В выпуске v8.4.1 Aspose.Cells API предоставил свойство PageSetup.PrintComments и перечисление PrintCommentsType, чтобы облегчить отображение комментариев при преобразовании электронных таблиц в формат PDF. Перечисление PrintCommentsType имеет следующие константы.

- PrintCommentsType.PRINT_НЕТ_КОММЕНТАРИИ: Комментарии не подлежат отображению.
- PrintCommentsType.PRINT_В_МЕСТО: комментарии должны отображаться там, где они размещены.
- PrintCommentsType.PRINT_ЛИСТ_END: комментарии должны отображаться в конце рабочего листа.

В следующем примере кода показано использование свойства PageSetup.PrintComments для отображения комментариев с использованием всех возможных значений перечисления PrintCommentsType.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Добавлено свойство Workbook.isLicensed**
Aspose.Cells for Java 8.4.1 выложил Workbook.isLicensed, который может очень помочь в определении того, была ли лицензия успешно загружена или нет. Если вы получите доступ к этому свойству до установки лицензии, оно вернет false и наоборот, однако лицензия должна быть действительной.

В следующем примере кода показано использование свойства Workbook.isLicensed.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **Добавлено свойство ImageOrPrintOptions.SVGFitToViewPort.**
Aspose.Cells for Java 8.4.1 предоставляет свойство SVGFitToViewPort для класса ImageOrPrintOptions, которое можно использовать для включения атрибута viewBox для формата файла SVG при экспорте электронных таблиц или диаграмм в формат SVG. Значение по умолчанию для этого свойства равно false, поэтому базовый XML-файл для SVG-файла, сгенерированный без установки вышеупомянутого свойства, не будет включать атрибут viewBox.

В следующем примере кода показано использование свойства ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **Устаревшие API**
### **Метод Workbook.validateFormula устарел**
Используйте свойство Cell.Formula для проверки формулы.
