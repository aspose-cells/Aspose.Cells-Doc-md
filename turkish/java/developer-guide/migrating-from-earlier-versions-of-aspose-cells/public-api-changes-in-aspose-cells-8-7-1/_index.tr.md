---
title: Genel API Aspose.Cells 8.7.1'deki değişiklikler
type: docs
weight: 250
url: /tr/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.7.0 sürümünden 8.7.1 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **LookInType.ORIGINAL_VALUES Özelliği Eklendi**
 Aspose.Cells API'ler zaten şunu destekliyor:[Veri Bul veya Ara](/cells/tr/java/find-or-search-data/)hücre değeri ve formülde belirli bir içerik parçasını bulmak için elektronik tablolar için özellik. Bununla birlikte, bu özellik, içeriğin değerinin yanı sıra görünümünü de değiştirebilecek, sonuç olarak metni orijinal değer kullanılarak aranamaz hale getirebilecek hücreye uygulanan biçimlendirmenin yönünden yoksundu. Aspose.Cells API'lerinin bu sürümüyle, LookInType.ORIGINAL_VALUES adlı başka bir sabit, yukarıda tartışılan durumun üstesinden gelinmesine izin veren API geneline sunuldu.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Orijinal Değerleri Kullanarak Veri Arama](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
