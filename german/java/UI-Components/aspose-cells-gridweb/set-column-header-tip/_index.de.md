---
title: Spaltentooltip festlegen
type: docs
weight: 90
url: /de/java/set-column-header-tip/
---

## **Mögliche Verwendungsszenarien**
Es besteht die Möglichkeit, beim Erstellen der Tabelle im Arbeitsblatt einen Tooltip für Ihre benutzerdefinierte Spalte festzulegen. Aspose.Cells.GridWeb ermöglicht es Ihnen, die Beschriftung einer Spalte umzubenennen und einen Tooltip für die Spalte festzulegen, sodass die Benutzer leicht verstehen können, wofür die Spalte dient.
## **Spaltentooltip festlegen**
Nachfolgend wird ein vollständiges Beispiel gegeben, um zu demonstrieren, wie Spaltenüberschriften geändert und Tooltip-Text angewendet wird. Nach Ausführung des Beispielcodes wird der Tooltip-Text angezeigt, wenn Sie den Mauszeiger über die angegebene Spaltenüberschrift bewegen.

## **Beispielcode**
Hier ist der Beispielcode der Datei **test.jsp**.

{{< highlight java >}}

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
