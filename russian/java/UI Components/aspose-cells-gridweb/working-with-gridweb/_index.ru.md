---
title: Работа с GridWeb
type: docs
weight: 20
url: /ru/java/working-with-gridweb/
---
## **Открытие файла Excel Microsoft**

Aspose.Cells. Элемент управления GridWeb может открывать и загружать Microsoft файлы Excel — с данными, форматированием, диаграммами, изображениями и т. д. В этом разделе объясняется, как это сделать.

Чтобы открыть файл Excel с помощью элемента управления GridWeb:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или на страницу.
1. Импортируйте файл Excel, указав путь к файлу.
1. Запустите приложение или откройте страницу.

Чтобы загрузить содержимое из файла Excel в элемент управления Aspose.Cells.GridWeb, необходимо вызвать метод importExcelFile, чтобы указать путь к файлу Excel. После этого элемент управления GridWeb автоматически найдет файл по указанному пути и отобразит в нем свое содержимое. Фрагмент кода, который загружает содержимое файла Excel, приведен ниже.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Приведенный выше фрагмент кода можно использовать как угодно. Например, чтобы автоматически загружать файл Excel при загрузке веб-формы, добавьте этот код в событие Page_Load формы, которое вы указали сами.

**Файл Excel загружается в GridWeb**

![дело:изображение_альтернативный_текст](working-with-gridweb_1.png)

## **Сохранение файла Excel Microsoft**

Можно создавать новые или управлять существующими Microsoft файлами Excel на веб-сайтах в режиме графического интерфейса с помощью элемента управления Aspose.Cells.GridWeb. Затем файлы можно сохранить в файлы Excel. Aspose.Cells.GridWeb эффективно служит онлайн-редактором электронных таблиц. В этом разделе описывается, как сохранить содержимое сетки в файлы Excel.

### **Сохранение в виде файла**

Чтобы сохранить содержимое элемента управления Aspose.Cells.GridWeb в виде файла Excel:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму или на страницу.
1. Сохраните свою работу в виде файла Excel по указанному пути.
1. Запустите приложение или откройте страницу.

В приведенном ниже примере кода показано, как сохранить содержимое сетки в файл Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Приведенный выше фрагмент кода можно использовать несколькими способами. Распространенным способом является добавление кнопки, которая при нажатии сохраняет содержимое сетки в файл Excel. Aspose.Cells.GridWeb предлагает более простой подход к решению этой задачи. Aspose.Cells. В GridWeb есть событие SaveCommand. Приведенный выше фрагмент кода можно добавить в обработчик события SaveCommand, который позволяет пользователям сохранять свою работу, щелкнув встроенную кнопку Aspose.Cells.GridWeb.**Сохранять** кнопка.

## **Изменение размера Aspose.Cells.GridWeb и его панели заголовка**

В этой статье объясняется, как изменить размер GridWeb во время выполнения с помощью Aspose.Cells.GridWeb API. Также объясняется, как изменить размер строк заголовков элемента управления Aspose.Cells.GridWeb, чтобы их данные было легче читать.

### **Изменение ширины и высоты Aspose.Cells.GridWeb**

Изменение ширины и высоты элемента управления Aspose.Cells.GridWeb — простая, но важная функция. Элемент управления Aspose.Cells.GridWeb представлен классом GridWeb в API. Чтобы изменить ширину и высоту элемента управления GridWeb, просто используйте его свойства ширины и высоты.

{{% alert color="primary" %}}

Ширина и высота элемента управления могут быть определены в пикселях или точках.

{{% /alert %}}

Вывод следующего фрагмента кода показан ниже.

**Изменена ширина и высота элемента управления GridWeb.**

