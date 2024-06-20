---
title: Работа с GridWeb
type: docs
weight: 20
url: /ru/java/working-with-gridweb/
---

## **Открытие файла Microsoft Excel**

Управление Aspose.Cells.GridWeb может открывать и загружать файлы Microsoft Excel - с данными, форматированием, диаграммами, изображениями и т. д. В этой теме объясняется, как это сделать.

Для открытия файла Excel с помощью элемента управления GridWeb:

1. Добавьте элемент управления Aspose.Cells.GridWeb на веб-форму или страницу.
1. Импортируйте файл Excel, указав путь к файлу.
1. Запустите приложение или откройте страницу.

Чтобы загрузить содержимое из файла Excel в элемент управления Aspose.Cells.GridWeb, вам нужно вызвать метод importExcelFile, чтобы указать путь к файлу Excel. После этого элемент управления GridWeb автоматически найдет файл по указанному пути и отобразит его содержимое. Приведен отрывок кода, который загружает содержимое файла Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Приведенный выше отрывок кода можно использовать любым удобным способом. Например, чтобы автоматически загружать файл Excel при загрузке веб-формы, добавьте этот код в событие Page_Load формы, которое вы сами укажете.

Файл Excel загружается в GridWeb

![todo:image_alt_text](working-with-gridweb_1.png)

## **Сохранение файла Microsoft Excel**

На веб-сайтах в режиме GUI с помощью элемента управления Aspose.Cells.GridWeb возможно создание новых или изменение существующих файлов Microsoft Excel. Затем файлы можно сохранить в файлы Excel. Элемент управления Aspose.Cells.GridWeb эффективно служит в качестве онлайн-редактора электронных таблиц. В этой теме описывается, как сохранить содержимое сетки в файлы Excel.

### **Сохранение в файл**

Для сохранения содержимого элемента управления Aspose.Cells.GridWeb в файл Excel:

1. Добавьте элемент управления Aspose.Cells.GridWeb на веб-форму или страницу.
1. Сохраните свою работу в файл Excel в указанном пути.
1. Запустите приложение или откройте страницу.

Приведенный ниже пример кода иллюстрирует, как сохранить содержимое сетки в файл Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

Приведенный выше фрагмент кода может быть использован несколькими способами. Обычным способом является добавление кнопки, которая сохраняет содержимое сетки в файл Excel при нажатии. Aspose.Cells.GridWeb предлагает более простой подход для этой задачи. У Aspose.Cells.GridWeb есть событие, называемое SaveCommand. Приведенный выше фрагмент кода может быть добавлен в обработчик события SaveCommand, что позволяет пользователям сохранить свою работу, нажав на встроенную кнопку **Сохранить** в Aspose.Cells.GridWeb.

## **Изменение размеров Aspose.Cells.GridWeb и его заголовка**

В этой статье объясняется, как изменить размер GridWeb во время выполнения с использованием API Aspose.Cells.GridWeb. Также объясняется, как изменить заголовки сетки Aspose.Cells.GridWeb, чтобы их данные было легче прочитать.

### **Изменение ширины и высоты Aspose.Cells.GridWeb**

Изменение ширины и высоты элемента управления Aspose.Cells.GridWeb - это простая, но важная функция. Элемент управления Aspose.Cells.GridWeb представляется классом GridWeb в API. Для изменения ширины и высоты элемента управления GridWeb просто используйте его свойства ширины и высоты.

{{% alert color="primary" %}}

Ширина и высота элемента управления могут быть определены в пикселях или пунктах.

{{% /alert %}}

Результатом следующего фрагмента кода является показанное ниже.

**Измененная ширина и высота элемента управления GridWeb**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Изменение ширины и высоты заголовочной панели**

Элемент управления Aspose.Cells.GridWeb содержит две заголовочные панели следующим образом:

- Верхний заголовок, этот заголовок представляет столбцы как A, B, C, D, и т. д.
- Левый заголовок, этот заголовок представляет строки как 1, 2, 3, 4, и т. д.

Обе эти заголовочные панели показаны ниже.

**Заголовочные панели**

![todo:image_alt_text](working-with-gridweb_3.png)

