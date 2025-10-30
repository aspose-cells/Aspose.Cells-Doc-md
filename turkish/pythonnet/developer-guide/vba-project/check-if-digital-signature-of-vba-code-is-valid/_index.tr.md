---
title: VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et
type: docs
weight: 120
url: /tr/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, VBA kodunun dijital imzanın geçerli olup olmadığını [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed) özelliğiyle kontrol etmenize olanak tanır. İmza geçerliyse **true** döner, aksi takdirde **false** döner. VBA kodunu değiştirdiğinizde dijital imza geçersiz hale gelir.

{{% /alert %}}

## **Python'da VBA Kodunun Dijital İmzasının Geçerli olup olmadığını Kontrol Etme**

Aşağıdaki kod, sağlanan bağlantıdan indirebileceğiniz [örnek excel dosyası](5115030.xlsm) kullanarak bu özelliğin kullanımını göstermektedir. Aynı excel dosyasının geçerli bir imzası vardır ancak VBA kodunu değiştirip çalıştırdıktan sonra imzanın geçersiz olduğunu buluruz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
