---
title: Çalışma Sayfalarından Senaryolar Oluşturun, Yönetin veya Kaldırın
linktitle: Senaryoları Yönet
type: docs
weight: 190
url: /tr/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Bazen elektronik tablolarda senaryolar oluşturmanız, değiştirmeniz veya silmeniz gerekir. Bir senaryo, 'ya eğer?' bir veya daha fazla formülle bağlantılı değişken girdi hücrelerini içeren model. Bir senaryo oluşturmadan önce, çalışma sayfasını farklı değerlerin eklenebileceği hücrelere bağlı en az bir formül içerecek şekilde tasarlayın. Aşağıdaki örnek, Aspose.Cells API'leri aracılığıyla bir çalışma kitabındaki bir çalışma sayfasından senaryoların nasıl oluşturulacağını ve kaldırılacağını gösterir.

{{% /alert %}}

Aspose.Cells bazı yararlı sınıflar sağlar, örneğin,[**Senaryo Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Senaryo**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**SenaryoGirişHücresiKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , ve[**SenaryoGirişHücresi**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) sınıflar. Ayrıca şunları sağlar:[**Çalışma Sayfası.Senaryolar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)Emlak. Aşağıdaki örnek kod, bazı senaryoları içeren ve mevcut bir senaryoyu kaldıran bir XLSX Excel dosyasını açar. Ayrıca, Excel dosyasını kaydetmeden önce çalışma sayfasına yeni bir senaryo ekler. Örnek, bir senaryo içeren çok basit bir şablon dosyası kullanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
