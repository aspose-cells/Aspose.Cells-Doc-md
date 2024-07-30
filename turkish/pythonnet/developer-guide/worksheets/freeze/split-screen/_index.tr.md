---
title: Excel Çalışma Sayfasının Bölünmüş Ekranı
linktitle: Bölünmüş Ekran
type: docs
weight: 190
url: /tr/python-net/how-to-split-screen-of-excel-worksheet
description: Bu makalede, Aspose.Cells için Python via .NET API lerini kullanarak çalışma sayfasını programlı olarak ikiye veya dörde bölerek belirli satırları ve/veya sütunları ayrı panellere nasıl göstereceğinizi öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python Üst Satırları Dondur, Python Üst Satırı Dondur, Python Sutunlara Göre Dikey Olarak Çalışma Sayfasını Bölmek, Python Satırlara Göre Yatay Olarak Çalışma Sayfasını Bölmek, Python Çalışma Sayfasını Dört Bölüme Bölmek Python Bölme.
---

## **Giriş**

Bu makalede, Excel çalışma sayfasını iki veya dört parçaya bölererek belirli satırları ve/veya sütunları ayrı bölmelere ayırmayı öğreneceğiz. Büyük veri kümeleriyle çalışırken, farklı veri alt kümelerini karşılaştırmak için aynı çalışma sayfasının birkaç bölümünü aynı anda görmemiz gerekebilir. Bölme ekranı işlevi ihtiyaçlarınızı karşılayabilir.

## **Excel'de ekranı nasıl bölebilirsiniz**
Bir elektronik tabloyu ikiye veya dörde bölmek için aşağıdakileri yapın:

1. Bölme yapmak istediğiniz satır/sütun/hücreyi seçin.
2. Görünüm sekmesinde, Pencereler grubunda, Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş-Ekran.png)**

## **Sutunlara Göre Çalışma Sayfasını Bölmek Nasıl Yapılır**

Elektronik tablonun farklı alanlarını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

Aspose.Cells için Python via .NET ile programlı olarak sutunlara göre çalışma sayfasını bölmek oldukça kolay, yalnızca üst satırdaki bir hücreyi etkin hücre olarak seçmemiz yeterli.
[**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Satırlara Göre Çalışma Sayfasını Bölmek Nasıl Yapılır**
Excel'de pencerenizi yatay olarak ayırmak için, bölmeyi istediğiniz satırın altındaki satırı seçin.

Aspose.Cells için Python via .NET ile programlı olarak satırlara göre çalışma sayfasını bölmek oldukça kolay, yalnızca sol sütundaki bir hücreyi etkin hücre olarak seçmemiz yeterli.
[**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Çalışma Sayfasını Dört Bölüme Ayırmak Nasıl Yapılır**
Aynı elektronik tablonun dört farklı bölümünü aynı anda görüntülemek için, Excel'de ekranınızı hem dikey hem yatay olarak bölebilirsiniz.

Aspose.Cells için Python via .NET ile programlı olarak sutunlara göre çalışma sayfasını bölmek oldukça kolay, yalnızca ilk sıra ve sütunda olmayan bir hücreyi etkin hücre olarak seçmemiz yeterli.
[**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Bölünmüş Üzerindeki Ayırmak Nasıl Yapılır**
Elektronik tabloyu bölme ayarını kaldırmak için, sadece Böl düğmesini tekrar tıklayın.

Aspose.Cells için Python via .NET bir bölme ayarı kaldırmak için [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) yöntemini sağlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
