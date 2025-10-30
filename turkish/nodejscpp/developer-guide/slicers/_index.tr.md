---
title: Dilimleyici Ekle
linktitle: Dilimleyiciler
type: docs
weight: 170
url: /tr/nodejs-cpp/create-slicer/
description: Aspose.Cells for Node.js via C++ ile Excel dosyalarının dilimleyicilerini yönetin.
---

## **Olası Kullanım Senaryoları**

Bir dilimleyici, verileri hızlıca filtrelemek için kullanılır. Bu, hem tablo hem de pivot tabloyu filtrelemek için kullanılabilir. Microsoft Excel, bir tablo veya pivot tablo seçip sonra *Ekle > Dilimleyici* tıklayarak dilimleyici oluşturmanıza olanak tanır. Aspose.Cells for Node.js via C++ ayrıca [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-) yöntemi kullanarak dilimleyici oluşturmanıza da olanak tanır.

## **Pivot Tablosuna Dilimleyici Oluştur**

Lütfen aşağıdaki örnek kodu inceleyin. Bu, pivot tabloyu içeren [örnek Excel dosyasını](67338470.xlsx) yükler. Ardından ilk temel pivot alanına dayanarak dilimleyici oluşturur. Son olarak, çalışma kitabını [dışa aktarma XLSX](67338471.xlsx) ve [dışa aktarma XLSB](67338472.xlsb) formatlarında kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells for Node.js via C++ tarafından oluşturulan dilimleyiciyi çıktı Excel dosyasında gösterir.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Excel Tablosuna Dilimleyici Oluştur**

Lütfen aşağıdaki örnek kodu görün. Bir tabloyu içeren [örnek Excel dosyasını](sampleCreateSlicerToExcelTable.xlsx) yükler. Ardından ilk sütuna dayalı dilimleyici oluşturur ve son olarak çalışma kitabını [çıktı XLSX](outputCreateSlicerToExcelTable.xlsx) formatında kaydeder.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