Измените высоту верхней панели заголовка и ширину левой панели заголовка с помощью свойств HeaderBarHeight и HeaderBarWidth управления GridWeb соответственно. Ниже приведен вывод примера кода, который следует за ним.

**Измененная ширина и высота панели заголовка**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Работа с событиями Aspose.Cells.GridWeb**

Все разработчики должны быть знакомы с событиями и их назначением. События используются для отправки уведомлений об изменениях, которые могут произойти в элементе управления или классе. У Aspose.Cells.GridWeb есть несколько событий, которые можно использовать для выполнения определенных задач, когда происходят определенные изменения в элементе управления.

Эта тема предоставляет введение во все события, поддерживаемые элементом управления Aspose.Cells.GridWeb, а также некоторую информацию о том, как обрабатывать эти события.

### **Введение в события Grid**

Элемент управления Aspose.Cells.GridWeb поддерживает несколько событий, которые позволяют более точно управлять выполнением операций при наступлении определенных событий в элементе управления. Полный список поддерживаемых событий элементом управления Aspose.Cells.GridWeb можно найти ниже.

|**События**|**Описание**|
| :- | :- |
|CellCommand| Срабатывает, когда пользователь нажимает гиперссылку команды в ячейке. Когда это событие срабатывает, его параметр e.Argument предоставляет имя команды.|
|CellDoubleClick| Срабатывает, когда ячейка дважды щелкается.|
|ColumnDeleted| Срабатывает, когда пользователь удаляет столбец из листа с помощью контекстного меню на стороне клиента.|
|ColumnDeleting| Срабатывает, когда пользователь пытается удалить столбец из листа с помощью контекстного меню на стороне клиента.|
|ColumnDoubleClick| Срабатывает, когда дважды щелкается заголовок столбца.|
|ColumnInserted| Срабатывает, когда пользователь вставляет столбец в лист с помощью контекстного меню на стороне клиента.|
|CustomCommand| Срабатывает, когда пользователь щелкает на кнопке пользовательской команды.|
|LoadCustomData| Срабатывает, когда свойство EnableSession элемента управления установлено в false и требуется загрузить данные листа. Вы можете обработать это событие в режиме без сеанса для загрузки данных листа из файла или базы данных.|
|PageIndexChanged| Срабатывает, когда изменяется индекс страницы листа элемента управления.|
|RowDeleted| Срабатывает, когда пользователь удаляет строку из листа с помощью контекстного меню на стороне клиента.|
|RowDeleting| Срабатывает, когда пользователь пытается удалить строку из листа с помощью контекстного меню на стороне клиента.|
|RowDoubleClick| Срабатывает, когда дважды щелкается заголовок строки.|
|RowInserted| Срабатывает, когда пользователь вставляет строку в лист с помощью контекстного меню на стороне клиента.|
|SaveCommand| Срабатывает, когда пользователь нажимает кнопку **Сохранить**.|
|SheetTabClick| Срабатывает, когда пользователь нажимает на вкладку листа.|
|SubmitCommand| Срабатывает, когда пользователь нажимает кнопку **Отправить**.|
|UndoCommand|Происходит, когда нажата кнопка **Отменить**.|
|AjaxCallFinished|Срабатывает при завершении AJAX-обновления элемента управления. (EnableAJAX должен быть установлен в true).|
|CellModifiedOnAjax|Срабатывает, когда ячейка изменяется в вызове AJAX.|
|AfterColumnFilter|Срабатывает при применении фильтра к столбцу.|

### **Обработка событий сетки**

Чтобы выполнить определенную операцию при возникновении конкретного события, необходимо создать обработчик событий. Обработчик событий выполняет желаемую задачу при возникновении определенного события. В следующем примере показано, как обрабатывать простое событие сетки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Работа с событиями двойного щелчка**

Aspose.Cells.GridWeb содержит три типа событий двойного щелчка:

- CellDoubleClick, срабатывает, когда ячейка дважды щелкается.
- ColumnDoubleClick, срабатывает, когда дважды щелкается заголовок столбца.
- RowDoubleClick, срабатывает, когда дважды щелкается заголовок строки.

В этой статье обсуждается, как включить события двойного щелчка в Aspose.Cells.GridWeb. Она также обсуждает создание обработчиков событий для этих событий.

