---
title: Изменения в публичном API в Aspose.Cells 8.4.1
type: docs
weight: 150
url: /ru/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 8.4.0 до 8.4.1, которые могут быть интересны разработчикам модулей/приложений. В нем содержатся не только новые и обновленные публичные методы, [добавленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-1/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Механизм модификации подключения к базе данных**
Класс com.aspose.cells.ExternalConnection уже содержал методы и свойства, которые можно использовать для проверки деталей подключения к базе данных, сохраненных в электронной таблице. Большинство свойств, связанных с классом ExternalConnection, были доступны только для чтения до выпуска Aspose.Cells for Java 8.4.1. С этим выпуском API предоставило поддержку для изменения настроек подключения к базе данных.

Ниже приведен фрагмент кода, показывающий, как динамически изменить настройки подключения к базе данных.

**Java**

{{< highlight csharp >}}

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

Вот несколько наиболее важных свойств, выведенных из класса {ExternalConnection}}.

|**Имя свойства** |**Описание** |
| :- | :- |
|BackgroundRefresh | Указывает, может ли подключение обновляться в фоновом режиме (асинхронно). <br> true, если предпочтительное использование подключения заключается в асинхронном обновлении в фоновом режиме; <br> false, если предпочтительное использование подключения заключается в синхронном обновлении на переднем плане. |
|ConnectionDescription | Указывает описание пользователя для этого подключения |
|ConnectionId | Указывает уникальный идентификатор этого подключения. |
|Credentials | Указывает метод аутентификации, используемый при установлении (или повторном установлении) подключения. |
|IsDeleted | Указывает, было ли связанное рабочее книга удалено. true, если<br> подключение было удалено; в противном случае false. |
|IsNew | True, если подключение еще не было обновлено впервые; в противном случае false. Это <br> состояние может возникнуть, когда пользователь сохраняет файл до завершения запроса. |
|KeepAlive | True, когда приложение электронной таблицы должно прикладывать усилия по сохранению подключения <br> открытым. Когда это значение равно false, приложение должно закрыть подключение после получения <br> информации. |
|Name | Указывает имя подключения. Каждое подключение должно иметь уникальное имя. |
|OdcFile |Указывает полный путь к внешнему файлу соединения, из которого было создано это соединение. Если соединение не удается во время попытки обновления данных, и reconnectionMethod=1, то приложение электронной таблицы попробует снова использовать информацию из внешнего файла подключения вместо объекта соединения, встроенного в книгу. |
|OnlyUseConnectionFile |Указывает, должно ли приложение электронной таблицы всегда и только использовать информацию о подключении во внешнем файле подключения, указанном атрибутом odcFile, при обновлении соединения. Если false, то приложение электронной таблицы должно следовать процедуре, указанной атрибутом reconnectionMethod |
|Parameters |Получает ConnectionParameterCollection для ODBC или веб-запроса. |
|ReConnectionMethod |Указывает тип reconnectionMethod |
|RefreshInternal|Указывает количество минут между автоматическими обновлениями соединения. |
|RefreshOnLoad |True, если это соединение должно быть обновлено при открытии файла; в противном случае false. |
|SaveData |True, если внешние данные, полученные с помощью соединения для заполнения таблицы, должны быть сохранены с книгой; в противном случае false. |
|SavePassword |True, если пароль должен быть сохранен как часть строки подключения; в противном случае False. |
|SourceFile |Используется, когда внешний источник данных основан на файлах. Когда соединение с таким источником данных не удается, приложение электронной таблицы пытается подключиться непосредственно к этому файлу. Может быть выражен в URI или системно-специфической нотации пути к файлу. |
|SSOId|Идентификатор для единого входа (SSO), используемый для аутентификации между промежуточным сервером формата SpreadsheetML и внешним источником данных. |
|Type |Указывает тип источника данных. |

### **Возможность форматировать подстроку текста DataLabels**
Aspose.Cells for Java 8.4.1 предоставил метод DataLabels.characters для извлечения экземпляра класса FontSetting, соответствующего подстроке ChartPoints.DataLabels. В свою очередь, экземпляр класса FontSetting может быть использован для форматирования подстроки DataLabels с другими настройками шрифта и цвета.

Приведенный ниже фрагмент кода показывает, как использовать метод DataLabels.characters.

**Java**

{{< highlight csharp >}}

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

### **Возможность установить желаемые размеры изображения для экспорта электронных таблиц и диаграмм**
Aspose.Cells for Java 8.4.1 предоставил метод setDesiredSize класса ImageOrPrintOptions для установки размеров результрующего изображения при экспорте электронных таблиц и диаграмм в изображения. Метод setDesiredSize принимает два параметра типа integer, где первый параметр - желаемая ширина, а второй - желаемая высота.

Приведенный ниже фрагмент кода показывает, как установить желаемые размеры при экспорте рабочего листа в формат PNG.

**Java**

{{< highlight csharp >}}

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

Тот же метод также можно использовать для преобразования диаграмм в изображения. 

{{% /alert %}} 

### **Отображение комментариев в формат PDF**
С выпуском v8.4.1 API Aspose.Cells предоставил свойство PageSetup.PrintComments и перечисление PrintCommentsType для облегчения отображения комментариев при преобразовании электронных таблиц в формат PDF. В перечислении PrintCommentsType есть следующие константы. 

- PrintCommentsType.PRINT_NO_COMMENTS: Комментарии не должны отображаться.
- PrintCommentsType.PRINT_IN_PLACE: Комментарии должны отображаться там, где они находятся.
- PrintCommentsType.PRINT_SHEET_END: Комментарии должны отображаться в конце листа.

Следующий образец кода демонстрирует использование свойства PageSetup.PrintComments для отображения комментариев с использованием всех возможных значений перечисления PrintCommentsType.

**Java**

{{< highlight csharp >}}

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

### **Добавлено свойство Workbook.isLicensed.**
Aspose.Cells for Java 8.4.1 предоставил Workbook.isLicensed, которое может быть очень полезным для определения успешной загрузки лицензии. Если вы обратитесь к этому свойству до установки лицензии, оно вернет false и наоборот, однако лицензия должна быть действительной.

Следующий образец кода демонстрирует использование свойства Workbook.isLicensed.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.4.1 предоставил свойство SVGFitToViewPort для класса ImageOrPrintOptions, которое можно использовать для включения атрибута viewBox для формата файла SVG при экспорте электронных таблиц или диаграмм в формат SVG. Значение по умолчанию этого свойства - false, поэтому базовый XML-файл для SVG, сгенерированный без установки вышеупомянутого свойства, не будет включать атрибут viewBox.

Следующий образец кода демонстрирует использование свойства ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight csharp >}}

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
### **Метод Workbook.validateFormula устарел.**
Используйте свойство Cell.Formula для проверки формулы.
{{< app/cells/assistant language="java" >}}
