---
title: Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulayın
type: docs
weight: 370
url: /tr/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) sınıfını geliştirerek bazı kullanışlı özellikler ve yöntemler eklemiştir. Bu tür bir yöntem, bir *string* örneği olarak bir şifreyi belirtmeyi ve aynı şifrenin [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) korumak için kullanılıp kullanılmadığını doğrulamayı mümkün kılar. 

{{% /alert %}}

[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) yöntemi, belirtilen şifrenin belirtilen çalışma sayfasını korumak için kullanılan şifre ile eşleşiyorsa **true** döndürür ve eşleşmiyorsa **false** döndürür. Aşağıdaki kod parçası, şifre korumasını tespit etmek ve şifreyi doğrulamak için [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) yöntemini [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) özelliği ile birlikte kullanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
