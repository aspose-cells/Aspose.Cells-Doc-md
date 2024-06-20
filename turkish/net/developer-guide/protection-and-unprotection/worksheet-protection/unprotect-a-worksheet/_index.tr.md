---
title: Bir Çalışma Sayfasının Korumasını Kaldır
type: docs
weight: 20
url: /tr/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Bir geliştirici, çalışma sayfasındaki korumayı çalışma zamanında kaldırarak dosyaya bazı değişiklikler yapabilir mi? Bu, Aspose.Cells ile kolayca yapılabilir.

{{% /alert %}}

## **Bir Çalışma Sayfasını Korumayı Kaldırma**

### **Microsoft Excel Kullanımı**

Çalışma sayfasından korumayı kaldırmak için:

**Araçlar** menüsünden, **Koruma**'yı seçin ve ardından **Sayfayı Korumasız Bırak**'ı seçin. Sayfa şifre korumalı değilse koruma kaldırılacaktır. Bu durumda, bir iletişim kutusu şifreyi isteyecektir. Şifreyi girin ve çalışma sayfası o zaman korumasız olacaktır.

### **Aspose.Cells Kullanarak Basit Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) yöntemi çağrılarak korumasız bırakılabilir.
Basit bir korumalı çalışma sayfası, bir şifre ile korunmayan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, bir parametre ile [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) yöntemi çağrılarak koruyarak korumadan kaldırılabilir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Aspose.Cells Kullanarak Şifre Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Şifre korumalı bir çalışma sayfası, bir şifre ile korunan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, şifreyi parametre olarak alan [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) yönteminin aşırı yüklenmiş bir sürümünü çağırarak koruyarak korumadan kaldırılabilir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
