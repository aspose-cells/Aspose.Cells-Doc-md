---
title: Dinamik Grafikler Oluşturma
type: docs
weight: 200
url: /tr/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, veri kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Başka bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde otomatik olarak değişiklikleri yansıtabilir. Veri kaynağında değişikliği tetiklemek için Excel Tablolarının filtreleme seçeneğini kullanabilir veya ComboBox veya Dropdown listesi gibi bir denetim kullanabilirsiniz.

Bu makale, yukarıda bahsedilen her iki yaklaşımı da kullanarak dinamik grafikler oluşturmak için Aspose.Cells for Java API'larının kullanımını göstermektedir.

{{% /alert %}}

## **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

Aspose.Cells'in bakış açısında Excel tabloları ListObjects olarak adlandırılır, bu nedenle netlik için "Tablo" terimi yerine "ListObject" terimini kullanacağız. Aspose.Cells for .NET API'si ile [ListObject oluşturmayı](/cells/tr/java/creating-a-list-object/) detaylı olarak okuyun.

{{% /alert %}}

ListObjects, kullanıcı etkileşimine bağlı olarak verileri sıralamak ve filtrelemek için yerleşik işlevselliği sağlar. Hem sıralama hem de filtreleme seçenekleri, otomatik olarak ListObject'in üst satırına eklenen açılır listeler aracılığıyla sağlanmaktadır. Bu özelliklere (sıralama ve filtreleme) sahip olmaları nedeniyle, ListObject, veri görselleştirmenin mevcut durumunu yansıtmak için verinin temsili durumunun değişmesini sağlamak için dinamik bir grafik için veri kaynağı olarak hizmet etmek için mükemmel aday gibi görünmektedir.

Demonstrasyonu anlaşılır tutmak için Workbook'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımları adım adım ilerleteceğiz.

1. Boş bir Workbook oluşturun.
1. Workbook'daki ilk Çalışsayfadaki Hücrelere erişin.
1. Hücrelere bazı veriler ekleyin.
1. Eklenen verilere dayalı olarak ListObject oluşturun.
1. ListObject veri aralığına dayalı olarak Grafik oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Dinamik Formüller Kullanma**

Eğer ListObjects'u bir veri kaynağı olarak kullanmak istemiyorsanız, diğer seçenek Excel fonksiyonlarını (veya formülleri) kullanarak dinamik bir veri aralığı oluşturmak ve bir kontrol (ComboBox gibi) kullanarak veride değişiklik yapmak olacaktır. Bu senaryoda, ComboBox'ın seçimine bağlı olarak uygun değerleri getirmek için VLOOKUP fonksiyonunu kullanacağız. Seçim değiştiğinde, VLOOKUP fonksiyonu hücre değerini güncelleyecektir. Eğer bir hücre aralığı VLOOKUP fonksiyonunu kullanıyorsa, tüm aralık kullanıcı etkileşimiyle güncellenebilir, dolayısıyla dinamik grafik için bir veri kaynağı olarak kullanılabilir.

Demonstrasyonu anlaşılır tutmak için Workbook'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımları adım adım ilerleteceğiz.

1. Boş bir Workbook oluşturun.
1. Workbook'daki ilk Çalışsayfadaki Hücrelere erişin.
1. Adlandırılmış Bir Aralık oluşturarak hücrelere bazı veriler ekleyin. Bu veriler dinamik grafik için ser olarak hizmet edecektir.
1. Önceki adımda oluşturulan Adlandırılmış Aralığa dayalı ComboBox oluşturun.
1. VLOOKUP fonksiyonuna dayanacak şekilde hücrelere daha fazla veri ekleyin. Bu veri, VLOOKUP fonksiyonuna kaynak olarak hizmet edecektir.
1. VLOOKUP fonksiyonunu (uygun parametrelerle) bir hücre aralığına ekleyin. Bu aralık, dinamik grafik için kaynak olarak hizmet edecektir.
1. Önceki adımda oluşturulan aralığa dayalı olarak Grafik oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
