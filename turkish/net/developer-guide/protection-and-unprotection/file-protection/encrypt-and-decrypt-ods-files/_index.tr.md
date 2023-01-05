---
title: ODS dosyalarını şifrele ve şifresini çöz
type: docs
weight: 10
url: /tr/net/encrypt-and-decrypt-ods-files/
description: saf bir net kitaplığı olan .Net için Aspose.Cells'i kullanarak ODS dosyalarını parolayla koruyun ve şifreleyin.
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

## **.Net için ODS dosyasını Aspose.Cells ile şifreleyin**
 ODS dosyasını şifrelemek için dosyayı yükleyin ve[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) kaydetmeden önce gerçek parolaya değer. Çıkış şifreli ODS dosyası yalnızca OpenOffice'te açılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **.Net için ODS dosyasının şifresini Aspose.Cells ile çözün**

 ODS dosyasının şifresini çözmek için, dosyayı bir parola girerek yükleyin.[**LoadOptions.Şifre**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Dosya yüklendikten sonra,[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) null için dize.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
