---
title: Использование Aspose.Cells for Java с ColdFusion
type: docs
weight: 40
url: /ru/java/using-aspose-cells-for-java-with-coldfusion/
---
{{% alert color="primary" %}}

В этой статье представлена основная информация и фрагменты кода, которые разработчикам ColdFusion необходимо использовать Aspose.Cells for Java в приложении ColdFusion.

В этой статье показано, как создать простую веб-страницу с помощью ColdFusion и использовать Aspose.Cells for Java для создания простого файла Excel.

{{% /alert %}}

## **Aspose.Cells: Настоящий продукт**

С Aspose.Cells разработчики могут экспортировать данные, форматировать электронные таблицы во всех деталях и на каждом уровне, импортировать изображения, импортировать диаграммы, создавать диаграммы, управлять диаграммами, передавать данные Excel Microsoft, сохранять в различных форматах, включая XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML. ([Aspose.Pdf](https://products.aspose.com/pdf/java/) комплексные) и многое другое.

 Чтобы узнать больше об информации о продукте, функциях и руководстве программиста, обратитесь к документации Aspose.Cells и онлайн-предложениям.[демо](https://github.com/aspose-cells/Aspose.Cells-for-Java) . Вы можете[скачать](https://downloads.aspose.com/cells/java) и оценить его бесплатно.

### **Предпосылки**

Чтобы использовать Aspose.Cells for Java в приложениях ColdFusion, скопируйте файл Aspose.Cells.jar в папку {InstallationFolder\\}\wwwroot\WEB-INF\lib.

Не забудьте перезапустить сервер приложений ColdFusion после помещения новых JAR-файлов в папку lib.

### **Использование Aspose.Cells for Java и ColdFusion для создания файла Excel**

Ниже мы создаем простое приложение, которое создает пустой файл Excel Microsoft, вставляет некоторый контент и сохраняет его как файл XLS.

Ниже приведен фактический код (ColdFusion и Aspose.Cells for Java). После выполнения кода создается файл Excel output.xls.

**Сгенерированный файл output.xls**

![дело:изображение_альтернативный_текст](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight "java" >}}

 <html>

<head><title>Hello World!</title></head>

<body>

    <b>This example shows how to create a simple MS Excel Workbook using Aspose.Cells</b>

    <cfset workbook=CreateObject("java", "com.aspose.cells.Workbook").init()>

    <cfset worksheets = workbook.getWorksheets()>

    <cfset sheet= worksheets.get("Sheet1")>

    <cfset cells= sheet.getCells()>

    <cfset cell= cells.getCell(0,0)>

    <cfset cell.setValue("Hello World!")>

    <cfset workbook.save("C:\output.xls")>

</body>

</html>

{{< /highlight >}}

## **Резюме**

{{% alert color="primary" %}}

В этой статье объясняется, как использовать Aspose.Cells for Java с ColdFusion.

Aspose.Cells предлагает большую гибкость и обеспечивает выдающуюся скорость, эффективность и надежность. Aspose.Cells стал результатом многолетних исследований, проектирования и тщательной настройки.

 Мы приветствуем вопросы, комментарии и предложения в[Aspose.Cells Форум](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
