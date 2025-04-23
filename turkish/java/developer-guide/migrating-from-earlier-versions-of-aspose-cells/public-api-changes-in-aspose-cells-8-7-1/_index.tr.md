---
title: Aspose.Cells 8.7.1 de Genel API Değişiklikleri
type: docs
weight: 250
url: /tr/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiriciler için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.7.0'dan 8.7.1'e kadar açıklar. Yeni ve güncelleştirilmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. dahil olduğu gibi, Aspose.Cells'in arkasındaki davranışlarda da herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **LookInType.ORIGINAL_VALUES Özelliği Eklendi**
Aspose.Cells API'ları zaten elektronik tablolarda [Veri bul veya Ara](/cells/tr/java/find-or-search-data/) özelliğini destekler, böylece hücre değeri ve formülündeki belirli bir içeriği bulabilir. Ancak, bu özellik, hücreye uygulanan biçimi ve onun değerini değiştirebilen biçimlendirmenin eksikliğini yaşamış ve sonuç olarak metni orijinal değer kullanılamaz hale getirmiştir. Bu Aspose.Cells API'ları sürümüyle, LookInType.ORIGINAL_VALUES adında başka bir sabit genel API'ya açılmıştır, bu da yukarıda tartışılan durumu aşmanızı sağlar. 

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için [Orijinal Değerleri Kullanarak Veri Arama](https://docs.aspose.com/cells/java/search-data-using-original-values/) adlı ayrıntılı makaleyi inceleyin

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
