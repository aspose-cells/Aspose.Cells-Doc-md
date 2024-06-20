---
title: Aspose.Cells 8.8.2 de Genel API Değişiklikleri
type: docs
weight: 280
url: /tr/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için Aspose.Cells API'sinde 8.8.1'den 8.8.2'ye yapılan değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells arkasındaki davranışlardaki değişikliklerin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Boş Satır ve Sütunları Silerken Referansları Otomatik Olarak Güncelleme**
Aspose.Cells for .NET 8.8.2, Cells.DeleteBlankRows ve Cells.DeleteBlankColumns yöntemlerinin aşırı yüklenmiş sürümlerini ortaya çıkardı. Yeni yöntemler, DeleteOptions sınıfının bir örneğini kabul edebilir ve formüllerdeki bozuk referanslar nedeniyle ortaya çıkabilecek durumların üstesinden gelmek için kullanılabilir. DeleteOptions sınıfının şu anda sadece bir üyesi bulunmaktadır, UpdateReference adında Boolean tipinde bir özelliktir. Söz konusu özellik true olarak ayarlandığında ve DeleteOptions sınıfının örneği Cells.DeleteBlankRows ve Cells.DeleteBlankColumns yöntemlerine geçirildiğinde, API içsel olarak formül referanslarını (varsa) değişiklikleri yansıtacak şekilde ayarlayacaktır.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Güncellenmiş Referanslarda Boş Sütun ve Satırların Silinmesi](/cells/tr/net/update-references-in-diğer-çalışma-kitaplarında-silinmiş-satırlar-ve-sütunları-silinirken-güncellenmiş-referanslar/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