### **Включение событий двойного щелчка**

Все типы событий двойного щелчка могут быть включены на стороне клиента, установив свойство EnableDoubleClickEvent элемента управления GridWeb в true.

{{% alert color="primary" %}}

По умолчанию свойство EnableDoubleClickEvent установлено в false. Это означает, что события двойного щелчка по умолчанию отключены. Чтобы реализовать такие события, сначала включите функцию.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

После включения событий двойного щелчка можно создать обработчики событий для любых событий двойного щелчка. Эти обработчики событий выполняют определенные задачи, когда данное событие двойного щелчка срабатывает.

### **Обработка событий двойного щелчка**

#### **Двойной щелчок по ячейке**

Обработчик события для события CellDoubleClick предоставляет аргумент типа CellEventArgs, который содержит полную информацию о ячейке, по которой был выполнен двойной щелчок.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Двойной щелчок по заголовку столбца**

Обработчик события для события ColumnDoubleClick предоставляет аргумент типа RowColumnEventArgs, который содержит номер индекса столбца для заголовка, по которому был выполнен двойной щелчок, а также другую информацию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Двойной щелчок по заголовку строки**

Обработчик события для события RowDoubleClick предоставляет аргумент типа RowColumnEventArgs, который содержит номер индекса строки для заголовка, по которому был выполнен двойной щелчок, а также другую связанную информацию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Установка стиля или внешнего вида Aspose.Cells.GridWeb**

У Aspose.Cells.GridWeb есть свой собственный внешний вид, но возможно изменить его внешний вид. Aspose.Cells.GridWeb предоставляет несколько свойств, позволяющих разработчикам полностью контролировать его внешний вид. В этой теме обсуждаются некоторые из этих свойств.

### **Установка стиля или внешнего вида Aspose.Cells.GridWeb**

#### **Предустановленные стили**

Для экономии усилий разработчиков Aspose.Cells.GridWeb предлагает несколько предустановленных стилей. Просто выберите стиль из списка, чтобы применить его.

|**Стили**|**Цветовая схема**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Когда выбран определенный стиль, он изменяет весь внешний вид элемента управления GridWeb. Разработчики могут выбрать предустановленный стиль для применения на выполнение с помощью гибкого API Aspose.Cells.GridWeb.

Управление GridWeb предоставляет свойство PresetStyle, к которому разработчики могут назначить любой желаемый предустановленный стиль.

Результат выполнения нижеприведенного фрагмента кода показан ниже.

**Управление GridWeb с примененным стилем Colorful1**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Стиль строки заголовка**

Если взглянуть на элемент управления GridWeb, можно заметить две панели заголовка. Одна для столбцов (то есть A, B, C, D и т. д.), а другая для строк (то есть 1, 2, 3, 4 и т. д.). Aspose.Cells.GridWeb позволяет разработчикам контролировать внешний вид этих панелей заголовка. Разработчики могут установить стиль панелей заголовка на время выполнения.

{{% alert color="primary" %}}

Управление GridWeb предоставляет свойство HeaderBarStyle, которое применяет стиль к обеим строкам заголовка элемента управления.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Стиль панели вкладок**

Также возможно установить стиль панели вкладок. Пожалуйста, ознакомьтесь с следующим кодом

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Загрузка файла стилей**

Чтобы применить настройки стиля из существующего файла стиля к элементу управления GridWeb, разработчики могут установить путь к файлу стиля в свойство CustomStyleFileName элемента управления. Но перед этим необходимо установить свойство PresetStyle элемента управления в значение Custom. Это потому, что файл стиля содержит информацию о пользовательском стиле, которая уже определена разработчиком.

Пожалуйста, посмотрите следующее изображение, которое показывает GridWeb с примененным пользовательским стилем.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

ВАЖНО: Загрузка файла стилей в элемент управления GridWeb не влияет на настройки форматирования ячеек элемента управления.

{{% /alert %}}

#### **Образец пользовательского шаблона стиля**

Вот образец пользовательского шаблона стиля. Вы можете изменить его в соответствии с вашими требованиями.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Создание элемента управления на веб-форме**

Эта статья поможет вам создать простую веб-форму JSP (Java Server Page) с элементом управления GridWeb.

