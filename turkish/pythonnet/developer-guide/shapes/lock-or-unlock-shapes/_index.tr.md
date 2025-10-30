---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir.

Bazı durumlarda, belirli korumalı çalışma sayfalarındaki belirli şekilleri değiştirmeniz gerekebilir; bu durumda, bu şekillerin kilidini açmanız gerekir.

Bu makale, belirtilen şekilleri kilitleme ve kilidini açma konusunda detaylı bir şekilde tanıtacaktır.

{{% /alert %}}

## **Belirtilen çalışma sayfasındaki tüm şekilleri koruma altına al**

Belirli bir çalışma sayfasındaki tüm şekilleri korumak için aşağıdaki örnek kodda gösterildiği gibi [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType) yöntemini kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Korumalı bir çalışma sayfasındaki belirtilen şekillerin kilidini aç**

Korunan bir çalışma sayfasında belirli bir şeklin kilidini açmak için [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) yöntemini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

Not: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) yöntemi, çalışma sayfası korunduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
