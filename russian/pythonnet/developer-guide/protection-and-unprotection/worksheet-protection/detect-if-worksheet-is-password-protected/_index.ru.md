---
title: Определить, защищен ли рабочий лист паролем
type: docs
weight: 360
url: /ru/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Возможно защитить рабочие книги и листы отдельно. Например, лист с данными может содержать один или несколько листов, защищенных паролем, однако сама книга может быть защищена или нет. API Aspose.Cells для Python via .NET предоставляют возможность определить, защищен ли лист паролем. В этой статье показано использование API Aspose.Cells для Python via .NET для достижения этого.

{{% /alert %}}

Aspose.Cells для Python via .NET exposes свойство [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) для обнаружения, защищен ли лист паролем. Булевое свойство [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) возвращает **true**, если [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) защищен паролем, и **false**, если нет.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

{{< app/cells/assistant language="python-net" >}}
