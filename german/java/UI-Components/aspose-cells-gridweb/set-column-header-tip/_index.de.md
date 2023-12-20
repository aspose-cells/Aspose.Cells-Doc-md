---
title: Setzen Sie den Tipp für die Spaltenüberschrift
type: docs
weight: 90
url: /de/java/set-column-header-tip/
---
## **Mögliche Nutzungsszenarien**
Möglicherweise müssen Sie QuickInfos für Ihre benutzerdefinierte Spalte festlegen, während Sie die Tabelle im Arbeitsblatt erstellen. Aspose.Cells.GridWeb ermöglicht es Ihnen, die Beschriftung einer Spalte umzubenennen, und Sie können QuickInfos für die Spalte festlegen, damit die Benutzer leicht verstehen können, wofür die Spalte ist.
## **Tipp zum Einstellen der Spaltenüberschrift**
Nachfolgend finden Sie ein vollständiges Beispiel, um zu demonstrieren, wie Sie die Spaltenbeschriftungen ändern und QuickInfo-Text anwenden. Nach dem Ausführen des Beispielcodes wird QuickInfo-Text eingeblendet, wenn Sie den Mauszeiger über die Kopfzeile der angegebenen Spalte platzieren.

## **Beispielcode**
Hier ist der Beispielcode der**test.jsp** Datei.

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
