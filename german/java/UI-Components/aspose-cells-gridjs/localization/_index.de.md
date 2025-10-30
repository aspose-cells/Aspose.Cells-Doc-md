---
title: GridJs Mehrsprachigkeitskonfigurationsanleitung
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Dieses Tutorial führt Sie durch die Konfiguration der Mehrsprachigkeit.
keywords: GridJs, Mehrsprachigkeit, Lokalisierung, Internationalisierung, Kultur, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs Mehrsprachigkeitskonfigurationsleitfaden

## Übersicht

Dieses Tutorial führt Sie durch die Konfiguration der Mehrsprachigkeit in Ihrem Aspose.Cells GridJs-Projekt. Es behandelt sowohl Frontend- als auch Backend-Konfigurationen.

Das Tutorial basiert auf dem [Demo-Projekt](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs), passen Sie es bitte entsprechend der tatsächlichen Situation an

## Frontend-Konfiguration

Stellen Sie auf Ihren Frontend-Seiten die Schnittstellensprache mit der Option [`local`](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/) ein.

Im Demo-Projekt müssen Sie die Datei [uidload.html](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html) anpassen

Hier ist ein Beispiel:

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

## Backend-Konfiguration

Im Backend-Code müssen Sie die entsprechende CultureInfo vor der Verarbeitung der Excel-Daten einstellen.

Im Demo-Projekt müssen Sie die [Anwendungs](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java) Datei ändern

### Legen Sie die Gebietssetz-Einstellungen in der Hauptmethode fest

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

## Wichtige Hinweise

1. Frontend- und Backend-Spracheneinstellungen müssen übereinstimmen.
2. CultureInfo muss vor der Verarbeitung von Excel-Daten festgelegt werden.
3. Unterstützte Sprachen: en(Englisch), zh(Chinesisch), es(Spanisch), pt(Portugiesisch), de(Deutsch), ru(Russisch), nl( Niederländisch), pl(Polnisch).
4. Das Beispiel verwendet Polnisch (pl-PL), aber Sie können es auf jede andere unterstützte Sprache ändern.
