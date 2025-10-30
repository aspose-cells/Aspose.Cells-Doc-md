---  
title: Node.js üzerinden C++ ile WordArt Filigranını Kilitleme  
linktitle: Kelime Sanatı Filigranı Kilitleme  
type: docs  
weight: 170  
url: /tr/nodejs-cpp/locking-wordart-watermark/  
description: Aspose.Cells for Node.js via C++ kullanarak WordArt filigranlarını kilitlemeyi öğrenin.  
---  

{{% alert color="primary" %}}  

Aspose.Cells API'leri, WordArt'un taşınabilir ve pozisyonlandırılabilir bir nesne olmasını sağlayan şekilde çalışma sayfasına WordArt filigranları eklemeye izin verir. Ayrıca, düzenleme, hareket ve seçim gibi etkileşimleri engellemek için WordArt nesnesini kilitlemek de mümkündür. Bu makale, [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) metodunun filigranın bazı yönlerini kilitlemekteki kullanımını açıklar.

{{% /alert %}}  

Aspose.Cells API'leri, kullanıcının etkileşimini sınırlamak veya tamamen engellemek amacıyla filigranın belirli yönlerini kilitlemeye imkan sağlar. Aşağıdaki kod parçası, başlangıçtan itibaren yeni bir çalışma kitabı oluşturarak seçim, hareket, düzenleme ve yeniden boyutlandırmayı kilitlemek için Aspose.Cells for Node.js via C++ kullanımıyla gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Lock Shape Aspects
wordart.setIsLocked(true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Selection, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.ShapeType, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Move, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Resize, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Text, true);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();

// Set the color
wordArtFormat.setOneColorGradient(AsposeCells.Color.Red, 0.2, AsposeCells.GradientStyleType.Horizontal, 2);

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
wordart.setHasLine(false);

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
