---
title: Dinamik Grafikler Oluşturma
description: Aspose.Cells for .NET de dinamik grafikler oluşturmayı öğrenin. Rehberimiz, değişen verileri görsel olarak sunmanıza olanak tanıyan gereksinimlerinize göre grafik verilerini, serilerini ve biçimlendirmeyi dinamik olarak nasıl güncelleyeceğinizi gösterecektir.
keywords: Aspose.Cells for .NET, grafik oluşturma, dinamik grafikler, veri, seriler, biçimlendirme, çalışma sayfaları, güncelleme
type: docs
weight: 240
url: /tr/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, veri kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Diğer bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde otomatik olarak değişiklikleri yansıtabilir. Veri kaynağında değişikliği tetiklemek için, Excel Tablolarının filtreleme seçeneğini veya ComboBox veya Dropdown listesi gibi bir kontrolü kullanabilirsiniz.

Bu makale, Aspose.Cells for .NET API'lerini kullanarak yukarıda bahsedilen her iki yaklaşımı da kullanarak dinamik grafikler oluşturmayı göstermektedir.

{{% /alert %}}

## **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

Aspose.Cells'ın bakış açısından Excel tabloları ListObjects olarak adlandırılır, bu nedenle netlik için "Tablo" yerine "ListObject" terimini kullanacağız. Aspose.Cells for .NET API'si ile [Tablo Oluşturma ve Biçimlendirme](/cells/tr/net/create-and-format-table/) hakkında detaylı bilgi edinin.

{{% /alert %}}

ListObjects, kullanıcı etkileşimi üzerine verileri sıralama ve filtreleme işlevselliği sağlar. Hem sıralama hem de filtreleme seçenekleri, otomatik olarak başlık satırına eklenen açılır listeler aracılığıyla sağlanır. Bu özellikler (sıralama ve filtreleme) nedeniyle, ListObject, veri kaynağı olarak dinamik bir grafik için mükemmel aday gibi görünmektedir, çünkü sıralama veya filtreleme değiştiğinde, grafikteki veri temsil edilen tablonun mevcut durumunu yansıtmak üzere değiştirilecektir.

Anlatımın anlaşılmasını basitleştirmek için, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) oluşturacağız ve aşağıda anlatılan adımlara göre adım adım ilerleyeceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) oluşturun.
1. İlk [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ın [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 'indeki [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 'na erişin.
1. Hücrelere bazı veriler ekleyin.
1. Eklenen verilere bağlı olarak [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) oluşturun.
1. [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) veri aralığına göre [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Dinamik Formüller Kullanma**

Dinamik grafiklerin veri kaynağı olarak [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) kullanmak istemiyorsanız, diğer seçenek Excel işlevlerini (veya formülleri) kullanarak verinin dinamik bir aralığını oluşturmak ve bir kontrolü (örneğin ComboBox) veri değişikliğini tetiklemek için kullanmak olacaktır. Bu senaryoda, ComboBox'un seçimine bağlı olarak uygun değerleri getirmek için VLOOKUP işlevini kullanacağız. Seçim değiştirildiğinde, VLOOKUP işlevi hücre değerini güncelleyecek. Bir hücre aralığı VLOOKUP işlevini kullanıyorsa, tüm aralık, kullanıcı etkileşimi sırasında yenilenebilir, bu nedenle dinamik bir grafik için veri kaynağı olarak kullanılabilir.

Demonstrasyonu anlaşılır tutmak için Workbook'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımları adım adım ilerleteceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) oluşturun.
1. İlk [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ın [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 'indeki [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 'na erişin.
1. Hücrelere Adlandırılmış Aralık oluşturarak bazı veriler ekleyin. Bu veriler, dinamik grafik için seri olarak hizmet edecektir.
1. Önceki adımda oluşturulan Adlandırılmış Aralık temel alınarak [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) oluşturun.
1. VLOOKUP işlevine veri kaynağı olacak hücrelere başka veriler ekleyin.
1. Uygun parametrelerle VLOOKUP işlevini bir hücre aralığına ekleyin. Bu aralık, dinamik grafik için kaynak olarak hizmet edecektir.
1. Önceki adımda oluşturulan aralığa dayalı olarak [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
