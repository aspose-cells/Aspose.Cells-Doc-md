---
title: GridJs Fler språk Konfigurationsguide
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Denna handledning guidar dig genom att konfigurera flerspråkstöd
keywords: GridJs, flerspråk, lokalisation, internationalisering, kultur, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs Flerspråkig Konfigurationsguide

## Översikt

Denna handledning guidar dig genom att konfigurera flerspråkstöd i ditt Aspose.Cells GridJs-projekt. Den täcker både frontend- och backend-konfigurationer.

Instruktionen är baserad på [demo-projektet](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs), vänligen anpassa enligt den faktiska situationen

## Frontend-Konfiguration

I dina frontend-sidor, ställ in gränssnittsspråket med hjälp av `local` [alternativet](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/)

I demo-projektet måste du ändra filen [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html)

Här är ett exempel:

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

I backend-koden måste du ställa in lämplig CultureInfo innan du bearbetar Excel-data.

I demo-projektet måste du ändra filen [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)

### ställ in språkinställningar i main-metoden

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

## Viktiga Anmärkningar

1. Frontend och backend språkinställningar måste vara konsekventa.
2. CultureInfo måste anges innan bearbetning av Excel-data.
3. Supported languages: en(Engelska), zh(Kinesiska), es(Spanska), pt(Portugisiska), de(Tyska), ru(Ryska), nl(Holländska), pl(Polska).
4. Exemplet använder polska (pl-PL), men du kan ändra till vilken som helst annan stödd lokal.
