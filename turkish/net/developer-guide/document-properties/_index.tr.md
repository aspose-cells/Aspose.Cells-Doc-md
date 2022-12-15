---
title: Belge Özelliklerini Yönet
linktitle: Döküman özellikleri
type: docs
weight: 80
url: /tr/net/managing-document-properties/
description: Elektronik tablo dosyalarının belge özelliklerini yönetin.
---
## **giriiş**

Microsoft Excel, elektronik tablo dosyalarına özellikler ekleme yeteneği sağlar. Bu belge özellikleri yararlı bilgiler sağlar ve aşağıda ayrıntıları verildiği gibi 2 kategoriye ayrılır.

- Sistem tanımlı (yerleşik) özellikler: Yerleşik özellikler, belge başlığı, yazar adı, belge istatistikleri vb. gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özel özellikler.

{{% alert color="primary" %}}

Yerleşik ve özel özellikler hakkında bilinmesi gereken en önemli nokta, yerleşik özelliklere erişilip değiştirilebileceği, ancak oluşturulamayacağı veya kaldırılamayacağıdır. Ancak, özel özellikler oluşturulabilir ve yönetilebilir.

{{% /alert %}}

## **Microsoft Excel Kullanarak Belge Özelliklerini Yönetme**

 Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG tarzında yönetmenizi sağlar. açmak için lütfen aşağıdaki adımları izleyin.**Özellikleri** Excel 2016'da iletişim kutusu.

1.  itibaren**Dosya** menü, seç**Bilgi**.

|**Bilgi Menüsünün Seçilmesi**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](managing-document-properties_1.png)|
1.  Tıklamak**Özellikleri** başlığını açın ve "Gelişmiş Özellikler"i seçin.

|**Gelişmiş Özellikler Seçimine Tıklama**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistikler, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosyayla ilgili farklı türden bilgilerin yapılandırılmasına yardımcı olur. Özel sekmesi, özel özellikleri yönetmek için kullanılır.

## **Aspose.Cells Kullanarak Belge Özellikleriyle Çalışma**

Geliştiriciler, Aspose.Cells API'lerini kullanarak belge özelliklerini dinamik olarak yönetebilir. Bu özellik geliştiricilerin, dosyanın ne zaman alındığı, işlendiği, zaman damgası eklendiği vb. yararlı bilgileri dosyayla birlikte depolamasına yardımcı olur.

{{% alert color="primary" %}}

 Aspose.Cells for .NET, API ve Sürüm Numarası ile ilgili bilgileri doğrudan çıktı belgelerine yazar. Örneğin, Belgeyi PDF'ye dönüştürürken, Aspose.Cells for .NET doldurulur**Başvuru** 'Aspose.Cells' değerine sahip alan ve**PDF Yapımcısı** değeri olan alan, örneğin 'Aspose.Cells v17.9'.

Lütfen Aspose.Cells for .NET'e bu bilgileri çıktı Belgelerinden değiştirme veya kaldırma talimatı veremeyeceğinizi unutmayın.

{{% /alert %}}

### **Belge Özelliklerine Erişme**

 Aspose.Cells API'ler, yerleşik ve özel olmak üzere her iki belge özelliği türünü de destekler. Aspose.Cells'[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class bir Excel dosyasını temsil eder ve bir Excel dosyası gibi[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf, her biri tarafından temsil edilen birden çok çalışma sayfası içerebilir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf, oysa çalışma sayfalarının koleksiyonu şu şekilde temsil edilir:[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)sınıf.

 Kullan[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Dosyanın belge özelliklerine aşağıda açıklandığı gibi erişmek için.

-  Yerleşik belge özelliklerine erişmek için şunu kullanın:[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Özel belge özelliklerine erişmek için şunu kullanın:[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 İkisi de[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) ve[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) örneğini geri ver[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Bu koleksiyon içerir[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)her biri tek bir yerleşik veya özel belge özelliğini temsil eden nesneler.

 Bir mülke nasıl erişileceği başvuru şartına bağlıdır, yani; özelliğin dizinini veya adını kullanarak[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)aşağıdaki örnekte gösterildiği gibi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 bu[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class, belge özelliğinin adını, değerini ve türünü almaya izin verir:

-  Özellik adını almak için şunu kullanın:[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Özellik değerini almak için şunu kullanın:[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)değeri bir Nesne olarak döndürür.
-  Özellik türünü almak için şunu kullanın:[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Bu, şunlardan birini döndürür:[**Emlak Tipi**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) numaralandırma değerleri. Özellik türünü aldıktan sonra,**DocumentProperty.ToXXX** kullanmak yerine uygun türün değerini elde etmek için yöntemler[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . bu**DocumentProperty.ToXXX**yöntemler aşağıdaki tabloda açıklanmıştır.

{{% alert color="primary" %}}

 bu[**Belge Özelliği**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class ayrıca diğer veri türlerinin değerlerini döndüren bir dizi yöntem sağlar.

{{% /alert %}}

|**Üye adı**|**Tanım**|**ToXXX Yöntemi**|
|:- |:- |:- |
|boole|Özellik veri türü Boolean'dır|ToBool|
|Tarih|Özellik veri türü DateTime'dır. Microsoft Excel'in yalnızca depoladığını unutmayın.<br>tarih bölümü, bu türden özel bir özellikte hiçbir zaman depolanamaz|ToDateTime|
|Batmadan yüzmek|Özellik veri türü Double|Çifte|
|Sayı|Özellik veri türü Int32'dir.|ToInt|
|Sicim|Özellik veri türü String'dir|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Özel Belge Özellikleri Ekleme veya Kaldırma**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı oldukları için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Ekleme**

 Aspose.Cells API'ler şu bilgileri açığa çıkardı:[**Ekle**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) için yöntem[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) koleksiyona özel özellikler eklemek için sınıf. bu[**Ekle**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) yöntemi, özelliği Excel dosyasına ekler ve yeni belge özelliği için bir referans olarak bir referans döndürür.[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **"İçeriğe bağlantı" Özel Özelliğini Yapılandırma**

 Belirli bir aralığın içeriğine bağlı özel bir özellik oluşturmak için[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) yöntem ve geçiş özelliği adı ve kaynağı. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını kontrol edebilirsiniz.[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) Emlak. Ayrıca, kullanarak kaynak aralığını elde etmek de mümkündür.[**Kaynak**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) mülkiyeti[**Belge Özelliği**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)sınıf.

 Örnekte basit bir şablon Microsoft Excel dosyası kullanıyoruz. Çalışma kitabı, etiketli tanımlanmış bir adlandırılmış aralığa sahiptir.**Aralığım** bu da bir hücre değerini ifade eder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Özel Özellikleri Kaldırma**

 Aspose.Cells'i kullanarak özel özellikleri kaldırmak için[**DocumentPropertyCollection.Kaldır**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)yöntemini seçin ve kaldırılacak belge özelliğinin adını iletin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **ileri konular**
- [Belge Bilgileri Panelinde görünen Özel Özellikler ekleme](/cells/tr/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama](/cells/tr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Yerleşik Belge Özelliklerini Kullanarak Excel Dosyasının Belge Sürümünü Belirtin](/cells/tr/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Yerleşik Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtin](/cells/tr/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
