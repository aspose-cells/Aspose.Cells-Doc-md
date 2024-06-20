---
title: Özel Uygulama Fabrikası kullanarak Bellek Akışı nın özel uygulamasını oluşturmak
type: docs
weight: 40
url: /tr/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) adında bir API sağlamıştır. Bu API, varsayılan MemoryStream yerine Geri Dönüştürülebilir bellek uygulamasını kullanarak özel uygulama sağlama imkanı sunar.

## **Özel Uygulama Fabrikası kullanarak Bellek Akışı'nın özel uygulamasını oluşturmak**

Aşağıdaki örnek kod, programınızda [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) kullanımını göstermektedir. Bazen sistemde yeterli bellek olabilir fakat bellek arka arkaya değildir. Bellek Akışı nesneleri ardışık bellek kullanır ancak Bellek Akışı'nın uygulamasını öyle bir şekilde sağlayabilirsiniz ki bunun yerine ardışık olmayan bellek kullanır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
