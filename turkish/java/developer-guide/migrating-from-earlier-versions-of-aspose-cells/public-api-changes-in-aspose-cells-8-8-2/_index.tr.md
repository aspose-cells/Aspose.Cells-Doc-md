---
title: Genel API Aspose.Cells 8.8.2'deki değişiklikler
type: docs
weight: 290
url: /tr/java/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.8.1'den 8.8.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Boş Satırları ve Sütunları Silerken Referansları Otomatik Olarak Güncelle**
 Aspose.Cells for Java 8.8.2, Cells.deleteBlankRows & Cells.deleteBlankColumns yöntemlerinin aşırı yüklenmiş sürümlerini ortaya çıkardı. Yeni yöntemler, DeleteOptions sınıfının bir örneğini kabul edebilir ve formüllerde, grafik serisi verilerinde vb. bozuk referanslardan kaynaklanabilecek durumların üstesinden gelmek için kullanılabilir. DeleteOptions sınıfının şu anda yalnızca bir üyesi var, UpdateReference adında bir Boole türü özelliği. Söz konusu özellik true olarak ayarlanırsa ve DeleteOptions sınıfı örneği Cells.deleteBlankRows & Cells.deleteBlankColumns yöntemlerine geçirilirse, API, değişiklikleri karşılamak için (varsa) formül referanslarını dahili olarak ayarlar.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Güncellenmiş Referanslarla Boş Satırları ve Sütunları Silme](/cells/tr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
