---
title: Определить, защищен ли рабочий лист паролем
type: docs
weight: 360
url: /ru/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Можно защитить рабочие книги и рабочие листы отдельно. Например, электронная таблица может содержать один или несколько рабочих листов, защищенных паролем, однако сама электронная таблица может быть защищена или не защищена. Aspose.Cells API-интерфейсы предоставляют средства для определения того, защищен ли данный лист паролем или нет. В этой статье показано использование Aspose.Cells for .NET API для достижения того же.

{{% /alert %}}

 Aspose.Cells for .NET 8.7.0 выставил[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) свойство, чтобы определить, защищен ли лист паролем или нет. Логический тип[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) недвижимость возвращается**истинный** если[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) защищен паролем и**ЛОЖЬ** если не.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
