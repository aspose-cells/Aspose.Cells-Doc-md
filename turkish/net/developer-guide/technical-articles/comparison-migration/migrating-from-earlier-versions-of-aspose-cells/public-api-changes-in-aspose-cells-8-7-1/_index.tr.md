---
title: Genel API Aspose.Cells 8.7.1'deki değişiklikler
type: docs
weight: 240
url: /tr/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.7.0 sürümünden 8.7.1 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **LookInType.OriginalValues Özelliği Eklendi**
 Aspose.Cells API'ler zaten şunu destekliyor:[Veri Bul veya Ara](/cells/tr/net/find-or-search-data/)hücre değeri ve formülde belirli bir içerik parçasını bulmak için elektronik tablolar için özellik. Bununla birlikte, bu özellik, içeriğin değerinin yanı sıra görünümünü de değiştirebilecek, sonuç olarak metni orijinal değer kullanılarak aranamaz hale getirebilecek hücreye uygulanan biçimlendirmenin yönünden yoksundu. Aspose.Cells API'lerinin bu sürümüyle, LookInType.OriginalValues adlı başka bir sabit, yukarıda tartışılan durumun üstesinden gelinmesine izin veren API geneline sunuldu.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Orijinal Değerleri Kullanarak Veri Arama](/cells/tr/net/search-data-using-original-values/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **GridWeb için OnBeforeColumnFilter Etkinliği Eklendi**
Aspose.Cells.GridWeb for .NET 8.7.1, GridWeb kullanıcı arabirimi aracılığıyla gerçekleştirilen filtreleme mekanizmasına geri arama işlevi gören OnBeforeColumnFilter olayını ortaya çıkardı. Adından da anlaşılacağı gibi olay, sütun filtreleme uygulanmadan önce tetiklenir ve sütun dizini ve filtrenin uygulanması gereken değer gibi filtreleme bilgilerini almak için kullanılabilir.

Basit kullanım senaryosu aşağıdaki gibidir.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Olayı GridWeb kontrolüne kaydetmeyi unutmayın<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
