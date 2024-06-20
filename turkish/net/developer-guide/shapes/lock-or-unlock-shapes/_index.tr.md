---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir.

Bazı durumlarda, belirli korumalı çalışma sayfalarındaki belirli şekilleri değiştirmeniz gerekebilir; bu durumda, bu şekillerin kilidini açmanız gerekir.

Bu makale, belirtilen şekilleri kilitleme ve kilidini açma konusunda detaylı bir şekilde tanıtacaktır.

{{% /alert %}}

## **Belirtilen çalışma sayfasındaki tüm şekilleri koruma altına al**

Belirli bir çalışma sayfasındaki tüm şekilleri korumak için [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) yöntemini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Korumalı bir çalışma sayfasındaki belirtilen şekillerin kilidini aç**

Korunan bir çalışma sayfasındaki belirli bir şeklin kilidini açmak için [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) özelliğini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

Not: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) özelliği, çalışma sayfası korunduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

