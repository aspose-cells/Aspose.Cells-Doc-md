---
title: Excel Çalışma Sayfasının Bölünmüş Ekranı
linktitle: Bölünmüş ekran
type: docs
weight: 190
url: /tr/net/how-to-split-screen-of-excel-worksheet
description: Bu makalede, C# Kitaplığı ile .NET API'i kullanarak çalışma sayfasını programlı olarak iki veya dört parçaya bölerek belirli satırları ve/veya sütunları ayrı bölmelerde nasıl görüntüleyeceğinizi öğreneceksiniz.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

Bu makalede, çalışma sayfasını iki veya dört parçaya bölerek belirli satır ve/veya sütunların ayrı bölmelerde nasıl görüntüleneceğini öğreneceğiz.
Büyük veri kümeleriyle çalışırken, farklı veri alt kümelerini karşılaştırmak için aynı çalışma sayfasının birkaç alanını aynı anda görmemiz gerekir.
Bölünmüş ekran işlevi ihtiyaçlarınızı karşılayabilir.

{{% /alert %}}

##  **Excel'de ekran nasıl bölünür**
Bir çalışma sayfasını iki veya dört parçaya bölmek için aşağıdakileri yapın:

1. Bölmeyi önüne yerleştirmek istediğiniz satırı/sütun/hücreyi seçin.
2. Görünüm sekmesinin Windows grubunda Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş Ekran.png)**

##  **Çalışma sayfasını sütunlara dikey olarak bölme**

Elektronik tablonun iki alanını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

.Net için Aspose.Cells ile çalışma sayfasını programlı olarak sütunlara dikey olarak bölmek kolaydır, yalnızca üst satırdaki bir hücreyi aktif hücre olarak seçmemiz gerekir, ardından
ile ayrılmak[**Çalışma Sayfası.Bölünmüş**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) yöntem.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **Çalışma sayfasını yatay olarak satırlara bölme**
Excel pencerenizi yatay olarak ayırmak için bölmenin Excel'de gerçekleşmesini istediğiniz satırın altındaki satırı seçin.

.Net için Aspose.Cells ile çalışma sayfasını programlı olarak satırlara yatay olarak bölmek kolaydır, sol sütundaki yalnızca bir hücreyi aktif hücre olarak seçmemiz gerekir, ardından
ile ayrılmak[**Çalışma Sayfası.Bölünmüş**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) yöntem.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **Çalışma sayfasını dört parçaya bölün**
Aynı çalışma sayfasının dört farklı bölümünü aynı anda görüntülemek için Excel'de ekranınızı hem dikey hem de yatay olarak bölün.

.Net için Aspose.Cells ile çalışma sayfasını programlı olarak sütunlara dikey olarak bölmek kolaydır, yalnızca ilk satırda ve sütunda olmayan bir hücreyi aktif hücre olarak seçmemiz gerekir, ardından
ile ayrılmak[**Çalışma Sayfası.Bölünmüş**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) yöntem.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **Bölünme nasıl kaldırılır**
Çalışma sayfasının bölünmesini kaldırmak için Böl düğmesini tekrar tıklamanız yeterlidir.

 .Net için Aspose.Cells şunları sağlar:[**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) Bölünmüş ayarı kaldırma yöntemi.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}