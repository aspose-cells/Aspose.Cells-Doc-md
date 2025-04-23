---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.1
type: docs
weight: 200
url: /de/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.6.0 auf 8.6.1, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für HTML-Link-Zieltyp**
Diese Version von Aspose.Cells for .NET API hat eine Enumeration namens HtmlLinkTargetType sowie eine neue Eigenschaft HtmlSaveOptions.LinkTargetType freigegeben, die es zusammen ermöglichen, den Zieltyp für die Links in der Tabelle beim Konvertieren in das HTML-Format zu [ändern](/cells/de/net/change-the-html-link-target-type/). Die möglichen Werte der HtmlLinkTargetType-Enumeration lauten wie folgt, wobei der Standardwert Self ist.

1. HtmlLinkTargetType.Blank: Öffnet das verlinkte Dokument/die verlinkte Seite in einem neuen Fenster oder Tab.
1. HtmlLinkTargetType.Parent: Öffnet das verlinkte Dokument/die verlinkte Seite im übergeordneten Rahmen.
1. HtmlLinkTargetType.Self: Öffnet das verlinkte Dokument/die verlinkte Seite im selben Rahmen, in dem der Link geklickt wurde.
1. HtmlLinkTargetType.Top: Öffnet das verlinkte Dokument/die verlinkte Seite im gesamten Fensterkörper.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Methode VbaModuleCollection.Remove hinzugefügt**
Aspose.Cells for .NET 8.6.1 hat eine weitere Überlastung der Methode VbaModuleCollection.Remove freigelegt, die jetzt eine Instanz von Worksheet akzeptieren kann, um alle VBA-Module zu entfernen, die mit dem angegebenen Worksheet verbunden sind.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Methode RangeCollection.Add hinzugefügt**
Aspose.Cells for .NET 8.6.1 hat die RangeCollection.Add Methode freigelegt, die verwendet werden kann, um Range-Objekte zur Sammlung von Bereichen für ein bestimmtes Arbeitsblatt hinzuzufügen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Methode Cell.SetCharacters hinzugefügt**
Die Methode Cell.SetCharacters kann verwendet werden, um die Teile des Rich-Texts eines bestimmten Zellenobjekts zu aktualisieren. Die Methode Cell.GetCharacters soll verwendet werden, um auf die Textteile zuzugreifen, und dann können Änderungen mithilfe der Methode Cell.SetCharacters vorgenommen werden, während die **Get**-Methode ein Array von FontSetting-Objekten zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftart, Schriftfarbe, Fettdruck usw. festzulegen, und die **Set**-Methode kann verwendet werden, um die Änderungen anzuwenden.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Eigenschaft VbaProject.IsSigned hinzugefügt**
Aspose.Cells for .NET 8.6.1 hat die Eigenschaft VbaProject.IsSigned freigelegt, die verwendet werden kann, um zu testen, ob ein VbaProject in einer Arbeitsmappe signiert ist oder nicht. Die Eigenschaft vom Typ Boolean gibt true zurück, wenn das Projekt signiert ist.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
## **Geänderte APIs**
### **Methode Cell.GetFormatConditions geändert**
Mit der Veröffentlichung von v8.6.1 hat die Aspose.Cells for .NET API den Rückgabetyp der Methode Cell.GetFormatConditions geändert, die jetzt ein Array vom Typ FormatConditionCollection zurückgibt.
## **Veraltete APIs**
### **Veraltete Methode Workbook.CheckWriteProtectedPassword**
Mit der Veröffentlichung von v8.6.1 wurde die Methode Workbook.CheckWriteProtectedPassword als veraltet markiert. Es wird empfohlen, die WorkbookSettings.WriteProtection.ValidatePassword Methode zu verwenden, die einen Zeichenfolgenwert als Parameter akzeptieren und einen booleschen Wert zurückgeben kann, wenn das Passwort mit dem voreingestellten Passwort der Tabellenkalkulation übereinstimmt.
{{< app/cells/assistant language="csharp" >}}
