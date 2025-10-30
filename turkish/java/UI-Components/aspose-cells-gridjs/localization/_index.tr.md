---
title: GridJs Çok Dilli Konfigürasyon Kılavuzu
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Bu eğitim, çok dilli desteği yapılandırmanıza rehberlik edecektir.
keywords: GridJs, çok dilli, yerelleştirme, uluslararasılaştırma, kültür, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs Çok Dilli Konfigürasyon Kılavuzu

## Genel Bakış

Bu eğitim, Aspose.Cells GridJs projenizde çok dilli desteği yapılandırmanıza rehberlik edecektir. Hem ön yüz hem de arka uç yapılandırmalarını kapsar.

Eğitici, [demo projesine](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs) dayanmıştır, lütfen duruma göre ayarlayın

## Ön Yüz Yapılandırması

Ön yüz sayfalarınızda, arayüz dilini `local` [seçeneği](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/) kullanarak ayarlayın

In the demo project, you need to modify the [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html) file

İşte bir örnek:

```javascript
const loadNormalContext = (sheet) => {
    const option = {
        updateMode: 'server',
        updateUrl: '/GridJs2/UpdateCell',
        showToolbar: true,
        mode: 'edit',
        // Supported languages: en/zh/es/pt/de/ru/nl/pl
        local: 'pl', // Set to Polish in this example
    };
    loadWithOption(jsondata, option);
};
```

## Sunucu Yapılandırması

Arka uç kodunda, Excel verisi işlenmeden önce uygun CultureInfo ayarlamanız gerekir.

Demo projesinde, [Uygulama](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java) dosyasını değiştirmelisiniz

### ana yöntemde yerel ayarları ayarla

```java

public static void main(String[] args) {

	// Set Polish locale for current thread
        Locale polishLocale = new Locale("pl", "PL");
        Locale.setDefault(polishLocale);

        // Demonstration of locale settings
        System.out.println("Current Locale: " + Locale.getDefault());

		 ApplicationContext context  = 	SpringApplication.run(GridjsdemoApplication.class, args);

		 MyConfig myConfig = context.getBean(MyConfig.class);

		 //set license for Aspose.Cells
		 com.aspose.cells.License  lic=new com.aspose.cells.License();
			if ((new File(myConfig.asposeLicensePath)).exists()) {
				lic.setLicense(myConfig.asposeLicensePath);
			}


	}

```

## Önemli Notlar

1. Ön yüz ve arka uç dil ayarları tutarlı olmalıdır.
2. Excel verileri işlenmeden önce CultureInfo ayarlanmalıdır.
3. Desteklenen diller: en(İngilizce), zh(Çince), es(İspanyolca), pt(Portekizce), de(Almanca), ru(Rusça), nl(Hollanda), pl(Lehçe).
4. Örnek Polonyaca (pl-PL) kullanır, ancak başka herhangi bir desteklenen bölgeye değiştirebilirsiniz.