![дело:изображение_альтернативный_текст](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Изменение ширины и высоты панели заголовка**

Aspose.Cells. Элемент управления GridWeb содержит две следующие строки заголовка:

- Верхняя панель заголовка, эта панель заголовка представляет столбцы A, B, C, D и т. д.
- Левая панель заголовка, эта панель заголовка представляет строки как 1, 2, 3, 4 и т. д.

Обе эти строки заголовка показаны ниже.

**Заголовки**

![дело:изображение_альтернативный_текст](working-with-gridweb_3.png)

Измените высоту верхней панели заголовка и ширину левой панели заголовка, используя свойства HeaderBarHeight и HeaderBarWidth элемента управления GridWeb соответственно. На рисунке ниже показан вывод следующего примера кода.

**Изменена ширина и высота панели заголовка**

![дело:изображение_альтернативный_текст](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Работа с событиями Aspose.Cells.GridWeb**

Все разработчики должны быть знакомы с событиями и их назначением. События используются для отправки уведомлений об изменениях, которые могут произойти в элементе управления или классе. Aspose.Cells.GridWeb имеет несколько событий, которые можно использовать для выполнения определенных задач, когда в элементе управления происходят определенные изменения.

В этом разделе представлены общие сведения обо всех событиях, поддерживаемых элементом управления Aspose.Cells.GridWeb, а также некоторые сведения о том, как обрабатывать эти события.

### **Введение в грид-события**

Aspose.Cells. Элемент управления GridWeb поддерживает несколько событий, обеспечивающих больший контроль над выполнением операций, когда в элементе управления инициируются определенные события. Полный список событий, поддерживаемых элементом управления Aspose.Cells.GridWeb, можно найти ниже.

|**События**|**Описание**|
|:- |:- |
|CellCommand|Происходит при щелчке командной гиперссылки ячейки. Когда это событие запускается, его параметр e.Argument предоставляет имя команды.|
|CellDoubleClick|Происходит при двойном щелчке ячейки.|
|Колонка удалена|Происходит, когда пользователь удаляет столбец с рабочего листа с помощью клиентского меню.|
|Удаление столбца|Происходит, когда пользователь пытается удалить столбец из листа с помощью клиентского меню.|
|КолонкаDoubleClick|Происходит при двойном щелчке заголовка столбца.|
|Колонка вставлена|Происходит, когда пользователь вставляет столбец на лист с помощью клиентского меню.|
|Пользовательская команда|Происходит, когда пользователь нажимает пользовательскую командную кнопку.|
|ЛоадКастомдата|Происходит, когда для свойства EnableSession элемента управления задано значение false и требуется загрузить данные рабочего листа. Вы можете обработать это событие в режиме без сеанса, чтобы загрузить данные рабочего листа из файла или базы данных.|
|PageIndexChanged|Происходит при изменении индекса страницы листа элемента управления.|
|RowDeleted|Происходит, когда пользователь удаляет строку с рабочего листа с помощью клиентского меню.|
|Удаление строки|Происходит, когда пользователь пытается удалить строку из листа с помощью клиентского меню.|
|СтрокаDoubleClick|Происходит при двойном щелчке заголовка строки.|
|Ровинсертед|Происходит, когда пользователь вставляет строку на лист с помощью клиентского меню.|
|СохранитьКоманда| Возникает, когда**Сохранять** кнопка нажата.|
|ЛистВкладкаКлик|Происходит при щелчке вкладки листа.|
|Отправить команду| Возникает, когда**Представлять на рассмотрение** кнопка нажата.|
|Отменить команду| Возникает, когда**Отменить** кнопка нажата.|
|AjaxCallFinished|Срабатывает, когда AJAX-обновление элемента управления завершено. (для параметра EnableAJAX должно быть установлено значение true).|
|CellModifiedOnAjax|Срабатывает, когда ячейка изменяется в вызове AJAX.|
|AfterColumnFilter|Срабатывает, когда фильтр применяется к столбцу.|

### **Обработка событий сетки**

Чтобы выполнить определенную операцию по запуску определенного события, мы должны создать обработчик события. Обработчик событий выполняет желаемую задачу, когда запускается определенное событие. В следующем примере показано, как обрабатывать простое событие сетки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Работа с событиями двойного щелчка**

Aspose.Cells.GridWeb содержит три типа событий двойного щелчка:

- CellDoubleClick, срабатывает при двойном щелчке по ячейке.
- ColumnDoubleClick, срабатывает при двойном щелчке заголовка столбца.
- RowDoubleClick, срабатывает при двойном щелчке заголовка строки.

В этом разделе обсуждается, как включить события двойного щелчка в Aspose.Cells.GridWeb. Также обсуждается создание обработчиков событий для этих событий.

### **Включение событий двойного щелчка**

Все типы событий двойного щелчка можно включить на стороне клиента, задав для свойства EnableDoubleClickEvent элемента управления GridWeb значение true.

{{% alert color="primary" %}}

По умолчанию для свойства EnableDoubleClickEvent установлено значение false. Это означает, что события двойного щелчка не включены по умолчанию. Чтобы реализовать такие события, сначала включите эту функцию.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

После включения событий двойного щелчка можно создавать обработчики событий для любых событий двойного щелчка. Эти обработчики событий выполняют определенные задачи, когда запускается данное событие двойного щелчка.

### **Обработка событий двойного щелчка**

#### **Двойной щелчок Cell**

Обработчик события CellDoubleClick предоставляет аргумент типа CellEventArgs, предоставляющий полную информацию о ячейке, по которой выполняется двойной щелчок.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Двойной щелчок по заголовку столбца**

Обработчик событий для события ColumnDoubleClick предоставляет аргумент типа RowColumnEventArgs, предоставляющий порядковый номер столбца для заголовка, по которому был выполнен двойной щелчок, и другую информацию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Двойной щелчок по заголовку строки**

Обработчик событий для события RowDoubleClick предоставляет аргумент типа RowColumnEventArgs, предоставляющий порядковый номер строки для заголовка, по которому был выполнен двойной щелчок, и другую связанную информацию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Настройка стиля или внешнего вида Aspose.Cells.GridWeb**

Aspose.Cells. GridWeb имеет собственный внешний вид по умолчанию, но его внешний вид можно изменить. Aspose.Cells.GridWeb предоставляет несколько свойств, позволяющих разработчикам полностью контролировать его внешний вид. В этом разделе обсуждаются некоторые из этих свойств.

### **Настройка стиля или внешнего вида Aspose.Cells.GridWeb**

#### **Предустановленные стили**

Чтобы сэкономить усилия разработчиков, Aspose.Cells.GridWeb предлагает несколько предустановленных стилей. Просто выберите стиль из списка, чтобы применить стиль.

|**Стили**|**Цветовая схема**|
|:- |:- |
|Стандарт|Серебряный|
|Красочный1|Роза|
|Красочный2|Синий|
|Профессиональный1|Голубой|
|Профессиональный2|Снова голубой|
|Традиционный1|Темный|
|Традиционный2|Серый|
|Обычай|Индивидуальные|
При выборе определенного стиля изменяется весь внешний вид элемента управления GridWeb. Разработчики могут выбрать предустановленный стиль, который будет применяться во время выполнения, используя гибкий API из Aspose.Cells.GridWeb.

Элемент управления GridWeb предоставляет свойство PresetStyle, которому разработчики могут назначать любой желаемый предустановленный стиль.

Вывод приведенного ниже фрагмента кода показан ниже.

**Элемент управления GridWeb с примененным к нему стилем Colorful1**

![дело:изображение_альтернативный_текст](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Стиль заголовка**

Если вы посмотрите на элемент управления GridWeb, вы заметите две полосы заголовка. Один для столбцов (то есть A, B, C, D и т. д.), а другой для строк (то есть 1, 2, 3, 4 и т. д.). Aspose.Cells.GridWeb позволяет разработчикам управлять внешним видом этих заголовков. Разработчики могут установить стиль заголовков во время выполнения.

{{% alert color="primary" %}}

Элемент управления GridWeb предоставляет свойство HeaderBarStyle, которое применяет стиль к обеим полосам заголовков элемента управления.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Стиль панели вкладок**

Также можно установить стиль панели вкладок. См. следующий код

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Загрузка файла стиля**

Чтобы применить параметры стиля из существующего файла стиля к элементу управления GridWeb, разработчики могут указать путь к файлу стиля в свойстве CustomStyleFileName элемента управления. Но перед этим необходимо установить для свойства PresetStyle элемента управления значение Custom. Это связано с тем, что этот файл стиля содержит информацию о пользовательском стиле, которая уже определена разработчиком.

См. следующее изображение, на котором показан GridWeb с примененным к нему пользовательским стилем.

![дело:изображение_альтернативный_текст](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

ВАЖНО. Загрузка файла стиля в элемент управления GridWeb не влияет на параметры форматирования ячеек элемента управления.

{{% /alert %}}

#### **Образец пользовательского шаблона стиля**

Вот пример шаблона пользовательского стиля. Вы можете изменить его в соответствии с вашими требованиями.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Создание элемента управления в веб-форме**

В этой статье вы узнаете, как создать простую веб-форму JSP (страница сервера Java) с элементом управления GridWeb.

**Шаг 1 — Создайте структуру каталогов**

 Вам необходимо создать следующую структуру каталогов в**веб-приложения**каталог сервера Tomcat

![дело:изображение_альтернативный_текст](working-with-gridweb_7.png)

 Это каталоги и файлы, которые вам нужно создать. Пожалуйста, читайте комментарии и следите за ними. Вы можете получить последние выпуски Aspose.Cells.GridWeb for Java из[эта ссылка](https://downloads.aspose.com/cells/java).

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

**Шаг 2 — Добавление кодов в созданные файлы**

В этом разделе показан код для различных файлов, созданных в приведенной выше структуре каталогов. Пожалуйста, получите эти коды и добавьте их в свои файлы, открыв их в Блокноте и скопировав/вставив их.

**Web.xml**

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

**голова.jsp**

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

**Шаг 3. Запуск примера веб-страницы JSP**

Теперь вы сделали все. Пришло время запустить веб-страницу. Пожалуйста, запустите свой сервер Tomcat, а затем вставьте следующий URL-адрес в веб-браузер.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Вы увидите что-то вроде следующего скриншота. Поздравляем, вы успешно использовали элемент управления GridWeb на своей странице JSP.

![дело:изображение_альтернативный_текст](working-with-gridweb_8.png)

## **Печать GridWeb**

Бывают случаи, когда разработчикам необходимо распечатать содержимое GridWeb, включенное в веб-страницу, без сохранения файла Excel Microsoft. Эта функция поддерживается элементом управления Aspose.Cells.GridWeb.

### **Печать GridWeb**

Чтобы распечатать без сохранения отдельного файла, вызовите метод print() класса GridWeb на стороне клиента, чтобы напечатать сетку. Вы также можете выбрать подходящее событие.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Поскольку вы вызываете его со стороны клиента, вам сначала нужно будет получить идентификатор клиента gridweb. Вы можете получить идентификатор клиента, используя метод gridweb.getClientID().

### **Пример кода на стороне клиента**

См. следующую ссылку, которая вызывает метод gridweb.print() со стороны клиента.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Введение в различные режимы сетки**

В этой статье описываются различные режимы Aspose.Cells.GridWeb. Эти режимы логически различаются из-за их различных функций и поведения. Мы определили различные типы режима:

- Режим редактирования
- Режим просмотра

Все эти режимы имеют свои особенности. Разработчики могут работать с Aspose.Cells.GridWeb в любом режиме в соответствии со своими требованиями. Ниже мы рассмотрим каждый режим.

### **Режим редактирования**

По умолчанию элемент управления Aspose.Cells.GridWeb находится в режиме редактирования. В режиме редактирования вы можете полностью редактировать или изменять содержимое сетки, используя все функции, предлагаемые элементом управления Aspose.Cells.GridWeb. Эти функции включают в себя:

- Сохранение содержимого сетки в файлы Excel Microsoft.
- Отправка данных на сервер.
- Расчетные формулы.
- Отмена или отказ от предыдущих действий.
- Управление строками и столбцами.
- Вырезание, копирование или вставка данных.
- Форматирование ячеек и т.д.

**Элемент управления GridWeb в режиме редактирования**

![дело:изображение_альтернативный_текст](working-with-gridweb_9.png)

Разработчики также могут переключиться в режим редактирования программно, задав для свойства EditMode элемента управления GridWeb значение true.

### **Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Режим просмотра**

Когда элемент управления GridWeb находится в режиме просмотра, пользователи не могут редактировать или изменять содержимое сетки, что означает, что пользователи могут только просматривать содержимое сетки. Вот почему этот режим называется режимом просмотра. В режиме просмотра несколько кнопок (**Представлять на рассмотрение**, **Сохранять** а также**Отменить** ) скрыты, а меню, которое появляется при щелчке правой кнопкой мыши, содержит только**Копировать** а также**Находить** вариант.

**Элемент управления GridWeb в режиме просмотра** 

![дело:изображение_альтернативный_текст](working-with-gridweb_10.png)

 Если разработчики хотят, чтобы их пользователи только просматривали данные, они могут программно переключиться в режим просмотра, задав для свойства EditMode элемента управления GridWeb значение**ЛОЖЬ**.

### **Пример кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Даже в режиме просмотра пользователи могут изменять высоту и ширину строк и столбцов.

{{% /alert %}}
