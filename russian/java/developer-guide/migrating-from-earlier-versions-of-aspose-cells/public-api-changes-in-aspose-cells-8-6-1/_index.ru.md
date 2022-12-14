---
title: Общедоступный API Изменения в Aspose.Cells 8.6.1
type: docs
weight: 210
url: /ru/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.6.0 до 8.6.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные классы, но и описание любых изменений поведения за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка целевого типа ссылки HTML**
В этом выпуске Aspose.Cells for Java API представлено перечисление, а именно HtmlLinkTargetType вместе с новым свойством HtmlSaveOptions.LinkTargetType, которое вместе позволяет[установить целевой тип для ссылок в электронной таблице при преобразовании в формат HTML](/cells/ru/java/change-the-html-link-target-type/). Ниже приведены возможные значения перечисления HtmlLinkTargetType, где значение по умолчанию — SELF.

1. HtmlLinkTargetType.BLANK: открывает связанный документ/страницу в новом окне или вкладке.
1. HtmlLinkTargetType.PARENT: открывает связанный документ/страницу в родительском фрейме.
1. HtmlLinkTargetType.SELF: открывает связанный документ/страницу в том же фрейме, где была нажата ссылка.
1. HtmlLinkTargetType.TOP: открывает связанный документ/страницу во всем теле окна.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.6.1 представила другую перегрузку метода VbaModuleCollection.remove, который теперь может принимать экземпляр Worksheet для удаления всех модулей VBA, связанных с указанным Worksheet.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Добавлен метод RangeCollection.add**
Aspose.Cells for Java 8.6.1 предоставил метод RangeCollection.Add, который можно использовать для добавления объектов Range в коллекцию диапазонов для определенного рабочего листа.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
 Метод Cell.setCharacters можно использовать для[обновить части форматированного текста](/cells/ru/java/access-and-update-the-portions-of-rich-text-of-cell/) данного объекта Cell. Метод Cell.getCharacters должен использоваться для доступа к частям текста, а затем можно вносить поправки с помощью метода Cell.setCharacters, тогда как метод**получить** Метод возвращает массив объектов FontSetting, которыми можно манипулировать, чтобы установить различные свойства: имя шрифта, цвет шрифта, жирность и т. д.**установлен** можно использовать для применения изменений.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Добавлено свойство VbaProject.isSigned**
 Aspose.Cells for Java 8.6.1 предоставил свойство VbaProject.isSigned, которое можно использовать для[проверить, подписан ли VbaProject в рабочей книге или нет](/cells/ru/java/check-if-vba-project-in-a-workbook-is-signed/). Свойство логического типа возвращает true, если проект подписан.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
### **Метод Cell.getFormatConditions изменен**
В выпуске версии 8.6.1 в Aspose.Cells for Java API был изменен тип возвращаемого значения метода Cell.getFormatConditions, который теперь возвращает массив типа FormatConditionCollection.
## **Устаревшие API**
### **Метод Workbook.checkWriteProtectedPassword устарел**
С выпуском версии 8.6.1 метод Workbook.checkWriteProtectedPassword был помечен как устаревший. Рекомендуется использовать метод WorkbookSettings.WriteProtection.validatePassword, который может принимать строковое значение в качестве параметра и возвращает логическое значение, если пароль соответствует предустановленному паролю электронной таблицы.
