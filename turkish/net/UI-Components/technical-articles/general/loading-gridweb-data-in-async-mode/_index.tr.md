---
title: GridWeb Verilerini Asenkron Modda Yükleme
type: docs
weight: 40
url: /tr/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: Bu makale, GridWeb de daha iyi performans elde etmek için asenkron modun nasıl kullanılacağını açıklar.
keywords: GridWeb,performans,asenkron,asenkron mod
---

{{% alert color="primary" %}} 

Büyük veri setleriyle bir Çalışma Kitabı oluşturulurken veya büyük bir Microsoft Excel dosyası okunurken, kesinlikle daha fazla zaman ve kaynak gerekecektir. İşlemın alacağı toplam bellek her zaman bir endişe kaynağıdır. Bu zorluğun üstesinden gelmek için alınabilecek önlemler bulunmaktadır. Aspose.Cells.GridWeb, bellek kullanımını düşürmek, azaltmak ve optimize etmek için bazı ilgili seçenekler ve API'lar sağlar. Ayrıca, işlemi daha verimli ve daha hızlı çalıştırmaya yardımcı olabilir. Büyük hücre verileri içeren bir çalışma sayfası için, veri setini asenkron olarak yükleyebilirsiniz, bu da kullanıcı deneyimi için genel performansı artırabilir.

{{% /alert %}} 

GridWeb.EnableAsync seçeneğini kullanarak hücre verileri için bellek ve performansı optimize edin. Büyük bir veri seti oluşturulurken. Seçeneği true olarak ayarladığınızda, veri yükleme yalnızca mevcut görünen pencere alanına dayalı olacaktır. Kısacası, GridWeb'deki çalışma sayfasındaki hücre verilerinde kaydırma yaptığınızda, yeni Pencere verileri yalnızca mevcut kaydırma konumuna bağlı olarak yüklenecektir.

Aşağıdaki örnek, GridWeb'in asenkron modunu etkinleştirmenin nasıl yapıldığını gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
