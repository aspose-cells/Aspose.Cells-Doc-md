---
title: Belge Özelliklerini Yönetme
type: docs
weight: 10
url: /tr/java/managing-document-properties/
---

## **Giriş**

Microsoft Excel, elektronik tablo dosyalarına özellik eklemek için yetenek sunmaktadır. Bu belge özellikleri kullanışlı bilgiler sağlar ve ayrıntıları aşağıdaki gibi 2 kategoriye ayrılmıştır.

- Sistem tanımlı (hazır) özellikler: Hazır özellikler belge başlığı, yazar adı, belge istatistikleri gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Kullanıcı tanımlı özellikler son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özelleştirilmiş özelliklerdir.

{{% alert color="primary" %}}

Dahili ve özel özellikler hakkında bilinmesi gereken en önemli nokta, dahili özelliklere erişilebilir ve değiştirilebilir, ancak oluşturulamaz veya kaldırılamazlar, ancak özel belge özellikleri oluşturulabilir ve yönetilebilir.

{{% /alert %}}

## **Microsoft Excel Kullanarak Belge Özelliklerini Yönetme**

Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG şekilde yönetmeyi sağlar. Lütfen aşağıda belirtilen adımları izleyerek Excel 2016'da **Özellikler** iletişim kutusunu açın.

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

## **Aspose.Cells Kullanarak Belge Özellikleri İle Çalışmak**

Geliştiriciler, Aspose.Cells ara yüz yöntemleri kullanarak belge portal değişkenlerini dinamik olarak yönetebilirler. Bu özellik, geliştiricilere dosya ile birlikte alınan bilgiyi depolama olanağı sağlar, örneğin dosyanın ne zaman alındığı, işlendiği, zaman damgalandığı v.b.

{{% alert color="primary" %}}

Aspose.Cells for Java, çıktı belgelerinde API ve Sürüm Numarası hakkında bilgileri doğrudan yazar. Örneğin, Bir Belgeyi PDF'ye dönüştürdüğünde, Aspose.Cells for Java; **Uygulama** alanını 'Aspose.Cells' değeriyle ve **PDF Üreticisi** alanını 'Aspose.Cells for Java v17.9' gibi bir değerle doldurur.

Lütfen unutmayın ki Aspose.Cells for Java'ye çıkış Belgerinden bu bilgileri değiştirmesini veya kaldırmasını talimat veremezsiniz.

{{% /alert %}}

### **Belge Özelliklerine Erişme**

Aspose.Cells API'leri hem hazır hem de özel belge portal özelliklerini destekler. Aspose.Cells'in [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı bir Excel dosyasını temsil eder ve bir Excel dosyası gibi, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı birden fazla çalışma sayfası içerebilir, her biri [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı ile temsil edilirken, çalışma sayfalarının koleksiyonu ise [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) sınıfı ile temsil edilir.

[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)’yi kullanarak dosyanın belge özelliklerine aşağıda açıklandığı şekilde erişebilirsiniz.

- Hazır belge özelliklerine ulaşmak için [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) kullanın.
- Özel belge özelliklerine erişmek için [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) kullanın.

Her ikisi de [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) ve [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) örneğini döndürür. Bu koleksiyon, her biri tek bir yerleşik veya özel belge özelliğini temsil eden [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) nesnelerini içerir.

Bir özelliğe erişmek uygulama gereksinimine bağlıdır, yani; aşağıdaki örnekte gösterildiği gibi, [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) ın dizin veya adını kullanarak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)  sınıfı, belge özelliğinin adını, değerini ve türünü almayı sağlar:

- Özellik adını almak için [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name) kullanın.
- Özellik değerini almak için [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) kullanın. [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value), değeri bir nesne olarak döndürür.
- Özellik türünü almak için [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) kullanın. Bu, [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType) enum değerlerinden birini döndürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Özel Belge Özellikleri Ekleme veya Kaldırma**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı olduğu için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Ekleme**

Aspose.Cells API'leri, özel özellikler eklemek için [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) metodunu [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) sınıfı için açığa çıkarmıştır. [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) metodu, özelliği Excel dosyasına ekler ve yeni belge özelliği için [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) nesnesi olarak bir referans döndürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **"İçeriğe Bağlantı" Özel Özelliği Yapılandırma**

Belirli bir aralığın içeriğine bağlı özel bir özellik oluşturmak için [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String)) yöntemini çağırın ve özellik adı ve kaynağı geçirin. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını kontrol edebilirsiniz. Ayrıca, [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) sınıfının [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) özelliğini kullanarak kaynağın aralığını da alabilirsiniz.

Örneğin basit bir şablon Microsoft Excel dosyası kullanıyoruz. Çalışma kitabında, **MyRange** olarak etiketlenmiş tanımlanan bir adlandırılmış aralık, bir hücre değerine atıfta bulunur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Özel Özellikleri Kaldırma**

Aspose.Cells kullanarak özel özellikleri kaldırmak için [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) yöntemini çağırın ve kaldırılacak belge özelliğinin adını geçirin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
