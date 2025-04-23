---
title: Node.js ile C++ aracılığıyla hücreleri biçimlendirin
description: Aspose.Cells for Node.js via C++ te hücreleri biçimlendirme ve stil verme yollarını öğrenin; sayı biçimlendirme, tarih biçimlendirme, yazı tipi stilleri ve diğer hücre stil seçenekleri dahil. Kılavuzumuz, çekici ve profesyonel görünümlü elektronik tablolar oluşturmanıza yardımcı olacak.
keywords: Aspose.Cells for Node.js via C++, hücre biçimlendirme, stil verme, sayı ve tarih biçimlendirme, font stili, hücre stil seçenekleri, elektronik tablo, oluştur, profesyonel görünüm, satır ve sütunları biçimlendir.
linktitle: Hücreleri Biçimlendirin
type: docs
weight: 120
url: /tr/nodejs-cpp/cells-formatting/
---

## **Giriş**

{{% alert color="primary" %}}

Aspose.Cells, hücrenin biçimlendirme stilini almak/ayarlamak için kullanılan [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) ve [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metodlarını sağlar. Ayrıca bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) sınıfı da sağlar.

{{% /alert %}}

## **GetStyle ve SetStyle Metodları Kullanılarak Hücreleri Biçimlendirme**

Hücrelere arka plan veya ön plan renkleri, kenarlıklar, fontlar, yatay ve dikey hizalamalar, girinti düzeyi, yazı yönü, döndürme açısı ve çok daha fazlası için farklı türde biçimlendirme stilleri uygulayın.

### **GetStyle ve SetStyle Metodlarını Kullanma**

Eğer geliştiriciler farklı hücrelere farklı biçimlendirme stilleri uygulamak istiyorsa, hücrenin [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) öğesini [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) metodu ile almak, stil özelliklerini belirlemek ve ardından biçimlendirmeyi [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metodu ile uygulamak daha iyidir. Aşağıda, bu yaklaşımı göstermek için bir örnek verilmiştir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Farklı Hücreleri Biçimlendirmek İçin Stil Nesnesini Kullanma**

Eğer geliştiriciler aynı biçimlendirme stilini farklı hücrelere uygulamak istiyorsa, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesini kullanabilirler. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesini kullanmak için aşağıdaki adımları takip edin:

1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) metodunu çağırarak bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi ekleyin
2. Yeni eklenen [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesine erişin
3. İstenen biçimlendirme ayarlarını uygulamak için [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin ilgili özelliklerini/atribütlerini ayarlayın
4. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesini istediğiniz hücrelere atayın

Bu yaklaşım uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve aynı zamanda bellek tasarrufu sağlayabilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Microsoft Excel 2007 Önceden Tanımlanmış Stilleri Nasıl Kullanılır**

Microsoft Excel 2007 için farklı biçimlendirme stilleri uygulamanız gerekiyorsa, Aspose.Cells API'sını kullanarak stilleri uygulayın. Aşağıdaki örnek, bir hücreye önceden tanımlanmış bir stil uygulamanın bu yaklaşımını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Bir Hücredeki Seçili Karakterleri Biçimlendirme**

Yazı tipi ayarlarıyla ilgilenmek, hücre içindeki metni biçimlendirmeyi açıklar, ancak sadece hücre içeriğinin tümünü biçimlendirmeyi açıklar. Seçili karakterleri biçimlendirmek istiyorsanız ne yapacaksınız?

Aspose.Cells bu özelliği de destekler. Bu konu, bu özelliğin etkin kullanımını açıklar.

### **Seçili Karakterleri Biçimlendirmek**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunu sağlar. [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfı nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfı, aşağıdaki parametreleri alan [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) metodunu sağlar; böylece bir hücre içindeki karakter aralığını seçebilirsiniz:

- **Başlangıç İndeksi**, seçimin nereden başlayacağı karakterin indeksi.
- **Karakter Sayısı**, seçilecek karakterlerin sayısı.

[**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) metodu, geliştiricilerin aşağıdaki kod örneğinde gösterildiği gibi hücreyle aynı şekilde karakterleri biçimlendirmelerine izin veren [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) sınıfı örneği döndürür. Çıktı dosyasında, A1 hücresinde 'Visit' kelimesi varsayılan font ile biçimlendirilirken, 'Aspose!' kalın ve mavi olacaktır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Bir hücredeki Zengin Metnin bir bölümünü biçimlendirmeyi ilginize aldıysanız, [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) ve [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) metodlarını kullanmayı düşünün. [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) metodu, metnin bölümlerine erişmek için kullanılır ve ardından [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) metodu ile değişiklikler yapılabilir. Ayrıca, **Get** metodu, font adı, font rengi, kalınlık vb. gibi çeşitli özellikleri ayarlamak için kullanılabilecek [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) nesnesi dizisi döndürür ve **Set** metodu bu değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}}

## **Satırları ve Sütunları Nasıl Biçimlendirilir**

Bazı durumlarda, geliştiricilerin satırlara veya sütunlara aynı biçimlendirmeyi uygulamaları gerekebilir. Hücrelere tek tek biçimlendirme uygulamak genellikle daha uzun sürer ve iyi bir çözüm değildir.
Bu sorunu ele almak için, Aspose.Cells bu makalede detaylı bir şekilde tartışılan basit ve hızlı bir yol sağlar.

### **Satırları ve Sütunları Biçimlendirme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunu sağlar. [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunda, bir [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) nesnesini temsil eden öğeler bulunur.

### **Bir Satırı Nasıl Biçimlendirirsiniz**

[**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) koleksiyonundaki her öğe, bir [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) nesnesini temsil eder. [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) nesnesi, satırın biçimlendirmesini ayarlamak için kullanılan [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) metodunu sunar. Aynı biçimlendirmeyi bir satıra uygulamak için, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesini kullanın. Aşağıdaki adımlar, nasıl kullanılacağını gösterir.

1. [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) metodunu çağırarak [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfına [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi ekleyin.
2. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin özelliklerini ayarlayarak biçimlendirme ayarları uygulayın.
3. [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) nesnesinin ilgili özelliklerini YASAKLAYIN.
4. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesini [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) nesnesine atayın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Bir Sutunu Nasıl Biçimlendirirsiniz**

[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu ayrıca bir [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) koleksiyonu da sağlar. [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) koleksiyonundaki her öğe bir [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) nesnesini temsil eder. Bir [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) nesnesine benzer şekilde, [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) nesnesi de sütunu biçimlendirmek için [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) metodunu sunar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Gelişmiş Konular**
- [Hizalama Ayarları](/cells/tr/nodejs-cpp/cells-alignment-settings/)
- [Kenarlık Ayarları](/cells/tr/nodejs-cpp/cells-border-settings/)
- [Excel ve ODS dosyalarının Koşullu Biçimleri ayarlanması.](/cells/tr/nodejs-cpp/conditional-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/nodejs-cpp/excel-themes-and-colors/)
- [Doldurma Ayarları](/cells/tr/nodejs-cpp/cells-fill-settings/)
- [Font Ayarları](/cells/tr/nodejs-cpp/cells-font-settings/)
- [Bir İşkitapta Hücreleri Biçimlendirme](/cells/tr/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemi Uygulama](/cells/tr/nodejs-cpp/implement-1904-date-system/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/nodejs-cpp/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/nodejs-cpp/cells-number-settings/)
- [Hücreler için Stili Getirme ve Ayarlama](/cells/tr/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

