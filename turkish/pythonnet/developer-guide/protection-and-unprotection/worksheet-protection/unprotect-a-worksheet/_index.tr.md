---
title: Bir Çalışma Sayfasının Korumasını Kaldır
type: docs
weight: 20
url: /tr/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Bir geliştirici, dosyada değişiklikler yapabilmek için çalışma sayfasındaki koruma kaldırmak istediğinde? Bu, Aspose.Cells for Python via .NET ile kolayca yapılabilir.

{{% /alert %}}

## **Bir Çalışma Sayfasını Korumayı Kaldırma**

### **Microsoft Excel Kullanımı**

Çalışma sayfasından korumayı kaldırmak için:

**Araçlar** menüsünden, **Koruma**'yı seçin ve ardından **Sayfayı Korumasız Bırak**'ı seçin. Sayfa şifre korumalı değilse koruma kaldırılacaktır. Bu durumda, bir iletişim kutusu şifreyi isteyecektir. Şifreyi girin ve çalışma sayfası o zaman korumasız olacaktır.

### **Aspose.Cells for Python via .NET kullanılarak Basit Koruma ile korunan çalışma sayfasını kaldırma**

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) yöntemi çağrılarak korumasız bırakılabilir.
Basit bir korumalı çalışma sayfası, bir şifre ile korunmayan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, bir parametre ile [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) yöntemi çağrılarak koruyarak korumadan kaldırılabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Aspose.Cells for Python via .NET kullanılarak Şifreyle korunan çalışma sayfasını kaldırma**

Şifre korumalı bir çalışma sayfası, bir şifre ile korunan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, şifreyi parametre olarak alan [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) yönteminin aşırı yüklenmiş bir sürümünü çağırarak koruyarak korumadan kaldırılabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

