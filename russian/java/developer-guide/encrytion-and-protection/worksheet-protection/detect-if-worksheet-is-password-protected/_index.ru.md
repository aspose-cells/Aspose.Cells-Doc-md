---
title: Определить, защищен ли рабочий лист паролем
type: docs
weight: 280
url: /ru/java/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Можно защитить рабочие книги и рабочие листы отдельно. Например, электронная таблица может содержать один или несколько рабочих листов, защищенных паролем, однако сама электронная таблица может быть защищена или не защищена. Aspose.Cells API-интерфейсы предоставляют средства для определения того, защищен ли данный лист паролем или нет. В этой статье показано использование Aspose.Cells for Java API для достижения того же.

{{% /alert %}}

## **Определить, защищен ли рабочий лист паролем**

Aspose.Cells for Java 8.7.0 выставил[**Защита.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) свойство, чтобы определить, защищен ли лист паролем или нет. Логический тип[**Защита.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) поле возвращает**истинный** если[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) защищен паролем и**ЛОЖЬ** если не.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
