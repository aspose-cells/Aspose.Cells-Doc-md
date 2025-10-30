---
title: Başlıklar ve Altbilgilerle Node.js C++ üzerinden Ayarlama
linktitle: Başlık ve Altbilgileri Ayarlama
type: docs
weight: 30
url: /tr/nodejs-cpp/setting-headers-and-footers/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel çalışma sayfalarının başlık ve altbilgisine nasıl programlı olarak resim ekleyeceğinizi açıklar. 
keywords: Excel başlık ve altbilgisine resim ekleme Node.js C++ üzerinden, Excel başlık ve altbilgi komutları ayarlama Node.js C++
---

{{% alert color="primary" %}}

Başlık ve altbilgiler, üst kenar boşluğunun altında veya alt kenar boşluğunun üstünde gösterilen metin satırlarıdır. Çalışma sayfalarına da başlık ve altbilgi eklemek mümkündür. Başlıklar ve altbilgiler, sayfa numarası, yazar adı, konu adı veya tarih ve saat gibi yararlı bilgileri göstermek için kullanılabilir. Başlıklar ve altbilgiler, sayfa düzeni ayarları kullanılarak yönetilir.

{{% /alert %}}

## **Başlık ve Altbilgileri Ayarlama**

Aspose.Cells for Node.js via C++, çalışma sayfalarına çalışma zamanı sırasında başlık ve altbilgi eklemenize izin verir, ancak baskı için önceden tasarlanmış bir dosyada başlık ve altbilgiyi manuel olarak ayarlamanızı öneririz. Microsoft Excel, başlık ve altbilgiyi ayarlamak için kullanılabilir ve çaba ile geliştirme zamanını azaltır. Aspose.Cells dosyayı içe aktarabilir ve ayarları kaydedebilir.

Çalışma zamanında başlık ve altbilgiler eklemek için Aspose.Cells, özel API çağrıları ve betik komutları sağlar.

### **Betik Komutları**

Betik komutları, başlık ve altbilgi biçimlendirmesini ayarlamanıza olanak tanıyan özel komutlardır.

|**Betik Komutları**|**Açıklama**|
| :- | :- |
|&P| Geçerli sayfa numarası
|&G| Bir resim
|&N| Toplam sayfa sayısı
|&D| Geçerli tarih
|&T| Geçerli saat
|&A| Çalışma sayfası adı
|&F| Dosya adı ve yolu olmadan
|&&Yazı|&Yazıyı gösterir. Örneğin: &&WO &WO olarak görüntülenir|
|&"\<FontName>"| Yazı tipi adını temsil eder. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"| Stil ile yazı tipi adını temsil eder. Örneğin: &"Arial,Kalın"|
|&\<FontSize>| Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak, bu komuttan sonra başlığa yazdırılacak düz bir sayı izlenecekse, bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Başlık ve Altbilgileri Ayarlama**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfı, çalışma sayfasına başlık ve altbilgi eklemek için kullanılan [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) ve [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-) olmak üzere iki yöntem sağlar. Bu yöntemler yalnızca iki parametre alır:

- **Bölüm** – başlığın veya altbilginin yerleştirileceği bölüm. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Betik** – başlık veya altbilgi için kullanılacak betik. Bu betik, başlıkları veya altbilgileri biçimlendirmek için betik komutları içerir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Bir Resmi Başlık veya Altbilgiye Ekleyin**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfının, başlık ve altbilgiye görseller eklemek için kullanılan iki ek yöntemi, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) ve [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-) bulunmaktadır. Bu yöntemler şu parametreleri alır:

- **Bölüm** – resmin yerleştirileceği başlık veya altbilgi bölümü. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Bayt dizisi** – görsel veri (ikili veri bir byte dizisinin tamponuna yazılmalıdır).

Aşağıdaki kodu çalıştırdıktan sonra dosyayı açarak, çalışma sayfasının üstbilgisini kontrol edin:

1. **Dosya** menüsünde **Sayfa Düzeni**'ni seçin. Bir iletişim kutusu görüntülenecektir.
1. **Üst Bilgi/Alt Bilgi** sekmesini seçin.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
