---
title: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 280
url: /ja/java/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

ワークブックとワークシートを別々に保護することができます。たとえば、スプレッドシートには、パスワードで保護された 1 つ以上のワークシートが含まれている場合がありますが、スプレッドシート自体は保護されている場合とされていない場合があります。 Aspose.Cells API は、特定のワークシートがパスワードで保護されているかどうかを検出する手段を提供します。この記事では、Aspose.Cells for Java API を使用して同じことを行う方法を示します。

{{% /alert %}}

## **ワークシートがパスワードで保護されているかどうかを検出する**

Aspose.Cells for Java 8.7.0 で[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)ワークシートがパスワードで保護されているかどうかを検出するプロパティ。ブール型[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)フィールドリターン**真実**もしも[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)パスワードで保護されており、**間違い**そうでない場合。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
