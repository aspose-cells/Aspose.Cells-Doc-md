---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir.

Bazı durumlarda, belirli korumalı çalışma sayfalarındaki belirli şekilleri değiştirmeniz gerekebilir; bu durumda, bu şekillerin kilidini açmanız gerekir.

Bu makale, belirtilen şekilleri kilitleme ve kilidini açma konusunda detaylı bir şekilde tanıtacaktır.

{{% /alert %}}

## **Belirtilen çalışma sayfasındaki tüm şekilleri koruma altına al**

Korumalı bir çalışsayıdaki belirtilen şekilleri kilidini açmak için, belirtilen çalışsayıdaki [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)) yöntemini kullanın. Aşağıdaki örnek kodda olduğu gibi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Korumalı bir çalışma sayfasındaki belirtilen şekillerin kilidini aç**

Korunan bir çalışma sayfasında belirli bir şekli kilidini açmak için [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) kullanın. Aşağıdaki örnek kodda gösterildiği gibi.

Not: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) yöntemi sadece çalışma sayfası korunduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

