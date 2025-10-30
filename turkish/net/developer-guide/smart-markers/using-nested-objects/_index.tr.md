---
title: Akıllıca Üst Üste Binen Nesneleri Akıllı İşaretçilerle Excel e İçe Aktarma
type: docs
weight: 30
url: /tr/net/how-to-import-nested-objects-with-smart-markers/
---

## **Neden Üst Üste Binen Nesneleri Akıllı İşaretçilerle Kullanmak**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Hiyerarşik Veri Temsili: Gerçek veri doğası gereği iç içe geçmiştir (örneğin, Bir Sipariş Bir Müşteri içerir, ona da Bir Adres). İç içe nesneler bu yapıyı yansıtır, düzleştirilmiş / yapay alanlardan kaçınır, örneğin müşteri_sehir. 
2. İsim Çakışmalarını Önleme: Düz yapılar karışıklık riski taşır (örneğin, ürün_adi vs. tedarikçi_adi).İç içe isim alanlarını doğal olarak kapsar:
<<product.name>> vs. <<supplier.name>>.
3. Modülerlik ve Yeniden Kullanım: Alt nesneleri çeşitli bağlamlarda yeniden kullanın, Adres nesnesi Müşteri, Satıcı veya Çalışan işaretçilerinde gömülebilir. Adrese yapılan değişiklikler evrensel olarak yansır.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Çerçeve / Araç Desteği: Modern motorlar (ör. Handlebars, React, FoxPro) iç içe geçmiş yolları yerel olarak çözümler. JSON / API'lerle uyumludur, burada iç içe veriler standarttır.

## **Anlaşılamayan Türleri veya Özel Nesneleri Akıllı İşaretçilerle Nasıl İçe Aktarılır**
Aspose.Cells ayrıca akıllı işaretçilerde anonim türleri veya özel nesneleri destekler. Aşağıdaki örnek, bu nasıl çalıştığını göstermektedir. Anlık nesnelerden veri içe aktarma kullanımı için şu makaleyi ziyaret edin:

[Dinamik nesneden veri içe aktarma](/cells/tr/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **İç içe Nesneleri Akıllı İşaretçilerle Nasıl İçe Aktarılır**
Aspose.Cells, iç içe geçmiş nesneleri akıllı işaretlerde destekler, iç içe geçen nesneler basit olmalıdır. Basit bir şablon dosyası kullanıyoruz. Birkaç iç içe akıllı işaret içeren tasarımcı elektronik tabloyu gösteren SM_NestedObjects.xlsx dosyasının ilk çalışma sayfasını görüntüleyin.

|** SM_NestedObjects.xlsx dosyasının ilk çalışma sayfasında iç içe akıllı işaretleri gösteren ilk çalışma sayfasının **|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Genel Listeyi İç içe Nesne Olarak Akıllı İşaretçilerle Nasıl İçe Aktarılır**
Aspose.Cells artık iç içe genel liste kullanımını da destekliyor. Lütfen aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin. Ekran görüntüsünde gördüğünüz gibi, bir Öğretmen nesnesinin birden fazla gömülü Öğrenci nesnesini içerdiğini görebilirsiniz.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **İç içe Nesneleri Satır Satır Olmadan Smart Markers ile Nasıl İçe Aktarılır**
Mevcut varsayılan işleme yöntemi akıllı işaretleri satır satır işlemektir. Ancak bazen aynı veri tablosunun akıllı işaretleri birlikte işlenmesi gerekebilir, satırda olup olmadığına bakılmaksızın, bu durumda işlemi çağırmadan önce bir adlandırılmış aralık "_CellsSmartMarkers" belirtmeniz ve WorkbookDesigner.LineByLine'ı false olarak belirtmeniz gerekir. 
Akıllı İşaretlerle Veri Birleştirirken Bildirim Alma

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
