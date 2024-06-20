---
title: ODS Dosyalarını Şifreleme ve Şifre Çözme
type: docs
weight: 10
url: /tr/java/encrypt-and-decrypt-ods-files/
description: Aspose.Cells, bir Java kütüphanesi olan Aspose.Cells for Java kullanarak ODS dosyalarını korumalı parolalı ve şifreli hale getirebilir.
---

{{% alert color="primary" %}}
OpenOffice.org şifre korumayı ve dosyaları şifrelemeyi destekleyen tam özellikli bir ofis paketidir. Ancak şifreli ODS dosyası yalnızca parolayı sağladıktan sonra OpenOffice tarafından açılabilir. Excel şifreli ODS dosyasını açamaz ve uyarı mesajı verebilir. Şifreleme seçenekleri diğer dosya türleri gibi ODS dosyası için uygulanamaz. 
Aspose.Cells, ODS dosyasını şifrelemeye ve şifresini çözmeye olanak tanır. Şifresi çözülmüş ODS dosyası hem Excel hem de OpenOffice'de açılabilir. 
{{% /alert %}}

## **OpenOffice Calc ile Şifrele**
1. **Farklı Kaydet**'i seçin ve **Parola ile Kaydet** kutusunu tıklayın.
1. **Kaydet** düğmesini tıklayın.
1. Açılan Set Parola penceresinde, hem **Açmak için Parolayı Girin** hem de **Parolayı Onaylayın** alanlarına istediğiniz parolayı yazın. 
1. Dosyayı kaydetmek için **Tamam** düğmesini tıklayın.

## **ODS Dosyasını Şifrelemek/Şifresini Çözmek:**

Bir ODS dosyasını şifrelemek için, dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) geçerli parolayı iletebilirsiniz. Çıkış şifrelenmiş ODS dosyası yalnızca OpenOffice'de açılabilir. Bir ODS dosyasını şifresini çözmek için, [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) ile parolayı sağlayarak dosyayı yükleyin. Dosya yüklendikten sonra, gerçek parolayla [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)) işlevini çağırın ve son olarak [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) null geçin.

### **Örnek Kod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
