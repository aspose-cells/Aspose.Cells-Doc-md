---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.1
type: docs
weight: 210
url: /de/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.6.0 auf 8.6.1, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für HTML-Link-Zieltyp**
Diese Version der Aspose.Cells for Java-API hat eine Aufzählung namens HtmlLinkTargetType freigelegt sowie eine neue Eigenschaft HtmlSaveOptions.LinkTargetType, die es ermöglicht, den Zieltyp für die Links im Tabellenkalkulationsformat zu setzen. Die möglichen Werte der HtmlLinkTargetType-Aufzählung sind wie folgt, wobei der Standardwert SELBST ist.

1. HtmlLinkTargetType.BLANK: Öffnet das verlinkte Dokument/die verlinkte Seite in einem neuen Fenster oder Tab.
1. HtmlLinkTargetType.PARENT: Öffnet das verlinkte Dokument/die verlinkte Seite im übergeordneten Rahmen.
1. HtmlLinkTargetType.SELF: Öffnet das verlinkte Dokument/die verlinkte Seite im gleichen Rahmen, in dem der Link geklickt wurde.
1. HtmlLinkTargetType.TOP: Öffnet das verlinkte Dokument/die verlinkte Seite im gesamten Fensterkörper.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Methode VbaModuleCollection.remove hinzugefügt**
Aspose.Cells for Java 8.6.1 hat eine weitere Überlastung der VbaModuleCollection.remove-Methode freigelegt, die nun eine Instanz von Arbeitsblatt akzeptieren kann, um alle mit dem angegebenen Arbeitsblatt verbundenen VBA-Module zu entfernen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Methode RangeCollection.add hinzugefügt**
Aspose.Cells for Java 8.6.1 hat die RangeCollection.Add-Methode freigelegt, die verwendet werden kann, um Range-Objekte zu der Sammlung von Bereichen für ein bestimmtes Arbeitsblatt hinzuzufügen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Methode Cell.setCharacters hinzugefügt**
Die Methode Cell.setCharacters kann verwendet werden, um die Abschnitte des Rich-Texts eines bestimmten Zellenobjekts zu aktualisieren. Die Methode Cell.getCharacters wird verwendet, um auf die Abschnitte des Textes zuzugreifen, und dann können Änderungen mit der Methode Cell.setCharacters vorgenommen werden, während die Methode **get** ein Array von FontSetting-Objekten zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftartname, Schriftfarbe, Fett usw. festzulegen, und die **set**-Methode kann verwendet werden, um die Änderungen anzuwenden.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Eigenschaft VbaProject.isSigned hinzugefügt**
Aspose.Cells for Java 8.6.1 hat die VbaProject.isSigned-Eigenschaft freigelegt, die verwendet werden kann, um [zu überprüfen, ob ein VbaProject in einer Arbeitsmappe signiert ist oder nicht](/cells/de/java/check-if-vba-project-in-a-workbook-is-signed/). Die Eigenschaft vom Typ Boolean gibt true zurück, wenn das Projekt signiert ist.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
## **Geänderte APIs**
### **Geänderte Cell.getFormatConditions-Methode**
Mit der Version v8.6.1 hat die Aspose.Cells for Java-API den Rückgabetyp der Cell.getFormatConditions-Methode modifiziert, der jetzt ein Array vom Typ FormatConditionCollection zurückgibt.
## **Veraltete APIs**
### **Veraltete Workbook.checkWriteProtectedPassword-Methode**
Mit der Version v8.6.1 wurde die Workbook.checkWriteProtectedPassword-Methode als veraltet markiert. Es wird empfohlen, die WorkbookSettings.WriteProtection.validatePassword-Methode zu verwenden, die einen String-Wert als Parameter akzeptieren und Boolean zurückgeben kann, wenn das Kennwort mit dem voreingestellten Kennwort der Tabelle übereinstimmt.
