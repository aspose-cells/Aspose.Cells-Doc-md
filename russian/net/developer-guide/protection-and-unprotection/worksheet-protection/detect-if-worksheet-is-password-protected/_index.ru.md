---
title: Определить, защищен ли рабочий лист паролем
type: docs
weight: 360
url: /ru/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Защиту рабочих книг и листов можно применять отдельно. Например, электронная таблица может содержать один или несколько листов, защищенных паролем, однако сама таблица может быть защищена или нет. API Aspose.Cells предоставляет средства для определения, защищен ли данный лист паролем. В данной статье демонстрируется использование API Aspose.Cells for .NET для достижения этой цели.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 предоставил свойство [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) для определения защищен ли лист паролем или нет. Логическое свойство типа [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) возвращает **true**, если [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) защищен паролем, и **false**, если нет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
