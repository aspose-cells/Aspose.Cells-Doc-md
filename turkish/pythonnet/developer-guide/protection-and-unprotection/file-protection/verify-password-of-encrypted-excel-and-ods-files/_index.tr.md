---
title: Şifrelenmiş Dosyaların Şifresini Doğrulama
type: docs
weight: 10
url: /tr/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Şifrelenmiş Excel (xlsx, xlsb, xls, xlsm) ve Open office (ODS) dosyalarının şifresini CShape kodları kullanarak doğrulayın.
---

{{% alert color="primary" %}}
Eğer Excel (xlsx, xlsb, xls, xlsm) ve Open office (ODS) dosyaları şifrelenmişse, Aspose belirli dosya verilerini ayrıştırmadan basit bir şifre doğrulamasını destekler.
{{% /alert %}}

## **Şifrelenmiş dosyanın parolasını doğrulama**

Şifreli dosyanın parolasını doğrulamak için, Aspose.Cells for Python via .NET, [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) yöntemini sağlar. Bu yöntemler, iki parametre alır, dosya akışı ve doğrulanması gereken parola.
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) yönteminin nasıl kullanıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