**Шаг 1 - Создание структуры каталогов**

Вам нужно создать следующую структуру каталогов в каталоге **webapps** сервера Tomcat

![todo:image_alt_text](working-with-gridweb_7.png)

Это каталоги и файлы, которые вам нужно создать. Пожалуйста, прочитайте комментарии и следуйте им. Вы можете получить последние архивы выпусков Aspose.Cells.GridWeb для Java по [этой ссылке](https://downloads.aspose.com/cells/java).

{{< highlight java >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Шаг 2 - Добавление кодов в созданные файлы**

Этот раздел показывает коды для различных файлов, созданных в вышеуказанной структуре каталогов. Пожалуйста, получите эти коды и добавьте их в ваши файлы, открыв их в Блокноте и скопируйте/вставьте их.

**Web.xml**

{{< highlight java >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight java >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Шаг 3 - Запуск вашей пробной веб-страницы JSP**

Теперь вы все сделали. Пришло время запустить веб-страницу. Пожалуйста, запустите ваш сервер Tomcat, а затем вставьте следующий URL в веб-браузер.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Вы увидите что-то похожее на следующий скриншот. Поздравляю, вы успешно использовали элемент управления GridWeb на своей странице JSP.

![todo:image_alt_text](working-with-gridweb_8.png)

## **Печать в GridWeb**

Иногда разработчикам нужно печатать содержимое элемента управления GridWeb, включенное на веб-странице, без сохранения файла Microsoft Excel. Элемент управления Aspose.Cells.GridWeb поддерживает эту функцию.

### **Печать в GridWeb**

Чтобы напечатать без сохранения отдельного файла, вызовите метод print() класса GridWeb на стороне клиента для печати сетки. Вы также можете выбрать подходящее событие.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Поскольку вы вызываете это с стороны клиента, вам нужно сначала получить идентификатор клиента gridweb. Вы можете получить его с помощью метода gridweb.getClientID().

### **Пример клиентского кода**

Пожалуйста, посмотрите следующую ссылку, которая вызывает метод gridweb.print() с клиентской стороны.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Введение в различные режимы сетки**

Эта статья описывает различные режимы Aspose.Cells.GridWeb. Эти режимы различаются логически из-за их различных функций и поведения. Мы выделили различные типы режимов:

- Режим редактирования
- Режим просмотра

У каждого из этих режимов есть свои характеристики. Разработчики могут работать с Aspose.Cells.GridWeb в любом режиме в соответствии с их требованиями. Мы рассмотрим каждый режим ниже.

### **Режим редактирования**

По умолчанию элемент управления Aspose.Cells.GridWeb находится в режиме редактирования. В режиме редактирования вы можете полностью редактировать или изменять содержимое сетки, используя все функции, предлагаемые элементом управления Aspose.Cells.GridWeb. Эти функции включают в себя:

- Сохранение содержимого сетки в файлы Microsoft Excel.
- Отправка данных на сервер.
- Вычисление формул.
- Отмена или отбрасывание предыдущих действий.
- Управление строками и столбцами.
- Вырезание, копирование или вставка данных.
- Форматирование ячеек и т.д.

**GridWeb управление в режиме редактирования**

![todo:image_alt_text](working-with-gridweb_9.png)

Разработчики также могут переключиться в режим редактирования программным способом, установив свойство EditMode элемента управления GridWeb в значение true.

### **Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Режим просмотра**

Когда элемент управления GridWeb находится в режиме просмотра, пользователи не могут редактировать или изменять содержимое сетки, что означает, что пользователи могут только просматривать содержимое сетки. Поэтому этот режим называется режимом просмотра. В режиме просмотра несколько кнопок (**Submit**, **Save** и **Undo**) скрыты, а меню, которое появляется при щелчке правой кнопкой мыши, содержит только опцию **Copy** и **Find**.

**GridWeb управление в режиме просмотра** 

![todo:image_alt_text](working-with-gridweb_10.png)

Если разработчики хотят, чтобы их пользователи видели только данные, то они могут переключиться в режим просмотра программно, установив свойство EditMode элемента управления GridWeb в значение **false**.

### **Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Даже в режиме просмотра пользователи могут изменять высоту и ширину строк и столбцов.

{{% /alert %}}
