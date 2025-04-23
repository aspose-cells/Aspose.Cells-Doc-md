---
title: Excel de Yorumun Arka Planını nasıl değiştiririm Node.js kullanarak C++ ile
linktitle: Yorum Arka Planı
type: docs
weight: 190
url: /tr/nodejs-cpp/how-to-set-comment-background/
description: Excel de yorunda renk değiştirme ve Yoruma resim veya görsel nasıl eklenir, Aspose.Cells for Node.js via C++ kullanarak.
keywords: NODE.js ile C++ kullanarak yorum arka planı renkli resim ekleme
---

{{% alert color="primary" %}}
Yorumlar, hücrelere eklenen, formül detayları, değerlerin kaynağı veya değerlendirme yapan kişilerden gelen soruları kaydetmek için kullanılır. Yorumlar, birden fazla kişinin aynı belgeyi farklı zamanlarda tartışması veya incelemesi sırasında çok önemli bir rol oynar. Farklı kişilerin yorumlarını nasıl ayırt edebilirim? Evet, her yorum için farklı bir arka plan rengi ayarlayabiliriz. Ama çok sayıda belge ve yorum işlememiz gerektiğinde manuel yapmak kabus olur. Neyse ki, [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) API sağlar ve bunu kodda yapmanıza olanak tanır.
{{% /alert %}}

## **Excel'de yorumda renk nasıl değiştirilir**

Varsayılan yorum arkaplan rengini kullanmak istemiyorsanız, onu ilgilendiğiniz bir renk ile değiştirmek isteyebilirsiniz. Excel'de Yorum kutusunun arkaplan rengini nasıl değiştiririm?

Yukarıdaki kod, istediğiniz kendi seçtiğiniz rengin yorumlara eklenmesi için [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) kullanımını gösterecektir.

 Size bir [örnek dosya](exmaple.xlsx) hazırladık. Bu dosya, aşağıdaki kodda Workbook nesnesini başlatmak için kullanılır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Yukarıdaki kodu çalıştırın ve bir [çıktı dosyası](result.xlsx) elde edeceksiniz.

## **Excel'de yorumlara resim veya görüntü eklemek**

 Microsoft Excel, kullanıcıların elektronik tabloların görünümünü ve hissini büyük ölçüde özelleştirmesine olanak tanır. Yorumlara arkaplan resmi eklemek bile mümkündür. Bir arkaplan resmi eklemek estetik bir tercih olabilir veya markalaşmayı güçlendirmek için kullanılabilir.

 Aşağıdaki örnek kod, [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) API kullanarak sıfırdan bir XLSX dosyası oluşturur ve hücre A1'e resimli arkaplan ile bir yorum ekler.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

