---
title: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 280
url: /ja/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

ワークブックとワークシートを別々に保護することができます。例えば、スプレッドシートには1つ以上のパスワードで保護されたワークシートが含まれている場合がありますが、スプレッドシート自体が保護されている場合といない場合があります。Aspose.Cells APIは、特定のワークシートがパスワードで保護されているかどうかを検出する手段を提供します。この記事では、Aspose.Cells for JavaAPIの使用方法を示しています。

{{% /alert %}}

## **ワークシートがパスワードで保護されているかどうかを検出する**

Aspose.Cells for Java 8.7.0は、ワークシートがパスワードで保護されているかどうかを検出するための[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)プロパティを公開しました。ブール型の[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)フィールドは、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)がパスワードで保護されている場合は**true**を返し、そうでない場合は**false**を返します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
{{< app/cells/assistant language="java" >}}
