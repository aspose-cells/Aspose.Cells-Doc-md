---
title: Dinamik Grafikler Oluşturma
description: Aspose.Cells for Python via .NET kullanarak dinamik grafikler nasıl oluşturulur öğrenin. Kılavuzumuz, grafik verilerini, serilerini ve biçimlendirmelerini ihtiyaçlarınıza göre dinamik olarak güncellemeyi gösterecek, böylece değişen verileri görsel olarak sunabilirsiniz.
keywords: Aspose.Cells for Python via .NET, grafikler, dinamik grafikler, veri, seriler, biçimlendirme, çalışma sayfaları, güncelleme.
type: docs
weight: 240
url: /tr/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dinamik (veya etkileşimli) grafikler, veri kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Diğer bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde otomatik olarak değişiklikleri yansıtabilir. Veri kaynağında değişikliği tetiklemek için, Excel Tablolarının filtreleme seçeneğini veya ComboBox veya Dropdown listesi gibi bir kontrolü kullanabilirsiniz.

Bu makale, Aspose.Cells for Python via .NET API'lerini kullanarak her iki yaklaşımla dinamik grafikler oluşturma kullanımını gösterir.

{{% /alert %}}

## **Excel Tablolarını Kullanma**

{{% alert color="primary" %}}

Excel tabloları, Aspose.Cells perspektifinde ListObject olarak adlandırılır, bu yüzden daha açıklayıcı olması için "Tablo" yerine "ListObject" terimini kullanacağız. Aspose.Cells for Python via .NET API'si ile ListObject'leri nasıl oluşturup biçimlendireceğinizi detaylıca okumak için lütfen [ListObject'ler nasıl oluşturulur](/cells/tr/python-net/create-and-format-table/) sayfasını ziyaret edin.

{{% /alert %}}

ListObject'ler, kullanıcı etkileşimiyle veri sıralaması ve filtrelemesi yapma özelliğine sahiptir. Hem sıralama hem de filtreleme seçenekleri, otomatik olarak eklenen başlık satırındaki açılır listeler aracılığıyla sağlanır. Bu özellikler (sıralama ve filtreleme) nedeniyle, [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) muhtemelen bir dinamik grafiğin veri kaynağı olarak mükemmel bir adaydır çünkü sıralama veya filtreleme değiştiğinde, grafikteki verilerin temsili güncellenecek ve grafikteki [veri kaynağı] güncel duruma uyacak şekilde değişecektir.

Anlatımın anlaşılmasını basitleştirmek için, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) oluşturacağız ve aşağıda anlatılan adımlara göre adım adım ilerleyeceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) oluşturun.
1. İlk [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) ın [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 'indeki [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 'na erişin.
1. Hücrelere bazı veriler ekleyin.
1. Eklenen verilere bağlı olarak [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) oluşturun.
1. [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) veri aralığına göre [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **Dinamik Formüller Kullanma**

Dinamik grafiklerin veri kaynağı olarak [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) kullanmak istemiyorsanız, diğer seçenek Excel işlevlerini (veya formülleri) kullanarak verinin dinamik bir aralığını oluşturmak ve bir kontrolü (örneğin ComboBox) veri değişikliğini tetiklemek için kullanmak olacaktır. Bu senaryoda, ComboBox'un seçimine bağlı olarak uygun değerleri getirmek için VLOOKUP işlevini kullanacağız. Seçim değiştirildiğinde, VLOOKUP işlevi hücre değerini güncelleyecek. Bir hücre aralığı VLOOKUP işlevini kullanıyorsa, tüm aralık, kullanıcı etkileşimi sırasında yenilenebilir, bu nedenle dinamik bir grafik için veri kaynağı olarak kullanılabilir.

Demonstrasyonu anlaşılır tutmak için Workbook'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımları adım adım ilerleteceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) oluşturun.
1. İlk [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) ın [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 'indeki [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 'na erişin.
1. Hücrelere Adlandırılmış Aralık oluşturarak bazı veriler ekleyin. Bu veriler, dinamik grafik için seri olarak hizmet edecektir.
1. Önceki adımda oluşturulan Adlandırılmış Aralık temel alınarak [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) oluşturun.
1. VLOOKUP işlevine veri kaynağı olacak hücrelere başka veriler ekleyin.
1. Uygun parametrelerle VLOOKUP işlevini bir hücre aralığına ekleyin. Bu aralık, dinamik grafik için kaynak olarak hizmet edecektir.
1. Önceki adımda oluşturulan aralığa dayalı olarak [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) oluşturun.
1. Sonucu diske kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
