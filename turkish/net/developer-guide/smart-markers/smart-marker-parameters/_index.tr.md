---
title: Akıllı İşaretleyici Parametreleri
type: docs
weight: 30
url: /tr/net/smart-marker-parameters/
---

## **Tasarım Elektronik Tablosu & Akıllı İşaretçiler**
Tasarımcı elektronik tablolar, görsel biçimlendirme, formüller ve akıllı işaretçiler içeren standart Excel dosyalarıdır. Bağlantılı bir ya da daha fazla veri kaynağını, örneğin proje bilgilerini ve ilgili kişilerin bilgilerini içerebilir. Akıllı işaretçiler, bilgilerin yer almasını istediğiniz hücrelere yazılır.

Tüm akıllı işaretçiler, &= ile başlar. Bir veri işaretçisinin bir örneği, örneğin, &=Party.FullName'dir. Veri işaretçisi birden fazla ögeye yol açarsa, örneğin, tam bir satır, o zaman yeni bilgilere yer açmak için otomatik olarak aşağıdaki satırlar taşınır. Bu şekilde, toplam ve alt toplamlar eklenen verilere dayalı olarak hesaplamak için veri işaretçisinden hemen sonra bir satıra yerleştirilebilir. Eklenen satırlarda hesaplama yapmak için **dinamik formüller** kullanın.

Akıllı işaretçiler çoğu bilgi için **veri kaynağı** ve **alan adı** bölümlerinden oluşur. Özel bilgi, değişkenler ve değişken dizileri ile de iletilmiş olabilir. Değişkenler her zaman sadece bir hücreyi doldururken, değişken dizileri birkaç hücreyi doldurabilir. Bir hücre başına yalnızca bir veri işareti kullanın. Kullanılmayan akıllı işaretçiler kaldırılır.

Akıllı işaretçi ayrıca parametreler içerebilir. Parametreler, bilgilerin nasıl düzenleneceğini değiştirmenize olanak tanır. Bunlar, virgülle ayrılmış bir liste olarak parantez içinde akıllı işaretçinin sonuna eklenir.

## **Akıllı İşaretçi Seçenekleri**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Smart Marker Parametreleri**
Aşağıdaki parametreler kabul edilir:

- **noadd** - Ekstra satırlar eklemeyin.
- **skip:n** - Her veri satırı için n sayısında satır atla.
- **ascending:n** ya da **descending:n** - Akıllı işaretçilerde veriyi sırala. n 1 ise, sütun sıralayıcının ilk anahtarıdır. Veri, veri kaynağının işlenmesinden sonra sıralanır. Örneğin: &=Tablo1.Alan3(ascending:1).
- **horizontal** - Veriyi yukarıdan aşağıya değil, soldan sağa yazın.
- **numeric** - Metni mümkünse numaraya dönüştürür.
- **kaydırma** - Veriyi sığdırmak için aşağıya ya da sağa kaydırarak ekstra satırlar veya sütunlar oluşturun. Kaydırma parametresi, Microsoft Excel'de olduğu gibi çalışır. Örneğin, Microsoft Excel'de bir hücre aralığını seçtiğinizde, sağ tıklayıp **Ekle**'yi seçerek **aşağıya hücre kaydır**, **sağa hücre kaydır** ve diğer seçenekleri belirlediğinizde. Kısacası, **kaydırma** parametresi dikey/normal (yukarıdan aşağıya) ya da yatay (soldan sağa) akıllı işaretler için aynı işlevi doldurur.
- **copystyle** - Temel hücrenin stilini o sütundaki tüm hücrelere kopyala.

noadd ve skip parametreleri, veriyi alternatif satırlara eklemek için birleştirilebilir. Şablon, üstten alta işlenir, bu nedenle alternatif satırın önünde ekstra satırların eklenmesini önlemek için ilk satıra noadd eklemelisiniz.

Birden fazla parametreniz varsa, bunları virgülle ayırın, ancak boşluk bırakmayın: parametreA,parametreB,parametreC

Aşağıdaki ekran görüntüleri, her iki satıra veri eklemenin nasıl yapılacağını göstermektedir.

|**Şablon Dosyası**|**Çıkış Dosyası**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **Dinamik Formüller**
Dinamik formüller, dışa aktarma işlemi sırasında eklenecek satırlara referans olan hücrelere Excel formüllerini eklemenizi sağlar. Dinamik formüller her eklenen satır için tekrarlayabilir veya yalnızca veri işaretinin konumlandığı hücreyi kullanabilir.

Dinamik formüller aşağıdaki ek seçenekleri sağlar:

- r - Geçerli satır numarası.
- 2, -1 - Geçerli satır numarasına göre ofset.

Örneğin:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Dinamik formül işaretleyicisinde, "-1", sırasıyla B ve C sütunlarında mevcut satıra ofset olarak belirlenecektir, atlamalı parametre bir satırdır. Ayrıca, dinamik formüllerde ileri parametreleri uygulamak için ayracı bir karakter olarak belirtmeliyiz.

{{< highlight java >}}

 "~"

{{< /highlight >}}

dinamik formüllerde ileri parametreleri uygulamak için ayraç karakterini bir ayraç kararkteri olarak kullanın.

Aşağıdaki ekran görüntüleri, tekrarlanan dinamik bir formülü ve sonuçlanan Excel çalışma sayfasını göstermektedir.

|**Şablon Dosyası**|**Çıktı Dosyası**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
Hücre "C1" formülü **= A1*B1** içerir, hücre "C2" **= A2*B2** ve hücre "C3" **= A3*B3** içerir.

Akıllı İşaretleri işlemek çok kolaydır. Aşağıdaki örnek kod, Akıllı İşaretlerde dinamik formüllerin nasıl kullanılacağını göstermektedir. [Şablon dosyasını](templateDynamicFormulas.xlsx) yükler ve test verileri oluşturur, işaretleri işleyerek hücrelere veri doldurur. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **SmartMarkers'da Dinamik Formüller ve Değişkenler Nasıl Kullanılır**
Bazen, SmartMarkers'da dinamik formüller ve değişkenler kullanmanız gerekebilir. Dinamik formüller için, özel karakter (~) ayırıcı olarak eklenmelidir. Aspose.Cells, SmartMarkers'da dinamik formüller ve değişkenler kullanımını sağlar. Lütfen [şablon dosyasını](template.xlsx), [json dosyasını](employees-data.json) ve aşağıdaki kodla oluşturulan çıktı Excel dosyasının ekran görüntüsünü kontrol edin.

|**Varsayımların gösterildiği template.xlsx dosyasının ilk sayfası.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**Şablon.xlsx dosyasının ikinci sayfasında smart markerlar gösteriliyor.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](template_result.png)|

Json verileri şu şekildedir:
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
