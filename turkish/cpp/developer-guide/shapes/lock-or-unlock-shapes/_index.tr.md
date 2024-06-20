---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir.

Bazı durumlarda, belirli korumalı çalışma sayfalarındaki belirli şekilleri değiştirmeniz gerekebilir; bu durumda, bu şekillerin kilidini açmanız gerekir.

Bu makale, belirtilen şekilleri kilitleme ve kilidini açma konusunda detaylı bir şekilde tanıtacaktır.

{{% /alert %}}

## **Belirtilen çalışma sayfasındaki tüm şekilleri koruma altına al**

Belirtilen çalışsaydaki tüm şekilleri korumak için [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) methodunu kullanın, aşağıdaki örnek kodda olduğu gibi.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Korumalı bir çalışma sayfasındaki belirtilen şekillerin kilidini aç**

Korunan çalışsaydaki belirli şeklin kilidini açmak için [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) ve [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) kullanın, aşağıdaki örnek kodda olduğu gibi.

Not: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) ve [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) yalnızca çalışma sayfası korunduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

