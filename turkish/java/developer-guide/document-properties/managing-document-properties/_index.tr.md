---
title: Belge Özelliklerini Yönetme
type: docs
weight: 10
url: /tr/java/managing-document-properties/
---
## **Giriş**

Microsoft Excel, elektronik tablo dosyalarına özellikler ekleme yeteneği sağlar. Bu belge özellikleri yararlı bilgiler sağlar ve aşağıda ayrıntıları verildiği gibi 2 kategoriye ayrılır.

- Sistem tanımlı (yerleşik) özellikler: Yerleşik özellikler, belge başlığı, yazar adı, belge istatistikleri vb. gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özel özellikler.

{{% alert color="primary" %}}

Yerleşik ve özel özellikler hakkında bilinmesi gereken en önemli nokta, yerleşik özelliklere erişilip değiştirilebileceği, ancak oluşturulamayacağı veya kaldırılamayacağı, ancak özel belge özelliklerinin oluşturulabileceği ve yönetilebileceğidir.

{{% /alert %}}

## **Microsoft Excel Kullanarak Belge Özelliklerini Yönetme**

 Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG tarzında yönetmeye izin verir. açmak için lütfen aşağıdaki adımları izleyin.**Özellikler** Excel 2016'da iletişim kutusu.

1.  itibaren**Dosya** menü, seç**Bilgi**.

|**Bilgi Menüsünün Seçilmesi**|
|:- |
|![yapılacaklar:resim_alternatif_metin](managing-document-properties_1.png)|
1.  Tıklamak**Özellikler**başlığını açın ve "Gelişmiş Özellikler"i seçin.

|**Gelişmiş Özellikler Seçimine Tıklama**|
|:- |
|![yapılacaklar:resim_alternatif_metin](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
|:- |
|![yapılacaklar:resim_alternatif_metin](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistikler, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosyayla ilgili farklı türden bilgilerin yapılandırılmasına yardımcı olur. Özel sekmesi, özel özellikleri yönetmek için kullanılır.

## **Aspose.Cells Kullanarak Belge Özellikleriyle Çalışma**

Geliştiriciler, Aspose.Cells API'lerini kullanarak belge özelliklerini dinamik olarak yönetebilir. Bu özellik geliştiricilerin, dosyanın ne zaman alındığı, işlendiği, zaman damgası eklendiği vb. yararlı bilgileri dosyayla birlikte depolamasına yardımcı olur.

{{% alert color="primary" %}}

 Aspose.Cells for Java, API ve Sürüm Numarası ile ilgili bilgileri doğrudan çıktı belgelerine yazar. Örneğin, Belge PDF'e işlendiğinde, Aspose.Cells for Java doldurulur**Uygulama** 'Aspose.Cells' değerine sahip alan ve**PDF Yapımcı** değeri olan alan, örneğin 'Aspose.Cells for Java v17.9'.

Lütfen Aspose.Cells for Java'e bu bilgileri çıktı Belgelerinden değiştirme veya kaldırma talimatı veremeyeceğinizi unutmayın.

{{% /alert %}}

### **Belge Özelliklerine Erişme**

Aspose.Cells API'ler, yerleşik ve özel olmak üzere her iki belge özelliği türünü de destekler. Aspose.Cells'[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class bir Excel dosyasını temsil eder ve bir Excel dosyası gibi[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf, her biri tarafından temsil edilen birden çok çalışma sayfası içerebilir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf, oysa çalışma sayfalarının koleksiyonu şu şekilde temsil edilir:[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)sınıf.

 Kullan[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Dosyanın belge özelliklerine aşağıda açıklandığı gibi erişmek için.

-  Yerleşik belge özelliklerine erişmek için şunu kullanın:[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  Özel belge özelliklerine erişmek için[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 İkisi de[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) ve[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) örneğini döndür[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Bu koleksiyon içerir[**Belge Özelliği**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)her biri tek bir yerleşik veya özel belge özelliğini temsil eden nesneler.

 Bir mülke nasıl erişileceği başvuru şartına bağlıdır, yani; özelliğin dizinini veya adını kullanarak[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)aşağıdaki örnekte gösterildiği gibi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 bu[**Belge Özelliği**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)class, belge özelliğinin adını, değerini ve türünü almaya izin verir:

-  Özellik adını almak için şunu kullanın:[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  Özellik değerini almak için şunu kullanın:[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)değeri bir Nesne olarak döndürür.
-  Özellik türünü almak için şunu kullanın:[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Bu, şunlardan birini döndürür:[**Emlak Tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)numaralandırma değerleri.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Özel Belge Özellikleri Ekleme veya Kaldırma**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı oldukları için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Ekleme**

 Aspose.Cells API'ler şu bilgileri açığa çıkardı:[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) yöntemi[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) koleksiyona özel özellikler eklemek için sınıf. bu[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) yöntemi, özelliği Excel dosyasına ekler ve yeni belge özelliği için bir referans olarak bir referans döndürür.[**Belge Özelliği**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)nesne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **"İçeriğe bağlantı" Özel Özelliğini Yapılandırma**

 Belirli bir aralığın içeriğine bağlı özel bir özellik oluşturmak için[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) yöntemi ve özelliğin adını ve kaynağını iletin. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını kontrol edebilirsiniz.[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) Emlak. Ayrıca, kullanarak kaynak aralığını elde etmek de mümkündür.[**Kaynak**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) mülkiyeti[**Belge Özelliği**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)sınıf.

 Örnekte basit bir şablon Microsoft Excel dosyası kullanıyoruz. Çalışma kitabı, etiketli tanımlanmış bir adlandırılmış aralığa sahiptir.**Aralığım** bu da bir hücre değerini ifade eder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Özel Özellikleri Kaldırma**

 Aspose.Cells'i kullanarak özel özellikleri kaldırmak için[**DocumentPropertyCollection.kaldır**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) yöntemi ve kaldırılacak belge özelliğinin adını iletin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
