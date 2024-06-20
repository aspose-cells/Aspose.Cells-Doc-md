---
title: Определение успешной загрузки лицензии
type: docs
weight: 210
url: /ru/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed), которое можно использовать для определения успешной загрузки лицензии. Если вы вызовете этот метод перед установкой лицензии, он вернет false, а если вы вызовете этот метод после установки лицензии, он вернет true, указывая на успешную загрузку лицензии.

{{% /alert %}}

## **Определение успешной загрузки лицензии**

В следующем коде происходит доступ к методу [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) перед установкой лицензии, и он возвращает false. Затем он загружает лицензию и снова получает доступ к свойству, которое теперь возвращает true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Вывод в консоль**

Вот вывод консоли из приведенного выше примера кода

{{< highlight java >}}

false

true

{{< /highlight >}}
