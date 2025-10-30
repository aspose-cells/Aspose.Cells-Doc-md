---
title: SmartMarkers da Aralık Parametresi Nasıl Kullanılır
type: docs
weight: 10
url: /tr/net/how-to-use-range-parameter-in-smart-markers/
---

## **Smart Markers'da Aralık Parametresi Kullanımının Nedenleri**
SmartMarkers'daki aralık parametresi, kaynak verilerle (örneğin, JSON, veritabanları) doldururken verilerin tam olarak nerede ve nasıl yerleştirileceğini hassas şekilde kontrol etmek için kullanılır. Bu, özellikle değişken uzunluktaki diziler veya karmaşık gruplamalarla çalışırken dinamik veri çıktısını yönetmeye yardımcı olur.

1. Veri Yerleştirmeyi Kontrol Et ve Çakışmayı Önle: Veri kaynaklarında dinamik diziler (örneğin, her kayıt için değişen eleman sayısı) varsa, aralık parametresi, verilerin tanımlı bir Excel aralığında doldurulmasını sağlar ve bitişik hücrelere veya bölümlere taşmayı engeller.

2. Dinamik Dizi Formüllerini Handle Et: Dinamik dizileri transpose etmek gibi işlemler (örneğin, &=TRANSPOSE(DataArray)) için aralık parametresi, çıktı boyutunun gerçek veriye uygun olmasını sağlar ve önceki işlemlerden kalan değerleri (örneğin, boş alanlarda sıfırlar) bırakmaz.

3. Gruplama ve Hiyerarşik Veri Desteği: Veri gruplaması gerekiyorsa (örneğin, iç içe JSON yapıları), aralık parametresi, hiyerarşik çıktı alanlarını tanımlamada yardımcı olur. Örneğin, kayıtları ana kategori altında gruplarken, manuel satır ayarlarına gerek kalmadan. Tanımlı bir aralık yoksa, SmartMarkers iç içe ilişkileri doğru şekilde temsil edemeyebilir, özellikle veri kaynaklarında açık hiyerarşiler yoksa.

4. Şablon Tasarımını ve Tutarlılığı Artırma: Aralıklar belirterek, biçimlendirme, formüller ve sınırların çıktı alanına tutarlı şekilde uygulanmasını sağlarsınız. Bu, tutarsız hücre stili veya bozuk formüller gibi sorunları önler.

5. Performansı Optimize Et ve Veri Sıralaması: Aralık parametresi, araçların verileri şablonlara doldurmadan önce önceden sıralamasını sağlar, böylece gruplandırılmış veriler doğru sırayla görünür.

## **SmartMarkers'da Aralık Parametresi Nasıl Kullanılır**
Bazen, SmartMarkers'da belirli bir aralıkta sıralama ve diğer işlemler yapmanız gerekebilir. Aspose.Cells, SmartMarkers'da aralık parametresi kullanımını mümkün kılar. Lütfen [şablon dosyasını](range.xlsx), [json dosyasını](range.json) ve aşağıdaki kodla oluşturulan çıktı Excel dosyasının ekran görüntüsünü kontrol edin.

|**range.xlsx dosyasının ilk sayfası ve akıllı işaretleyiciler gösteriliyor.**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](range_result.png)|

Json verileri şu şekildedir:
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
