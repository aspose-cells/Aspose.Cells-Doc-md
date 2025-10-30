---
title: Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulayın
type: docs
weight: 370
url: /tr/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET API'leri, kullanışlı özellikler ve yöntemler ekleyerek [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) sınıfını geliştirmiştir. Bu yöntemlerden biri, bir şifreyi *string* örneği olarak belirlemeye ve bunun, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)'yi korumak için kullanılan şifre olup olmadığını doğrulamaya olanak tanıyan [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) yöntemidir.

{{% /alert %}}

[**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) yöntemi, belirtilen şifrenin belirtilen çalışma sayfasını korumak için kullanılan şifre ile eşleşiyorsa **true** döndürür ve eşleşmiyorsa **false** döndürür. Aşağıdaki kod parçası, şifre korumasını tespit etmek ve şifreyi doğrulamak için [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) yöntemini [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) özelliği ile birlikte kullanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

{{< app/cells/assistant language="python-net" >}}
