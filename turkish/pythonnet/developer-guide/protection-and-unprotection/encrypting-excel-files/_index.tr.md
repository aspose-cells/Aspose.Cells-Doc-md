---
title: Excel Dosyalarını Şifreleme
type: docs
weight: 90
url: /tr/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemeye ve parola koruması yapmaya olanak tanır. Bir şifreleme hizmet sağlayıcısı tarafından sağlanan algoritmalar, yani bir dizi farklı özelliklere sahip şifreleme algoritmaları kullanır. Varsayılan CSP 'Ofis 97/2000 Uyumlu' veya 'Zayıf Şifreleme (XOR)' dur. Doğru şifreleme anahtar uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bit'ten fazlasını desteklemez. Bu zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir. Microsoft Windows, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcısı' gibi güçlü şifreleme türleri sunan CSP'ler içerir. Size bir fikir vermek gerekirse, 128 bitlik şifreleme, bankaların İnternet Bankacılığı sistemleriyle olan bağlantıyı şifrelemek için kullandığı şeydir.

Aspose.Cells for Python via .NET, Microsoft Excel dosyalarını istediğiniz şifreleme türüyle şifreleyip parola koruma özelliği eklemenize izin verir.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin. Bir iletişim kutusu görünecektir.
1. **Güvenlik** sekmesini seçin.
1. Bir parola girin ve **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells ile Şifreleme**

Aşağıdaki örnek, Aspose.Cells for Python via .NET API kullanarak bir Excel dosyasını nasıl şifreleyip parola koruma altına alacağınızı gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Değiştirilecek Parolayı Belirtme Seçeneği**

Aşağıdaki örnek, mevcut bir dosya için Aspose.Cells for Python via .NET API kullanarak **Değiştirmek için Parola** Microsoft Excel seçeneğinin nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Şifrelenmiş dosyanın parolasını doğrulama**

Şifreli dosyanın parolasını doğrulamak için, Aspose.Cells for Python via .NET, [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) yöntemini sağlar. Bu yöntemler, iki parametre alır, dosya akışı ve doğrulanması gereken parola.
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) yönteminin nasıl kullanıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **ODS dosyasının Şifrelenmesi / Şifresinin Çözülmesi**

Aspose.Cells for Python via .NET, ODS dosyasını şifreleyip şifresini çözmenize imkan tanır. Çözülen ODS dosyası hem Excel hem de OpenOffice'de açılabilir, ancak şifreli ODS dosyası yalnızca şifre girilerek OpenOffice tarafından açılabilir. Excel, şifreli ODS dosyasını açamaz ve uyarı mesajı gösterebilir. Şifreleme seçenekleri, diğer dosya türlerinin aksine, ODS dosyası için uygulanmaz. Bir ODS dosyasını şifrelemek için, dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) değerini gerçek şifre ile ayarlayın. Çıktı şifreli ODS dosyası yalnızca OpenOffice'te açılabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

ODS dosyasını çözmek için, dosyayı yüklemek için [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password) ile bir parola sağlayın. Dosya yüklendikten sonra, [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) dizesini null olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
