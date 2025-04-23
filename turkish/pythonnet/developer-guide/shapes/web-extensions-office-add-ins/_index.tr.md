---
title: Web Eklentileri  Ofis Eklentileri
type: docs
weight: 130
url: /tr/python-net/web-extensions-office-add-ins/
---

Web Eklentileri, Ofis belgelerindeki içerikle etkileşimde bulunarak Ofis uygulamalarını genişletir. Web Eklentileri, kullanıcı deneyimini ve üretkenliği artırmak için Ofis istemcisine ek işlevsellik ekler.

Aspose.Cells for Python via .NET ayrıca Web Eklentileri ile çalışma yeteneği sağlar.

## **Web Eklentisi Ekleme**

Excel'de Web Eklentileri(Office Eklentileri) eklemek için **Ekle** sekmesine tıklayarak **Mağaza**/**Eklenti Al** bağlantısını tıklamanız gerekmektedir. Eklenti kutusunda istediğiniz eklentiyi gözatın ve ekleyin.

Aspose.Cells for Python via .NET ayrıca [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) sınıflarını kullanarak Web Eklentileri ekleme özelliği sağlar. Aşağıdaki kod örneği, Excel dosyasına web eklentisi eklemek için [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) sınıflarının kullanılmasını gösterir. Lütfen referans için kod tarafından oluşturulan [çıktı Excel dosyasına](89849869.xlsx) bakınız.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells for Python via .NET, Excel dosyasındaki Web Eklentileri bilgisine erişim sağlama yeteneği sunar. Aşağıdaki kod örneği, [örnek Excel dosyasını](89849870.xlsx) yükleyerek web eklentisi bilgisine nasıl erişileceğini gösterir. Referans için kod tarafından üretilen konsol çıktısına bakınız.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

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
