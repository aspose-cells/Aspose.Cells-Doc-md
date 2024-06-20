---
title: Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulayın
type: docs
weight: 290
url: /tr/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells API'ları, [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) sınıfını bazı kullanışlı özellikler ve metotlar ekleyerek geliştirdi. Bu metotlardan biri, bir String örneği olarak parola belirlemeye ve Çalışsayıyı korumak için kullanılan parolanın doğruluğunu denetlemeye izin veren [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) metodu.

{{% /alert %}}

## **Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulama**

Belirtilen parola, verilen çalışsayısını korumak için kullanılan parola ile eşleşiyorsa **true** değerini, eşleşmiyorsa **false** değerini döndürür. Aşağıdaki kod örneği, Parola korumasını algılamak ve parolayı doğrulamak için [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) metodu ve [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) özelliği ile bir arada kullanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
