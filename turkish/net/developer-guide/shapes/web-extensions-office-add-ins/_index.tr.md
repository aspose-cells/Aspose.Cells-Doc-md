---
title: Web Eklentileri  Ofis Eklentileri
type: docs
weight: 130
url: /tr/net/web-extensions-office-add-ins/
---

Web Eklentileri, Ofis belgelerindeki içerikle etkileşimde bulunarak Ofis uygulamalarını genişletir. Web Eklentileri, kullanıcı deneyimini ve üretkenliği artırmak için Ofis istemcisine ek işlevsellik ekler.

Aspose.Cells, Web Eklentileri ile çalışma kabiliyeti de sunar.

## **Web Eklentisi Ekleme**

Excel'de Web Eklentileri(Office Eklentileri) eklemek için **Ekle** sekmesine tıklayarak **Mağaza**/**Eklenti Al** bağlantısını tıklamanız gerekmektedir. Eklenti kutusunda istediğiniz eklentiyi gözatın ve ekleyin.

Aspose.Cells ayrıca [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) sınıflarını kullanarak Web Eklentileri eklemeyi de sağlar. Aşağıdaki kod örneği, bir Web Eklentisi eklemek için [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) sınıflarının kullanımını göstermektedir. Referans için kod tarafından oluşturulan [çıktı Excel dosyasını](89849869.xlsx) inceleyebilirsiniz.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells, Excel dosyasındaki Web Eklentileri bilgilerine erişme kabiliyeti sunar. Aşağıdaki kod örneği, [örnek Excel dosyasını](89849870.xlsx) yükleyerek Web Eklentisi bilgilerine erişmeyi nasıl yapacağınızı göstermektedir. Referans için kodun ürettiği konsol çıktısını inceleyebilirsiniz.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
