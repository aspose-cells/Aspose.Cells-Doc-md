---
title : "Set Column Header Tip" 
description : "" 
weight : 12335 
toc : false
type: docs
url: /java/developerguide/gridweb/set+column+header+tip/
---

# Aspose.Cells for Java : Set Column Header Tip


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Setting Column Header Tip](#setting-column-header-tip)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

 

## Possible Usage Scenarios

You might need to set tooltip for your custom column while creating the table in the worksheet. Aspose.Cells.GridWeb allows you to rename a column's caption and you may set tooltip to the column, so the users could easily understand what is the column for.

## Setting Column Header Tip

A complete example is given below to demonstrate how to change columns' captions and apply tooltip text. After executing the example code, tooltip text would be popped out when you place the mouse cursor over the specified column's header as shown below.

![image](https://docs2.aspose.com/cells/java/attachments/45908471/46465025.png?effects=drop-shadow)

## Sample Code

Here is the sample code of the **test.jsp** file.

{{< code lang="cs" >}}
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
{{< /code >}}

