---
title: Belge Özelliklerini Yönet
linktitle: Döküman özellikleri
type: docs
weight: 80
url: /tr/net/managing-document-properties/
description: NET API'leri için Aspose.Cells aracılığıyla Belge Özelliklerini nasıl yöneteceğinizi öğrenin.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **giriiş**

Microsoft Excel, elektronik tablo dosyalarına özellikler ekleme olanağı sağlar. Bu belge özellikleri yararlı bilgiler sağlar ve aşağıda ayrıntıları verildiği gibi 2 kategoriye ayrılır.

- Sistem tanımlı (yerleşik) özellikler: Yerleşik özellikler, belge başlığı, yazar adı, belge istatistikleri vb. gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Son kullanıcı tarafından isim-değer çifti şeklinde tanımlanan özel özelliklerdir.

{{% alert color="primary" %}}

Yerleşik ve özel özellikler hakkında bilmeniz gereken en önemli nokta, yerleşik özelliklere erişilip değiştirilebildiği, ancak oluşturulamadığı veya kaldırılamadığıdır. Ancak özel özellikler oluşturulabilir ve yönetilebilir.

{{% /alert %}}

##  **Microsoft Excel'i Kullanarak Belge Özellikleri Nasıl Yönetilir**

 Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG biçiminde yönetmenize olanak tanır. Açmak için lütfen aşağıdaki adımları izleyin.**Özellikler** Excel 2016'daki iletişim kutusu.

1.  itibaren**Dosya** menüsünde *Bilgi**'yi seçin.

|**Bilgi Menüsünün Seçilmesi**|
| :- |
|![yapılacak şey:image_alt_text](managing-document-properties_1.png)|
1.  Tıklamak**Özellikler** başlığına gidin ve "Gelişmiş Özellikler"i seçin.

|**Gelişmiş Özellikler Seçimine Tıklama**|
| :- |
|![yapılacak şey:image_alt_text](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
| :- |
|![yapılacak şey:image_alt_text](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistik, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosyayla ilgili farklı türde bilgilerin yapılandırılmasına yardımcı olur. Özel sekmesi özel özellikleri yönetmek için kullanılır.

##  **Aspose.Cells Kullanarak Belge Özellikleriyle Nasıl Çalışılır**

Geliştiriciler, Aspose.Cells API'lerini kullanarak belge özelliklerini dinamik olarak yönetebilirler. Bu özellik, geliştiricilerin, dosyanın ne zaman alındığı, işlendiği, zaman damgası vb. gibi yararlı bilgileri dosyayla birlikte saklamasına yardımcı olur.

{{% alert color="primary" %}}

 Aspose.Cells for .NET, çıktı dokümanlarına doğrudan API ve Versiyon Numarası bilgilerini yazar. Örneğin, Belge PDF'e işlendiğinde Aspose.Cells for .NET doldurulur**Başvuru** 'Aspose.Cells' değerine sahip alan ve**PDF Üretici** değeri olan alan, örneğin 'Aspose.Cells v17.9'.

Lütfen Aspose.Cells for .NET'e bu bilgiyi çıktı Belgelerinden değiştirmesi veya kaldırması talimatını veremeyeceğinizi unutmayın.

{{% /alert %}}

###  **Belge Özelliklerine Nasıl Erişilir**

 Aspose.Cells API'ler, yerleşik ve özel olmak üzere her iki belge özelliği türünü de destekler. Aspose.Cells'[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir Excel dosyasını temsil eder ve bir Excel dosyası gibi,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf, her biri aşağıdakilerle temsil edilen birden fazla çalışma sayfası içerebilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf, çalışma sayfalarının koleksiyonu ise[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)sınıf.

 Kullan[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Aşağıda açıklandığı gibi dosyanın belge özelliklerine erişmek için.

- Yerleşik belge özelliklerine erişmek için şunu kullanın:[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Özel belge özelliklerine erişmek için şunu kullanın:[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 İkisi de[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) Ve[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) örneğini döndür[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Bu koleksiyon şunları içerir:[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)her biri tek bir yerleşik veya özel belge özelliğini temsil eden nesneler.

 Bir mülke nasıl erişileceği başvuru şartına bağlıdır, yani; özelliğin dizinini veya adını kullanarak[**BelgeÖzellikKoleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)aşağıdaki örnekte gösterildiği gibi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class, belge özelliğinin adını, değerini ve türünü almaya izin verir:

-  Özellik adını almak için şunu kullanın:[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Özellik değerini almak için şunu kullanın:[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)değeri bir Nesne olarak döndürür.
-  Özellik türünü almak için şunu kullanın:[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Bu aşağıdakilerden birini döndürür[**Emlak Tipi**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)numaralandırma değerleri. Özellik türünü aldıktan sonra aşağıdakilerden birini kullanın:**DocumentProperty.ToXXX** kullanmak yerine uygun türün değerini elde etme yöntemleri[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) .**DocumentProperty.ToXXX**yöntemler aşağıdaki tabloda açıklanmıştır.

{{% alert color="primary" %}}

[**Belge Özelliği**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)sınıf ayrıca diğer veri türlerinin değerlerini döndüren bir dizi yöntem de sağlar.

{{% /alert %}}

|**Üye adı**|**Tanım**|**ToXXX Yöntemi**|
| :- | :- | :- |
|Boolean|Özellik veri türü Boolean'dır|ToBool|
|Tarih| Özellik veri türü DateTime'dır. Microsoft Excel'in yalnızca depoladığını unutmayın<br>tarih kısmı, bu türdeki özel bir özellikte saat saklanamaz|ToDateTime|
|Batmadan yüzmek|Özellik veri türü Double'dır|Çifte|
|Sayı|Özellik veri türü Int32'dir|Hedef|
|String|Özellik veri türü: String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **Özel Belge Özellikleri Nasıl Eklenir veya Kaldırılır**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikleri ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır ancak özel özellikleri eklemek veya kaldırmak mümkündür çünkü bunlar kullanıcı tanımlıdır.

###  **Özel Özellikler Nasıl Eklenir?**

 Aspose.Cells API'ler şunları ortaya çıkardı:[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) için yöntem[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) Koleksiyona özel özellikler eklemek için class.[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) yöntemi, özelliği Excel dosyasına ekler ve yeni belge özelliği için bir referansı bir referans olarak döndürür.[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **“İçeriğe bağlantı” Özel Özelliği Nasıl Yapılandırılır**

 Belirli bir aralığın içeriğine bağlı özel bir özellik oluşturmak için[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) yöntem ve geçiş özelliği adı ve kaynağı. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını kontrol edebilirsiniz.[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) mülk. Ayrıca, kaynak aralığını kullanarak da ulaşmak mümkündür.[**Kaynak**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) mülkiyeti[**Belge Özelliği**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)sınıf.

Örnekte basit bir şablon olan Microsoft Excel dosyasını kullanıyoruz. Çalışma kitabında etiketli tanımlanmış bir adlandırılmış aralık var**Aralığım** bu bir hücre değerini ifade eder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **Özel Özellikler Nasıl Kaldırılır**

 Aspose.Cells'i kullanarak özel özellikleri kaldırmak için[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)yöntemi ve kaldırılacak belge özelliğinin adını iletin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **İleri konular**
- [Belge Bilgileri Panelinde görünen Özel Özellikler Ekleme](/cells/tr/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama](/cells/tr/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Yerleşik Belge Özelliklerini kullanarak Excel Dosyasının Belge Sürümünü Belirleme](/cells/tr/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Yerleşik Belge Özelliklerini kullanarak Excel Dosyasının Dilini Belirleme](/cells/tr/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
