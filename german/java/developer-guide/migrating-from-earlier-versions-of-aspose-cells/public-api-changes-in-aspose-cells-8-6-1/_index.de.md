---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.1
type: docs
weight: 210
url: /de/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.0 zu 8.6.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für den Zieltyp HTML-Link**
Diese Version von Aspose.Cells for Java API hat eine Aufzählung namens HtmlLinkTargetType zusammen mit einer neuen Eigenschaft HtmlSaveOptions.LinkTargetType verfügbar gemacht, die zusammen dies ermöglicht[Legen Sie den Zieltyp für die Links in der Tabelle während der Konvertierung in das HTML-Format fest](/cells/de/java/change-the-html-link-target-type/). Die möglichen Werte der HtmlLinkTargetType-Enumeration lauten wie folgt, wobei der Standardwert SELF ist.

1. HtmlLinkTargetType.BLANK: Öffnet das verlinkte Dokument/die verlinkte Seite in einem neuen Fenster oder Tab.
1. HtmlLinkTargetType.PARENT: Öffnet das verlinkte Dokument/die verlinkte Seite im übergeordneten Frame.
1. HtmlLinkTargetType.SELF: Öffnet das verlinkte Dokument/die verlinkte Seite in demselben Frame, in dem der Link angeklickt wurde.
1. HtmlLinkTargetType.TOP: Öffnet das verlinkte Dokument/die verlinkte Seite im gesamten Fensterbereich.

Es folgt das einfache Nutzungsszenario.

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
### **Methode VbaModuleCollection.remove Hinzugefügt**
Aspose.Cells for Java 8.6.1 hat eine weitere Überladung der Methode VbaModuleCollection.remove verfügbar gemacht, die jetzt eine Instanz von Worksheet akzeptieren kann, um alle VBA-Module zu entfernen, die dem angegebenen Worksheet zugeordnet sind.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Methode RangeCollection.add Hinzugefügt**
Aspose.Cells for Java 8.6.1 hat die RangeCollection.Add-Methode verfügbar gemacht, die zum Hinzufügen von Range-Objekten zur Sammlung von Bereichen für ein bestimmtes Arbeitsblatt verwendet werden kann.

Es folgt das einfache Nutzungsszenario.

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
### **Methode Cell.setCharacters Hinzugefügt**
 Dazu kann die Methode Cell.setCharacters verwendet werden[Aktualisieren Sie die Teile des Rich-Texts](/cells/de/java/access-and-update-the-portions-of-rich-text-of-cell/) eines bestimmten Cell-Objekts. Die Methode Cell.getCharacters muss verwendet werden, um auf die Teile des Textes zuzugreifen, und dann können Änderungen mit der Methode Cell.setCharacters vorgenommen werden, während die**erhalten** -Methode gibt ein Array von FontSetting-Objekten zurück, die manipuliert werden können, um verschiedene Eigenschaften Schriftartname, Schriftfarbe, Fettschrift usw. festzulegen**einstellen** -Methode verwendet werden, um die Änderungen anzuwenden.

Es folgt das einfache Nutzungsszenario.

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
### **Eigenschaft VbaProject.isSigned Hinzugefügt**
 Aspose.Cells for Java 8.6.1 hat die VbaProject.isSigned-Eigenschaft verfügbar gemacht, die verwendet werden kann[Testen Sie, ob ein VbaProject in einer Arbeitsmappe signiert ist oder nicht](/cells/de/java/check-if-vba-project-in-a-workbook-is-signed/). Die Eigenschaft vom Typ Boolean gibt „true“ zurück, wenn das Projekt signiert ist.

Es folgt das einfache Nutzungsszenario.

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
## **Modifizierte APIs**
### **Methode Cell.getFormatConditions Geändert**
Mit der Veröffentlichung von v8.6.1 hat Aspose.Cells for Java API den Rückgabetyp der Methode Cell.getFormatConditions geändert, die jetzt ein Array vom Typ FormatConditionCollection zurückgibt.
## **Veraltete APIs**
### **Methode Workbook.checkWriteProtectedPassword Veraltet**
Mit der Veröffentlichung von v8.6.1 wurde die Workbook.checkWriteProtectedPassword-Methode als veraltet gekennzeichnet. Es wird empfohlen, die WorkbookSettings.WriteProtection.validatePassword-Methode zu verwenden, die einen String-Wert als Parameter akzeptieren kann und einen booleschen Wert zurückgibt, wenn das Passwort mit dem voreingestellten Passwort der Tabelle übereinstimmt.
