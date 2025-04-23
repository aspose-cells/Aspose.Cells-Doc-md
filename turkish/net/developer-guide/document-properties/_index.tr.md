---
title: Belge Portal Yönetimi
linktitle: Belge Portalları
type: docs
weight: 80
url: /tr/net/managing-document-properties/
description: Belge Portalları üzerinden Aspose.Cells for NET arayüz yöntemleri ile nasıl yöneteceğinizi öğrenin.
keywords: Belge Portalları nasıl yönetilir C# dilinde, C# kullanarak Belge Portal Değişkenlerini veya Yöntemlerini belirleme, C# kullanarak Belge Portal Değişkenlerini veya Yöntemlerini ekleme ya da silme, Aspose.Cells for NET üzerinden Belge Portalları Neşelerine nasıl ulaşılır.
---


## **Giriş**

Microsoft Excel, elektronik tablo dosyalarına özellik eklemek için yetenek sunmaktadır. Bu belge özellikleri kullanışlı bilgiler sağlar ve ayrıntıları aşağıdaki gibi 2 kategoriye ayrılmıştır.

- Sistem tanımlı (hazır) özellikler: Hazır özellikler belge başlığı, yazar adı, belge istatistikleri gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Kullanıcı tanımlı özellikler son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özelleştirilmiş özelliklerdir.

{{% alert color="primary" %}}

Hazır ve özel özellikler hakkında bilinmesi gereken en önemli nokta hazır özelliklerin erişilebilir ve değiştirilebilir olduğudur, ancak oluşturulamaz veya kaldırılamaz. Öte yandan, özel özellikler oluşturulabilir ve yönetilebilir.

{{% /alert %}}

## **Microsoft Excel ile Belge Portalları Nasıl Yönetilir**

Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG yöntemiyle yönetmenize izin verir. Lütfen aşağıdaki adımları izleyerek Excel 2016'daki **Özellikler** iletişim kutusunu açın.

1. **Dosya** menüsünden **Bilgi**'yi seçin.

|**Bilgi Menüsünü Seçme**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **Özellikler** başlığına tıklayıp "Gelişmiş Özellikler”'i seçin.

|**Gelişmiş Özellikler Seçimini Tıklama**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistikler, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosya ile ilgili farklı türde bilgileri yapılandırmaya yardımcı olur. Gümrük sekmesi, özel özellikleri yönetmek için kullanılır.

## **Aspose.Cells Kullanarak Belge Portalları İle Nasıl Çalışılır**

Geliştiriciler, Aspose.Cells ara yüz yöntemleri kullanarak belge portal değişkenlerini dinamik olarak yönetebilirler. Bu özellik, geliştiricilere dosya ile birlikte alınan bilgiyi depolama olanağı sağlar, örneğin dosyanın ne zaman alındığı, işlendiği, zaman damgalandığı v.b.

{{% alert color="primary" %}}

Aspose.Cells for .NET API ve Versiyon Numarası hakkındaki bilgileri doğrudan çıktı belgelerine yazar. Örneğin, bir belgeyi PDF formatına dönüştürdüğünüzde, Aspose.Cells for .NET **Uygulama** alanını 'Aspose.Cells' değeri ile ve **PDF Üreticisi** alanını, örneğin 'Aspose.Cells v17.9' değeri ile doldurur.

Lütfen dikkat edin ki, Aspose.Cells for .NET'ye çıktı Belgelerinden bu bilgileri değiştirmesini ya da kaldırmasını söyleyemezsiniz.

{{% /alert %}}

### **Belge Portallarına Erişim Yöntemleri**

Aspose.Cells API'leri hem hazır hem de özel belge portal özelliklerini destekler. Aspose.Cells'in [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı bir Excel dosyasını temsil eder ve bir Excel dosyası gibi, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı birden fazla çalışma sayfası içerebilir, her biri [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı ile temsil edilirken, çalışma sayfalarının koleksiyonu ise [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) sınıfı ile temsil edilir.

[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)’yi kullanarak dosyanın belge özelliklerine aşağıda açıklandığı şekilde erişebilirsiniz.

- Hazır belge özelliklerine ulaşmak için [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) kullanın.
- Özel belge özelliklerine ulaşmak için [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) kullanın.

Her iki [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) ve [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties), [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) örneğini döndürür. Bu koleksiyon, her biri yerleşik veya özel belge özelliğini temsil eden [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) nesne içerir.

Bir özelliğe erişmek uygulama gereksinimine bağlıdır, yani; aşağıdaki örnekte gösterildiği gibi, [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) ın dizin veya adını kullanarak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)  sınıfı, belge özelliğinin adını, değerini ve türünü almayı sağlar:

- Özellik adını almak için [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name) kullanın.
- Özellik değerini almak için [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) kullanın. [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value), değeri bir nesne olarak döndürür.
- Özellik türünü almak için [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) kullanın. Bu, [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) numaralandırma değerlerinden birini döndürür. Özellik türünü aldıktan sonra, uygun türün değerini almak için [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) kullanmak yerine **DocumentProperty.ToXXX** yöntemlerinden birini kullanın. **DocumentProperty.ToXXX** yöntemleri aşağıdaki tabloda tanımlanmıştır.

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)  sınıfı ayrıca diğer veri tiplerinin değerlerini döndüren bir dizi yöntem de sağlar.

{{% /alert %}}

|**Üye Adı**|**Açıklama**|**ToXXX Yöntemi**|
| :- | :- | :- |
|Boolean| Özellik veri türü Boolean'dır|ToBool|
|Date| Özellik veri türü DateTime'dir. Microsoft Excel'in bu tür özel bir özelliğinde sadece tarih kısmının saklandığına dikkat edin, zaman saklanamaz|ToDateTime|
|Float| Özellik veri türü Double'dır|ToDouble|
|Number| Özellik veri türü Int32'dir|ToInt|
|String| Özellik veri türü String'dir|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Özel Belge Özellikleri Nasıl Eklenir veya Kaldırılır**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı olduğu için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Nasıl Eklenir**

Aspose.Cells API'leri, özel özellikleri koleksiyona eklemek için [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) yöntemini [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) sınıfı için açığa çıkardı. [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) yöntemi, özelliği Excel dosyasına ekler ve yeni belge özelliği için bir referans olarak bir [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) nesnesi döndürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **“İçeriğe bağlantı” Özel Özelliğin Yapılandırılması Nasıl Yapılır**

Belirli bir aralığın içeriğine bağlı özel bir özellik oluşturmak için [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) yöntemini çağırın ve özellik adı ve kaynağı geçirin. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını kontrol edebilirsiniz. Ayrıca, [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) sınıfının [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) özelliğini kullanarak kaynağın aralığını da alabilirsiniz.

Örneğin basit bir şablon Microsoft Excel dosyası kullanıyoruz. Çalışma kitabında, **MyRange** olarak etiketlenmiş tanımlanan bir adlandırılmış aralık, bir hücre değerine atıfta bulunur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Özel Özellikler Nasıl Kaldırılır**

Aspose.Cells kullanarak özel özellikleri kaldırmak için [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) yöntemini çağırın ve kaldırılacak belge özelliğinin adını geçirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Gelişmiş Konular**
- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama](/cells/tr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme](/cells/tr/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme](/cells/tr/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="csharp" >}}
