---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.1
type: docs
weight: 200
url: /de/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.0 zu 8.6.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für HTML Linkzieltyp**
 Diese Version von Aspose.Cells for .NET API hat eine Aufzählung namens HtmlLinkTargetType zusammen mit einer neuen Eigenschaft HtmlSaveOptions.LinkTargetType verfügbar gemacht, die zusammen dies ermöglicht[Stellen Sie den Zieltyp für die Links in der Tabelle während der Konvertierung in das Format HTML ein](/cells/de/net/change-the-html-link-target-type/). Die möglichen Werte der HtmlLinkTargetType-Enumeration lauten wie folgt, wobei der Standardwert Self ist.

1. HtmlLinkTargetType.Blank: Öffnet das verlinkte Dokument/die verlinkte Seite in einem neuen Fenster oder Tab.
1. HtmlLinkTargetType.Parent: Öffnet das verlinkte Dokument/die verlinkte Seite im übergeordneten Frame.
1. HtmlLinkTargetType.Self: Öffnet das verlinkte Dokument/die verlinkte Seite in demselben Frame, in dem der Link angeklickt wurde.
1. HtmlLinkTargetType.Top: Öffnet das verlinkte Dokument/die verlinkte Seite im gesamten Fensterbereich.

Es folgt das einfache Nutzungsszenario.

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


### **Methode VbaModuleCollection.Remove Hinzugefügt**
Aspose.Cells for .NET 8.6.1 hat eine weitere Überladung der VbaModuleCollection.Remove-Methode verfügbar gemacht, die jetzt eine Instanz von Worksheet akzeptieren kann, um alle VBA-Module zu entfernen, die dem angegebenen Worksheet zugeordnet sind.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Methode RangeCollection.Add Hinzugefügt**
Aspose.Cells for .NET 8.6.1 hat die RangeCollection.Add-Methode verfügbar gemacht, die zum Hinzufügen von Range-Objekten zur Sammlung von Bereichen für ein bestimmtes Arbeitsblatt verwendet werden kann.

Es folgt das einfache Nutzungsszenario.

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


### **Methode Cell.SetCharacters hinzugefügt**
 Dazu kann die Methode Cell.SetCharacters verwendet werden[Aktualisieren Sie die Teile des Rich-Texts](/cells/de/net/access-and-update-the-portions-of-rich-text-of-cell/) eines bestimmten Cell-Objekts. Die Methode Cell.GetCharacters muss verwendet werden, um auf die Teile des Textes zuzugreifen, und dann können Änderungen mit der Methode Cell.SetCharacters vorgenommen werden, während die**Bekommen** -Methode gibt ein Array von FontSetting-Objekten zurück, die manipuliert werden können, um verschiedene Eigenschaften Schriftartname, Schriftfarbe, Fettschrift usw. festzulegen**Satz** -Methode verwendet werden, um die Änderungen anzuwenden.

Es folgt das einfache Nutzungsszenario.

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


### **Eigenschaft VbaProject.IsSigned Hinzugefügt**
 Aspose.Cells for .NET 8.6.1 hat die VbaProject.IsSigned-Eigenschaft verfügbar gemacht, die verwendet werden kann[Testen Sie, ob ein VbaProject in einer Arbeitsmappe signiert ist oder nicht](/cells/de/net/check-if-vba-project-in-a-workbook-is-signed/)Die Eigenschaft vom Typ Boolean gibt „true“ zurück, wenn das Projekt signiert ist.

Es folgt das einfache Nutzungsszenario.

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
## **Modifizierte APIs**
### **Methode Cell.GetFormatConditions geändert**
Mit der Veröffentlichung von v8.6.1 hat Aspose.Cells for .NET API den Rückgabetyp der Methode Cell.GetFormatConditions geändert, die jetzt ein Array vom Typ FormatConditionCollection zurückgibt.
## **Veraltete APIs**
### **Methode Workbook.CheckWriteProtectedPassword Veraltet**
Mit der Veröffentlichung von v8.6.1 wurde die Workbook.CheckWriteProtectedPassword-Methode als veraltet gekennzeichnet. Es wird empfohlen, die WorkbookSettings.WriteProtection.ValidatePassword-Methode zu verwenden, die einen Zeichenfolgenwert als Parameter akzeptieren kann und einen booleschen Wert zurückgibt, wenn das Kennwort mit dem voreingestellten Kennwort der Tabelle übereinstimmt.
