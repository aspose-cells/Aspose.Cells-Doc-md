---  
title: Webアドレスからリンクされた画像をNode.js経由でC++で挿入  
linktitle: Webアドレスからリンクされた画像の挿入  
type: docs  
weight: 450  
url: /ja/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: ウェブアドレスからリンクされた画像をワークシートに挿入する方法をAspose.Cells for Node.js via C++を使って学びます。  
---  

{{% alert color="primary" %}}  
時には、ウェブ（http://）から画像をワークシートに挿入する必要があります。その場合、画像のURLを指定すると、そのスプレッドシートをExcelで開くたびに画像がダウンロードされます。画像はExcelドキュメントに物理的に埋め込まれるのではなく、ウェブリソースを指し示します。  
{{% /alert %}}  

## **Microsoft Excel の使用**  

Microsoft Excel（たとえば2007）で：  

1. **挿入**メニューをクリックし、**画像**を選択します。  
1. 挿入画像ダイアログで画像のWebアドレスを指定します。  

## **Aspose.Cells for Node.js via C++を使用して**  

Aspose.Cells for Node.js via C++は、[**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-)を使用したリンク画像の追加をサポートします。この方法は[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)オブジェクトを返します。  

以下の例では、Webアドレスからリンクされた画像をワークシートに追加する方法を示しています。  

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
