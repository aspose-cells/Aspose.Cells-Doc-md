---  
title: Einfügen eines verknüpften Bildes von Webadresse mit Node.js über C++  
linktitle: Verknüpftes Bild aus Webadresse einfügen  
type: docs  
weight: 450  
url: /de/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Lernen Sie, wie Sie ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt einfügen, indem Sie Aspose.Cells for Node.js via C++ verwenden.  
---  

{{% alert color="primary" %}}  
Manchmal müssen Sie ein Bild aus dem Web (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und jedes Mal, wenn die Tabelle in Excel geöffnet wird, wird das Bild heruntergeladen. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.  
{{% /alert %}}  

## **Verwendung von Microsoft Excel**  

In Microsoft Excel (zum Beispiel 2007):  

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.  
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.  

## **Mit Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ unterstützt das Hinzufügen eines verknüpften Bildes mit [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)-Objekt zurück.  

Das folgende Beispiel zeigt, wie man ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 Cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  

