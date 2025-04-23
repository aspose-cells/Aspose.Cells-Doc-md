---
title: Excel Çalışma Sayfasının Bölünmüş Ekranı
linktitle: Bölünmüş Ekran
type: docs
weight: 190
url: /tr/python-net/how-to-split-screen-of-excel-worksheet
description: Bu makalede, çalışma sayfasını ikiye veya dörde bölerek farklı bölümlerde belirli satır ve/veya sütunları programlı olarak nasıl göstereceğinizi öğreneceksiniz. Aspose.Cells for Python via .NET API lerini kullanarak.
keywords: Python Excel Kütüphanesi, Python Üst Satırları Dondur, Python Üst Satırları Dondur, Python çalışma sayfasını dikey olarak sütunlar üzerinde böl, Python çalışma sayfasını yatay olarak satırlar üzerinde böl, Python çalışma sayfasını dört parçaya böl, Python bölmeyi kaldırma.
---

## **Giriş**

Bu makalede, Excel çalışma sayfasını iki veya dört parçaya bölererek belirli satırları ve/veya sütunları ayrı bölmelere ayırmayı öğreneceğiz. Büyük veri kümeleriyle çalışırken, farklı veri alt kümelerini karşılaştırmak için aynı çalışma sayfasının birkaç bölümünü aynı anda görmemiz gerekebilir. Bölme ekranı işlevi ihtiyaçlarınızı karşılayabilir.

## **Excel'de ekranı nasıl bölebilirsiniz**
Bir elektronik tabloyu ikiye veya dörde bölmek için aşağıdakileri yapın:

1. Bölme yapmak istediğiniz satır/sütun/hücreyi seçin.
2. Görünüm sekmesinde, Pencereler grubunda, Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş-Ekran.png)**

## **Çalışma Sayfasını Dikey Olarak Bölme**

Elektronik tablonun farklı alanlarını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

Python ile Aspose.Cells kullanarak, sekmeleri programatik olarak dikey bölmek oldukça kolaydır. via .NET, sadece aktif hücre olmaya uygun olan üst satırda bir hücre seçmemiz yeterlidir, sonra
[**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **İşsayfasını Satırlara Göre Yatay Bölme Yöntemi**
Excel'de pencerenizi yatay olarak ayırmak için, bölmeyi istediğiniz satırın altındaki satırı seçin.

Python ile Aspose.Cells kullanarak, işsayfasını yatay olarak satırlara bölmek oldukça kolaydır. via .NET, sadece uygun olan sol sütunda bir hücre seçmemiz yeterlidir, sonra
[**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **İşsayfasını Dört Bölüme Ayırma Yöntemi**
Aynı elektronik tablonun dört farklı bölümünü aynı anda görüntülemek için, Excel'de ekranınızı hem dikey hem yatay olarak bölebilirsiniz.

Python ile Aspose.Cells kullanarak, sekmeleri programatik olarak dikey bölmek oldukça kolaydır. via .NET, ilk satır ve sütunda olmayan bir hücreyi aktif hücre olarak seçmemiz yeterlidir, sonra
[**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) yöntemi ile bölmek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Bölmeyi Kaldırma Yöntemi**
Elektronik tabloyu bölme ayarını kaldırmak için, sadece Böl düğmesini tekrar tıklayın.

Aspose.Cells for Python via .NET, bölmeyi kaldırmak için [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) metodunu sağlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
