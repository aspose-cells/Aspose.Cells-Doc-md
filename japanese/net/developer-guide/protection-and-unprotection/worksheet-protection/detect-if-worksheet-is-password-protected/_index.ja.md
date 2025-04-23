---
title: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 360
url: /ja/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

ワークブックとワークシートを別々に保護することが可能です。たとえば、スプレッドシートにはパスワード保護されたワークシートが1つ以上含まれる場合がありますが、スプレッドシート自体は保護されている場合といない場合があります。Aspose.Cells APIは、指定されたワークシートがパスワードで保護されているかどうかを検出する手段を提供します。この記事では、同じことを達成するためのAspose.Cells for .NET APIの使用方法を示します。

{{% /alert %}}

Aspose.Cells for .NET 8.7.0では、ワークシートがパスワードで保護されているかどうかを検出するための[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)プロパティが公開されています。ブール型の[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)プロパティは、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)がパスワードで保護されている場合は**true**を、そうでない場合は**false**を返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
