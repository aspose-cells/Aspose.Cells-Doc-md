---
title: Работа с GridWeb
type: docs
weight: 20
url: /ru/java/working-with-gridweb/
---
##  **Открытие файла Excel Microsoft**

Aspose.Cells. Элемент управления GridWeb может открывать и загружать файлы Excel Microsoft с данными, форматированием, диаграммами, изображениями и т. д. В этом разделе объясняется, как это сделать.

Чтобы открыть файл Excel с помощью элемента управления GridWeb:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или страницу.
1. Импортируйте файл Excel, указав путь к файлу.
1. Запустите приложение или откройте страницу.

Чтобы загрузить содержимое из файла Excel в элемент управления Aspose.Cells.GridWeb, необходимо вызвать метод importExcelFile, чтобы указать путь к файлу Excel. После этого элемент управления GridWeb автоматически найдет файл по указанному пути и отобразит в нем его содержимое. Ниже представлен фрагмент кода, который загружает содержимое файла Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Приведенный выше фрагмент кода можно использовать по своему усмотрению. Например, чтобы автоматически загружать файл Excel при загрузке веб-формы, добавьте этот код в событие Page_Load формы, которое вы указали самостоятельно.

**Файл Excel загружается в GridWeb.**

![задача: image_alt_text](working-with-gridweb_1.png)

##  **Сохранение файла Excel Microsoft**

Можно создавать новые или манипулировать существующими файлами Excel Microsoft на веб-сайтах в режиме графического интерфейса с помощью элемента управления Aspose.Cells.GridWeb. Затем файлы можно сохранить в файлы Excel. Aspose.Cells.GridWeb эффективно служит онлайн-редактором электронных таблиц. В этом разделе описывается, как сохранить содержимое сетки в файлах Excel.

###  **Сохранение в виде файла**

Чтобы сохранить содержимое элемента управления Aspose.Cells.GridWeb в виде файла Excel:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или страницу.
1. Сохраните свою работу в виде файла Excel по указанному пути.
1. Запустите приложение или откройте страницу.

В приведенном ниже примере кода показано, как сохранить содержимое сетки в файл Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Приведенный выше фрагмент кода можно использовать несколькими способами. Распространенным способом является добавление кнопки, которая сохраняет содержимое сетки в файл Excel при нажатии. Aspose.Cells.GridWeb предлагает более простой подход к решению этой задачи. Aspose.Cells.GridWeb имеет событие SaveCommand. Приведенный выше фрагмент кода можно добавить в обработчик событий SaveCommand, который позволяет пользователям сохранять свою работу, щелкнув встроенный значок Aspose.Cells.GridWeb.**Сохранять** кнопка.

##  **Изменение размера Aspose.Cells.GridWeb и его панели заголовка**

В этой статье объясняется, как изменить размер GridWeb во время выполнения с помощью Aspose.Cells.GridWeb API. Также объясняется, как изменить размер заголовков элемента управления Aspose.Cells.GridWeb, чтобы их данные было легче читать.

###  **Изменение ширины и высоты Aspose.Cells.GridWeb**

Изменение ширины и высоты элемента управления Aspose.Cells.GridWeb — простая, но важная функция. Элемент управления Aspose.Cells.GridWeb представлен классом GridWeb в API. Чтобы изменить размер ширины и высоты элемента управления GridWeb, просто используйте его свойства ширины и высоты.

{{% alert color="primary" %}}

Ширина и высота элемента управления могут быть определены в пикселях или точках.

{{% /alert %}}

Вывод следующего фрагмента кода показан ниже.

**Изменена ширина и высота элемента управления GridWeb.**

