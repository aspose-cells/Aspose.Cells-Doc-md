---
title: Node.js ile C++ üzerinden Yorumlar ve Notlar Yönetimi
linktitle: Yorumlar ve Notlar
type: docs
weight: 128
url: /tr/nodejs-cpp/comments-and-notes/
description: Yorum veya not ekleyin ve yönetin Aspose.Cells for Node.js via C++ ile.
keywords: Yorum ekleyin, not ekleyin Node.js ile C++
---

## **Giriş**

Yorumlar, hücrelere ek bilgi eklemek için kullanılır. Aspose.Cells for Node.js via C++, hücrelere yorum eklemek için iki yöntem sunar. Birincisi, tasarımcı dosyasında manuel olarak yorumlar oluşturmaktır. Bu yorumlar, Aspose.Cells kullanılarak içe aktarılır. İkincisi ise, Aspose.Cells API kullanılarak çalışma zamanında yorum eklemektir. Bu konu, Aspose.Cells API kullanarak hücrelere yorum eklemeyi tartışır. Yorumların biçimlendirilmesi de açıklanacaktır.

## **Yorum Ekleme**

Yorum eklemek için [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) koleksiyonunun [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-) metodunu çağırın ({2} nesnesinde kapsüllenmiş). Yeni [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) nesnesine, yorum dizinine geçerek erişilebilir. [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) nesnesine eriştikten sonra, yorumu özelleştirmek için [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--) özelliği kullanılır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Yorum Biçimlendirme**

Yorumların görünümünü yükseklik, genişlik ve yazı tipi ayarlarıyla biçimlendirmek de mümkündür.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Yoruma Resim Ekle**

Microsoft Excel 2007 ile, bir hücre yorumuna arka plan olarak bir resim eklemek de mümkündür. Excel 2007'de bunu aşağıdaki adımları takip ederek başarabilirsiniz. (Zaten bir hücre yorumu eklediğinizi varsayarlar.)

1. Yorum içeren hücreye sağ tıklayın.
1. **Yorumları Göster/Gizle**'yi seçin ve yorumdan herhangi bir metni temizleyin.
1. Yorumun kenarına tıklayın.
1. **Biçim**, ardından **Yorum**'u seçin.
1. **Renk ve Çizgiler** sekmesinde, **Renk** listesini genişletin.
1. **Dolgu Efektleri**'ni tıklayın.
1. **Resim** sekmesinde, **Resim Seç**'i tıklayın.
1. Resmi bulun ve seçin.
1. Tüm iletiler kapatılıncaya kadar **Tamam**'ı tıklayın.

Aspose.Cells ayrıca bu özelliği sağlar. Aşağıda, sıfırdan XLSX dosyası oluşturan ve "A1" hücresine resimli bir arka plan ekleyen bir kod örneği bulunmaktadır.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

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
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Gelişmiş Konular**
- [Yorumun Yazı Yönünü Değiştirme](/cells/tr/nodejs-cpp/change-text-direction-of-the-comment/)
- [Yorum Yazı Tipi Rengini Nasıl Değiştirilir](/cells/tr/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Yorum arka planını nasıl ayarlarım](/cells/tr/nodejs-cpp/how-to-set-comment-background/)
- [İz bırakan Yorumlar](/cells/tr/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
