---
title: Изменения в общедоступном API в Aspose.Cells 8.6.1
type: docs
weight: 210
url: /ru/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.6.0 по 8.6.1, которые могут быть интересны модульным/приложенческим разработчикам. В нем содержится не только новые и обновленные открытые методы, добавленные классы, но также описание любых изменений в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка типа цели HTML-ссылки**
В этой версии API Aspose.Cells for Java было представлено перечисление, а именно HtmlLinkTargetType, вместе с новым свойством HtmlSaveOptions.LinkTargetType, которые вместе позволяют [установить тип цели для ссылок в электронной таблице при конвертации в формат HTML](/cells/ru/java/change-the-html-link-target-type/). Возможные значения перечисления HtmlLinkTargetType следующие, где значение по умолчанию - SELF.

1. HtmlLinkTargetType.BLANK: Открывает связанный документ/страницу в новом окне или вкладке.
1. HtmlLinkTargetType.PARENT: Открывает связанный документ/страницу в родительском фрейме.
1. HtmlLinkTargetType.SELF: Открывает связанный документ/страницу в том же фрейме, где была кликнута ссылка.
1. HtmlLinkTargetType.TOP: Открывает связанный документ/страницу в полной области окна.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Добавлен метод VbaModuleCollection.remove**
Aspose.Cells for Java 8.6.1 представляет еще одну перегрузку метода VbaModuleCollection.remove, которая теперь может принимать экземпляр Worksheet для удаления всех модулей VBA, связанных с указанным Worksheet.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Добавлен метод RangeCollection.add**
Aspose.Cells for Java 8.6.1 представил метод RangeCollection.Add, который может быть использован для добавления объектов Range в коллекцию диапазонов для конкретного Worksheet.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Добавлен метод Cell.setCharacters**
Метод Cell.setCharacters может быть использован для [обновления частей форматированного текста](/cells/ru/java/access-and-update-the-portions-of-rich-text-of-cell/) заданного объекта Cell. Метод Cell.getCharacters должен быть использован для доступа к частям текста, после чего изменения можно внести с использованием метода Cell.setCharacters, в то время как метод **get** возвращает массив объектов FontSetting, которые могут быть изменены для установки различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д., и метод **set** может быть использован для применения изменений.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Добавлено свойство VbaProject.isSigned**
Aspose.Cells for Java 8.6.1 представил свойство VbaProject.isSigned, которое может быть использовано для [проверки, подписан ли проект VBA в книге Excel или нет](/cells/ru/java/check-if-vba-project-in-a-workbook-is-signed/). Свойство типа Boolean возвращает true, если проект подписан.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **Измененные API**
### **Изменен метод Cell.getFormatConditions**
С выпуском v8.6.1 API Aspose.Cells for Java изменил возвращаемый тип метода Cell.getFormatConditions, теперь он возвращает массив типа FormatConditionCollection.
## **Устаревшие API**
### **Устаревший метод Workbook.checkWriteProtectedPassword**
С выпуском v8.6.1 метод Workbook.checkWriteProtectedPassword был отмечен как устаревший. Рекомендуется использовать метод WorkbookSettings.WriteProtection.validatePassword, который может принимать строковое значение в качестве параметра и возвращает булево значение, если пароль соответствует предустановленному паролю таблицы.
{{< app/cells/assistant language="java" >}}
