---
title: ODS Dosyalarını Şifreleme ve Şifre Çözme
type: docs
weight: 10
url: /tr/python-net/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for Python via .NET kullanarak ODS dosyalarını parola korumalı ve şifreli hale getirin, bu saf. net kütüphanesidir.
---

{{% alert color="primary" %}}
OpenOffice.org şifre korumayı ve dosyaları şifrelemeyi destekleyen tam özellikli bir ofis paketidir. Ancak şifreli ODS dosyası yalnızca parolayı sağladıktan sonra OpenOffice tarafından açılabilir. Excel şifreli ODS dosyasını açamaz ve uyarı mesajı verebilir. Şifreleme seçenekleri diğer dosya türleri gibi ODS dosyası için uygulanamaz. 
Aspose.Cells for Python via .NET, ODS dosyasını şifreleyip şifresini çözmenize olanak tanır. Şifre çözülmüş ODS dosyası hem Excel hem de OpenOffice’de açılabilir. 
{{% /alert %}}

## **OpenOffice Calc ile Şifrele**
1. **Farklı Kaydet**'i seçin ve **Parola ile Kaydet** kutusunu tıklayın.
1. **Kaydet** düğmesini tıklayın.
1. Açılan Set Parola penceresinde, hem **Açmak için Parolayı Girin** hem de **Parolayı Onaylayın** alanlarına istediğiniz parolayı yazın. 
1. Dosyayı kaydetmek için **Tamam** düğmesini tıklayın.

## **Aspose.Cells for Python via .NET ile ODS dosyasını şifreleyin.**
Bir ODS dosyasını şifrelemek için dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) değerini gerçek parolaya ayarlayın. Oluşturulan şifrelenmiş ODS dosyası yalnızca OpenOffice'de açılabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Aspose.Cells for Python via .NET ile ODS dosyasını şifre çözün.**

ODS dosyasını çözmek için, dosyayı yüklemek için [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password) ile bir parola sağlayın. Dosya yüklendikten sonra, [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) dizesini null olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

