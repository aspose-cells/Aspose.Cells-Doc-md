---
title: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 360
url: /ja/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

ワークブックとワークシートを別々に保護することができます。たとえば、スプレッドシートには、パスワードで保護された 1 つ以上のワークシートが含まれている場合がありますが、スプレッドシート自体は保護されている場合とされていない場合があります。 Aspose.Cells API は、特定のワークシートがパスワードで保護されているかどうかを検出する手段を提供します。この記事では、Aspose.Cells for .NET API を使用して同じことを行う方法を示します。

{{% /alert %}}

 Aspose.Cells for .NET 8.7.0 で[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)ワークシートがパスワードで保護されているかどうかを検出するプロパティ。ブール型[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)プロパティリターン**真実**もしも[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)パスワードで保護されており、**間違い**そうでない場合。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
