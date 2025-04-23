---  
title: Node.js kullanarak C++ ile Yorum Yazı Tipi Rengini Nasıl Değiştirilir  
linktitle: Yorum Metin Rengini Nasıl Değiştirilir  
type: docs  
weight: 180  
url: /tr/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel, hücrelere ek bilgiler eklemek ve veriyi vurgulamak için yorumlar eklemeye izin verir. Geliştiriciler, yorumu hizalama ayarları, metin yönü, Yazı Tipi Rengi vb. özelleştirmeleri gerekebilir. Aspose.Cells for Node.js via C++, bu işlemi yapmak için API'ler sağlar.  
{{% /alert %}}  

Aspose.Cells for Node.js via C++, yorunun yazı tipi rengini ayarlamak için [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) özelliği sağlar. Aşağıdaki örnek kod, [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) özelliğinin kullanımıyla yorunun metin yönünü ayarlamayı gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add some text in cell A1
worksheet.getCells().get("A1").putValue("Here");

// Add a comment to A1 cell
const commentIndex = worksheet.getComments().add("A1");
const comment = worksheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set the Comment note
comment.setNote("This is my Comment Text. This is Test.");

const shape = worksheet.getComments().get("A1").getCommentShape();

shape.getFill().getSolidFill().setColor(AsposeCells.Color.Black);
const font = shape.getFont();
font.setColor(AsposeCells.Color.White);
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setFontColor(true);
shape.getTextBody().format(0, shape.getText().length, font, styleFlag);

// Save the Excel file
workbook.save(path.join(outputDir, "outputChangeCommentFontColor.xlsx"));
```  

Yukarıdaki kod tarafından oluşturulan çıktı dosyası, referansınız için ekte bulunmaktadır.  
