---
title: Excel Dosyalarını Şifreleme
type: docs
weight: 90
url: /tr/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemenizi ve parolayla korumanızı sağlar. Bir şifreleme hizmeti sağlayıcısı tarafından sağlanan algoritmaları veya farklı özelliklere sahip bir dizi şifreleme algoritması olan CSP'yi kullanır. Varsayılan CSP, "Office 97/2000 Uyumlu" veya "Zayıf Şifreleme (XOR)" şeklindedir. Uygun şifreleme anahtarı uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bitten fazlasını desteklemez. Bu, zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bit anahtar uzunluğu gerekir. Microsoft Windows, güçlü şifreleme türleri de sunan CSP'ler içerir, örneğin 'Microsoft Güçlü Şifreleme Sağlayıcı'. Size bir fikir vermesi için, bankaların İnternet Bankacılığı sistemleriyle bağlantıyı şifrelemek için kullandıkları 128 bit şifrelemedir.

Aspose.Cells, Microsoft Excel dosyalarını istediğiniz şifreleme türüyle şifrelemenizi ve parola korumanızı sağlar.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1.  itibaren**Aletler** menü, seç**Seçenekler**Bir iletişim kutusu görünecektir.
1.  seçin**Güvenlik** sekme.
1.  Bir şifre girin ve tıklayın**Gelişmiş**
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells ile şifreleme**

Aşağıdaki örnek, Aspose.Cells API kullanılarak bir excel dosyasının nasıl şifreleneceğini ve parolayla korunacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Seçeneği değiştirmek için Parola Belirtme**

 Aşağıdaki örnek, nasıl ayarlanacağını gösterir.**Değiştirilecek şifre** Microsoft Aspose.Cells API'i kullanan mevcut bir dosya için Excel seçeneği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Şifrelenmiş dosyanın parolasını doğrulayın**

 Aspose.Cells for .NET, şifrelenmiş dosyanın parolasını doğrulamak için şu bilgileri sağlar:[**Parolayı Doğrula**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) yöntem. Bu yöntemler, dosya akışı ve doğrulanması gereken parola olmak üzere iki parametreyi kabul eder.
 Aşağıdaki kod parçacığı,[**Parolayı Doğrula**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) Sağlanan parolanın geçerli olup olmadığını doğrulama yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Aspose.Cells ile ODS dosyasının Şifrelenmesi/Şifresinin Çözülmesi**

Aspose.Cells, ODS dosyasını şifrelemeye ve şifresini çözmeye izin verir. Şifresi çözülmüş ODS dosyası hem Excel'de hem de OpenOffice'te açılabilir, ancak şifreli ODS dosyası yalnızca şifre girildikten sonra OpenOffice tarafından açılabilir. Excel, şifrelenmiş ODS dosyasını açamaz ve uyarı mesajı verebilir. Şifreleme seçenekleri, diğer dosya türlerinden farklı olarak ODS dosyası için geçerli değildir. Bir ODS dosyasını şifrelemek için dosyayı yükleyin ve[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) kaydetmeden önce gerçek parolaya değer. Çıktı şifreli ODS dosyası yalnızca OpenOffice'te açılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 Bir ODS dosyasının şifresini çözmek için, dosyayı bir şifre girerek yükleyin.[**LoadOptions.Şifre**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Dosya yüklendikten sonra,[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) null için dize.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
