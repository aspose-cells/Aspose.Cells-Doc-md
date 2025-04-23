---
title: Web Eklentileri  Ofis Eklentileri
type: docs
weight: 120
url: /tr/java/web-extensions-office-add-ins/
---

Web Eklentileri, Ofis belgelerindeki içerikle etkileşimde bulunarak Ofis uygulamalarını genişletir. Web Eklentileri, kullanıcı deneyimini ve üretkenliği artırmak için Ofis istemcisine ek işlevsellik ekler.

Aspose.Cells, Web Eklentileri ile çalışma kabiliyeti de sunar.

## **Web Eklentisi Ekleme**

Excel'de Web Uzantıları(Office Eklentileri) ekleyebilirsiniz. **Ekle** sekmesine tıklayarak ardından **Mağaza**/**Eklenti Al** bağlantısına tıklayın. Eklentiler kutusunda istediğiniz eklentiyi bulun ve ekleyin.

Aspose.Cells ayrıca, Web Uzantıları eklemek için WebExtension ve WebExtensionTaskPane sınıflarını kullanma özelliği sağlar. Aşağıdaki kod örneği, Excel dosyasına web uzantısı eklemek için WebExtension ve WebExtensionTaskPane sınıflarının kullanımını göstermektedir. Referans için lütfen kod tarafından oluşturulan [çıktı Excel dosyasına](AddWebExtension_Out.xlsx) bakınız.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells, Excel dosyasındaki Web Uzantılarının bilgilerine erişme olanağı sağlar. Aşağıdaki kod örneği, [örnek Excel dosyasını](WebExtensionsSample.xlsx) yükleyerek web uzantısı bilgilerine nasıl erişileceğini göstermektedir. Referans için lütfen kod tarafından oluşturulan konsol çıktısına bakınız.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

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
{{< app/cells/assistant language="java" >}}
