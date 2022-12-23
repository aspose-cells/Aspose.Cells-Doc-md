---
title: ODS dosyalarını şifrele ve şifresini çöz
type: docs
weight: 10
url: /tr/java/encrypt-and-decrypt-ods-files/
description: saf bir Java kitaplığı olan Aspose.Cells for Java'i kullanarak ODS dosyalarını parolayla koruyun ve şifreleyin.
---
{{% alert color="primary" %}}
OpenOffice.org, parola korumayı ve dosyaları şifrelemeyi destekleyen tam özellikli bir ofis paketidir. Ancak şifreli ODS dosyası, şifre girildikten sonra yalnızca OpenOffice tarafından açılabilir. Excel, şifrelenmiş ODS dosyasını açamaz ve uyarı mesajı verebilir. Şifreleme seçenekleri, diğer dosya türlerinden farklı olarak ODS dosyası için geçerli değildir.
 Aspose.Cells, ODS dosyasını şifrelemeye ve şifresini çözmeye izin verir. Şifresi çözülmüş ODS dosyası hem Excel'de hem de OpenOffice'te açılabilir,
{{% /alert %}}

## **OpenOffice Calc ile şifreleyin**
1.  Seçme**Farklı kaydet** ve tıklayın**Şifre ile Kaydet** Kutu.
1.  Tıkla**Kayıt etmek** buton.
1.  İstediğiniz şifreyi her ikisine de yazın.**Açmak için Parolayı Girin** ve**Şifreyi Onayla** açılan Parola Belirle penceresindeki alanlar.
1.  Tıkla**Tamam** dosyayı kaydetmek için düğmesine basın.

## **Şifreleme/Şifre çözme ODS Dosya:**

 ODS dosyasını şifrelemek için dosyayı yükleyin ve gerçek parolayı[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)kaydetmeden önce. Çıkış şifreli ODS dosyası yalnızca OpenOffice'te açılabilir. ODS dosyasının şifresini çözmek için, parolayı girerek dosyayı yükleyin.[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . Dosya yüklendikten sonra, çağrı fonksiyonu[**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) argüman olarak gerçek şifre ile ve son olarak null değerini iletin[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Basit kod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
