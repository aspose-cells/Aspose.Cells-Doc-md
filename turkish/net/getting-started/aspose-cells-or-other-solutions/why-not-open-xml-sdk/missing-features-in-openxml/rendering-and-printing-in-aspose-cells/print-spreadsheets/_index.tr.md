---
title: Elektronik Tabloları Yazdır
type: docs
weight: 20
url: /tr/net/print-spreadsheets/
---

Sayfa ayarları ayarlarının yanı sıra, Kullanıcıların çalışma sayfalarının basılı sayfalarını kontrol etmelerine izin veren birkaç Yazdırma Seçeneği (ayrıca Sayfa Seçenekleri olarak da adlandırılır) sağlar.

- Çalışma sayfasının belirli bir Baskı Alanını seç
- Başlıkları Yazdır
- Izgara Çizgilerini Yazdır
- Satır/Sütun Başlıklarını Yazdır
- Taslak Kalitesine Ulaş
- Yorumları Yazdır
- Hücre Hatalarını Yazdır
- Sayfa Sıralamasını Belirle
  **Yazdırma/Sayfa Seçeneklerini Ayarlama**

Aspose.Cells, tüm bu yazdırma seçeneklerini destekler ve geliştiriciler, PageSetup sınıfının sunmuş olduğu çeşitli özellikler kullanarak istedikleri çalışma sayfaları için bu seçenekleri kolayca yapılandırabilirler. PageSetup sınıfının bu özelliklerinin kullanımı aşağıda daha detaylı olarak tartışılmıştır.
## **Baskı Alanı Belirle**
Varsayılan olarak, veri içeren çalışma sayfasının tam alanını içeren baskı alanı seçilir, ancak geliştiriciler istediklerine göre çalışma sayfasının belirli bir baskı alanını da belirleyebilirler.

Belirli bir baskı alanını seçmek için, geliştiriciler, **PageSetup** sınıfının **PrintArea** yöntemini kullanabilir. Bu yönteme argüman olarak baskı alanının hücre aralığını sağlayabilirsiniz.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Başlıkları Yazdırma**
Aspose.Cells, basılı çalışma sayfasının tüm sayfalarında tekrarlanmasını istediğiniz satır ve sütun başlıklarını belirlemenize olanak tanır. Bunu yapmak için, geliştiriciler **PrintTitleColumns** ve **PrintTitleRows** yöntemlerini **PageSetup** sınıfının kullanabilirler.

(Basılı çalışma sayfasının tüm sayfalarında tekrarlanacak) Satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin, satırlar \$1: \$2 ve sütunlar \$A: \$B olarak tanımlanır.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Diğer Yazdırma Seçeneklerini Belirleme**
**PageSetup** sınıfı ayrıca aşağıdaki genel yazdırma seçeneklerini belirlemek için birkaç başka yöntem sunar:

- **setPrintGridlines yöntemi**, bu yönteme yazdırılacak ızgara çizgilerini yazdır veya yazdırma konusunda tanımlayan bir boolean parametre geçirilir
- **setPrintHeadings yöntemi**, bu yönteme yazdırılacak satır ve sütun başlıklarını yazdır veya yazdırmama konusunda tanımlayan bir boolean parametre geçirilir
- **setBlackAndWhite yöntemi**, bu yönteme çalışma sayfasını siyah beyaz modda yazdır veya yazdırmama konusunda tanımlayan bir boolean parametre geçirilir
- **setPrintComments yöntemi**, çalışma sayfasında yazdırma yorumlarını veya çalışma sayfasının sonunda göstermeyi tanımlayan bir yöntem
- **setPrintDraft yöntemi**, bu yönteme çalışma sayfasını taslak kalitesinde yazdır veya yazdırmama konusunda tanımlayan bir boolean parametre geçirilir
- **setPrintErrors yöntemi**, yazdırılacak hücre hatalarını görüntülenen, boş, tire veya N/A olarak yazdır veya yazdırmama konusunda tanımlayan bir yöntem

**PrintComments** ve **PrintErrors** yöntemlerini kullanmak için, Aspose.Cells ayrıca iki tane enuma sahiptir, PrintCommentsType ve PrintErrorsType, sırasıyla PrintComments ve PrintErrors yöntemlerine geçirilecek önceden tanımlanmış değerleri içerir.

{{< highlight csharp >}}

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
## **Sayfa Sırasını Belirleme**
**PageSetup** sınıfı, çalışma sayfasının birden fazla sayfasının yazdırılacağı sırayı belirlemek için kullanılan bir Order yöntemi sağlar. Sayfaları aşağıda sağdaki sayfalardan önce yazdırmak için iki olasılık vardır:

Önce aşağıya sonra ise alttaki sayfaları yazdırmadan önce sağdan sola doğru tüm sayfaları yazdırır
Önce soldan sağa sonra ise aşağıdan yukarıya doğru tüm sayfaları yazdırmadan önce sol taraftaki sayfaları yazdırır
Aspose.Cells, setPage Order methodi için atanan tüm önceden tanımlanmış sipariş tiplerini içeren PrintOrderType adlı bir numaralandırma sağlar.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
