---  
title: Inserire un immagine collegata da indirizzo web con Node.js tramite C++  
linktitle: Inserisci un immagine collegata da un indirizzo web  
type: docs  
weight: 450  
url: /it/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Impara come inserire un immagine collegata da un indirizzo web in un foglio di lavoro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A volte è necessario inserire un’immagine dal web (http://) in un foglio di lavoro. Per farlo, specifica l'URL dell’immagine e questa verrà scaricata ogni volta che il foglio di calcolo viene aperto in Excel. L’immagine non è incorporata fisicamente nel documento Excel, ma punta a una risorsa web.  
{{% /alert %}}  

## **Utilizzando Microsoft Excel**  

In Microsoft Excel (ad esempio 2007):  

1. Fare clic sul menu **Inserisci** e selezionare **Immagine**.  
1. Specifica l'indirizzo web dell'immagine nella finestra di dialogo Inserisci immagine.  

## **Usando Aspose.Cells for Node.js via C++**  

Aspose.Cells for Node.js via C++ supporta l'aggiunta di un'immagine collegata usando [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Il metodo restituisce un oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).  

L'esempio seguente mostra come aggiungere un'immagine collegata da un indirizzo web a un foglio di lavoro.  

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
