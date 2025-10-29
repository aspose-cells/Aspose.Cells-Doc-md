---  
title: Insérer une image liée depuis une adresse Web avec Node.js via C++  
linktitle: Insérer une image liée à partir de l adresse Web  
type: docs  
weight: 450  
url: /fr/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Apprenez comment insérer une image liée depuis une adresse web dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Parfois, vous devez insérer une image provenant du web (http://) dans une feuille de calcul. Pour ce faire, spécifiez l'URL de l'image et l'image sera téléchargée à chaque ouverture du classeur dans Excel. L'image n'est pas physiquement intégrée dans le document Excel, mais pointe vers une ressource web.  
{{% /alert %}}  

## **Utilisation de Microsoft Excel**  

Dans Microsoft Excel (par exemple 2007) :  

1. Cliquez sur le menu **Insérer** et sélectionnez **Image**.  
1. Spécifiez l'adresse web de l'image dans la boîte de dialogue Insérer une image.  

## **Utilisation de Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ supporte l'ajout d'une image liée en utilisant [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). La méthode retourne un objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).  

L'exemple suivant montre comment ajouter une image liée depuis une adresse web dans une feuille de calcul.  

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
