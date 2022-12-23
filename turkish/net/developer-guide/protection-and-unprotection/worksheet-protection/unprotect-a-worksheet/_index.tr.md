---
title: Bir Çalışma Sayfasının korumasını kaldırın
type: docs
weight: 20
url: /tr/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

Bir geliştiricinin dosyada bazı değişiklikler yapılabilmesi için çalışma zamanında korumalı bir çalışma sayfasındaki korumayı kaldırması gerekiyorsa? Bu, Aspose.Cells ile kolayca yapılabilir.

{{% /alert %}}

## **Bir Çalışma Sayfasının korumasını kaldırın**

### **Microsoft Excel'i kullanma**

Bir çalışma sayfasından korumayı kaldırmak için:

 itibaren**Araçlar** menü, seç**Koruma** bunu takiben**Sayfanın korumasını kaldır**. Çalışma sayfası parola korumalı olmadığı sürece koruma kaldırılacaktır. Bu durumda, bir iletişim kutusu parola ister. Parolayı girin ve çalışma sayfası korumasız olacaktır.

### **Aspose.Cells Kullanarak Basitçe Korunan Bir Çalışma Sayfasının Korumasını Kaldırma**

 Bir çalışma sayfası, çağrılarak korumasız bırakılabilir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Korumayı kaldır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)yöntem.
 Basitçe korunan bir çalışma sayfası, parola ile korunmayan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, çağrılarak korumasız bırakılabilir.[**Korumayı kaldır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)bir parametre geçirmeden yöntem.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Aspose.Cells Kullanarak Parola Korumalı Çalışma Sayfasının Korumasını Kaldırma**

Parola korumalı bir çalışma sayfası, parolayla korunan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, programın aşırı yüklenmiş bir sürümü çağrılarak korumasız bırakılabilir.[**Korumayı kaldır**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)şifreyi parametre olarak alan metod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
