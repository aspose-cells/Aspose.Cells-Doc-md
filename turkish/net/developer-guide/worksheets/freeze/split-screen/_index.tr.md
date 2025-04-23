---
title: Excel Çalışma Sayfasının Bölünmüş Ekranı
linktitle: Bölünmüş Ekran
type: docs
weight: 190
url: /tr/net/how-to-split-screen-of-excel-worksheet
description: Bu makalede, belirli satırları ve/veya sütunları ayrı panolarda görüntülemeyi öğreneceksiniz, C# Kütüphanesi ve .NET API ile çalışarak elektronik tabloyu programlı olarak ikiye veya dörde bölmeyi öğreneceksiniz.
keywords: Üst satırları dondur, Üst satırı dondur.
---

## **Giriş**

Bu makalede, Excel çalışma sayfasını iki veya dört parçaya bölererek belirli satırları ve/veya sütunları ayrı bölmelere ayırmayı öğreneceğiz. Büyük veri kümeleriyle çalışırken, farklı veri alt kümelerini karşılaştırmak için aynı çalışma sayfasının birkaç bölümünü aynı anda görmemiz gerekebilir. Bölme ekranı işlevi ihtiyaçlarınızı karşılayabilir.

## **Excel'de ekranı nasıl bölebilirsiniz**
Bir elektronik tabloyu ikiye veya dörde bölmek için aşağıdakileri yapın:

1. Bölme yapmak istediğiniz satır/sütun/hücreyi seçin.
2. Görünüm sekmesinde, Pencereler grubunda, Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş-Ekran.png)**

## **Excel'de sütunlara dik olarak elektronik tabloyu bölmek**

Elektronik tablonun farklı alanlarını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

Aspose.Cells for .Net ile sütunlara dik şekilde elektronik tabloyu programlı olarak bölmek Aspose.Cells for .Net ile kolaydır, yalnızca en üst satırda bir hücre seçmemiz gerekiyor, sonra
[**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **Satırlara yatay olarak elektronik tabloyu bölmek**
Excel'de pencerenizi yatay olarak ayırmak için, bölmeyi istediğiniz satırın altındaki satırı seçin.

Aspose.Cells for .Net ile satırlara yatay olarak elektronik tabloyu programlı olarak bölmek Aspose.Cells for .Net ile kolaydır, yalnızca soldaki sütunda bir hücre seçmemiz gerekiyor, sonra
[**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **Elektronik tabloyu dört bölüme ayırmak**
Aynı elektronik tablonun dört farklı bölümünü aynı anda görüntülemek için, Excel'de ekranınızı hem dikey hem yatay olarak bölebilirsiniz.

Aspose.Cells for .Net ile sütunlara dik olarak elektronik tabloyu programlı olarak bölmek Aspose.Cells for .Net ile kolaydır, yalnızca en üst satır veya sütunda olmayan bir hücre seçmemiz gerekiyor, sonra
[**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **Bölünmüş bölgeyi kaldırmak için**
Elektronik tabloyu bölme ayarını kaldırmak için, sadece Böl düğmesini tekrar tıklayın.

Aspose.Cells for .Net, bölme ayarını kaldırmak için bir [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) yöntemi sağlar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
{{< app/cells/assistant language="csharp" >}}
