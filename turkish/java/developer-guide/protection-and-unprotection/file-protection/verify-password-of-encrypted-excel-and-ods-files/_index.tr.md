---
title: Şifrelenmiş Dosyaların Şifresini Doğrulama
type: docs
weight: 10
url: /tr/java/verify-password-of-encrypted-excel-and-ods-files/
description: Şifreli Excel (xlsx, xlsb, xls, xlsm) ve OpenOffice (ODS) dosyalarının şifresini Java kodları kullanarak doğrulayın.
---

{{% alert color="primary" %}}
Excel (xlsx, xlsb, xls, xlsm) ve OpenOffice (ODS) dosyaları şifrelenmişse, Aspose.Cells for Java belirli dosyanın verilerini ayrıştırmadan basit parola doğrulamasını destekler.
{{% /alert %}}

## **Şifrelenmiş dosyanın parolasını doğrulama**

Şifreli dosyanın parolasını doğrulamak için, Aspose.Cells for Java [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) yöntemini sağlar. Yöntem iki parametre kabul eder, dosya akışı ve doğrulanması gereken parola.
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) yönteminin nasıl kullanıldığını göstermektedir.

### **Örnek Kod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}
