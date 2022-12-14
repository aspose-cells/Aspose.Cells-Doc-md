---
title: تعيين تلميح رأس العمود
type: docs
weight: 90
url: /ar/java/set-column-header-tip/
---
## **سيناريوهات الاستخدام الممكنة**
قد تحتاج إلى تعيين تلميح الأدوات لعمودك المخصص أثناء إنشاء الجدول في ورقة العمل. Aspose.Cells.GridWeb يسمح لك بإعادة تسمية التسمية التوضيحية للعمود ويمكنك تعيين تلميح الأدوات على العمود ، حتى يتمكن المستخدمون من فهم الغرض من العمود بسهولة.
## **إعداد تلميح رأس العمود**
فيما يلي مثال كامل لشرح كيفية تغيير تسميات الأعمدة وتطبيق نص تلميح الأدوات. بعد تنفيذ رمز المثال ، سيظهر نص تلميح الأداة عند وضع مؤشر الماوس فوق رأس العمود المحدد.

## **عينة من الرموز**
هنا هو نموذج التعليمات البرمجية لملف**test.jsp** ملف.

{{< highlight "java" >}}

 <%@ page language="java" contentType="text/html; charset=UTF-8"

 import="com.aspose.gridweb.*" pageEncoding="UTF-8"%>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Setting Column Header ToolTip</title>

<%

ExtPage BeanManager=ExtPage.getInstance();

GridWebBean gridweb=BeanManager.getBean(request);

out.println(gridweb.getHTMLHead());

%>

</head>

<BODY>



<%

gridweb.setReqRes(request, response);

gridweb.setEnableAsync(false);

//Access the first worksheet

GridWorksheet gridSheet = gridweb.getWorkSheets().get(0);

//Input data into the cells of the first worksheet.

gridSheet.getCells().get("A1").putValue("Product1");

gridSheet.getCells().get("A2").putValue("Product2");

gridSheet.getCells().get("A3").putValue("Product3");

gridSheet.getCells().get("A4").putValue("Product4");

gridSheet.getCells().get("B1").putValue(100);

gridSheet.getCells().get("B2").putValue(200);

gridSheet.getCells().get("B3").putValue(300);

gridSheet.getCells().get("B4").putValue(400);

//Set the caption of the first two columns.

gridSheet.setColumnCaption(0, "Product Name");

gridSheet.setColumnCaption(1, "Price");

//Set the column width of the first column.

gridSheet.getCells().setColumnWidth(0, 20);

//Set the second column header's tip.

gridSheet.setColumnHeaderToolTip(1, "Unit Price of Products");

gridweb.prepareRender();

out.println(gridweb.getHTMLBody());

%>

<br>



</BODY>

</html>

{{< /highlight >}}
