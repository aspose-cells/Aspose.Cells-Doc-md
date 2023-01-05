---
title: GridWeb Verilerini Zaman Uyumsuz Modda Yükleme
type: docs
weight: 40
url: /tr/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

Büyük veri kümeleri içeren bir Çalışma Kitabı oluştururken veya büyük bir Microsoft Excel dosyasını okurken, bunu yapmak kesinlikle daha fazla zaman ve kaynak gerektirecektir. İşlemin alacağı toplam bellek her zaman bir endişe kaynağıdır. Zorlukla başa çıkmak için alınabilecek önlemler var. Aspose.Cells.GridWeb, bellek kullanımını azaltmak, azaltmak ve optimize etmek için bazı ilgili seçenekler ve API'ler sağlar. Ayrıca, sürecin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir. Büyük hücre verileri içeren bir çalışma sayfası için, veri kümesini eşzamansız olarak yükleyebilirsiniz; bu, kullanıcı deneyimi için genel performansı artırabilir.

{{% /alert %}} 

Hücre verileri için belleği ve performansı optimize etmek üzere GridWeb.EnableAsync seçeneğini kullanın. Hücreler için büyük bir veri seti oluştururken. Seçeneği true olarak ayarladığınızda, veri yükleme yalnızca mevcut görünür Windows alanını temel alacaktır. Kısacası, GridWeb'de çalışma sayfasının hücre verilerini kaydırdığınızda, yalnızca geçerli kaydırma konumuna dayalı olarak yeni Windows verilerini yükleyecektir.

Aşağıdaki örnek, GridWeb'in zaman uyumsuz modunun nasıl etkinleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
