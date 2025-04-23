---
title: Çalışma sayfasının Parola Korumalı Olup Olmadığını Algılama
type: docs
weight: 360
url: /tr/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Çalışma kitaplarını ve çalışma sayfalarını ayrı ayrı korumak mümkündür. Örneğin, bir çalışma sayfası şifreyle korunan bir veya daha fazla çalışma sayfası içerebilir, ancak, çalışma kitabı kendisi korumalı veya değil olabilir. Aspose.Cells for Python via .NET API'leri, belirli bir çalışma sayfasının şifre korumalı olup olmadığını tespit etme imkanı sağlar. Bu makale, Aspose.Cells for Python via .NET API'sinin kullanımıyla aynı işlemi gerçekleştirmeyi göstermektedir.

{{% /alert %}}

Aspose.Cells for Python via .NET, bir çalışma sayfasının şifre korumalı olup olmadığını tespit etmek için [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) özelliğini ortaya çıkardı. Boolean türündeki [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) özelliği, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) şifreyle korunduysa **doğru**, değilse **yanlış** döner.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

