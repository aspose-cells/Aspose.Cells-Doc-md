---
title: Çalışma Sayfalarından Senaryoları Oluşturma, Manipüle Etme veya Kaldırma
linktitle: Senaryoları Yönetme
type: docs
weight: 190
url: /tr/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Bu makalede, C# Kitaplığı ve .NET API ile Excel Çalışma Sayfalarında Senaryolar oluşturmayı, manipüle etmeyi veya kaldırmayı nasıl öğreneceksiniz.
keywords: c# ile senaryo çalışma sayfası oluşturma, c# ile senaryo excel çalışma sayfasından kaldırma, c# ile senaryo çalışma sayfasını manipüle etme
---

{{% alert color="primary" %}}

Bazen Elektronik Tablolarda senaryolar oluşturmanızı, manipüle etmenizi veya silmenizi gerekebilir. Senaryo, bir veya daha fazla formülle bağlı değişken giriş hücrelerini içeren adlandırılmış 'ne olurdu?' modelidir. Bir senaryo oluşturmadan önce, farklı değerlerin eklenebileceği en az bir formül içeren çalışma sayfasını tasarlayın. Aşağıdaki örnek, Aspose.Cells API'leri aracılığıyla bir iş kitabındaki bir çalışma sayfasından senaryolar oluşturmayı ve kaldırmayı gösterir.

{{% /alert %}}

Aspose.Cells, örneğin [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection), ve [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) sınıfları gibi bazı kullanışlı sınıflar sağlar. Ayrıca [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios) özelliğini sağlar. Aşağıdaki örnek, birkaç senaryo içeren XLSX Excel dosyasını açar ve mevcut bir senaryoyu kaldırır. Ayrıca, Excel dosyasını kaydetmeden önce çalışma sayfasına yeni bir senaryo ekler. Örnek, senaryo içeren çok basit bir şablon dosyası kullanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
