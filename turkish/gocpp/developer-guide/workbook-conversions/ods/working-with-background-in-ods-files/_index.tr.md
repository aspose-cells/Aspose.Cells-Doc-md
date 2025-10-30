---
title: Golang kullanarak C++ ile ODS Dosyalarında Arka Plan ile çalışma
linktitle: ODS Dosyalarında Arka Planla Çalışma
type: docs
weight: 150
url: /tr/go-cpp/working-with-background-in-ods-files/
description: Aspose.Cells ve Golang kullanarak ODS dosyalarında renkli ve grafik arka planları nasıl yönetebileceğinizi öğrenin.
---

## **ODS Dosyalarında Arka Plan**

Arka plan, ODS dosyalarındaki sayfalara eklenebilir. Arka plan ya renkli bir arka plan ya da grafik arka plan olabilir. Arka plan, dosya açıldığında görünmez ancak dosya PDF olarak yazdırılırsa, arka plan, oluşturulan PDF'de görünür. Arka plan ayrıca yazdırma önizleme ile de görüntülenir.

Aspose.Cells, arka plan bilgilerini okuma ve ODS dosyalarına arka plan ekleme yeteneği sağlar.

## **ODS dosyalarına arka plan ekleme yeteneği sağlamak için Aspose.Cells, arka plan ile ilgili bilgileri yönetmek için {0} sınıfını sağlar. Aşağıdaki kod örneği, [kaynak ODS](90112030.ods) dosyasını yükleyerek arka plan bilgilerini okuma yeteneğini gösterir.**

Aspose.Cells, ODS dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) sınıfını sağlar. Aşağıdaki kod örneği, [kaynak ODS dosyasını](90112030.ods) yükleyerek ve arka plan bilgilerini okuyarak [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) sınıfının kullanımını gösterir. Lütfen, kod tarafından oluşturulan Consol Çıktısını referans olarak inceleyiniz.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Konsol Çıktısı**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **ODS dosyasına Renkli Arka Plan Ekleme**

Aspose.Cells, ODS dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) sınıfını sağlar. Aşağıdaki kod örneği, [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) özelliğini kullanarak ODS dosyasına renkli arka plan eklemeyi gösterir. Lütfen, kod tarafından oluşturulan [çıktı ODS](90112031.ods) dosyasını referans alın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **ODS dosyasına Grafik Arka Plan Ekleme**

Aspose.Cells, ODS dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) sınıfını sağlar. Aşağıdaki kod örneği, [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) özelliğini kullanarak ODS dosyasına grafik arka plan eklemeyi gösterir. Lütfen, kod tarafından oluşturulan [çıktı ODS](90112030.ods) dosyasını referans alın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
