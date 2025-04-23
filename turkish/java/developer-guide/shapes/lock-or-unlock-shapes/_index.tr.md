---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir.

Bazı durumlarda, belirli korumalı çalışma sayfalarındaki belirli şekilleri değiştirmeniz gerekebilir; bu durumda, bu şekillerin kilidini açmanız gerekir.

Bu makale, belirtilen şekilleri kilitleme ve kilidini açma konusunda detaylı bir şekilde tanıtacaktır.

{{% /alert %}}

## **Belirtilen çalışma sayfasındaki tüm şekilleri koruma altına al**

Belirtilen çalışma sayfasındaki tüm şekilleri korumak için [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-) methodunu kullanın, aşağıdaki örnek kodda gösterildiği gibi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **Korumalı bir çalışma sayfasındaki belirtilen şekillerin kilidini aç**

Korumalı bir çalışma sayfasındaki belirtilen şekillerin kilidini açmak için [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) ve [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) methodlarını aşağıdaki örnek kodda gösterildiği gibi kullanın.

Not: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) ve [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) yalnızca çalışma sayfası korumalı olduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

{{< app/cells/assistant language="java" >}}
