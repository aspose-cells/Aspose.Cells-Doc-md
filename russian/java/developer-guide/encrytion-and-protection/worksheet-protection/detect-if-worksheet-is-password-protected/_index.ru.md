---
title: Определить, защищен ли рабочий лист паролем
type: docs
weight: 280
url: /ru/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Возможна защита книг и рабочих листов отдельно. Например, электронная таблица может содержать один или несколько рабочих листов, защищенных паролем, однако сама электронная таблица может быть защищена или нет. API Aspose.Cells предоставляет возможность определить, защищен ли заданный рабочий лист паролем. В этой статье демонстрируется использование API Aspose.Cells for Java для достижения этой цели.

{{% /alert %}}

## **Определение, защищен ли рабочий лист паролем**

Aspose.Cells for Java 8.7.0 предоставил свойство [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) для определения, защищен ли рабочий лист паролем или нет. Логическое поле [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) возвращает **true**, если [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) защищен паролем, и **false**, если нет.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
