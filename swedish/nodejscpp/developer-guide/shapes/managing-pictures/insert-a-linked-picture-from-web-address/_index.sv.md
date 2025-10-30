---  
title: Infoga en länkad bild från webbadress med Node.js via C++  
linktitle: Infoga en länkad bild från webbadress  
type: docs  
weight: 450  
url: /sv/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Lär dig hur du infogar en länkad bild från en webbadress i ett kalkylblad med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. Ange bildens URL och bilden laddas ner varje gång kalkylbladet öppnas i Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.  
{{% /alert %}}  

## **Använda Microsoft Excel**  

I Microsoft Excel (till exempel 2007):  

1. Klicka på **Infoga** i menyn och välj **Bild**.  
1. Ange webbadressen för bilden i dialogrutan Infoga bild.  

## **Användning av Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ stöder att lägga till en länkad bild med [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)-objekt.  

Följande exempel visar hur man lägger till en länkad bild från en webbadress till ett arbetsblad.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
