---
title: Aspose.Cells 8.7.1 de Genel API Değişiklikleri
type: docs
weight: 240
url: /tr/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiriciler için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.7.0'dan 8.7.1'e kadar açıklar. Yeni ve güncelleştirilmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. dahil olduğu gibi, Aspose.Cells'in arkasındaki davranışlarda da herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Eklenen LookInType.OriginalValues Özelliği**
Aspose.Cells API'leri zaten elektronik tablolardaki [Veri Bulma veya Arama](/cells/tr/net/find-or-search-data/) özelliğini destekler, böylece hücre değeri ve formülünde belirli bir içeriği bulmak için. Bununla birlikte, bu özellik, içeriğin görünümünü ve değerini değiştirebilecek olan hücreye uygulanan biçimlendirmenin yönünü eksikti, bu nedenle metni orijinal değeri kullanarak aranamaz hale getirir. Aspose.Cells API'lerinin bu sürümü ile LookInType.OriginalValues adında başka bir sabit genel API'ye açılmıştır. Bu, yukarıda tartışılan durumu aşmak için kullanılabilen bir sabit genel API'ye izin verir.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla ayrıntı için [Orijinal Değerleri Kullanarak Veri Arama](/cells/tr/net/search-data-using-original-values/) ayrıntılı makalesine göz atın

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **GridWeb için OnBeforeColumnFilter Olayı Eklendi**
Aspose.Cells.GridWeb for .NET 8.7.1, GridWeb UI aracılığıyla yapılan filtreleme mekanizmasına geri çağrı sağlayan OnBeforeColumnFilter olayını açığa çıkardı. İsminden de anlaşılacağı gibi, olay filtreleme uygulamadan önce tetiklenir ve filtrelemenin uygulanacağı sütun endeksi ve değeri gibi filtreleme bilgilerini almak için kullanılabilir.

Basit kullanım senaryosu aşağıdaki gibi görünüyor.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
