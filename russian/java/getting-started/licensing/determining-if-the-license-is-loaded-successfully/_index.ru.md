---
title: Определение того, успешно ли загружена лицензия
type: docs
weight: 210
url: /ru/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)свойство, которое вы можете использовать, чтобы определить, успешно ли загружена лицензия или нет. Если вы вызовете этот метод до установки лицензии, он вернет false, а если вы вызовете этот метод после установки лицензии, он вернет true, указывая на то, что лицензия была успешно загружена.

{{% /alert %}}

## **Определение того, успешно ли загружена лицензия**

 Следующий код обращается к[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)перед установкой лицензии и возвращает false. Затем он загружает лицензию и снова обращается к свойству, которое теперь возвращает true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Консольный вывод**

Вот консольный вывод приведенного выше примера кода

{{< highlight "java" >}}

false

true

{{< /highlight >}}
