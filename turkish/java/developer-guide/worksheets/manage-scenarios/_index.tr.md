---
title: Çalışma Sayfalarından Senaryoları Oluşturma, Manipüle Etme veya Kaldırma
linktitle: Senaryoları Yönetme
type: docs
weight: 120
url: /tr/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

Bazen çalışma kitaplarında senaryo oluşturmanız, manipüle etmeniz veya silmeniz gerekebilir. Senaryo, bir veya daha fazla formülle birbirine bağlanmış değişken giriş hücrelerini içeren adlandırılmış bir ne olur modelidir. Senaryo oluşturmadan önce, farklı değerlerin eklenebileceği en az bir hücre içeren bir çalışma sayfası tasarlayın. Aşağıdaki örnek, Aspose.Cells API'lerini kullanarak bir çalışma sayfasından senaryo oluşturmayı ve kaldırmayı göstermektedir.

{{% /alert %}}

Aspose.Cells, örneğin [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) ve [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) gibi bazı kullanışlı sınıflar sağlar. Ayrıca, [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios) özelliğini sağlar. Aşağıdaki örnek kod, senaryolar içeren bir XLSX Excel dosyası açar (bazı senaryolar içeren) ve mevcut senaryoyu çalışma sayfasından kaldırır. Excel dosyasını kaydetmeden önce yeni bir senaryo ekler. Senaryoları içeren çok basit bir şablon dosyası kullanır.

Kod çalıştırıldıktan sonra mevcut bir senaryo kaldırılır ve çalışma sayfasına yeni bir senaryo eklenir.

**Çıkış dosyası**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
