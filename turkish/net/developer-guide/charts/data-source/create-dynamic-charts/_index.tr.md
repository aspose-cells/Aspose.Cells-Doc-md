---
title: Dinamik Grafikler Oluşturun
description: Aspose.Cells for .NET numaralı telefondan dinamik grafiklerin nasıl oluşturulacağını öğrenin. Kılavuzumuz, gereksinimlerinize göre grafik verilerini, serilerini ve biçimlendirmesini dinamik olarak nasıl güncelleyeceğinizi göstererek, değişen verileri çalışma sayfalarınızda görsel olarak sunmanıza olanak tanıyacaktır.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /tr/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, verilerin kapsamını değiştirdiğinizde değişme özelliğine sahiptir. Başka bir deyişle dinamik grafikler, veri kaynağı değiştiğinde değişiklikleri otomatik olarak yansıtabilmektedir. Veri kaynağındaki değişikliği tetiklemek için Excel Tablolarının filtreleme seçeneği veya ComboBox veya Dropdown list gibi bir kontrol kullanılabilir.

Bu makalede, yukarıda belirtilen yaklaşımların her ikisini de kullanarak dinamik grafikler oluşturmak için Aspose.Cells for .NET API'lerin kullanımı gösterilmektedir.

{{% /alert %}}

##  **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

 Excel tabloları Aspose.Cells' perspektifinde ListObjects olarak anılır, bu nedenle açıklık sağlamak için "Tablo" yerine "ListObject" terimini kullanacağız. Lütfen nasıl yapılacağını ayrıntılı olarak okuyun[ListObjects'i oluştur](/cells/tr/net/create-and-format-table/)Aspose.Cells for .NET API ile.

{{% /alert %}}

 ListObjects, kullanıcı etkileşimi üzerine verileri sıralamak ve filtrelemek için yerleşik işlevsellik sağlar. Hem sıralama hem de filtreleme seçenekleri, başlığın başlık satırına otomatik olarak eklenen açılır listeler aracılığıyla sağlanır.[**ListeObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Bu özelliklerden dolayı (sıralama ve filtreleme),[**ListeObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) dinamik bir grafiğe veri kaynağı olarak hizmet etmek için mükemmel bir aday gibi görünüyor çünkü sıralama veya filtreleme değiştirildiğinde, verilerin grafikteki temsili grafiğin mevcut durumunu yansıtacak şekilde değişecektir.[**ListeObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Gösteriyi anlaşılır kılmak için, aşağıdakileri oluşturacağız:[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sıfırdan başlayın ve aşağıda belirtildiği gibi adım adım ilerleyin.

1.  Boş bir tane oluştur[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Erişmek[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) ilkinin[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) içinde[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Hücrelere bazı veriler ekleyin.
1.  Yaratmak[**ListeObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)girilen verilere dayanmaktadır.
1.  Yaratmak[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) veri aralığına dayalı olarak[**ListeObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **Dinamik Formülleri Kullanma**

Kullanmak istememeniz durumunda[**ListeObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Dinamik grafiğin veri kaynağı olarak diğer seçenek, dinamik bir veri aralığı oluşturmak için Excel işlevlerini (veya formüllerini) ve verilerdeki değişikliği tetiklemek için bir denetimi (ComboBox gibi) kullanmaktır. Bu senaryoda ComboBox seçimine göre uygun değerleri getirmek için DÜŞEYARA fonksiyonunu kullanacağız. Seçim değiştirildiğinde DÜŞEYARA işlevi hücre değerini yeniler. Bir hücre aralığı DÜŞEYARA işlevini kullanıyorsa, tüm aralık kullanıcı etkileşimi üzerine yenilenebilir, dolayısıyla dinamik grafik için bir kaynak olarak kullanılabilir.

Gösterimin anlaşılır olmasını sağlamak için, Çalışma Kitabını sıfırdan oluşturacağız ve aşağıda belirtildiği gibi adım adım ilerleyeceğiz.

1.  Boş bir tane oluştur[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Erişmek[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) ilkinin[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) içinde[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Adlandırılmış Aralık oluşturarak hücrelere bazı veriler ekleyin. Bu veriler dinamik grafikte bir seri görevi görecektir.
1.  Yaratmak[**Açılan kutu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)önceki adımda oluşturulan Adlandırılmış Aralığa göre.
1. DÜŞEYARA işlevine kaynak görevi görecek hücrelere biraz daha veri ekleyin.
1. DÜŞEYARA işlevini (uygun parametrelerle) bir hücre aralığına ekleyin. Bu aralık, dinamik grafik için kaynak görevi görecektir.
1.  Yaratmak[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)önceki adımda oluşturulan aralığa göre.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
