---
title: Establecer sugerencia de encabezado de columna
type: docs
weight: 90
url: /es/java/set-column-header-tip/
---
## **Posibles escenarios de uso**
Es posible que deba configurar información sobre herramientas para su columna personalizada al crear la tabla en la hoja de trabajo. Aspose.Cells. GridWeb le permite cambiar el nombre del título de una columna y puede configurar la información sobre herramientas en la columna, para que los usuarios puedan entender fácilmente para qué sirve la columna.
## **Configuración de la sugerencia de encabezado de columna**
A continuación se proporciona un ejemplo completo para demostrar cómo cambiar los títulos de las columnas y aplicar texto de información sobre herramientas. Después de ejecutar el código de ejemplo, el texto de información sobre herramientas aparecerá cuando coloque el cursor del mouse sobre el encabezado de la columna especificada.

## **Código de muestra**
Aquí está el código de muestra del**prueba.jsp** expediente.

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
