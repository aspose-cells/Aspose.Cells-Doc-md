---
title: Изменения в общедоступном API в Aspose.Cells 8.6.1
type: docs
weight: 200
url: /ru/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.6.0 по 8.6.1, которые могут быть интересны модульным/приложенческим разработчикам. В нем содержится не только новые и обновленные открытые методы, добавленные классы, но также описание любых изменений в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка типа цели HTML-ссылки**
Этот релиз Aspose.Cells for .NET API раскрыл перечисление с именем HtmlLinkTargetType вместе с новым свойством HtmlSaveOptions.LinkTargetType, которые вместе позволяют [устанавливать тип цели для ссылок в электронной таблице при преобразовании в формат HTML](/cells/ru/net/change-the-html-link-target-type/). Возможные значения перечисления HtmlLinkTargetType следующие, где значение по умолчанию - Self.

1. HtmlLinkTargetType.Blank: Открывает связанный документ/страницу в новом окне или вкладке.
1. HtmlLinkTargetType.Parent: Открывает связанный документ/страницу в родительском фрейме.
1. HtmlLinkTargetType.Self: Открывает связанный документ/страницу в том же фрейме, в котором была выполнена клик.
1. HtmlLinkTargetType.Top: Открывает связанный документ/страницу в полном окне.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Добавлен метод VbaModuleCollection.Remove**
Aspose.Cells for .NET 8.6.1 раскрыл еще одно перегруженное свойство метода VbaModuleCollection.Remove, которое теперь может принимать экземпляр Worksheet для удаления всех модулей VBA, связанных с указанным Worksheet.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Добавлен метод RangeCollection.Add**
Aspose.Cells for .NET 8.6.1 раскрыл метод RangeCollection.Add, который может использоваться для добавления объектов Range в коллекцию диапазонов для конкретного Worksheet.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Добавлен метод Cell.SetCharacters**
Метод Cell.SetCharacters может использоваться для [обновления частей форматированного текста](/cells/ru/net/access-and-update-the-portions-of-rich-text-of-cell/) заданного объекта Cell. Метод Cell.GetCharacters предназначен для доступа к частям текста, после чего изменения могут быть внесены с использованием метода Cell.SetCharacters, в то время как метод **Get** возвращает массив объектов FontSetting, которые могут быть изменены для установки различных свойств имени шрифта, цвета шрифта, жирности и т. д., а метод **Set** может использоваться для применения изменений.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Добавлено свойство VbaProject.IsSigned**
Aspose.Cells for .NET 8.6.1 раскрыл свойство VbaProject.IsSigned, которое может использоваться для [проверки, подписан ли проект VbaProject в книге Excel или нет](/cells/ru/net/check-if-vba-project-in-a-workbook-is-signed/). Логическое свойство возвращает true, если проект подписан.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **Измененные API**
### **Изменен метод Cell.GetFormatConditions**
С выпуском v8.6.1 API Aspose.Cells for .NET был изменен тип возвращаемого значения метода Cell.GetFormatConditions, который теперь возвращает массив типа FormatConditionCollection.
## **Устаревшие API**
### **Устаревший метод Workbook.CheckWriteProtectedPassword**
С выпуском v8.6.1 метод Workbook.CheckWriteProtectedPassword был помечен устаревшим. Рекомендуется использовать метод WorkbookSettings.WriteProtection.ValidatePassword, который может принимать строковое значение в качестве параметра и возвращает булево значение, если пароль совпадает с предварительно установленным паролем электронной таблицы.
{{< app/cells/assistant language="csharp" >}}
