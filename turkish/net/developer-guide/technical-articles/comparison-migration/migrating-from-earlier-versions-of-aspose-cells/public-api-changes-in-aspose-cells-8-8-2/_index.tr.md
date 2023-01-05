---
title: Genel API Aspose.Cells 8.8.2'deki değişiklikler
type: docs
weight: 280
url: /tr/net/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.8.1'den 8.8.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Boş Satırları ve Sütunları Silerken Referansları Otomatik Olarak Güncelleyin**
Aspose.Cells for .NET 8.8.2, Cells.DeleteBlankRows & Cells.DeleteBlankColumns yöntemlerinin aşırı yüklenmiş sürümlerini ortaya çıkardı. Yeni yöntemler, DeleteOptions sınıfının bir örneğini kabul edebilir ve formüllerde, grafik serisi verilerinde vb. bozuk referanslardan kaynaklanabilecek durumların üstesinden gelmek için kullanılabilir. DeleteOptions sınıfının şu anda yalnızca bir üyesi var, UpdateReference adında bir Boole türü özelliği. Söz konusu özellik true olarak ayarlanırsa ve DeleteOptions sınıfı örneği Cells.DeleteBlankRows & Cells.DeleteBlankColumns yöntemlerine geçirilirse, API, değişiklikleri karşılamak için (varsa) formül başvurularını dahili olarak ayarlar.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Güncellenmiş Referanslarla Boş Satırları ve Sütunları Silme](/cells/tr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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
