---
title: Sütun Filtre Sunucu Tarafı Olaylarını Kullanımı
type: docs
weight: 90
url: /tr/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: Bu makale, GridWeb de sütun filtre olayını nasıl ele alınacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Veri filtreleme muhtemelen belirli bir kriter temelinde verileri filtrelemenize izin veren en yaygın kullanılan Excel özelliğidir. Filtrelenmiş veriler, kriteri karşılayan yalnızca satırları göstererek, kriteri karşılamayan satırları gizleyerek gösterilir.
Aspose.Cells.GridWeb bileşeni, arabirimi kullanarak veri filtreleme yapma yeteneği sağlar. Yeteneklerini genişletmek için Aspose.Cells.GridWeb bileşeni ayrıca GridWeb UI aracılığıyla yapılan filtreleme mekanizmasına geri çağrı olarak hizmet edebilecek iki olay sağlar.

{{% /alert %}} 
## **Sütun Filtre Uygulama Üzerinde Sunucu Tarafı Olayını Kullanma**
Ayrıntılar aşağıda belirtilmiştir.

1. OnBeforeColumnFilter: Bir sütuna uygulanmadan önce filtre uygulanmadan önce ateşlenir.
1. OnAfterColumnFilter: Bir sütuna filtre uygulandıktan sonra ateşlenir.

Yukarıdaki olayları eklemek ve atamak için Aspose.Cells.GridWeb bileşeninin ASPX betiğidir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Bu olaylar, filtreleme işlemi hakkında kullanıcı tarafından seçilen sütun indisini ve değerini almak için kullanılabilir. OnBeforeColumnFilter etkinliğinin sütun indisini ve değerini almak için aşağıdaki örnekte kullanımı gösterilmiştir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Öte yandan, filtre uygulandıktan sonra filtrelenmiş satır sayısını almak gerekiyorsa, aşağıdaki gibi OnAfterColumnFilter etkinliği kullanılabilir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Tüm [GridWeb etkinlikleriyle çalışma](/cells/tr/net/aspose-cells-gridweb/working-with-gridweb-events/) tanıtımına bakın ve bu etkinliklerin nasıl ele alınacağına dair bazı ayrıntılarını inceleyin.

{{% /alert %}}