![задача: image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

###  **Изменение ширины и высоты заголовка**

Aspose.Cells. Элемент управления GridWeb содержит две строки заголовка следующим образом:

- Верхняя панель заголовка. Эта панель заголовка представляет столбцы как A, B, C, D и т. д.
- Левая панель заголовка, эта панель заголовка представляет строки как 1, 2, 3, 4 и т. д.

Обе эти строки заголовков показаны ниже.

**Заголовки**

![задача: image_alt_text](working-with-gridweb_3.png)

Измените высоту верхней панели заголовка и ширину левой панели заголовка, используя свойства HeaderBarHeight и HeaderBarWidth элемента управления GridWeb соответственно. На рисунке ниже показаны выходные данные следующего примера кода.

**Изменена ширина и высота заголовка.**

![задача: image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

##  **Работа с событиями Aspose.Cells.GridWeb**

Все разработчики должны быть знакомы с событиями и их целью. События используются для отправки уведомлений об изменениях, которые могут произойти в элементе управления или классе. Aspose.Cells.GridWeb имеет несколько событий, которые можно использовать для выполнения определенных задач при возникновении определенных изменений в элементе управления.

В этом разделе представлены общие сведения обо всех событиях, поддерживаемых элементом управления Aspose.Cells.GridWeb, а также некоторые сведения о том, как обрабатывать эти события.

###  **Введение в события сетки**

Aspose.Cells. Элемент управления GridWeb поддерживает несколько событий, которые обеспечивают больший контроль над выполнением операций при запуске определенных событий в элементе управления. Полный список событий, поддерживаемых элементом управления Aspose.Cells.GridWeb, можно найти ниже.

|**События**|**Описание**|
| :- | :- |
|ЯчейкаКоманда|Происходит при щелчке командной гиперссылки ячейки. Когда это событие запускается, его параметр e.Argument предоставляет имя команды.|
|ЯчейкаDoubleClick|Происходит при двойном щелчке ячейки.|
|Столбец удален|Происходит, когда пользователь удаляет столбец с листа с помощью клиентского меню.|
|Удаление столбца|Происходит, когда пользователь пытается удалить столбец с листа с помощью клиентского меню.|
|СтолбецDoubleClick|Происходит при двойном щелчке заголовка столбца.|
|СтолбецВставлен|Происходит, когда пользователь вставляет столбец в лист с помощью клиентского меню.|
|ПользовательскаяКоманда|Происходит, когда пользователь нажимает пользовательскую командную кнопку.|
|Лоадкустомдата|Происходит, когда для свойства EnableSession элемента управления установлено значение false и необходимо загрузить данные листа. Вы можете обработать это событие в бессеансовом режиме, чтобы загрузить данные листа из файла или базы данных.|
|PageIndexChanged|Происходит при изменении индекса страницы листа элемента управления.|
|СтрокаDeleted|Происходит, когда пользователь удаляет строку с листа с помощью клиентского меню.|
|Удаление строки|Происходит, когда пользователь пытается удалить строку из листа с помощью клиентского меню.|
|СтрокаDoubleClick|Происходит при двойном щелчке заголовка строки.|
|строка вставлена|Происходит, когда пользователь вставляет строку в лист с помощью клиентского меню.|
|СохранитьКоманду| Происходит, когда**Сохранять** кнопка нажата.|
|ЛистTabНажмите|Происходит при нажатии на вкладку листа.|
|Отправитькоманду| Происходит, когда**Представлять на рассмотрение** кнопка нажата.|
|Отменитькоманду| Происходит, когда**Отменить** кнопка нажата.|
|AjaxCallЗавершен|Срабатывает, когда обновление AJAX элемента управления завершено. (для EnableAJAX должно быть установлено значение true).|
|CellModifiedOnAjax|Срабатывает, когда ячейка изменяется при вызове AJAX.|
|AfterColumnFilter|Срабатывает, когда фильтр применяется к столбцу.|

###  **Обработка событий сетки**

Чтобы выполнить определенную операцию по запуску определенного события, нам необходимо создать обработчик событий. Обработчик событий выполняет желаемую задачу при возникновении определенного события. В следующем примере показано, как обрабатывать простое событие сетки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

##  **Работа с событиями двойного щелчка**

Aspose.Cells.GridWeb содержит три типа событий двойного щелчка:

- CellDoubleClick, вызывается при двойном щелчке по ячейке.
- ColumnDoubleClick, вызывается при двойном щелчке заголовка столбца.
- RowDoubleClick, вызывается при двойном щелчке заголовка строки.

В этом разделе обсуждается, как включить события двойного щелчка в Aspose.Cells.GridWeb. Также обсуждается создание обработчиков для этих событий.

###  **Включение событий двойного щелчка**

Все типы событий двойного щелчка можно включить на стороне клиента, установив для свойства EnableDoubleClickEvent элемента управления GridWeb значение true.

{{% alert color="primary" %}}

По умолчанию для свойства EnableDoubleClickEvent установлено значение false. Это означает, что события двойного щелчка по умолчанию не включены. Чтобы реализовать такие события, сначала включите эту функцию.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

После включения событий двойного щелчка можно создавать обработчики событий для любых событий двойного щелчка. Эти обработчики событий выполняют определенные задачи при возникновении определенного события двойного щелчка.

###  **Обработка событий двойного щелчка**

####  **Двойной клик Cell**

Обработчик событий CellDoubleClick предоставляет аргумент типа CellEventArgs, который предоставляет полную информацию о ячейке, по которой выполняется двойной щелчок.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

####  **Двойной щелчок по заголовку столбца**

Обработчик события ColumnDoubleClick предоставляет аргумент типа RowColumnEventArgs, который предоставляет индексный номер столбца для заголовка, по которому был выполнен двойной щелчок, и другую информацию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

####  **Двойной щелчок по заголовку строки**

Обработчик события RowDoubleClick предоставляет аргумент типа RowColumnEventArgs, который предоставляет индексный номер строки для заголовка, по которому был выполнен двойной щелчок, и другую соответствующую информацию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

##  **Настройка стиля или внешнего вида Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb имеет собственный внешний вид по умолчанию, но его внешний вид можно изменить. Aspose.Cells.GridWeb предоставляет несколько свойств, позволяющих разработчикам полностью контролировать его внешний вид. В этом разделе обсуждаются некоторые из этих свойств.

###  **Настройка стиля или внешнего вида Aspose.Cells.GridWeb**

####  **Предустановленные стили**

Чтобы сэкономить усилия разработчиков, Aspose.Cells.GridWeb предлагает несколько предустановленных стилей. Просто выберите стиль из списка, чтобы применить его.

|**Стили**|**Цветовая схема**|
| :- | :- |
|Стандартный|Серебро|
|Красочный1|Роза|
|Красочный2|Синий|
|Профессионал1|Голубой|
|Профессионал2|снова циан|
|Традиционный1|Темный|
|Традиционный2|Серый|
|Обычай|Индивидуальные|
Когда выбран определенный стиль, он меняет весь внешний вид элемента управления GridWeb. Разработчики могут выбрать предустановленный стиль, который будет применяться во время выполнения, используя гибкий API из Aspose.Cells.GridWeb.

Элемент управления GridWeb предоставляет свойство PresetStyle, которому разработчики могут назначить любой желаемый заранее заданный стиль.

Вывод приведенного ниже фрагмента кода показан ниже.

**Элемент управления GridWeb с примененным к нему стилем Colorful1**

![задача: image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **Стиль заголовка**

Если вы посмотрите на элемент управления GridWeb, вы заметите две панели заголовков. Один для столбцов (то есть A, B, C, D и т. д.), а другой — для строк (то есть 1, 2, 3, 4 и т. д.). Aspose.Cells.GridWeb позволяет разработчикам контролировать внешний вид этих строк заголовков. Разработчики могут устанавливать стиль заголовков во время выполнения.

{{% alert color="primary" %}}

Элемент управления GridWeb предоставляет свойство HeaderBarStyle, которое применяет стиль к обеим полосам заголовков элемента управления.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **Стиль панели вкладок**

Также можно установить стиль панели вкладок. Пожалуйста, посмотрите следующий код

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

####  **Загрузка файла стиля**

Чтобы применить настройки стиля из существующего файла стиля к элементу управления GridWeb, разработчики могут указать путь к файлу стиля в свойстве CustomStyleFileName элемента управления. Но прежде чем это сделать, необходимо установить для свойства PresetStyle элемента управления значение Custom. Это связано с тем, что этот файл стиля содержит информацию о пользовательском стиле, уже определенную разработчиком.

См. следующее изображение, на котором показан GridWeb с примененным к нему пользовательским стилем.

![задача: image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

ВАЖНО: Загрузка файла стиля в элемент управления GridWeb не влияет на параметры форматирования ячеек элемента управления.

{{% /alert %}}

####  **Пример шаблона пользовательского стиля**

Вот пример шаблона пользовательского стиля. Вы можете изменить его в соответствии с вашими требованиями.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

##  **Создание элемента управления в веб-форме**

В этой статье вы узнаете, как создать простую веб-форму JSP (Java Серверная страница) с элементом управления GridWeb.

**Шаг 1 — Создайте структуру каталогов**

 Вам необходимо создать следующую структуру каталогов в**веб-приложения**каталог сервера Tomcat

![задача: image_alt_text](working-with-gridweb_7.png)

 Это каталоги и файлы, которые вам нужно создать. Пожалуйста, читайте комментарии и подписывайтесь на них. Вы можете получить последние архивы выпусков Aspose.Cells.GridWeb for Java по адресу[эта ссылка](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

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

**Шаг 2. Добавление кодов в созданные файлы**

В этом разделе показан код для различных файлов, созданных в указанной выше структуре каталогов. Получите эти коды и добавьте их в свои файлы, открыв их в Блокноте и скопировав/вставив.

**Веб.xml**

{{< highlight "java" >}}

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

{{< highlight "java" >}}

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

**Шаг 3. Запуск образца веб-страницы JSP**

Теперь вы все сделали. Пришло время запустить веб-страницу. Запустите сервер Tomcat и вставьте следующий URL-адрес в веб-браузер.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Вы увидите что-то вроде следующего скриншота. Поздравляем, вы успешно использовали элемент управления GridWeb на своей странице JSP.

![задача: image_alt_text](working-with-gridweb_8.png)

##  **Печать GridWeb**

Бывают случаи, когда разработчикам необходимо распечатать содержимое GridWeb, включенное в веб-страницу, без сохранения файла Excel Microsoft. Элемент управления Aspose.Cells.GridWeb поддерживает эту функцию.

###  **Печать GridWeb**

Чтобы распечатать без сохранения отдельного файла, вызовите метод print() класса GridWeb на стороне клиента, чтобы распечатать сетку. Вы также можете выбрать какое-нибудь подходящее мероприятие.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Поскольку вы вызываете его со стороны клиента, вам сначала нужно будет получить идентификатор клиента GridWeb. Вы можете получить идентификатор клиента, используя метод Gridweb.getClientID().

###  **Пример кода на стороне клиента**

См. следующую ссылку, которая вызывает метод Gridweb.print() со стороны клиента.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

##  **Введение в различные режимы сетки**

В этой статье описаны различные режимы Aspose.Cells.GridWeb. Эти режимы логически различаются из-за их различных функций и поведения. Мы определили различные типы режима:

- Режим редактирования
- Режим просмотра

Все эти режимы имеют свои особенности. Разработчики могут работать с Aspose.Cells.GridWeb в любом режиме по своему усмотрению. Ниже мы рассмотрим каждый режим.

###  **Режим редактирования**

По умолчанию элемент управления Aspose.Cells.GridWeb находится в режиме редактирования. В режиме редактирования вы можете полностью редактировать или изменять содержимое сетки, используя все функции, предлагаемые элементом управления Aspose.Cells.GridWeb. Эти функции включают в себя:

- Сохранение содержимого сетки в файлы Excel Microsoft.
- Отправка данных на сервер.
- Расчетные формулы.
- Отмена или отказ от предыдущих действий.
- Управление строками и столбцами.
- Вырезание, копирование или вставка данных.
- Форматирование ячеек и т. д.

**Элемент управления GridWeb в режиме редактирования**

![задача: image_alt_text](working-with-gridweb_9.png)

Разработчики также могут переключиться в режим редактирования программно, установив для свойства EditMode элемента управления GridWeb значение true.

###  **Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

###  **Режим просмотра**

Когда элемент управления GridWeb находится в режиме просмотра, пользователи не могут редактировать или изменять содержимое сетки. Это означает, что пользователи могут только просматривать содержимое сетки. Вот почему этот режим называется режимом просмотра. В режиме просмотра несколько кнопок (**Отправить**,**Сохранять** и**Отменить**) скрыты, а меню, которое появляется при щелчке правой кнопкой мыши, содержит только команду **Копировать.** и**Находить** вариант.

**Элемент управления GridWeb в режиме просмотра** 

![задача: image_alt_text](working-with-gridweb_10.png)

Если разработчики хотят, чтобы их пользователи могли только просматривать данные, они могут переключиться в режим просмотра программно, установив для свойства EditMode элемента управления GridWeb значение *false**.

###  **Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Даже в режиме просмотра пользователи могут изменять высоту и ширину строк и столбцов.

{{% /alert %}}
