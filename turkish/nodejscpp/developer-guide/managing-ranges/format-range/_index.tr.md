---  
title: Node.js ile C++ üzerinden Format Aralıkları  
linktitle: Aralıkları Biçimlendir  
type: docs  
weight: 105  
url: /tr/nodejs-cpp/how-to-format-a-range/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel de hücre aralığını nasıl biçimlendireceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  
Bir aralığa stili uygulamanız gerektiğinde, aralık biçimlendirme kullanabilirsiniz.  

## **Excel'de bir Aralığı Nasıl Biçimlendirirsiniz**  

Excel'de bir aralığı biçimlendirmek için, Excel tarafından sağlanan yerleşik biçimlendirme seçeneklerini kullanabilirsiniz. İşte Excel'de bir aralığı doğrudan nasıl biçimlendireceğiniz:  

1. Excel'i açın ve biçimlendirmek istediğiniz aralığı içeren çalışma kitabını açın.  

2. Biçimlendirmek istediğiniz hücre aralığını seçin. Aralığı seçmek için tıklayıp sürükleyebilirsiniz veya Shift + Ok tuşları gibi klavye kısayollarını kullanarak seçimi genişletebilirsiniz.  

3. Aralık seçildikten sonra, seçilen aralık üzerine sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir" öğesini seçin. Alternatif olarak, Excel şeridindeki Ana sekmesine giderek, "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayın ve "Hücreleri Biçimlendir" seçeneğini belirleyin.  

4. "Hücreleri Biçimlendir" iletişim kutusu görünecektir. Burada, seçilen aralığa uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stili, yazı tipi boyutu, yazı tipi rengi, sayı formatı, kenarlıklar, arka plan rengi vb. değiştirebilirsiniz. Farklı sekmeleri keşfetmek için iletişim kutusundaki farklı sekmelere bakın.  

5. İstenen biçimlendirme değişikliklerini yaptıktan sonra, seçilen aralığa biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.  

## **Node.js kullanarak Aralık Nasıl Biçimlendirilir**  

Aspose.Cells for Node.js via C++ kullanarak aralığı biçimlendirmek için aşağıdaki yöntemleri kullanabilirsiniz:  
1. [Range.applyStyle(stil, bayrak)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(stil)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(stil)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Örnek Kod**  
Bu örnekte bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veri ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık("A1:C3" ve "A4:C5") tanımlıyoruz. Daha sonra yeni stiller oluşturuyoruz, çeşitli biçimlendirme seçeneklerini belirliyoruz (örneğin, yazı tipi rengi, kalın), ve stili aralığa uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

