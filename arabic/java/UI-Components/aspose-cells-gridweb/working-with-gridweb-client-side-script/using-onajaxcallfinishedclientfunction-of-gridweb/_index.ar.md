---
title: استخدام OnAjaxCallFinishedClientFunction من GridWeb
type: docs
weight: 20
url: /ar/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **سيناريوهات الاستخدام المحتملة**
OnAjaxCallFinishedClientFunction هو وظيفة جانب العميل يتم استدعاؤها عندما يقوم المستخدم بنسخ بعض البيانات إلى ورقة عمل GridWeb. تكون هذه الوظيفة مفيدة عندما يتم تحديث الخلايا بكميات كبيرة وترغب في تتبع تلك الخلايا المحدثة في الجانب العميل (على سبيل المثال في متصفحات الويب مثل FireFox و Google Chrome وما إلى ذلك).
## **استخدام OnAjaxCallFinishedClientFunction من GridWeb**
الرمز البرمجي المعروض أدناه يشرح كيفية الاستفادة من وظيفة العميل OnAjaxCallFinishedClientFunction. تظهر اللقطات الشاشة لمخرجات الكونسول في Google Chrome و FireFox عند تنفيذ الكود. بمجرد تنفيذ الكود ، يرجى نسخ / لصق بعض البيانات تمتد عبر عدة خلايا داخل ورقة العمل GridWeb ثم التحقق من كونسول متصفح الويب كما هو موضح في اللقطات.
## **مخرجات كونسول Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **مخرجات كونسول FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **الكود المثالي**
{{< highlight java >}}

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
