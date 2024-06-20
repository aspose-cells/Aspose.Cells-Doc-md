---
title: ODS Dosyalarını Şifreleme ve Şifre Çözme
type: docs
weight: 10
url: /tr/net/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for .Net i kullanarak ODS dosyalarını şifre koruma altına alabilir ve şifreleyebilirsiniz, bu saf Net kütüphanesidir.
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

## **Aspose.Cells for .Net ile ODS dosyası şifreleme**
Bir ODS dosyasını şifrelemek için dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) değerini gerçek parolaya ayarlayın. Oluşturulan şifrelenmiş ODS dosyası yalnızca OpenOffice'de açılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Aspose.Cells for .Net ile ODS dosyası şifresini çözme**

ODS dosyasını çözmek için, dosyayı yüklemek için [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) ile bir parola sağlayın. Dosya yüklendikten sonra, [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) dizesini null olarak ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
