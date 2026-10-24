---
title: Paylaşılan Çalışma Kitabını Koruma Altına Alma veya Korumasız Yapma
linktitle: Paylaşılan Çalışma Kitabını Koruma veya Korumasız Hale Getirme
type: docs
weight: 70
url: /tr/java/password-protect-or-unprotect-the-shared-workbook/
---

## **Olası Kullanım Senaryoları**

Aşağıdaki ekran görüntüsünde gösterildiği gibi, Microsoft Excel ile paylaşılan çalışma kitabını koruyabilir veya korumasız hale getirebilirsiniz. Aspose.Cells, bu özelliği [**Workbook.protectSharedWorkbook()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#protectSharedWorkbook-java.lang.String-) ve [**Workbook.unprotectSharedWorkbook()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotectSharedWorkbook-java.lang.String-) yöntemleriyle destekler.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Paylaşılan çalışma kitabını koruma altına alan ve paylaşımı etkinleştiren bir çalışma kitabı oluşturan aşağıdaki örnek kod ve bunu [çıktı Excel dosyası](55541777.xlsx) olarak kaydeden bir çalışma sayfasına şifre eklemesini göstermektedir. Ekran görüntüsü, korumasız yapmaya çalıştığınızda Microsoft Excel'in şifreyi girmenizi istediğini göstermektedir.**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve paylaşımı etkinleştirerek korur ve [çıktı Excel dosyası](55541800.xlsx) olarak kaydeder. Ekran görüntüsü, korumasını kaldırmayı denediğinizde, Microsoft Excel'in onu korumayı kaldırmak için şifreyi girmeniz gerektiği konusunda size bir ileti gösterir.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PasswordProtectOrUnprotectSharedWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
