---
title: Общедоступный API Изменения в Aspose.Cells 8.6.1
type: docs
weight: 200
url: /ru/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.6.0 до 8.6.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные классы, но и описание любых изменений поведения за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка HTML Тип цели ссылки**
 В этом выпуске Aspose.Cells for .NET API представлено перечисление, а именно HtmlLinkTargetType вместе с новым свойством HtmlSaveOptions.LinkTargetType, которое вместе позволяет[установить целевой тип для ссылок в электронной таблице при преобразовании в формат HTML](/cells/ru/net/change-the-html-link-target-type/). Ниже приведены возможные значения перечисления HtmlLinkTargetType, где значением по умолчанию является Self.

1. HtmlLinkTargetType.Blank: открывает связанный документ/страницу в новом окне или вкладке.
1. HtmlLinkTargetType.Parent: открывает связанный документ/страницу в родительском фрейме.
1. HtmlLinkTargetType.Self: открывает связанный документ/страницу в том же фрейме, где была нажата ссылка.
1. HtmlLinkTargetType.Top: открывает связанный документ/страницу во всем теле окна.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET 8.6.1 представил другую перегрузку метода VbaModuleCollection.Remove, который теперь может принимать экземпляр Worksheet для удаления всех модулей VBA, связанных с указанным Worksheet.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Добавлен метод RangeCollection.Add**
Aspose.Cells for .NET 8.6.1 предоставил метод RangeCollection.Add, который можно использовать для добавления объектов Range в коллекцию диапазонов для определенного рабочего листа.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
 Метод Cell.SetCharacters можно использовать для[обновить части форматированного текста](/cells/ru/net/access-and-update-the-portions-of-rich-text-of-cell/) данного объекта Cell. Метод Cell.GetCharacters должен использоваться для доступа к частям текста, а затем можно вносить поправки с помощью метода Cell.SetCharacters, тогда как метод**Получать** Метод возвращает массив объектов FontSetting, которыми можно манипулировать, чтобы установить различные свойства: имя шрифта, цвет шрифта, жирность и т. д.**Установлен** можно использовать для применения изменений.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Добавлено свойство VbaProject.IsSigned**
 Aspose.Cells for .NET 8.6.1 предоставил свойство VbaProject.IsSigned, которое можно использовать для[проверить, подписан ли VbaProject в рабочей книге или нет](/cells/ru/net/check-if-vba-project-in-a-workbook-is-signed/)Свойство логического типа возвращает true, если проект подписан.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
### **Метод Cell.GetFormatConditions изменен**
В версии 8.6.1 Aspose.Cells for .NET API изменился тип возвращаемого значения метода Cell.GetFormatConditions, который теперь возвращает массив типа FormatConditionCollection.
## **Устаревшие API**
### **Метод Workbook.CheckWriteProtectedPassword устарел**
С выпуском версии 8.6.1 метод Workbook.CheckWriteProtectedPassword был помечен как устаревший. Рекомендуется использовать метод WorkbookSettings.WriteProtection.ValidatePassword, который может принимать строковое значение в качестве параметра и возвращает логическое значение, если пароль совпадает с предустановленным паролем электронной таблицы.
