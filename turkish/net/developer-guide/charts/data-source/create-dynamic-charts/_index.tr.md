---
title: Dinamik Grafikler Oluşturun
type: docs
weight: 240
url: /tr/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, verilerin kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Başka bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde değişiklikleri otomatik olarak yansıtabilir. Veri kaynağındaki değişikliği tetiklemek için Excel Tablolarının filtreleme seçeneği veya ComboBox veya Dropdown list gibi bir kontrol kullanılabilir.

Bu makale, yukarıda belirtilen yaklaşımların her ikisini de kullanarak dinamik grafikler oluşturmak için Aspose.Cells for .NET API'lerin kullanımını göstermektedir.

{{% /alert %}}

## **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

 Excel tabloları Aspose.Cells' perspektifinde ListObjects olarak adlandırılır, bu nedenle netlik için "Tablo" yerine "ListObject" terimini kullanacağız. Lütfen nasıl yapılacağını ayrıntılı olarak okuyun[ListObjects oluştur](/cells/tr/net/create-and-format-table/) Aspose.Cells for .NET API ile.

{{% /alert %}}

 ListObjects, kullanıcı etkileşimi üzerine verileri sıralamak ve filtrelemek için yerleşik işlevsellik sağlar. Hem sıralama hem de filtreleme seçenekleri, otomatik olarak başlık satırına eklenen açılır listeler aracılığıyla sağlanır.[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Bu özellikler (sıralama ve filtreleme) nedeniyle,[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)dinamik bir grafiğin veri kaynağı olarak hizmet etmek için mükemmel bir aday gibi görünüyor, çünkü sıralama veya filtreleme değiştirildiğinde, grafikteki verilerin temsili grafiğin mevcut durumunu yansıtacak şekilde değiştirilecektir.[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Gösterimi anlaşılır kılmak için,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sıfırdan ve aşağıda özetlendiği gibi adım adım ilerleyin.

1.  boş oluştur[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Erişmek[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) ilkinden[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) içinde[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Hücrelere bazı veriler ekleyin.
1.  Oluşturmak[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Girilen verilere göre.
1.  Oluşturmak[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) veri aralığına göre[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Dinamik Formülleri Kullanma**

 kullanmak istememeniz durumunda[**Nesne Listesi**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)dinamik grafiğe bir veri kaynağı olarak, diğer seçenek ise dinamik bir veri aralığı oluşturmak için Excel işlevlerini (veya formüllerini) ve verilerdeki değişikliği tetiklemek için bir denetimi (ComboBox gibi) kullanmaktır. Bu senaryoda, ComboBox seçimine dayalı olarak uygun değerleri getirmek için DÜŞEYARA işlevini kullanacağız. Seçim değiştirildiğinde DÜŞEYARA işlevi hücre değerini yeniler. Bir hücre aralığı DÜŞEYARA işlevini kullanıyorsa, tüm aralık kullanıcı etkileşimi üzerine yenilenebilir, bu nedenle dinamik grafiğin kaynağı olarak kullanılabilir.

Gösterimin anlaşılmasını kolaylaştırmak için, Çalışma Kitabını sıfırdan oluşturacağız ve aşağıda özetlendiği gibi adım adım ilerleyeceğiz.

1.  boş oluştur[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Erişmek[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) ilkinden[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) içinde[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Bir Adlandırılmış Aralık oluşturarak hücrelere bazı veriler ekleyin. Bu veriler, dinamik tabloya bir dizi olarak hizmet edecektir.
1.  Oluşturmak[**Açılan kutu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)önceki adımda oluşturulan Adlandırılmış Aralığa göre.
1. DÜŞEYARA işlevine kaynak görevi görecek hücrelere biraz daha veri ekleyin.
1. DÜŞEYARA işlevini (uygun parametrelerle) bir hücre aralığına ekleyin. Bu aralık, dinamik tablo için bir kaynak görevi görecektir.
1.  Oluşturmak[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)önceki adımda oluşturulan aralığa göre.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
