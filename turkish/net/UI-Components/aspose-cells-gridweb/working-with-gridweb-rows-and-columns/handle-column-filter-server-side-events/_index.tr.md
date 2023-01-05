---
title: Sütun Filtre Sunucusu Yan Olaylarını İşle
type: docs
weight: 90
url: /tr/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

Veri filtreleme, muhtemelen verileri belirli bir kritere göre filtrelemenize izin veren en yaygın kullanılan Excel özelliğidir. Filtrelenen veriler, ölçütü karşılamayan satırları gizleyerek yalnızca koşulu sağlayan satırları görüntüler.
Aspose.Cells.GridWeb bileşeni, arayüzünü kullanarak veri filtrelemeyi gerçekleştirme olanağı sağlar. Aspose.Cells.GridWeb bileşeni, yeteneklerini genişletmek için GridWeb UI aracılığıyla yapılan filtreleme mekanizmasına geri arama görevi görebilecek iki olay da sağlar.

{{% /alert %}} 
## **Sütun Filtresi Uygulanırken Sunucu Tarafı Olayını İşleme**
Aşağıda ayrıntıları verilen iki ana olay vardır.

1. OnBeforeColumnFilter: Filtre bir sütuna uygulanmadan önce tetiklenir.
1. OnAfterColumnFilter: Filtre bir sütuna uygulandıktan sonra tetiklenir.

Yukarıda belirtilen olayları eklemek ve atamak için Aspose.Cells.GridWeb bileşeninin ASPX komut dosyası aşağıdadır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Bu olaylar, sütun indeksi ve filtrenin uygulanması gereken değer gibi filtreleme işlemi hakkında yararlı bilgiler elde etmek için kullanılabilir. Aşağıda, OnBeforeColumnFilter olayının kullanıcının filtreleme için GridWeb kullanıcı arayüzünde seçtiği sütun indeksini ve değerini almak için kullanıldığını gösteren kod parçası yer almaktadır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Öte yandan, filtre uygulandıktan sonra gereksinim filtrelenmiş satır sayısını almaksa, OnAfterColumnFilter olayını aşağıda gösterildiği gibi kullanabilirsiniz.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 Tüm girişleri kontrol edin[GridWeb Events ile Çalışma](/cells/tr/net/working-with-gridweb-events/) bu olayın nasıl ele alınacağına dair bazı ayrıntılarla birlikte.

{{% /alert %}}
