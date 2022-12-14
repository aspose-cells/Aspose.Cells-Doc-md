---
title: Dinamik Grafikler Oluşturun
type: docs
weight: 200
url: /tr/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, verilerin kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Başka bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde değişiklikleri otomatik olarak yansıtabilir. Veri kaynağındaki değişikliği tetiklemek için Excel Tablolarının filtreleme seçeneği veya ComboBox veya Dropdown list gibi bir kontrol kullanılabilir.

Bu makale, yukarıda belirtilen yaklaşımların her ikisini de kullanarak dinamik grafikler oluşturmak için Aspose.Cells for Java API'lerin kullanımını göstermektedir.

{{% /alert %}}

## **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

 Excel tabloları Aspose.Cells' perspektifinde ListObjects olarak adlandırılır, bu nedenle netlik için "Tablo" yerine "ListObject" terimini kullanacağız. Lütfen nasıl yapılacağını ayrıntılı olarak okuyun[ListObjects oluştur](/cells/tr/java/creating-a-list-object/) Aspose.Cells for .NET API ile.

{{% /alert %}}

ListObjects, kullanıcı etkileşimi üzerine verileri sıralamak ve filtrelemek için yerleşik işlevsellik sağlar. Hem sıralama hem de filtreleme seçenekleri, ListObject'in başlık satırına otomatik olarak eklenen açılır listeler aracılığıyla sağlanır. Bu özellikler (sıralama ve filtreleme) nedeniyle, ListObject, dinamik bir grafiğin veri kaynağı olarak hizmet etmek için mükemmel bir aday gibi görünüyor çünkü sıralama veya filtreleme değiştirildiğinde, grafikteki verilerin temsili mevcut durumu yansıtacak şekilde değiştirilecektir. ListObject durumu.

Gösterimin anlaşılmasını kolaylaştırmak için, Çalışma Kitabını sıfırdan oluşturacağız ve aşağıda özetlendiği gibi adım adım ilerleyeceğiz.

1. Boş bir Çalışma Kitabı oluşturun.
1. Çalışma Kitabındaki ilk Çalışma Sayfasının Cells numarasına erişin.
1. Hücrelere bazı veriler ekleyin.
1. Girilen verilere göre ListObject oluşturun.
1. ListObject'in veri aralığına göre Grafik oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Dinamik Formülleri Kullanma**

ListObjects'i dinamik grafiğe veri kaynağı olarak kullanmak istemiyorsanız, diğer seçenek, dinamik bir veri aralığı oluşturmak için Excel işlevlerini (veya formüllerini) ve değişikliği tetiklemek için bir kontrolü (ComboBox gibi) kullanmaktır. verilerde. Bu senaryoda, ComboBox seçimine dayalı olarak uygun değerleri getirmek için DÜŞEYARA işlevini kullanacağız. Seçim değiştirildiğinde DÜŞEYARA işlevi hücre değerini yeniler. Bir hücre aralığı DÜŞEYARA işlevini kullanıyorsa, kullanıcı etkileşimi üzerine tüm aralık yenilenebilir, bu nedenle dinamik grafiğin kaynağı olarak kullanılabilir.

Gösterimin anlaşılmasını kolaylaştırmak için, Çalışma Kitabını sıfırdan oluşturacağız ve aşağıda özetlendiği gibi adım adım ilerleyeceğiz.

1. Boş bir Çalışma Kitabı oluşturun.
1. Çalışma Kitabındaki ilk Çalışma Sayfasının Cells numarasına erişin.
1. Bir Adlandırılmış Aralık oluşturarak hücrelere bazı veriler ekleyin. Bu veriler, dinamik grafiğe seri olarak hizmet edecektir.
1. Önceki adımda oluşturulan Adlandırılmış Aralığa göre ComboBox oluşturun.
1. DÜŞEYARA işlevine kaynak görevi görecek hücrelere biraz daha veri ekleyin.
1. DÜŞEYARA işlevini (uygun parametrelerle) bir hücre aralığına ekleyin. Bu aralık, dinamik grafiğin kaynağı olarak hizmet edecektir.
1. Önceki adımda oluşturulan aralığa göre Grafik oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
