---
title: ODS Dosyalarında Arka Planla Çalışma
type: docs
weight: 150
url: /tr/python-net/working-with-background-in-ods-files/
description: Python via .NET API ile ODS Dosyalarında Arka Planla Çalışma Nasıl
keywords: Python ile ODS Dosyalarında Arka Planla Çalışma, ODS dosyasından Arka Plan Bilgisi Okuma Python via NET, ODS dosyasına Renkli Arka Plan Ekleme Python via NET, Python via NET ile ODS dosyasına Grafiksel Arka Plan Ekleme
---

## **ODS Dosyalarında Arka Plan**

Arka plan, ODS dosyalarındaki sayfalara eklenebilir. Arka plan ya renkli bir arka plan ya da grafik arka plan olabilir. Arka plan, dosya açıldığında görünmez ancak dosya PDF olarak yazdırılırsa, arka plan, oluşturulan PDF'de görünür. Arka plan ayrıca yazdırma önizleme ile de görüntülenir.

Aspose.Cells for Python via .NET, arka plan bilgisini okuma ve ODS dosyalarına arka plan ekleme yeteneği sağlar.

## **ODS dosyalarına arka plan ekleme yeteneği sağlamak için Aspose.Cells, arka plan ile ilgili bilgileri yönetmek için {0} sınıfını sağlar. Aşağıdaki kod örneği, [kaynak ODS](90112030.ods) dosyasını yükleyerek arka plan bilgilerini okuma yeteneğini gösterir.**

Aspose.Cells for Python via .NET, ODS Dosyalarındaki arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) sınıfını sağlar. Aşağıdaki kod örneği, [kaynak ODS](90112030.ods) dosyasını yükleyerek arka plan bilgilerini okuma kullanımını göstermektedir. Lütfen referans için kodun oluşturduğu Konsol Çıktısını görün.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **ODS dosyasına Renkli Arka Plan Ekleme**

Aspose.Cells for Python via .NET, ODS Dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) sınıfını sağlar. Aşağıdaki örnek kod, ODS dosyasına renkli bir arka plan eklemek için [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) özelliğini kullanımını göstermektedir. Referans için oluşturulan [çıktı ODS](90112031.ods) dosyasını görün.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **ODS dosyasına Grafik Arka Plan Ekleme**

Aspose.Cells for Python via .NET, ODS Dosyalarındaki arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) sınıfını sağlar. Aşağıdaki örnek kod, ODS dosyasına grafiksel bir arka plan eklemek için [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) özelliğini kullanımını göstermektedir. Referans için oluşturulan [çıktı ODS](90112030.ods) dosyasını görün.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
