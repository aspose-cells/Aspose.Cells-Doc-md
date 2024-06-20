---
title: ODS Dosyalarında Arka Planla Çalışma
type: docs
weight: 170
url: /tr/java/working-with-background-in-ods-files/
---

## **ODS Dosyalarında Arka Plan**

Arka plan ODS dosyalarına eklenebilir. Arka plan ya renkli arka plan ya da grafik arka planı olabilir. Dosya açıkken arka plan görünmez ancak dosya PDF olarak yazdırılırsa, arka plan oluşturulan PDF'de görünür. Arka plan ayrıca yazdırma önizleme ile de görünür.

Aspose.Cells, ODS dosyalarında arka plan bilgilerini okuma ve arka plan ekleme yeteneği sağlar.

## **OSD dosyasından Arka Plan Bilgisi Oku**

Aspose.Cells, ODS Dosyalarında arka planı yönetmek için [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) sınıfını sağlar. Aşağıdaki kod örneği, [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) sınıfının kullanımını göstererek [kaynak ODS dosyasını](GraphicBackground.ods) yükler ve arka plan bilgilerini okur. Referans için lütfen kod tarafından oluşturulmuş Konsol Çıktısına bakın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **ODS dosyasına Renkli Arka Plan Ekleme**

Aspose.Cells, [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) sınıfını kullanarak ODS dosyalarında arka planı yönetir. Aşağıdaki kod örneği, [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) özelliğinin kullanımını göstererek renkli arka planı ODS dosyasına ekler. Referans için lütfen kod tarafından oluşturulmuş [çıktı ODS dosyasına](ColoredBackground.ods) bakın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **ODS dosyasına Grafik Arka Plan Ekleme**

Aspose.Cells, [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) sınıfını kullanarak ODS dosyalarında arka planı yönetir. Aşağıdaki kod örneği, [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) özelliğinin kullanımını göstererek grafik arka planı ODS dosyasına ekler. Referans için lütfen kod tarafından oluşturulmuş [çıktı ODS dosyasına](GraphicBackground.ods) bakın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
