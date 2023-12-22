---
title: Bir Çalışma Sayfasında Maksimum Aralığı Alın
type: docs
weight: 360
url: /tr/net/get-max-range-in-a-worksheet/
description: Bu makalede, .Net kitaplığı için Aspose.Cells ile Excel dosyalarının maksimum aralığının, maksimum veri aralığının ve maksimum görüntüleme aralığının nasıl elde edileceği açıklanmaktadır.
---
{{% alert color="primary" %}} 

Çalışma sayfasından veri okurken maksimum alanı bilmemiz gerekir.

Bir çalışma sayfasındaki tüm verileri kopyalarken maksimum alanı bilmemiz gerekir.

Belirli bir alanı html ve pdf'e aktarırken maksimum alanı bilmemiz gerekir.

 .Net için Aspose.Cells, bir çalışma sayfasında maksimum aralığı bulmanın farklı yollarını içerir.


{{% /alert %}} 



##  **Maksimum menzil elde etme**
 Aspose.Cells'de, eğer[**sıra**](https://reference.aspose.com/cells/net/aspose.cells/row) Ve[**kolon**](https://reference.aspose.com/cells/net/aspose.cells/column) nesneler başlatıldığında, boş satır veya sütunlarda veri olmasa bile bu satırlar ve sütunlar maksimum alana kadar sayılacaktır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **Maksimum veri aralığı elde ediliyor**
Çoğu durumda, aralığın dışındaki boş hücreler biçimlendirilmiş olsa bile yalnızca tüm verileri içeren tüm aralıkları elde etmemiz gerekir.
Şekiller, tablolar ve pivot tablolarla ilgili ayarlar da göz ardı edilecek.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **Maksimum görüntüleme aralığı elde ediliyor**
Çalışma sayfasındaki tüm verileri HTML, PDF veya görsellere aktardığımızda veriler, stiller, grafikler, tablolar ve pivot tablolar dahil olmak üzere tüm görünür nesneleri içeren bir alan elde etmemiz gerekir.
Aşağıdaki kodlar maksimum gösterim aralığının html'ye nasıl dönüştürüleceğini gösterir:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

 Burada[kaynak excel dosyası](Book1.xlsx).
