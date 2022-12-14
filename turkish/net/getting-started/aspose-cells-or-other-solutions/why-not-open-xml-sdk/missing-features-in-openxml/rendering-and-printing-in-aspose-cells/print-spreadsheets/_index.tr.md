---
title: Elektronik tabloları yazdır
type: docs
weight: 20
url: /tr/net/print-spreadsheets/
---
Sayfa yapısı ayarları ayrıca, kullanıcıların çalışma sayfalarının yazdırılan sayfalarını kontrol etmelerine olanak tanıyan çeşitli Yazdırma Seçenekleri (Sayfa Seçenekleri olarak da anılır) sağlar. Bu yazdırma seçenekleri, kullanıcıların şunları yapmasına olanak tanır:

- Çalışma sayfasının belirli bir Yazdırma Alanını seçin
- Başlıkları Yazdır
- Kılavuz Çizgilerini Yazdır
- Satır/Sütun Başlıklarını Yazdır
- Taslak Kalitesine Ulaşın
- Yorumları Yazdır
- Yazdır Cell Hataları
- Sayfa Sıralamasını Tanımla
  **Yazdırma/Sayfa Seçeneklerini Ayarlama**

Aspose.Cells, tüm bu yazdırma seçeneklerini destekler ve geliştiriciler, PageSetup sınıfı tarafından sunulan çeşitli özellikleri kullanarak bu seçenekleri istedikleri çalışma sayfaları için kolayca yapılandırabilir. PageSetup sınıfının bu özelliklerinin kullanımı aşağıda daha ayrıntılı olarak ele alınmıştır.
## **Yazdırma Alanını Ayarla**
Varsayılan olarak, yalnızca veri içeren çalışma sayfasının tüm alanını içeren yazdırma alanı seçilir, ancak geliştiriciler de arzularına göre çalışma sayfasının belirli bir yazdırma alanını oluşturabilirler.

 Geliştiriciler, belirli bir yazdırma alanı seçmek için set**Alanı yazdır** yöntemi**Sayfa ayarı** sınıf. Yazdırma alanının hücre aralığını bu yönteme argüman olarak sağlayabilirsiniz.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Baskı Başlıklarını Ayarla**
 Aspose.Cells, basılı çalışma sayfanızın tüm sayfalarında tekrarlanmasını istediğiniz satır ve sütun başlıklarını belirlemenizi sağlar. Bunu yapmak için, geliştiriciler set'i kullanabilir.**Başlık Sütunlarını Yazdır** ve**setPrintTitleRows** yöntemleri**Sayfa ayarı** sınıf.

Satırlar veya sütunlar (yazdırılan çalışma sayfasının tüm sayfalarında tekrarlanacak), satır veya sütun numaraları geçirilerek tanımlanır. Örneğin, satırlar \ $1: \ $2 olarak tanımlanır ve sütunlar \ $A: \ $B olarak tanımlanır.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Diğer Yazdırma Seçeneklerini Ayarlayın**
**Sayfa ayarı** class ayrıca genel yazdırma seçeneklerini aşağıdaki gibi ayarlamak için birkaç başka yöntem sağlar:

- **setPrintGridline yöntemi** , kılavuz çizgilerinin yazdırılıp yazdırılmayacağını tanımlayan bu yönteme bir boolean parametresi iletilir
- **setPrintHeadings yöntemi** bu yönteme satır ve sütun başlıklarının yazdırılıp yazdırılmayacağını tanımlayan bir boolean parametresi iletilir.
- **BlackAndWhite yöntemini ayarla** , çalışma sayfasının siyah beyaz modda yazdırılıp yazdırılmayacağını tanımlayan bu yönteme bir boolean parametresi iletilir.
- **setPrintComments yöntemi** , yazdırma yorumlarının çalışma sayfasında mı yoksa çalışma sayfasının sonunda mı görüntüleneceğini tanımlar.
- **setPrintDraft yöntemi** , çalışma sayfasının taslak kalitesinde yazdırılıp yazdırılmayacağını tanımlayan bu yönteme bir boolean parametresi iletilir.
- **setPrintErrors yöntemi** , hücre hatalarının görüntülenen, boş, kısa çizgi veya N/A olarak yazdırılıp yazdırılmayacağını tanımlar

 seti kullanmak için**Yorumları Yazdır** ve ayarla**Yazdırma Hataları** yöntemleri, Aspose.Cells ayrıca, sırasıyla PrintComments ve Set PrintErrors yöntemlerini ayarlamak için bir parametreden geçirilecek önceden tanımlanmış değerleri içeren PrintCommentsType ve PrintErrorsType olmak üzere iki numaralandırma sağlar.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Sayfa Sırasını Ayarla**
**Sayfa ayarı**class, çalışma sayfanızın birden çok sayfasının yazdırılmasını sıralamak için kullanılan set Order yöntemini sağlar. Sayfaları aşağıdaki gibi sıralamak için iki olasılık vardır:

Aşağı ve yukarı, böylece sayfaları sağa yazdırmadan önce tüm sayfaları aşağı yazdırır
Aşağıya doğru, aşağıdaki sayfaları yazdırmadan önce sayfaları soldan sağa yazdıracaktır.
Aspose.Cells, setPage Order yöntemine atanacak önceden tanımlanmış tüm sipariş türlerini içeren PrintOrderType adlı bir numaralandırma sağlar.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
