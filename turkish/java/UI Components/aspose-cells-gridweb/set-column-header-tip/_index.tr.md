---
title: Sütun Başlığı İpucunu Ayarla
type: docs
weight: 90
url: /tr/java/set-column-header-tip/
---
## **Olası Kullanım Senaryoları**
Çalışma sayfasında tabloyu oluştururken özel sütununuz için araç ipucu ayarlamanız gerekebilir. Aspose.Cells.GridWeb, bir sütunun başlığını yeniden adlandırmanıza izin verir ve sütuna araç ipucu ayarlayabilirsiniz, böylece kullanıcılar sütunun ne için olduğunu kolayca anlayabilir.
## **Ayar Sütun Başlığı İpucu**
Sütun başlıklarının nasıl değiştirileceğini ve araç ipucu metninin nasıl uygulanacağını göstermek için aşağıda eksiksiz bir örnek verilmiştir. Örnek kodu yürüttükten sonra, fare imlecini belirtilen sütun başlığının üzerine getirdiğinizde araç ipucu metni çıkar.

## **Basit kod**
İşte örnek kod**test.jsp** dosya.

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
