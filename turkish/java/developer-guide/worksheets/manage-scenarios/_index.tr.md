---
title: Çalışma Sayfalarından Senaryolar Oluşturun, Yönetin veya Kaldırın
linktitle: Senaryoları Yönet
type: docs
weight: 120
url: /tr/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Bazen elektronik tablolarda senaryolar oluşturmanız, değiştirmeniz veya silmeniz gerekir. Senaryo, bir veya daha fazla formülle birbirine bağlanan değişken girdi hücrelerini içeren, adlandırılmış bir what-if modelidir. Bir senaryo oluşturmadan önce, içine farklı değerlerin eklenebileceği hücrelere bağlı en az bir formül içerecek şekilde bir çalışma sayfası tasarlayın. Aşağıdaki örnek, Aspose.Cells API'leri kullanılarak bir çalışma sayfasından senaryoların nasıl oluşturulacağını ve kaldırılacağını gösterir.

{{% /alert %}}

 Aspose.Cells bazı yararlı sınıflar sağlar, örneğin[**Senaryo Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Senaryo**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**SenaryoGirişHücresiKoleksiyon**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) ve[**SenaryoGirişHücresi**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . Ayrıca şunları sağlar:[**Çalışma Sayfası.Senaryolar**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)Emlak. Aşağıdaki örnek kod, (bazı senaryoları içeren) bir XLSX Excel dosyasını açar ve mevcut bir senaryoyu çalışma sayfasından kaldırır. Ayrıca Excel dosyasını kaydetmeden önce yeni bir senaryo ekler. Bir senaryo içeren çok basit bir şablon dosyası kullanır.

Kodu çalıştırdıktan sonra var olan bir senaryo kaldırılır ve çalışma sayfasına yeni bir senaryo eklenir.

**çıktı dosyası**

![yapılacaklar:resim_alternatif_Metin](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
