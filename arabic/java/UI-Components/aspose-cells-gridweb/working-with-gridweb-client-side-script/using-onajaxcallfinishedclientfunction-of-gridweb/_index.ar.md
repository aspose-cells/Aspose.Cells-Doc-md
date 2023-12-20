---
title: استخدام وظيفة OnAjaxCallFinishedClient في GridWeb
type: docs
weight: 20
url: /ar/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **سيناريوهات الاستخدام الممكنة**
OnAjaxCallFinishedClientFunction هي وظيفة من جانب العميل تسمى عندما ينسخ المستخدم بعض البيانات إلى ورقة عمل GridWeb. هذه الوظيفة مفيدة عندما يتم تحديث الجزء الأكبر من الخلايا وتريد تتبع تلك الخلايا المحدثة من جانب العميل (على سبيل المثال في متصفحات الويب مثل FireFox و Google Chrome وما إلى ذلك).
## **استخدام وظيفة OnAjaxCallFinishedClient في GridWeb**
يوضح نموذج التعليمات البرمجية التالي كيفية الاستفادة من وظيفة العميل OnAjaxCallFinishedClientFunction. تُظهر لقطات الشاشة إخراج وحدة التحكم في Google Chrome و FireFox عند تنفيذ الكود. بمجرد تنفيذ التعليمات البرمجية ، يرجى نسخ / لصق بعض البيانات التي تمتد عبر خلايا متعددة داخل ورقة عمل GridWeb ثم التحقق من وحدة تحكم متصفح الويب كما هو موضح في لقطات الشاشة.
## **Google إخراج وحدة تحكم كروم**
![ما يجب القيام به: image_بديل_نص](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **إخراج وحدة تحكم FireFox**
![ما يجب القيام به: image_بديل_نص](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **عينة من الرموز**
{{< highlight "java" >}}

 <%@page language="java" contentType="text/html; charset=UTF-8" import="com.aspose.gridweb.*"  pageEncoding="UTF-8"%>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript" src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript" src="grid/acw_client/lang_en.js"></script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<script type="text/javascript">



    var updateCells = new Array();



    function TestAjaxCallFinish()

    {





        for (var i = 0; i < updateCells.length; i++) {

            console.log("updated:" + toString(this,updateCells[i]));

        }

        updateCells = [];

    }

    function CellUpdate(cell) {

        var id = updateCells.length;

        updateCells[id++] = cell;

    }

    function toString(gridweb,cell) {

        return gridweb.getCellName(cell) +

            ",value is:" +

            gridweb.getCellValueByCell(cell) +

            " ,row:" +

            gridweb.getCellRow(cell) +

            ",col:" +

            gridweb.getCellColumn(cell);

    }

</script>

<title>Aspose.Cells.GridWeb for Java - Sample JSP Page</title>

<%

//Print GridWeb version on Console

System.out.println("Aspose.Cells.GridWeb for Java Version: " + GridWebBean.getVersion());

ExtPage BeanManager=ExtPage.getInstance();

GridWebBean gridweb=BeanManager.getBean(request);

out.println(gridweb.getHTMLHead());

%>

</head>

<body>

<%

gridweb.setReqRes(request, response);

gridweb.setEnableAJAX(true);

gridweb.setOnAjaxCallFinishedClientFunction("TestAjaxCallFinish");

gridweb.setOnCellUpdatedClientFunction("CellUpdate");

gridweb.setWidth(Unit.Pixel(600));

gridweb.setHeight(Unit.Pixel(400));

gridweb.prepareRender();

out.print(gridweb.getHTMLBody());

%>

</body>

</html>

{{< /highlight >}}
