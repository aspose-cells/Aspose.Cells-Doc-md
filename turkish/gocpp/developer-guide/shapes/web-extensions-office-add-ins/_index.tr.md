---
title: Web Uzantıları  Office Eklentileri Golang ve C++ ile
linktitle: Web Eklentileri  Ofis Eklentileri
type: docs
weight: 130
url: /tr/go-cpp/web-extensions-office-add-ins/
description: Aspose.Cells kullanarak Golang ve C++ ile Excel dosyalarına Web Uzantıları (Office Eklentileri) ekleme ve erişim yapmayı öğrenin.
---

Web Eklentileri, Office uygulamalarını genişletir ve Office belgelerindeki içerikle etkileşime girer. Web Eklentileri, Office kullanıcı deneyimini ve üretkenliğini artırmak amacıyla ek fonksiyonlar ekler.

Aspose.Cells, Web Eklentileri ile çalışma kabiliyeti de sunar.

## **Web Eklentisi Ekleme**

Excel'de Web Eklentileri (Office Eklentileri) ekleyebilirsiniz, bunun için **Ekle** sekmesine tıklayın ve sonra **Mağaza**/**Ekle Eklentileri Al** bağlantısını tıklayın. Eklentiler kutusunda, istediğiniz eklentiyi arayın ve ekleyin.

Aspose.Cells, ayrıca [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) sınıflarını kullanarak Web Eklentileri ekleme özelliği sağlar. Aşağıdaki kod örneği, [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) sınıflarını kullanarak bir Excel dosyasına web eklentisi eklemeyi gösterir. Lütfen referans olarak kod tarafından oluşturulan [çıktı Excel dosyasına](89849869.xlsx) bakın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells, Excel dosyasındaki Web Eklentileri bilgisine erişim sağlar. Aşağıdaki kod örneği, [örnek Excel dosyasını](89849870.xlsx) yükleyerek web eklentisi bilgisine nasıl ulaşılacağını gösterir. Kod tarafından üretilen konsol çıktısına bakın.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
### **Konsol Çıktısı**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
